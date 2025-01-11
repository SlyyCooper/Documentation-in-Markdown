Plan-and-Execute¶
This notebook shows how to create a "plan-and-execute" style agent. This is heavily inspired by the Plan-and-Solve paper as well as the Baby-AGI project.

The core idea is to first come up with a multi-step plan, and then go through that plan one item at a time. After accomplishing a particular task, you can then revisit the plan and modify as appropriate.

The general computational graph looks like the following:

plan-and-execute diagram

This compares to a typical ReAct style agent where you think one step at a time. The advantages of this "plan-and-execute" style agent are:

Explicit long term planning (which even really strong LLMs can struggle with)
Ability to use smaller/weaker models for the execution step, only using larger/better models for the planning step
The following walkthrough demonstrates how to do so in LangGraph. The resulting agent will leave a trace like the following example: (link).

Setup¶
First, we need to install the packages required.


%%capture --no-stderr
%pip install --quiet -U langgraph langchain-community langchain-openai tavily-python
Next, we need to set API keys for OpenAI (the LLM we will use) and Tavily (the search tool we will use)


import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("OPENAI_API_KEY")
_set_env("TAVILY_API_KEY")
Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started here.

Define Tools¶
We will first define the tools we want to use. For this simple example, we will use a built-in search tool via Tavily. However, it is really easy to create your own tools - see documentation here on how to do that.


from langchain_community.tools.tavily_search import TavilySearchResults

tools = [TavilySearchResults(max_results=3)]
API Reference: TavilySearchResults

Define our Execution Agent¶
Now we will create the execution agent we want to use to execute tasks. Note that for this example, we will be using the same execution agent for each task, but this doesn't HAVE to be the case.


from langchain import hub
from langchain_openai import ChatOpenAI

from langgraph.prebuilt import create_react_agent

# Get the prompt to use - you can modify this!
prompt = hub.pull("ih/ih-react-agent-executor")
prompt.pretty_print()

# Choose the LLM that will drive the agent
llm = ChatOpenAI(model="gpt-4-turbo-preview")
agent_executor = create_react_agent(llm, tools, state_modifier=prompt)
API Reference: ChatOpenAI | create_react_agent


