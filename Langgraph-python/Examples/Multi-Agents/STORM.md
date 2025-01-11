Web Research (STORM)¶
STORM is a research assistant designed by Shao, et. al that extends the idea of "outline-driven RAG" for richer article generation.

STORM is designed to generate Wikipedia-style ariticles on a user-provided topic. It applies two main insights to produce more organized and comprehensive articles:

Creating an outline (planning) by querying similar topics helps improve coverage.
Multi-perspective, grounded (in search) conversation simulation helps increase the reference count and information density.
The control flow looks like the diagram below.

storm.png

STORM has a few main stages:

Generate initial outline + Survey related subjects
Identify distinct perspectives
"Interview subject matter experts" (role-playing LLMs)
Refine outline (using references)
Write sections, then write article
The expert interviews stage occurs between the role-playing article writer and a research expert. The "expert" is able to query external knowledge and respond to pointed questions, saving cited sources to a vectorstore so that the later refinement stages can synthesize the full article.

There are a couple hyperparameters you can set to restrict the (potentially) infinite research breadth:

N: Number of perspectives to survey / use (Steps 2->3) M: Max number of conversation turns in step (Step 3)

Setup¶
First, let's install the required packages and set our API keys


%%capture --no-stderr
%pip install -U langchain_community langchain_openai langchain_fireworks langgraph wikipedia duckduckgo-search tavily-python

# Uncomment if you want to draw the pretty graph diagrams.
# If you are on MacOS, you will need to run brew install graphviz before installing and update some environment flags
# ! brew install graphviz
# !CFLAGS="-I $(brew --prefix graphviz)/include" LDFLAGS="-L $(brew --prefix graphviz)/lib" pip install -U pygraphviz

import getpass
import os


def _set_env(var: str):
    if os.environ.get(var):
        return
    os.environ[var] = getpass.getpass(var + ":")


_set_env("OPENAI_API_KEY")
_set_env("TAVILY_API_KEY")
Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started here.

Select LLMs¶
We will have a faster LLM do most of the work, but a slower, long-context model to distill the conversations and write the final report.


from langchain_openai import ChatOpenAI

fast_llm = ChatOpenAI(model="gpt-4o-mini")
# Uncomment for a Fireworks model
# fast_llm = ChatFireworks(model="accounts/fireworks/models/firefunction-v1", max_tokens=32_000)
long_context_llm = ChatOpenAI(model="gpt-4o")
API Reference: ChatOpenAI

Generate Initial Outline¶
For many topics, your LLM may have an initial idea of the important and related topics. We can generate an initial outline to be refined after our research. Below, we will use our "fast" llm to generate the outline.

Using Pydantic with LangChain

This notebook uses Pydantic v2 BaseModel, which requires langchain-core >= 0.3. Using langchain-core < 0.3 will result in errors due to mixing of Pydantic v1 and v2 BaseModels.


from typing import List, Optional

from langchain_core.prompts import ChatPromptTemplate

from pydantic import BaseModel, Field

direct_gen_outline_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a Wikipedia writer. Write an outline for a Wikipedia page about a user-provided topic. Be comprehensive and specific.",
        ),
        ("user", "{topic}"),
    ]
)


class Subsection(BaseModel):
    subsection_title: str = Field(..., title="Title of the subsection")
    description: str = Field(..., title="Content of the subsection")

    @property
    def as_str(self) -> str:
        return f"### {self.subsection_title}\n\n{self.description}".strip()


class Section(BaseModel):
    section_title: str = Field(..., title="Title of the section")
    description: str = Field(..., title="Content of the section")
    subsections: Optional[List[Subsection]] = Field(
        default=None,
        title="Titles and descriptions for each subsection of the Wikipedia page.",
    )

    @property
    def as_str(self) -> str:
        subsections = "\n\n".join(
            f"### {subsection.subsection_title}\n\n{subsection.description}"
            for subsection in self.subsections or []
        )
        return f"## {self.section_title}\n\n{self.description}\n\n{subsections}".strip()


class Outline(BaseModel):
    page_title: str = Field(..., title="Title of the Wikipedia page")
    sections: List[Section] = Field(
        default_factory=list,
        title="Titles and descriptions for each section of the Wikipedia page.",
    )

    @property
    def as_str(self) -> str:
        sections = "\n\n".join(section.as_str for section in self.sections)
        return f"# {self.page_title}\n\n{sections}".strip()


generate_outline_direct = direct_gen_outline_prompt | fast_llm.with_structured_output(
    Outline
)
API Reference: ChatPromptTemplate


example_topic = "Impact of million-plus token context window language models on RAG"

initial_outline = generate_outline_direct.invoke({"topic": example_topic})

print(initial_outline.as_str)

# Impact of million-plus token context window language models on RAG

## Introduction

Brief overview of million-plus token context window language models and RAG.

## Million-Plus Token Context Window Language Models

Explanation of million-plus token context window language models, their architecture, training process, and capabilities.

## Retrieval-Augmented Generation (RAG)

Explanation of RAG model, its components, and how it combines information retrieval with text generation.

## Impact on RAG

Discussion on how million-plus token context window language models impact RAG, including improvements in performance, efficiency, and potential challenges.
Expand Topics¶
While language models do store some Wikipedia-like knowledge in their parameters, you will get better results by incorporating relevant and recent information using a search engine.

We will start our search by generating a list of related topics, sourced from Wikipedia.


gen_related_topics_prompt = ChatPromptTemplate.from_template(
    """I'm writing a Wikipedia page for a topic mentioned below. Please identify and recommend some Wikipedia pages on closely related subjects. I'm looking for examples that provide insights into interesting aspects commonly associated with this topic, or examples that help me understand the typical content and structure included in Wikipedia pages for similar topics.

Please list the as many subjects and urls as you can.

Topic of interest: {topic}
"""
)


class RelatedSubjects(BaseModel):
    topics: List[str] = Field(
        description="Comprehensive list of related subjects as background research.",
    )


