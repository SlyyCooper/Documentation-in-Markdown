## Table of Contents

- [How to create map-reduce branches for parallel execution¶](#how-to-create-map-reduce-branches-for-parallel-execution)
  - [Setup¶](#setup)
  - [Define the graph¶](#define-the-graph)
  - [Use the graph¶](#use-the-graph)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to create map-reduce branches for parallel execution

Initializing search

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 
  * Conceptual Guides 
  * Reference 

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 

How-to Guides

    * LangGraph  LangGraph 
      * LangGraph 
      * Controllability  Controllability 
        * Controllability 
        * How to create branches for parallel node execution 
        * How to create map-reduce branches for parallel execution  How to create map-reduce branches for parallel execution  Table of contents 
          * Setup 
          * Define the graph 
          * Use the graph 
        * How to control graph recursion limit 
        * How to combine control flow and state updates with Command 
      * Persistence 
      * Memory 
      * Human-in-the-loop 
      * Streaming 
      * Tool calling 
      * Subgraphs 
      * Multi-agent 
      * State Management 
      * Other 
      * Prebuilt ReAct Agent 
    * LangGraph Platform  LangGraph Platform 
      * LangGraph Platform 
      * Application Structure 
      * Deployment 
      * Authentication & Access Control 
      * Assistants 
      * Threads 
      * Runs 
      * Streaming 
      * Human-in-the-loop 
      * Double-texting 
      * Webhooks 
      * Cron Jobs 
      * LangGraph Studio 
    * Troubleshooting 

Troubleshooting

      * Troubleshooting 
      * GRAPH_RECURSION_LIMIT 
      * INVALID_CONCURRENT_GRAPH_UPDATE 
      * INVALID_GRAPH_NODE_RETURN_VALUE 
      * MULTIPLE_SUBGRAPHS 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Setup 
  * Define the graph 
  * Use the graph 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Controllability 

# How to create map-reduce branches for parallel execution¶

Prerequisites

This guide assumes familiarity with the following:

  * LangGraph Glossary 
  * Send API 
  * Chat Models 
  * Structured Output 

Map-reduce operations are essential for efficient task decomposition and
parallel processing. This approach involves breaking a task into smaller sub-
tasks, processing each sub-task in parallel, and aggregating the results
across all of the completed sub-tasks.

Consider this example: given a general topic from the user, generate a list of
related subjects, generate a joke for each subject, and select the best joke
from the resulting list. In this design pattern, a first node may generate a
list of objects (e.g., related subjects) and we want to apply some other node
(e.g., generate a joke) to all those objects (e.g., subjects). However, two
main challenges arise.

(1) the number of objects (e.g., subjects) may be unknown ahead of time
(meaning the number of edges may not be known) when we lay out the graph and
(2) the input State to the downstream Node should be different (one for each
generated object).

LangGraph addresses these challenges through its `Send` API. By utilizing
conditional edges, `Send` can distribute different states (e.g., subjects) to
multiple instances of a node (e.g., joke generation). Importantly, the sent
state can differ from the core graph's state, allowing for flexible and
dynamic workflow management.

## Setup¶

First, let's install the required packages and set our API keys

    
    
    %%capture --no-stderr
    %pip install -U langchain-anthropic langgraph
    
    
    
    import os
    import getpass
    
    
    def _set_env(name: str):
        if not os.getenv(name):
            os.environ[name] = getpass.getpass(f"{name}: ")
    
    
    _set_env("ANTHROPIC_API_KEY")
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Define the graph¶

Using Pydantic with LangChain

This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >=
0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of
Pydantic v1 and v2 `BaseModels`.

    
    
    import operator
    from typing import Annotated
    from typing_extensions import TypedDict
    
    from langchain_anthropic import ChatAnthropic
    
    from langgraph.types import Send
    from langgraph.graph import END, StateGraph, START
    
    from pydantic import BaseModel, Field
    
    # Model and prompts
    # Define model and prompts we will use
    subjects_prompt = """Generate a comma separated list of between 2 and 5 examples related to: {topic}."""
    joke_prompt = """Generate a joke about {subject}"""
    best_joke_prompt = """Below are a bunch of jokes about {topic}. Select the best one! Return the ID of the best one.
    
    {jokes}"""
    
    
    class Subjects(BaseModel):
        subjects: list[str]
    
    
    class Joke(BaseModel):
        joke: str
    
    
    class BestJoke(BaseModel):
        id: int = Field(description="Index of the best joke, starting with 0", ge=0)
    
    
    model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    
    # Graph components: define the components that will make up the graph
    
    
    # This will be the overall state of the main graph.
    # It will contain a topic (which we expect the user to provide)
    # and then will generate a list of subjects, and then a joke for
    # each subject
    class OverallState(TypedDict):
        topic: str
        subjects: list
        # Notice here we use the operator.add
        # This is because we want combine all the jokes we generate
        # from individual nodes back into one list - this is essentially
        # the "reduce" part
        jokes: Annotated[list, operator.add]
        best_selected_joke: str
    
    
    # This will be the state of the node that we will "map" all
    # subjects to in order to generate a joke
    class JokeState(TypedDict):
        subject: str
    
    
    # This is the function we will use to generate the subjects of the jokes
    def generate_topics(state: OverallState):
        prompt = subjects_prompt.format(topic=state["topic"])
        response = model.with_structured_output(Subjects).invoke(prompt)
        return {"subjects": response.subjects}
    
    
    # Here we generate a joke, given a subject
    def generate_joke(state: JokeState):
        prompt = joke_prompt.format(subject=state["subject"])
        response = model.with_structured_output(Joke).invoke(prompt)
        return {"jokes": [response.joke]}
    
    
    # Here we define the logic to map out over the generated subjects
    # We will use this an edge in the graph
    def continue_to_jokes(state: OverallState):
        # We will return a list of `Send` objects
        # Each `Send` object consists of the name of a node in the graph
        # as well as the state to send to that node
        return [Send("generate_joke", {"subject": s}) for s in state["subjects"]]
    
    
    # Here we will judge the best joke
    def best_joke(state: OverallState):
        jokes = "\n\n".join(state["jokes"])
        prompt = best_joke_prompt.format(topic=state["topic"], jokes=jokes)
        response = model.with_structured_output(BestJoke).invoke(prompt)
        return {"best_selected_joke": state["jokes"][response.id]}
    
    
    # Construct the graph: here we put everything together to construct our graph
    graph = StateGraph(OverallState)
    graph.add_node("generate_topics", generate_topics)
    graph.add_node("generate_joke", generate_joke)
    graph.add_node("best_joke", best_joke)
    graph.add_edge(START, "generate_topics")
    graph.add_conditional_edges("generate_topics", continue_to_jokes, ["generate_joke"])
    graph.add_edge("generate_joke", "best_joke")
    graph.add_edge("best_joke", END)
    app = graph.compile()
    

API Reference: ChatAnthropic | Send | END | StateGraph | START
    
    
    from IPython.display import Image
    
    Image(app.get_graph().draw_mermaid_png())
    

## Use the graph¶

    
    
    # Call the graph: here we call it to generate a list of jokes
    for s in app.stream({"topic": "animals"}):
        print(s)
    
    
    
    {'generate_topics': {'subjects': ['Lions', 'Elephants', 'Penguins', 'Dolphins']}}
    {'generate_joke': {'jokes': ["Why don't elephants use computers? They're afraid of the mouse!"]}}
    {'generate_joke': {'jokes': ["Why don't dolphins use smartphones? Because they're afraid of phishing!"]}}
    {'generate_joke': {'jokes': ["Why don't you see penguins in Britain? Because they're afraid of Wales!"]}}
    {'generate_joke': {'jokes': ["Why don't lions like fast food? Because they can't catch it!"]}}
    {'best_joke': {'best_selected_joke': "Why don't dolphins use smartphones? Because they're afraid of phishing!"}}
    

## Comments

Back to top

Previous

How to create branches for parallel node execution

Next

How to control graph recursion limit

Made with  Material for MkDocs Insiders