================================[1m System Message [0m================================

You are a helpful assistant.

=============================[1m Messages Placeholder [0m=============================

[33;1m[1;3m{messages}[0m

agent_executor.invoke({"messages": [("user", "who is the winnner of the us open")]})

{'messages': [HumanMessage(content='who is the winnner of the us open', additional_kwargs={}, response_metadata={}, id='388a14b3-f556-4f91-ad36-def0a075638e'),
  AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_5nbeRa0fgh4ZslRkjk75Kzxs', 'function': {'arguments': '{"query":"US Open 2023 winner"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 23, 'prompt_tokens': 97, 'total_tokens': 120, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4-0125-preview', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-3bb25f7a-49e5-43b7-ad53-718bd0107db1-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'US Open 2023 winner'}, 'id': 'call_5nbeRa0fgh4ZslRkjk75Kzxs', 'type': 'tool_call'}], usage_metadata={'input_tokens': 97, 'output_tokens': 23, 'total_tokens': 120}),
  ToolMessage(content='[{"url": "https://www.youtube.com/watch?v=rZ0XQWWFIAo", "content": "The moment Coco Gauff beat Aryna Sabalenka in the final of the 2023 US Open.Don\'t miss a moment of the US Open! Subscribe now: https://bit.ly/2Pdr81iThe 2023..."}, {"url": "https://www.cbssports.com/tennis/news/us-open-2023-scores-novak-djokovic-makes-history-with-24th-grand-slam-title-while-coco-gauff-earns-her-first/", "content": "Here is all you need to know about the 2023 US Open:\\nMen\'s final\\nWomen\'s final\\nMen\'s singles seeds\\nWomen\'s singles seeds\\nOur Latest Tennis Stories\\nUS Open 2023: Schedule, scores, how to watch, seeds\\nRafael Nadal to return next month at Brisbane\\nNovak Djokovic breaks Federer\'s ATP Finals record\\nTennis bettor wins $486,000 off $28 on 10-match parlay\\nTennis player DQ\'d on match point for hitting umpire\\nRafael Nadal says Novak Djokovic is tennis\' GOAT\\nHalep suspended four years for anti-doping violations\\nDjokovic pays tribute to Kobe after winning US Open\\nDjokovic vs. Medvedev odds, US Open final picks, bets\\nAryna Sabalenka-Coco Gauff odds, US Open final picks\\n© 2004-2023 CBS Interactive. Novak Djokovic makes history with 24th Grand Slam title, while Coco Gauff earns her first\\nThe 2023 US Open is officially in the books\\nThe 2023 US open came to a close as Coco Gauff earned her first major title and Novak Djokovic made history with his 24th Grand Slam trophy. Gauff is the first woman to win the Cincinnati Masters 1000 and US Open in the same year since Williams in 2014.\\n Gauff landed in New York as the No. 6 player in the world but will be climbing to a career-best No. 3 when the next rankings get released.\\n He arrived to this competition as the world No. 2 but will improve to No. 1 in the next rankings, extending his record total of 389 weeks at the top.\\n"}, {"url": "https://www.usopen.org/en_US/news/articles/2023-09-10/novak_djokovic_wins_24th_grand_slam_singles_title_at_2023_us_open.html", "content": "Novak Djokovic defeated Daniil Medvedev in three sets to claim his 24th Grand Slam singles title and match Margaret Court\'s all-time record. The Serb saved a set point in the second set and attacked the net to win his fourth US Open crown."}]', name='tavily_search_results_json', id='3ea00623-86b3-4d6f-9978-3503a7eecf0f', tool_call_id='call_5nbeRa0fgh4ZslRkjk75Kzxs', artifact={'query': 'US Open 2023 winner', 'follow_up_questions': None, 'answer': None, 'images': [], 'results': [{'title': "Championship Point | Coco Gauff Wins Women's Singles Title | 2023 US Open", 'url': 'https://www.youtube.com/watch?v=rZ0XQWWFIAo', 'content': "The moment Coco Gauff beat Aryna Sabalenka in the final of the 2023 US Open.Don't miss a moment of the US Open! Subscribe now: https://bit.ly/2Pdr81iThe 2023...", 'score': 0.9975177, 'raw_content': None}, {'title': 'US Open 2023 scores: Novak Djokovic makes history with 24th Grand Slam ...', 'url': 'https://www.cbssports.com/tennis/news/us-open-2023-scores-novak-djokovic-makes-history-with-24th-grand-slam-title-while-coco-gauff-earns-her-first/', 'content': "Here is all you need to know about the 2023 US Open:\nMen's final\nWomen's final\nMen's singles seeds\nWomen's singles seeds\nOur Latest Tennis Stories\nUS Open 2023: Schedule, scores, how to watch, seeds\nRafael Nadal to return next month at Brisbane\nNovak Djokovic breaks Federer's ATP Finals record\nTennis bettor wins $486,000 off $28 on 10-match parlay\nTennis player DQ'd on match point for hitting umpire\nRafael Nadal says Novak Djokovic is tennis' GOAT\nHalep suspended four years for anti-doping violations\nDjokovic pays tribute to Kobe after winning US Open\nDjokovic vs. Medvedev odds, US Open final picks, bets\nAryna Sabalenka-Coco Gauff odds, US Open final picks\n© 2004-2023 CBS Interactive. Novak Djokovic makes history with 24th Grand Slam title, while Coco Gauff earns her first\nThe 2023 US Open is officially in the books\nThe 2023 US open came to a close as Coco Gauff earned her first major title and Novak Djokovic made history with his 24th Grand Slam trophy. Gauff is the first woman to win the Cincinnati Masters 1000 and US Open in the same year since Williams in 2014.\n Gauff landed in New York as the No. 6 player in the world but will be climbing to a career-best No. 3 when the next rankings get released.\n He arrived to this competition as the world No. 2 but will improve to No. 1 in the next rankings, extending his record total of 389 weeks at the top.\n", 'score': 0.9937101, 'raw_content': None}, {'title': 'Novak Djokovic wins 24th Grand Slam singles title at 2023 US Open', 'url': 'https://www.usopen.org/en_US/news/articles/2023-09-10/novak_djokovic_wins_24th_grand_slam_singles_title_at_2023_us_open.html', 'content': "Novak Djokovic defeated Daniil Medvedev in three sets to claim his 24th Grand Slam singles title and match Margaret Court's all-time record. The Serb saved a set point in the second set and attacked the net to win his fourth US Open crown.", 'score': 0.8146434, 'raw_content': None}], 'response_time': 2.24}),
  AIMessage(content="The winners of the 2023 US Open are Coco Gauff and Novak Djokovic. Coco Gauff won her first major title at the US Open, making history, while Novak Djokovic secured his 24th Grand Slam title, matching Margaret Court's all-time record and winning his fourth US Open crown. Coco Gauff defeated Aryna Sabalenka in the final, and Novak Djokovic defeated Daniil Medvedev.", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 93, 'prompt_tokens': 751, 'total_tokens': 844, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-4-0125-preview', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-eedb1782-6120-441d-ab5d-ccf6bef75b02-0', usage_metadata={'input_tokens': 751, 'output_tokens': 93, 'total_tokens': 844})]}
Define the State¶
Let's now start by defining the state the track for this agent.

First, we will need to track the current plan. Let's represent that as a list of strings.

Next, we should track previously executed steps. Let's represent that as a list of tuples (these tuples will contain the step and then the result)

Finally, we need to have some state to represent the final response as well as the original input.


import operator
from typing import Annotated, List, Tuple
from typing_extensions import TypedDict


class PlanExecute(TypedDict):
    input: str
    plan: List[str]
    past_steps: Annotated[List[Tuple], operator.add]
    response: str
Planning Step¶
Let's now think about creating the planning step. This will use function calling to create a plan.

Using Pydantic with LangChain

This notebook uses Pydantic v2 BaseModel, which requires langchain-core >= 0.3. Using langchain-core < 0.3 will result in errors due to mixing of Pydantic v1 and v2 BaseModels.


from pydantic import BaseModel, Field


class Plan(BaseModel):
    """Plan to follow in future"""

    steps: List[str] = Field(
        description="different steps to follow, should be in sorted order"
    )

from langchain_core.prompts import ChatPromptTemplate

planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.""",
        ),
        ("placeholder", "{messages}"),
    ]
)
planner = planner_prompt | ChatOpenAI(
    model="gpt-4o", temperature=0
).with_structured_output(Plan)
API Reference: ChatPromptTemplate


planner.invoke(
    {
        "messages": [
            ("user", "what is the hometown of the current Australia open winner?")
        ]
    }
)

Plan(steps=['Identify the current winner of the Australia Open.', 'Find the hometown of the identified winner.'])
Re-Plan Step¶
Now, let's create a step that re-does the plan based on the result of the previous step.


from typing import Union


class Response(BaseModel):
    """Response to user."""

    response: str


class Act(BaseModel):
    """Action to perform."""

    action: Union[Response, Plan] = Field(
        description="Action to perform. If you want to respond to user, use Response. "
        "If you need to further use tools to get the answer, use Plan."
    )


replanner_prompt = ChatPromptTemplate.from_template(
    """For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.

Your objective was this:
{input}

Your original plan was this:
{plan}

You have currently done the follow steps:
{past_steps}

Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan."""
)


replanner = replanner_prompt | ChatOpenAI(
    model="gpt-4o", temperature=0
).with_structured_output(Act)
Create the Graph¶
We can now create the graph!


from typing import Literal
from langgraph.graph import END


async def execute_step(state: PlanExecute):
    plan = state["plan"]
    plan_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(plan))
    task = plan[0]
    task_formatted = f"""For the following plan:
{plan_str}\n\nYou are tasked with executing step {1}, {task}."""
    agent_response = await agent_executor.ainvoke(
        {"messages": [("user", task_formatted)]}
    )
    return {
        "past_steps": [(task, agent_response["messages"][-1].content)],
    }


async def plan_step(state: PlanExecute):
    plan = await planner.ainvoke({"messages": [("user", state["input"])]})
    return {"plan": plan.steps}


async def replan_step(state: PlanExecute):
    output = await replanner.ainvoke(state)
    if isinstance(output.action, Response):
        return {"response": output.action.response}
    else:
        return {"plan": output.action.steps}


def should_end(state: PlanExecute):
    if "response" in state and state["response"]:
        return END
    else:
        return "agent"
API Reference: END


from langgraph.graph import StateGraph, START

workflow = StateGraph(PlanExecute)

# Add the plan node
workflow.add_node("planner", plan_step)

# Add the execution step
workflow.add_node("agent", execute_step)

# Add a replan node
workflow.add_node("replan", replan_step)

workflow.add_edge(START, "planner")

# From plan we go to agent
workflow.add_edge("planner", "agent")

# From agent, we replan
workflow.add_edge("agent", "replan")

workflow.add_conditional_edges(
    "replan",
    # Next, we pass in the function that will determine which node is called next.
    should_end,
    ["agent", END],
)

# Finally, we compile it!
# This compiles it into a LangChain Runnable,
# meaning you can use it as you would any other runnable
app = workflow.compile()
API Reference: StateGraph | START


from IPython.display import Image, display

display(Image(app.get_graph(xray=True).draw_mermaid_png()))



config = {"recursion_limit": 50}
inputs = {"input": "what is the hometown of the mens 2024 Australia open winner?"}
async for event in app.astream(inputs, config=config):
    for k, v in event.items():
        if k != "__end__":
            print(v)

{'plan': ["Identify the winner of the men's 2024 Australian Open.", 'Research the hometown of the identified winner.']}
{'past_steps': [("Identify the winner of the men's 2024 Australian Open.", "The winner of the men's singles tennis title at the 2024 Australian Open was Jannik Sinner. He defeated Daniil Medvedev in the final with scores of 3-6, 3-6, 6-4, 6-4, 6-3 to win his first major singles title.")]}
{'plan': ['Research the hometown of Jannik Sinner.']}
{'past_steps': [('Research the hometown of Jannik Sinner.', "Jannik Sinner's hometown is Sexten, which is located in northern Italy.")]}
{'response': "The hometown of the men's 2024 Australian Open winner, Jannik Sinner, is Sexten, located in northern Italy."}
Conclusion¶
Congrats on making a plan-and-execute agent! One known limitations of the above design is that each task is still executed in sequence, meaning embarrassingly parallel operations all add to the total execution time. You could improve on this by having each task represented as a DAG (similar to LLMCompiler), rather than a regular list.