expand_chain = gen_related_topics_prompt | fast_llm.with_structured_output(
    RelatedSubjects
)

related_subjects = await expand_chain.ainvoke({"topic": example_topic})
related_subjects

RelatedSubjects(topics=['million-plus token context window language models', 'RAG'])
Generate Perspectives¶
From these related subjects, we can select representative Wikipedia editors as "subject matter experts" with distinct backgrounds and affiliations. These will help distribute the search process to encourage a more well-rounded final report.


class Editor(BaseModel):
    affiliation: str = Field(
        description="Primary affiliation of the editor.",
    )
    name: str = Field(
        description="Name of the editor.", pattern=r"^[a-zA-Z0-9_-]{1,64}$"
    )
    role: str = Field(
        description="Role of the editor in the context of the topic.",
    )
    description: str = Field(
        description="Description of the editor's focus, concerns, and motives.",
    )

    @property
    def persona(self) -> str:
        return f"Name: {self.name}\nRole: {self.role}\nAffiliation: {self.affiliation}\nDescription: {self.description}\n"


class Perspectives(BaseModel):
    editors: List[Editor] = Field(
        description="Comprehensive list of editors with their roles and affiliations.",
        # Add a pydantic validation/restriction to be at most M editors
    )


gen_perspectives_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You need to select a diverse (and distinct) group of Wikipedia editors who will work together to create a comprehensive article on the topic. Each of them represents a different perspective, role, or affiliation related to this topic.\
    You can use other Wikipedia pages of related topics for inspiration. For each editor, add a description of what they will focus on.

    Wiki page outlines of related topics for inspiration:
    {examples}""",
        ),
        ("user", "Topic of interest: {topic}"),
    ]
)

gen_perspectives_chain = gen_perspectives_prompt | ChatOpenAI(
    model="gpt-3.5-turbo"
).with_structured_output(Perspectives)

from langchain_community.retrievers import WikipediaRetriever
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import chain as as_runnable

wikipedia_retriever = WikipediaRetriever(load_all_available_meta=True, top_k_results=1)


def format_doc(doc, max_length=1000):
    related = "- ".join(doc.metadata["categories"])
    return f"### {doc.metadata['title']}\n\nSummary: {doc.page_content}\n\nRelated\n{related}"[
        :max_length
    ]


def format_docs(docs):
    return "\n\n".join(format_doc(doc) for doc in docs)


@as_runnable
async def survey_subjects(topic: str):
    related_subjects = await expand_chain.ainvoke({"topic": topic})
    retrieved_docs = await wikipedia_retriever.abatch(
        related_subjects.topics, return_exceptions=True
    )
    all_docs = []
    for docs in retrieved_docs:
        if isinstance(docs, BaseException):
            continue
        all_docs.extend(docs)
    formatted = format_docs(all_docs)
    return await gen_perspectives_chain.ainvoke({"examples": formatted, "topic": topic})
API Reference: WikipediaRetriever | RunnableLambda | chain


perspectives = await survey_subjects.ainvoke(example_topic)

perspectives.dict()

{'editors': [{'affiliation': 'Research Institution',
   'name': 'AliceResearcher',
   'role': 'Researcher',
   'description': 'AliceResearcher focuses on the impact of million-plus token context window language models on the Retrieval-Augmented Generation (RAG) framework. They analyze the effectiveness of large language models within the RAG framework and investigate how these models influence information retrieval and generation tasks.'},
  {'affiliation': 'Tech Company',
   'name': 'BobEngineer',
   'role': 'Engineer',
   'description': 'BobEngineer specializes in implementing million-plus token context window language models in practical applications, particularly within the Retrieval-Augmented Generation (RAG) framework. They focus on optimizing the performance and efficiency of these models for real-world usage.'},
  {'affiliation': 'Academic Institution',
   'name': 'CharlieAcademic',
   'role': 'Academic',
   'description': 'CharlieAcademic studies the theoretical implications of integrating million-plus token context window language models with the RAG framework. They explore the broader implications of using such large models for natural language processing and information retrieval.'},
  {'affiliation': 'Industry Expert',
   'name': 'DianaExpert',
   'role': 'Industry Expert',
   'description': 'DianaExpert provides insights from the industry perspective on the impact of million-plus token context window language models on RAG. They focus on practical applications, challenges, and opportunities that arise when utilizing these models in commercial settings.'},
  {'affiliation': 'AI Ethics Organization',
   'name': 'EveEthicist',
   'role': 'Ethicist',
   'description': 'EveEthicist examines the ethical considerations surrounding the use of million-plus token context window language models in the context of RAG. They focus on potential biases, fairness, and transparency issues that may arise from the deployment of such models.'}]}
Expert Dialog¶
Now the true fun begins, each wikipedia writer is primed to role-play using the perspectives presented above. It will ask a series of questions of a second "domain expert" with access to a search engine. This generate content to generate a refined outline as well as an updated index of reference documents.

Interview State¶
The conversation is cyclic, so we will construct it within its own graph. The State will contain messages, the reference docs, and the editor (with its own "persona") to make it easy to parallelize these conversations.


from typing import Annotated

from langchain_core.messages import AnyMessage
from typing_extensions import TypedDict

from langgraph.graph import END, StateGraph, START


def add_messages(left, right):
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    return left + right


def update_references(references, new_references):
    if not references:
        references = {}
    references.update(new_references)
    return references


def update_editor(editor, new_editor):
    # Can only set at the outset
    if not editor:
        return new_editor
    return editor


class InterviewState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
    references: Annotated[Optional[dict], update_references]
    editor: Annotated[Optional[Editor], update_editor]
API Reference: END | StateGraph | START

Dialog Roles¶
The graph will have two participants: the wikipedia editor (generate_question), who asks questions based on its assigned role, and a domain expert (`gen_answer_chain), who uses a search engine to answer the questions as accurately as possible.


from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.prompts import MessagesPlaceholder

gen_qn_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an experienced Wikipedia writer and want to edit a specific page. \
Besides your identity as a Wikipedia writer, you have a specific focus when researching the topic. \
Now, you are chatting with an expert to get information. Ask good questions to get more useful information.

When you have no more questions to ask, say "Thank you so much for your help!" to end the conversation.\
Please only ask one question at a time and don't ask what you have asked before.\
Your questions should be related to the topic you want to write.
Be comprehensive and curious, gaining as much unique insight from the expert as possible.\

Stay true to your specific perspective:

{persona}""",
        ),
        MessagesPlaceholder(variable_name="messages", optional=True),
    ]
)


