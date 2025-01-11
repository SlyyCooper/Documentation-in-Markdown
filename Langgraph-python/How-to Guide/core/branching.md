## Table of Contents

- [How to create branches for parallel node execution¶](#how-to-create-branches-for-parallel-node-execution)
  - [Setup¶](#setup)
  - [Parallel node fan-out and fan-in¶](#parallel-node-fan-out-and-fan-in)
  - [Parallel node fan-out and fan-in with extra steps¶](#parallel-node-fan-out-and-fan-in-with-extra-steps)
  - [Conditional Branching¶](#conditional-branching)
  - [Stable Sorting¶](#stable-sorting)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to create branches for parallel node execution

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
        * How to create branches for parallel node execution  How to create branches for parallel node execution  Table of contents 
          * Setup 
          * Parallel node fan-out and fan-in 
          * Parallel node fan-out and fan-in with extra steps 
          * Conditional Branching 
          * Stable Sorting 
        * How to create map-reduce branches for parallel execution 
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
  * Parallel node fan-out and fan-in 
  * Parallel node fan-out and fan-in with extra steps 
  * Conditional Branching 
  * Stable Sorting 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Controllability 

# How to create branches for parallel node execution¶

Prerequisites

This guide assumes familiarity with the following:

  * Node 
  * Edge 
  * Reducer 

Parallel execution of nodes is essential to speed up overall graph operation.
LangGraph offers native support for parallel execution of nodes, which can
significantly enhance the performance of graph-based workflows. This
parallelization is achieved through fan-out and fan-in mechanisms, utilizing
both standard edges and conditional_edges. Below are some examples showing how
to add create branching dataflows that work for you.

## Setup¶

First, let's install the required packages

    
    
    %%capture --no-stderr
    %pip install -U langgraph
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Parallel node fan-out and fan-in¶

In this example, we fan out from `Node A` to `B and C` and then fan in to `D`.
With our state, we specify the reducer add operation. This will combine or
accumulate values for the specific key in the State, rather than simply
overwriting the existing value. For lists, this means concatenating the new
list with the existing list.

Note that LangGraph uses `Annotated` type to specify reducer functions for
specific keys in the State: it maintains the original type (`list`) for type
checking, but allows attaching the reducer function (`add`) to the type
without changing the type itself.

    
    
    import operator
    from typing import Annotated, Any
    
    from typing_extensions import TypedDict
    
    from langgraph.graph import StateGraph, START, END
    
    
    class State(TypedDict):
        # The operator.add reducer fn makes this append-only
        aggregate: Annotated[list, operator.add]
    
    
    class ReturnNodeValue:
        def __init__(self, node_secret: str):
            self._value = node_secret
    
        def __call__(self, state: State) -> Any:
            print(f"Adding {self._value} to {state['aggregate']}")
            return {"aggregate": [self._value]}
    
    
    builder = StateGraph(State)
    builder.add_node("a", ReturnNodeValue("I'm A"))
    builder.add_edge(START, "a")
    builder.add_node("b", ReturnNodeValue("I'm B"))
    builder.add_node("c", ReturnNodeValue("I'm C"))
    builder.add_node("d", ReturnNodeValue("I'm D"))
    builder.add_edge("a", "b")
    builder.add_edge("a", "c")
    builder.add_edge("b", "d")
    builder.add_edge("c", "d")
    builder.add_edge("d", END)
    graph = builder.compile()
    

API Reference: StateGraph | START | END
    
    
    from IPython.display import Image, display
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    

With the reducer, you can see that the values added in each node are
accumulated.

    
    
    graph.invoke({"aggregate": []}, {"configurable": {"thread_id": "foo"}})
    
    
    
    Adding I'm A to []
    Adding I'm B to ["I'm A"]
    Adding I'm C to ["I'm A"]
    Adding I'm D to ["I'm A", "I'm B", "I'm C"]
    
    
    
    {'aggregate': ["I'm A", "I'm B", "I'm C", "I'm D"]}
    

Exception handling?

LangGraph executes nodes within "supersteps", meaning that while parallel
branches are executed in parallel, the entire superstep is **transactional**.
If any of these branches raises an exception, **none** of the updates are
applied to the state (the entire superstep errors).  
  
If you have error-prone (perhaps want to handle flakey API calls), LangGraph
provides two ways to address this:  

  1. You can write regular python code within your node to catch and handle exceptions.
  2. You can set a **retry_policy** to direct the graph to retry nodes that raise certain types of exceptions. Only failing branches are retried, so you needn't worry about performing redundant work.

Together, these let you perform parallel execution and fully control exception
handling.

## Parallel node fan-out and fan-in with extra steps¶

The above example showed how to fan-out and fan-in when each path was only one
step. But what if one path had more than one step?

    
    
    import operator
    from typing import Annotated
    
    from typing_extensions import TypedDict
    
    from langgraph.graph import StateGraph
    
    
    class State(TypedDict):
        # The operator.add reducer fn makes this append-only
        aggregate: Annotated[list, operator.add]
    
    
    class ReturnNodeValue:
        def __init__(self, node_secret: str):
            self._value = node_secret
    
        def __call__(self, state: State) -> Any:
            print(f"Adding {self._value} to {state['aggregate']}")
            return {"aggregate": [self._value]}
    
    
    builder = StateGraph(State)
    builder.add_node("a", ReturnNodeValue("I'm A"))
    builder.add_edge(START, "a")
    builder.add_node("b", ReturnNodeValue("I'm B"))
    builder.add_node("b2", ReturnNodeValue("I'm B2"))
    builder.add_node("c", ReturnNodeValue("I'm C"))
    builder.add_node("d", ReturnNodeValue("I'm D"))
    builder.add_edge("a", "b")
    builder.add_edge("a", "c")
    builder.add_edge("b", "b2")
    builder.add_edge(["b2", "c"], "d")
    builder.add_edge("d", END)
    graph = builder.compile()
    

API Reference: StateGraph

    
    
    from IPython.display import Image, display
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    
    
    
    graph.invoke({"aggregate": []})
    
    
    
    Adding I'm A to []
    Adding I'm B to ["I'm A"]
    Adding I'm C to ["I'm A"]
    Adding I'm B2 to ["I'm A", "I'm B", "I'm C"]
    Adding I'm D to ["I'm A", "I'm B", "I'm C", "I'm B2"]
    
    
    
    {'aggregate': ["I'm A", "I'm B", "I'm C", "I'm B2", "I'm D"]}
    

## Conditional Branching¶

If your fan-out is not deterministic, you can use add_conditional_edges
directly.

If you have a known "sink" node that the conditional branches will route to
afterwards, you can provide `then=<final-node-name>` when creating the
conditional edges.

    
    
    import operator
    from typing import Annotated, Sequence
    
    from typing_extensions import TypedDict
    
    from langgraph.graph import END, START, StateGraph
    
    
    class State(TypedDict):
        # The operator.add reducer fn makes this append-only
        aggregate: Annotated[list, operator.add]
        which: str
    
    
    class ReturnNodeValue:
        def __init__(self, node_secret: str):
            self._value = node_secret
    
        def __call__(self, state: State) -> Any:
            print(f"Adding {self._value} to {state['aggregate']}")
            return {"aggregate": [self._value]}
    
    
    builder = StateGraph(State)
    builder.add_node("a", ReturnNodeValue("I'm A"))
    builder.add_edge(START, "a")
    builder.add_node("b", ReturnNodeValue("I'm B"))
    builder.add_node("c", ReturnNodeValue("I'm C"))
    builder.add_node("d", ReturnNodeValue("I'm D"))
    builder.add_node("e", ReturnNodeValue("I'm E"))
    
    
    def route_bc_or_cd(state: State) -> Sequence[str]:
        if state["which"] == "cd":
            return ["c", "d"]
        return ["b", "c"]
    
    
    intermediates = ["b", "c", "d"]
    builder.add_conditional_edges(
        "a",
        route_bc_or_cd,
        intermediates,
    )
    for node in intermediates:
        builder.add_edge(node, "e")
    
    
    builder.add_edge("e", END)
    graph = builder.compile()
    

API Reference: END | START | StateGraph
    
    
    from IPython.display import Image, display
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    
    
    
    graph.invoke({"aggregate": [], "which": "bc"})
    
    
    
    Adding I'm A to []
    Adding I'm B to ["I'm A"]
    Adding I'm C to ["I'm A"]
    Adding I'm E to ["I'm A", "I'm B", "I'm C"]
    
    
    
    {'aggregate': ["I'm A", "I'm B", "I'm C", "I'm E"], 'which': 'bc'}
    
    
    
    graph.invoke({"aggregate": [], "which": "cd"})
    
    
    
    Adding I'm A to []
    Adding I'm C to ["I'm A"]
    Adding I'm D to ["I'm A"]
    Adding I'm E to ["I'm A", "I'm C", "I'm D"]
    
    
    
    {'aggregate': ["I'm A", "I'm C", "I'm D", "I'm E"], 'which': 'cd'}
    

## Stable Sorting¶

When fanned out, nodes are run in parallel as a single "superstep". The
updates from each superstep are all applied to the state in sequence once the
superstep has completed.

If you need consistent, predetermined ordering of updates from a parallel
superstep, you should write the outputs (along with an identifying key) to a
separate field in your state, then combine them in the "sink" node by adding
regular `edge`'s from each of the fanout nodes to the rendezvous point.

For instance, suppose I want to order the outputs of the parallel step by
"reliability".

    
    
    import operator
    from typing import Annotated, Sequence
    
    from typing_extensions import TypedDict
    
    from langgraph.graph import StateGraph
    
    
    def reduce_fanouts(left, right):
        if left is None:
            left = []
        if not right:
            # Overwrite
            return []
        return left + right
    
    
    class State(TypedDict):
        # The operator.add reducer fn makes this append-only
        aggregate: Annotated[list, operator.add]
        fanout_values: Annotated[list, reduce_fanouts]
        which: str
    
    
    builder = StateGraph(State)
    builder.add_node("a", ReturnNodeValue("I'm A"))
    builder.add_edge(START, "a")
    
    
    class ParallelReturnNodeValue:
        def __init__(
            self,
            node_secret: str,
            reliability: float,
        ):
            self._value = node_secret
            self._reliability = reliability
    
        def __call__(self, state: State) -> Any:
            print(f"Adding {self._value} to {state['aggregate']} in parallel.")
            return {
                "fanout_values": [
                    {
                        "value": [self._value],
                        "reliability": self._reliability,
                    }
                ]
            }
    
    
    builder.add_node("b", ParallelReturnNodeValue("I'm B", reliability=0.9))
    
    builder.add_node("c", ParallelReturnNodeValue("I'm C", reliability=0.1))
    builder.add_node("d", ParallelReturnNodeValue("I'm D", reliability=0.3))
    
    
    def aggregate_fanout_values(state: State) -> Any:
        # Sort by reliability
        ranked_values = sorted(
            state["fanout_values"], key=lambda x: x["reliability"], reverse=True
        )
        return {
            "aggregate": [x["value"] for x in ranked_values] + ["I'm E"],
            "fanout_values": [],
        }
    
    
    builder.add_node("e", aggregate_fanout_values)
    
    
    def route_bc_or_cd(state: State) -> Sequence[str]:
        if state["which"] == "cd":
            return ["c", "d"]
        return ["b", "c"]
    
    
    intermediates = ["b", "c", "d"]
    builder.add_conditional_edges("a", route_bc_or_cd, intermediates)
    
    for node in intermediates:
        builder.add_edge(node, "e")
    
    builder.add_edge("e", END)
    graph = builder.compile()
    

API Reference: StateGraph

    
    
    from IPython.display import Image, display
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    
    
    
    graph.invoke({"aggregate": [], "which": "bc", "fanout_values": []})
    
    
    
    Adding I'm A to []
    Adding I'm B to ["I'm A"] in parallel.
    Adding I'm C to ["I'm A"] in parallel.
    
    
    
    {'aggregate': ["I'm A", ["I'm B"], ["I'm C"], "I'm E"],
     'fanout_values': [],
     'which': 'bc'}
    
    
    
    graph.invoke({"aggregate": [], "which": "cd"})
    
    
    
    Adding I'm A to []
    Adding I'm C to ["I'm A"] in parallel.
    Adding I'm D to ["I'm A"] in parallel.
    
    
    
    {'aggregate': ["I'm A", ["I'm D"], ["I'm C"], "I'm E"],
     'fanout_values': [],
     'which': 'cd'}
    

## Comments

Back to top

Previous

How-to Guides

Next

How to create map-reduce branches for parallel execution

Made with  Material for MkDocs Insiders