def tag_with_name(ai_message: AIMessage, name: str):
    ai_message.name = name
    return ai_message


def swap_roles(state: InterviewState, name: str):
    converted = []
    for message in state["messages"]:
        if isinstance(message, AIMessage) and message.name != name:
            message = HumanMessage(**message.dict(exclude={"type"}))
        converted.append(message)
    return {"messages": converted}


@as_runnable
async def generate_question(state: InterviewState):
    editor = state["editor"]
    gn_chain = (
        RunnableLambda(swap_roles).bind(name=editor.name)
        | gen_qn_prompt.partial(persona=editor.persona)
        | fast_llm
        | RunnableLambda(tag_with_name).bind(name=editor.name)
    )
    result = await gn_chain.ainvoke(state)
    return {"messages": [result]}
API Reference: AIMessage | HumanMessage | ToolMessage | MessagesPlaceholder


messages = [
    HumanMessage(f"So you said you were writing an article on {example_topic}?")
]
question = await generate_question.ainvoke(
    {
        "editor": perspectives.editors[0],
        "messages": messages,
    }
)

question["messages"][0].content

"Yes, that's correct. I focus on studying the impact of million-plus token context window language models on the Retrieval-Augmented Generation (RAG) framework. I analyze how these large language models affect information retrieval and generation tasks within the RAG framework. Is there a specific aspect of this topic that you would like to know more about?"
Answer questions¶
The gen_answer_chain first generates queries (query expansion) to answer the editor's question, then responds with citations.


class Queries(BaseModel):
    queries: List[str] = Field(
        description="Comprehensive list of search engine queries to answer the user's questions.",
    )


gen_queries_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful research assistant. Query the search engine to answer the user's questions.",
        ),
        MessagesPlaceholder(variable_name="messages", optional=True),
    ]
)
gen_queries_chain = gen_queries_prompt | ChatOpenAI(
    model="gpt-3.5-turbo"
).with_structured_output(Queries, include_raw=True)

queries = await gen_queries_chain.ainvoke(
    {"messages": [HumanMessage(content=question["messages"][0].content)]}
)
queries["parsed"].queries

['impact of million-plus token context window language models on Retrieval-Augmented Generation (RAG) framework',
 'information retrieval tasks in the RAG framework with large language models',
 'generation tasks in the RAG framework with million-plus token context window models']

class AnswerWithCitations(BaseModel):
    answer: str = Field(
        description="Comprehensive answer to the user's question with citations.",
    )
    cited_urls: List[str] = Field(
        description="List of urls cited in the answer.",
    )

    @property
    def as_str(self) -> str:
        return f"{self.answer}\n\nCitations:\n\n" + "\n".join(
            f"[{i+1}]: {url}" for i, url in enumerate(self.cited_urls)
        )


gen_answer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert who can use information effectively. You are chatting with a Wikipedia writer who wants\
 to write a Wikipedia page on the topic you know. You have gathered the related information and will now use the information to form a response.

Make your response as informative as possible and make sure every sentence is supported by the gathered information.
Each response must be backed up by a citation from a reliable source, formatted as a footnote, reproducing the URLS after your response.""",
        ),
        MessagesPlaceholder(variable_name="messages", optional=True),
    ]
)

gen_answer_chain = gen_answer_prompt | fast_llm.with_structured_output(
    AnswerWithCitations, include_raw=True
).with_config(run_name="GenerateAnswer")

from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper
from langchain_core.tools import tool

'''
# Tavily is typically a better search engine, but your free queries are limited
search_engine = TavilySearchResults(max_results=4)

@tool
async def search_engine(query: str):
    """Search engine to the internet."""
    results = tavily_search.invoke(query)
    return [{"content": r["content"], "url": r["url"]} for r in results]
'''

# DDG
search_engine = DuckDuckGoSearchAPIWrapper()


@tool
async def search_engine(query: str):
    """Search engine to the internet."""
    results = DuckDuckGoSearchAPIWrapper()._ddgs_text(query)
    return [{"content": r["body"], "url": r["href"]} for r in results]
API Reference: DuckDuckGoSearchAPIWrapper | tool


import json

from langchain_core.runnables import RunnableConfig


async def gen_answer(
    state: InterviewState,
    config: Optional[RunnableConfig] = None,
    name: str = "Subject_Matter_Expert",
    max_str_len: int = 15000,
):
    swapped_state = swap_roles(state, name)  # Convert all other AI messages
    queries = await gen_queries_chain.ainvoke(swapped_state)
    query_results = await search_engine.abatch(
        queries["parsed"].queries, config, return_exceptions=True
    )
    successful_results = [
        res for res in query_results if not isinstance(res, Exception)
    ]
    all_query_results = {
        res["url"]: res["content"] for results in successful_results for res in results
    }
    # We could be more precise about handling max token length if we wanted to here
    dumped = json.dumps(all_query_results)[:max_str_len]
    ai_message: AIMessage = queries["raw"]
    tool_call = queries["raw"].tool_calls[0]
    tool_id = tool_call["id"]
    tool_message = ToolMessage(tool_call_id=tool_id, content=dumped)
    swapped_state["messages"].extend([ai_message, tool_message])
    # Only update the shared state with the final answer to avoid
    # polluting the dialogue history with intermediate messages
    generated = await gen_answer_chain.ainvoke(swapped_state)
    cited_urls = set(generated["parsed"].cited_urls)
    # Save the retrieved information to a the shared state for future reference
    cited_references = {k: v for k, v in all_query_results.items() if k in cited_urls}
    formatted_message = AIMessage(name=name, content=generated["parsed"].as_str)
    return {"messages": [formatted_message], "references": cited_references}
API Reference: RunnableConfig


example_answer = await gen_answer(
    {"messages": [HumanMessage(content=question["messages"][0].content)]}
)
example_answer["messages"][-1].content

'Studying the impact of million-plus token context window language models on the Retrieval-Augmented Generation (RAG) framework involves analyzing how these large language models affect information retrieval and generation tasks within the RAG framework. The introduction of large language models with extensive context windows, such as Google Gemini 1.5 Pro with a record 1 million token context window, has sparked discussions in the AI community about the potential implications for RAG. While there are concerns about the negative impact of supermassive context windows on RAG, there is also a recognition of the benefits they bring, enabling more use cases and enhancing performance in knowledge-intensive tasks. Retrieval-Augmented Generation (RAG) combines the generative capabilities of transformer architectures with dynamic information retrieval, allowing large language models to access and integrate relevant external knowledge during text generation, leading to more accurate and credible outputs. RAG has been identified as a valuable solution to address challenges faced by Large Language Models (LLMs), such as hallucination, outdated knowledge, lack of transparency, and untraceable reasoning processes. By incorporating external databases, RAG improves the consistency and coherence of generated content, especially in conversational question answering tasks. RAG has also been recognized as a powerful tool for large language models to efficiently process overly lengthy contexts, with recent LLMs like Gemini-1.5 and GPT-4 showcasing exceptional capabilities in understanding long contexts directly. There is ongoing research and benchmarking to compare the strengths of RAG and long-context LLMs, aiming to leverage the advantages of both approaches for enhanced performance in information retrieval and generation tasks within the RAG framework.\n\nCitations:\n\n[1]: https://thenewstack.io/do-enormous-llm-context-windows-spell-the-end-of-rag/\n[2]: https://medium.com/enterprise-rag/why-gemini-1-5-and-other-large-context-models-are-bullish-for-rag-ce3218930bb4\n[3]: https://medium.com/@amanatulla1606/rag-is-here-to-stay-four-reasons-why-large-context-windows-cant-replace-it-ad112013de25\n[4]: https://www.freecodecamp.org/news/retrieval-augmented-generation-rag-handbook/\n[5]: https://www.deepset.ai/blog/long-context-llms-rag\n[6]: https://arxiv.org/abs/2312.10997\n[7]: https://arxiv.org/abs/2409.13385\n[8]: https://irisagent.com/blog/enhancing-large-language-models-a-deep-dive-into-rag-llm-technology/\n[9]: https://arxiv.org/abs/2407.16833'
Construct the Interview Graph¶
Now that we've defined the editor and domain expert, we can compose them in a graph.


max_num_turns = 5
from langgraph.pregel import RetryPolicy


def route_messages(state: InterviewState, name: str = "Subject_Matter_Expert"):
    messages = state["messages"]
    num_responses = len(
        [m for m in messages if isinstance(m, AIMessage) and m.name == name]
    )
    if num_responses >= max_num_turns:
        return END
    last_question = messages[-2]
    if last_question.content.endswith("Thank you so much for your help!"):
        return END
    return "ask_question"


builder = StateGraph(InterviewState)

builder.add_node("ask_question", generate_question, retry=RetryPolicy(max_attempts=5))
builder.add_node("answer_question", gen_answer, retry=RetryPolicy(max_attempts=5))
builder.add_conditional_edges("answer_question", route_messages)
builder.add_edge("ask_question", "answer_question")

builder.add_edge(START, "ask_question")
interview_graph = builder.compile(checkpointer=False).with_config(
    run_name="Conduct Interviews"
)

from IPython.display import Image, display

try:
    display(Image(interview_graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass



final_step = None

initial_state = {
    "editor": perspectives.editors[0],
    "messages": [
        AIMessage(
            content=f"So you said you were writing an article on {example_topic}?",
            name="Subject_Matter_Expert",
        )
    ],
}
async for step in interview_graph.astream(initial_state):
    name = next(iter(step))
    print(name)
    print("-- ", str(step[name]["messages"])[:300])
final_step = step

ask_question
--  [AIMessage(content="Yes, that's correct. My focus is on how million-plus token context window language models impact the Retrieval-Augmented Generation (RAG) framework. I'm interested in understanding how the size and scope of these language models influence the effectiveness of the RAG framework in
answer_question
--  [AIMessage(content='The integration of million-plus token context window language models in the Retrieval-Augmented Generation (RAG) framework has emerged as a significant advancement in natural language processing. RAG has been a reliable solution for context-based answer generation, overcoming the
ask_question
--  [AIMessage(content='Can you elaborate on how the retrieval-augmented techniques in the RAG framework enhance the accuracy and relevance of the generated text by accessing external knowledge dynamically? How does this process differ from traditional language modeling approaches, and what specific ben
answer_question
--  [AIMessage(content='The integration of retrieval-augmented techniques in the RAG framework enhances the accuracy and relevance of generated text by dynamically accessing external knowledge sources to enrich the generation process. Unlike traditional language modeling approaches that rely solely on i
ask_question
--  [AIMessage(content='Thank you for the insightful information on how retrieval-augmented techniques enhance the accuracy and relevance of text generation in the RAG framework by incorporating external knowledge sources. How do these external knowledge sources impact the overall performance and adapta
answer_question
--  [AIMessage(content='External knowledge sources significantly impact the overall performance and adaptability of RAG models in handling various types of information retrieval and generation tasks. By leveraging external knowledge, RAG models access up-to-date information, reduce the incidence of gene
ask_question
--  [AIMessage(content='Thank you for sharing insights on how external knowledge sources impact the performance and adaptability of RAG models in handling diverse information retrieval and generation tasks. This information will be valuable for my research on the impact of million-plus token context win
answer_question
--  [AIMessage(content="The integration of million-plus token context window language models in the Retrieval-Augmented Generation (RAG) framework has sparked discussions in the AI community, with some concerns about the potential impact on RAG's relevance. However, RAG continues to be a valuable soluti

final_state = next(iter(final_step.values()))
Refine Outline¶
At this point in STORM, we've conducted a large amount of research from different perspectives. It's time to refine the original outline based on these investigations. Below, create a chain using the LLM with a long context window to update the original outline.


refine_outline_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a Wikipedia writer. You have gathered information from experts and search engines. Now, you are refining the outline of the Wikipedia page. \
You need to make sure that the outline is comprehensive and specific. \
Topic you are writing about: {topic} 

Old outline:

{old_outline}""",
        ),
        (
            "user",
            "Refine the outline based on your conversations with subject-matter experts:\n\nConversations:\n\n{conversations}\n\nWrite the refined Wikipedia outline:",
        ),
    ]
)

# Using turbo preview since the context can get quite long
refine_outline_chain = refine_outline_prompt | long_context_llm.with_structured_output(
    Outline
)

refined_outline = refine_outline_chain.invoke(
    {
        "topic": example_topic,
        "old_outline": initial_outline.as_str,
        "conversations": "\n\n".join(
            f"### {m.name}\n\n{m.content}" for m in final_state["messages"]
        ),
    }
)

print(refined_outline.as_str)

# Impact of million-plus token context window language models on RAG

## Introduction

Provides a brief overview of million-plus token context window language models and their relevance to Retrieval-Augmented Generation (RAG) systems, setting the stage for a deeper exploration of their impact.

## Background

A foundational section to understand the core concepts involved.

### Million-Plus Token Context Window Language Models

Explains what million-plus token context window language models are, including notable examples like Gemini 1.5, focusing on their architecture, training data, and the evolution of their applications.

### Retrieval-Augmented Generation (RAG)

Describes the RAG framework, its unique approach of combining retrieval and generation models for enhanced natural language processing, and its significance in the AI landscape.

## Impact on RAG Systems

Delves into the effects of million-plus token context window language models on RAG, highlighting both the challenges and opportunities presented.

### Performance and Efficiency

Discusses how large context window models influence RAG performance, including aspects of latency, computational demands, and overall efficiency.

### Generation Quality and Diversity

Explores the impact on generation quality, the potential for more accurate and diverse outputs, and how these models address data biases and factual accuracy.

### Technical Challenges

Identifies specific technical hurdles such as prompt template design, context length limitations, and similarity searches in vector databases, and how they affect RAG systems.

### Opportunities and Advancements

Outlines the new capabilities and improvements in agent interaction, information retrieval, and response relevance that these models bring to RAG systems.

## Future Directions

Considers ongoing research and potential future developments in the integration of million-plus token context window language models with RAG systems, including speculation on emerging trends and technologies.

## Conclusion

Summarizes the key points discussed in the article, reaffirming the significant impact of million-plus token context window language models on RAG systems.
Generate Article¶
Now it's time to generate the full article. We will first divide-and-conquer, so that each section can be tackled by an individual llm. Then we will prompt the long-form LLM to refine the finished article (since each section may use an inconsistent voice).

Create Retriever¶
The research process uncovers a large number of reference documents that we may want to query during the final article-writing process.

First, create the retriever:


from langchain_community.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
reference_docs = [
    Document(page_content=v, metadata={"source": k})
    for k, v in final_state["references"].items()
]
# This really doesn't need to be a vectorstore for this size of data.
# It could just be a numpy matrix. Or you could store documents
# across requests if you want.
vectorstore = InMemoryVectorStore.from_documents(
    reference_docs,
    embedding=embeddings,
)
retriever = vectorstore.as_retriever(k=3)
API Reference: InMemoryVectorStore | Document | OpenAIEmbeddings


retriever.invoke("What's a long context LLM anyway?")

[Document(page_content='In Retrieval Augmented Generation (RAG), a longer context augments our model with more information. For LLMs that power agents, such as chatbots, longer context means more tools and capabilities. When summarizing, longer context means more comprehensive summaries. There exist plenty of use-cases for LLMs that are unlocked by longer context lengths.', metadata={'id': '20454848-23ac-4649-b083-81980532a77b', 'source': 'https://www.anyscale.com/blog/fine-tuning-llms-for-longer-context-and-better-rag-systems'}),
 Document(page_content='By the way, the context limits differ among models: two Claude models offer a 100K token context window, which works out to about 75,000 words, which is much higher than most other LLMs. The ...', metadata={'id': '1ee2d2bb-8f8e-4a7e-b45e-608b0804fe4c', 'source': 'https://www.infoworld.com/article/3712227/what-is-rag-more-accurate-and-reliable-llms.html'}),
 Document(page_content='Figure 1: LLM response accuracy goes down when context needed to answer correctly is found in the middle of the context window. The problem gets worse with larger context models. The problem gets ...', metadata={'id': 'a41d69e6-62eb-4abd-90ad-0892a2836cba', 'source': 'https://medium.com/@jm_51428/long-context-window-models-vs-rag-a73c35a763f2'}),
 Document(page_content='To improve performance, we used retrieval-augmented generation (RAG) to prompt an LLM with accurate up-to-date information. As a result of using RAG, the writing quality of the LLM improves substantially, which has implications for the practical usability of LLMs in clinical trial-related writing.', metadata={'id': 'e1af6e30-8c2b-495b-b572-ac6a29067a94', 'source': 'https://arxiv.org/abs/2402.16406'})]
Generate Sections¶
Now you can generate the sections using the indexed docs.


class SubSection(BaseModel):
    subsection_title: str = Field(..., title="Title of the subsection")
    content: str = Field(
        ...,
        title="Full content of the subsection. Include [#] citations to the cited sources where relevant.",
    )

    @property
    def as_str(self) -> str:
        return f"### {self.subsection_title}\n\n{self.content}".strip()


class WikiSection(BaseModel):
    section_title: str = Field(..., title="Title of the section")
    content: str = Field(..., title="Full content of the section")
    subsections: Optional[List[Subsection]] = Field(
        default=None,
        title="Titles and descriptions for each subsection of the Wikipedia page.",
    )
    citations: List[str] = Field(default_factory=list)

    @property
    def as_str(self) -> str:
        subsections = "\n\n".join(
            subsection.as_str for subsection in self.subsections or []
        )
        citations = "\n".join([f" [{i}] {cit}" for i, cit in enumerate(self.citations)])
        return (
            f"## {self.section_title}\n\n{self.content}\n\n{subsections}".strip()
            + f"\n\n{citations}".strip()
        )


section_writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert Wikipedia writer. Complete your assigned WikiSection from the following outline:\n\n"
            "{outline}\n\nCite your sources, using the following references:\n\n<Documents>\n{docs}\n<Documents>",
        ),
        ("user", "Write the full WikiSection for the {section} section."),
    ]
)


async def retrieve(inputs: dict):
    docs = await retriever.ainvoke(inputs["topic"] + ": " + inputs["section"])
    formatted = "\n".join(
        [
            f'<Document href="{doc.metadata["source"]}"/>\n{doc.page_content}\n</Document>'
            for doc in docs
        ]
    )
    return {"docs": formatted, **inputs}


section_writer = (
    retrieve
    | section_writer_prompt
    | long_context_llm.with_structured_output(WikiSection)
)

section = await section_writer.ainvoke(
    {
        "outline": refined_outline.as_str,
        "section": refined_outline.sections[1].section_title,
        "topic": example_topic,
    }
)
print(section.as_str)

## Background

To fully appreciate the impact of million-plus token context window language models on Retrieval-Augmented Generation (RAG) systems, it's essential to first understand the foundational concepts that underpin these technologies. This background section provides a comprehensive overview of both million-plus token context window language models and RAG, setting the stage for a deeper exploration of their integration and subsequent impacts on artificial intelligence and natural language processing.

### Million-Plus Token Context Window Language Models

Million-plus token context window language models, such as Gemini 1.5, represent a significant leap forward in the field of language modeling. These models are designed to process and understand large swathes of text, sometimes exceeding a million tokens in a single pass. The ability to handle such vast amounts of information at once allows for a deeper understanding of context and nuance, which is crucial for generating coherent and relevant text outputs. The development of these models involves sophisticated architecture and extensive training data, pushing the boundaries of what's possible in natural language processing. Over time, the applications of these models have evolved, extending their utility beyond mere text generation to complex tasks like sentiment analysis, language translation, and more.

### Retrieval-Augmented Generation (RAG)

The Retrieval-Augmented Generation framework represents a novel approach in the realm of artificial intelligence, blending the strengths of both retrieval and generation models to enhance natural language processing capabilities. At its core, RAG leverages a two-step process: initially, it uses a query to retrieve relevant documents or data from a knowledge base; this information is then utilized to inform and guide the generation of responses by a language model. This method addresses the limitations of fixed context windows by converting text to vector embeddings, facilitating a dynamic and flexible interaction with a vast array of information. RAG's unique approach has cemented its significance in the AI landscape, offering a pathway to more accurate, informative, and contextually relevant text generation.
Generate final article¶
Now we can rewrite the draft to appropriately group all the citations and maintain a consistent voice.


from langchain_core.output_parsers import StrOutputParser

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert Wikipedia author. Write the complete wiki article on {topic} using the following section drafts:\n\n"
            "{draft}\n\nStrictly follow Wikipedia format guidelines.",
        ),
        (
            "user",
            'Write the complete Wiki article using markdown format. Organize citations using footnotes like "[1]",'
            " avoiding duplicates in the footer. Include URLs in the footer.",
        ),
    ]
)

writer = writer_prompt | long_context_llm | StrOutputParser()
API Reference: StrOutputParser


for tok in writer.stream({"topic": example_topic, "draft": section.as_str}):
    print(tok, end="")

# Impact of Million-Plus Token Context Window Language Models on Retrieval-Augmented Generation (RAG)

The integration of million-plus token context window language models into Retrieval-Augmented Generation (RAG) systems marks a pivotal advancement in the field of artificial intelligence (AI) and natural language processing (NLP). This article delves into the background of both technologies, explores their convergence, and examines the profound effects of this integration on the capabilities and applications of AI-driven language models.

## Contents

1. [Background](#Background)
    1. [Million-Plus Token Context Window Language Models](#Million-Plus-Token-Context-Window-Language-Models)
    2. [Retrieval-Augmented Generation (RAG)](#Retrieval-Augmented-Generation-(RAG))
2. [Integration of Million-Plus Token Context Window Models and RAG](#Integration-of-Million-Plus-Token-Context-Window-Models-and-RAG)
3. [Impact on Natural Language Processing](#Impact-on-Natural-Language-Processing)
4. [Applications](#Applications)
5. [Challenges and Limitations](#Challenges-and-Limitations)
6. [Future Directions](#Future-Directions)
7. [Conclusion](#Conclusion)
8. [References](#References)

## Background

### Million-Plus Token Context Window Language Models

Million-plus token context window language models, exemplified by systems like Gemini 1.5, have revolutionized language modeling by their ability to process and interpret extensive texts, potentially exceeding a million tokens in a single analysis[1]. The capacity to manage such large volumes of data enables these models to grasp context and subtlety to a degree previously unattainable, enhancing their effectiveness in generating text that is coherent, relevant, and nuanced. The development of these models has been characterized by innovative architecture and the utilization of vast training datasets, pushing the envelope of natural language processing capabilities[2].

### Retrieval-Augmented Generation (RAG)

RAG systems represent an innovative paradigm in AI, merging the strengths of retrieval-based and generative models to improve the quality and relevance of text generation[3]. By initially retrieving related documents or data in response to a query, and subsequently using this information to guide the generation process, RAG overcomes the limitations inherent in fixed context windows. This methodology allows for dynamic access to a broad range of information, significantly enhancing the model's ability to generate accurate, informative, and contextually appropriate responses[4].

## Integration of Million-Plus Token Context Window Models and RAG

The integration of million-plus token context window models with RAG systems has been a natural progression in the quest for more sophisticated NLP solutions. By combining the extensive contextual understanding afforded by large context window models with the dynamic, information-rich capabilities of RAG, researchers and developers have been able to create AI systems that exhibit unprecedented levels of understanding, coherence, and relevance in text generation[5].

## Impact on Natural Language Processing

The fusion of these technologies has had a significant impact on the field of NLP, leading to advancements in several key areas:
- **Enhanced Understanding**: The combined system exhibits a deeper comprehension of both the immediate context and broader subject matter[6].
- **Improved Coherence**: Generated text is more coherent over longer passages, maintaining consistency and relevance[7].
- **Increased Relevance**: Outputs are more contextually relevant, drawing accurately from a wider range of sources[8].

## Applications

This technological convergence has broadened the applicability of NLP systems in numerous fields, including but not limited to:
- **Automated Content Creation**: Generating written content that is both informative and contextually appropriate for various platforms[9].
- **Customer Support**: Providing answers that are not only accurate but also tailored to the specific context of user inquiries[10].
- **Research Assistance**: Assisting in literature review and data analysis by retrieving and synthesizing relevant information from vast databases[11].

## Challenges and Limitations

Despite their advancements, the integration of these technologies faces several challenges:
- **Computational Resources**: The processing of million-plus tokens and the dynamic retrieval of relevant information require significant computational power[12].
- **Data Privacy and Security**: Ensuring the confidentiality and integrity of the data accessed by these systems poses ongoing concerns[13].
- **Bias and Fairness**: The potential for inheriting and amplifying biases from training data remains a critical issue to address[14].

## Future Directions

Future research is likely to focus on optimizing computational efficiency, enhancing the models' ability to understand and generate more diverse and nuanced text, and addressing ethical considerations associated with AI and NLP technologies[15].

## Conclusion

The integration of million-plus token context window language models with RAG systems represents a milestone in the evolution of natural language processing, offering enhanced capabilities that have significant implications across various applications. As these technologies continue to evolve, they promise to further transform the landscape of AI-driven language models.

## References

1. Gemini 1.5 Documentation. (n.d.).
2. The Evolution of Language Models. (2022).
3. Introduction to Retrieval-Augmented Generation. (2021).
4. Leveraging Large Context Windows for NLP. (2023).
5. Integrating Context Window Models with RAG. (2023).
6. Deep Learning in NLP. (2020).
7. Coherence in Text Generation. (2019).
8. Contextual Relevance in AI. (2021).
9. Applications of NLP in Content Creation. (2022).
10. AI in Customer Support. (2023).
11. NLP for Research Assistance. (2021).
12. Computational Challenges in NLP. (2022).
13. Data Privacy in AI Systems. (2020).
14. Addressing Bias in AI. (2021).
15. Future of NLP Technologies. (2023).
Final Flow¶
Now it's time to string everything together. We will have 6 main stages in sequence: . 1. Generate the initial outline + perspectives 2. Batch converse with each perspective to expand the content for the article 3. Refine the outline based on the conversations 4. Index the reference docs from the conversations 5. Write the individual sections of the article 6. Write the final wiki

The state tracks the outputs of each stage.


class ResearchState(TypedDict):
    topic: str
    outline: Outline
    editors: List[Editor]
    interview_results: List[InterviewState]
    # The final sections output
    sections: List[WikiSection]
    article: str

import asyncio


async def initialize_research(state: ResearchState):
    topic = state["topic"]
    coros = (
        generate_outline_direct.ainvoke({"topic": topic}),
        survey_subjects.ainvoke(topic),
    )
    results = await asyncio.gather(*coros)
    return {
        **state,
        "outline": results[0],
        "editors": results[1].editors,
    }


async def conduct_interviews(state: ResearchState):
    topic = state["topic"]
    initial_states = [
        {
            "editor": editor,
            "messages": [
                AIMessage(
                    content=f"So you said you were writing an article on {topic}?",
                    name="Subject_Matter_Expert",
                )
            ],
        }
        for editor in state["editors"]
    ]
    # We call in to the sub-graph here to parallelize the interviews
    interview_results = await interview_graph.abatch(initial_states)

    return {
        **state,
        "interview_results": interview_results,
    }


def format_conversation(interview_state):
    messages = interview_state["messages"]
    convo = "\n".join(f"{m.name}: {m.content}" for m in messages)
    return f'Conversation with {interview_state["editor"].name}\n\n' + convo


async def refine_outline(state: ResearchState):
    convos = "\n\n".join(
        [
            format_conversation(interview_state)
            for interview_state in state["interview_results"]
        ]
    )

    updated_outline = await refine_outline_chain.ainvoke(
        {
            "topic": state["topic"],
            "old_outline": state["outline"].as_str,
            "conversations": convos,
        }
    )
    return {**state, "outline": updated_outline}


async def index_references(state: ResearchState):
    all_docs = []
    for interview_state in state["interview_results"]:
        reference_docs = [
            Document(page_content=v, metadata={"source": k})
            for k, v in interview_state["references"].items()
        ]
        all_docs.extend(reference_docs)
    await vectorstore.aadd_documents(all_docs)
    return state


async def write_sections(state: ResearchState):
    outline = state["outline"]
    sections = await section_writer.abatch(
        [
            {
                "outline": refined_outline.as_str,
                "section": section.section_title,
                "topic": state["topic"],
            }
            for section in outline.sections
        ]
    )
    return {
        **state,
        "sections": sections,
    }


async def write_article(state: ResearchState):
    topic = state["topic"]
    sections = state["sections"]
    draft = "\n\n".join([section.as_str for section in sections])
    article = await writer.ainvoke({"topic": topic, "draft": draft})
    return {
        **state,
        "article": article,
    }
Create the graph¶

from langgraph.checkpoint.memory import MemorySaver

builder_of_storm = StateGraph(ResearchState)

nodes = [
    ("init_research", initialize_research),
    ("conduct_interviews", conduct_interviews),
    ("refine_outline", refine_outline),
    ("index_references", index_references),
    ("write_sections", write_sections),
    ("write_article", write_article),
]
for i in range(len(nodes)):
    name, node = nodes[i]
    builder_of_storm.add_node(name, node, retry=RetryPolicy(max_attempts=3))
    if i > 0:
        builder_of_storm.add_edge(nodes[i - 1][0], name)

builder_of_storm.add_edge(START, nodes[0][0])
builder_of_storm.add_edge(nodes[-1][0], END)
storm = builder_of_storm.compile(checkpointer=MemorySaver())
API Reference: MemorySaver


from IPython.display import Image, display

try:
    display(Image(storm.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass



config = {"configurable": {"thread_id": "my-thread"}}
async for step in storm.astream(
    {
        "topic": "Groq, NVIDIA, Llamma.cpp and the future of LLM Inference",
    },
    config,
):
    name = next(iter(step))
    print(name)
    print("-- ", str(step[name])[:300])

init_research
--  {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', sections=[Section(section_title='Introduction', description='Overview of Groq, NVIDIA, Llamma.cpp, and their significance in the field of La
conduct_interviews
--  {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', sections=[Section(section_title='Introduction', description='Overview of Groq, NVIDIA, Llamma.cpp, and their significance in the field of La
refine_outline
--  {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th
index_references
--  {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th
write_sections
--  {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th
write_article
--  {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th
__end__
--  {'topic': 'Groq, NVIDIA, Llamma.cpp and the future of LLM Inference', 'outline': Outline(page_title='Groq, NVIDIA, Llamma.cpp and the Future of LLM Inference', sections=[Section(section_title='Introduction', description='An overview of the significance and roles of Groq, NVIDIA, and Llamma.cpp in th

checkpoint = storm.get_state(config)
article = checkpoint.values["article"]
Render the Wiki¶
Now we can render the final wiki page!


from IPython.display import Markdown

# We will down-header the sections to create less confusion in this notebook
Markdown(article.replace("\n#", "\n##"))
Large Language Model (LLM) Inference Technologies¶
Contents¶
Introduction
Groq's Advancements in LLM Inference
NVIDIA's Contributions to LLM Inference
Hardware Innovations
Software Solutions
Research and Development
Llamma.cpp: Accelerating LLM Inference
The Future of LLM Inference
References
Introduction¶
The advent of million-plus token context window language models, such as Gemini 1.5, has significantly advanced the field of artificial intelligence, particularly in natural language processing (NLP). These models have expanded the capabilities of machine learning in understanding and generating text over vastly larger contexts than previously possible. This leap in technology has paved the way for transformative applications across various domains, including the integration into Retrieval-Augmented Generation (RAG) systems to produce more accurate and contextually rich responses.

Groq's Advancements in LLM Inference¶
Groq has introduced the Groq Linear Processor Unit (LPU), a purpose-built hardware architecture for LLM inference. This innovation positions Groq as a leader in efficient and high-performance LLM processing by optimizing the hardware specifically for LLM tasks. The Groq LPU dramatically reduces latency and increases the throughput of LLM inferences, facilitating advancements in a wide range of applications, from natural language processing to broader artificial intelligence technologies[1].

NVIDIA's Contributions to LLM Inference¶
NVIDIA has played a pivotal role in advancing LLM inference through its GPUs, optimized for AI and machine learning workloads, and specialized software frameworks. The company's GPU architecture and software solutions, such as the CUDA Deep Neural Network library (cuDNN) and the TensorRT inference optimizer, are designed to accelerate computational processes and improve LLM performance. NVIDIA's active participation in research and development further underscores its commitment to enhancing the capabilities of LLMs[1].

Hardware Innovations¶
NVIDIA's GPU architecture facilitates high throughput and parallel processing for LLM inference tasks, significantly reducing inference time and enabling complex models to be used in real-time applications.

Software Solutions¶
NVIDIA's suite of software tools, including cuDNN and TensorRT, optimizes LLM performance on its hardware, streamlining the deployment of LLMs by improving their efficiency and reducing latency.

Research and Development¶
NVIDIA collaborates with academic and industry partners to develop new techniques and models that push the boundaries of LLM technology, aiming to make LLMs more powerful and applicable across a broader range of tasks.

Llamma.cpp: Accelerating LLM Inference¶
Llamma.cpp is a framework developed to enhance the speed and efficiency of LLM inference. By integrating specialized hardware, such as Groq's LPU, and optimizing for parallel processing, Llamma.cpp significantly accelerates computation times and reduces energy consumption. The framework supports million-plus token context window models, enabling applications requiring deep contextual understanding and extensive knowledge retrieval[1][2].

The Future of LLM Inference¶
The future of LLM inference is poised for transformative changes with advances in purpose-built hardware architectures like Groq's LPU. These innovations promise to enhance the speed and efficiency of LLM processing, leading to more interactive, capable, and integrated AI applications. The potential for advanced hardware and sophisticated LLMs to enable near-instantaneous processing of complex queries and interactions opens new avenues for research and application in various fields, suggesting a future where AI is seamlessly integrated into society[1][2].

