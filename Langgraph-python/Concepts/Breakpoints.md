Breakpoints¶
Breakpoints pause graph execution at specific points and enable stepping through execution step by step. Breakpoints are powered by LangGraph's persistence layer, which saves the state after each graph step. Breakpoints can also be used to enable human-in-the-loop workflows, though we recommend using the interrupt function for this purpose.

Requirements¶
To use breakpoints, you will need to:

Specify a checkpointer to save the graph state after each step.
Set breakpoints to specify where execution should pause.
Run the graph with a thread ID to pause execution at the breakpoint.
Resume execution using invoke/ainvoke/stream/astream (see The Command primitive).
Setting breakpoints¶
There are two places where you can set breakpoints:

Before or after a node executes by setting breakpoints at compile time or run time. We call these static breakpoints.
Inside a node using the NodeInterrupt exception.
Static breakpoints¶
Static breakpoints are triggered either before or after a node executes. You can set static breakpoints by specifying interrupt_before and interrupt_after at "compile" time or run time.


# Compile time
Run time

graph = graph_builder.compile(
    interrupt_before=["node_a"], 
    interrupt_after=["node_b", "node_c"],
    checkpointer=..., # Specify a checkpointer
)

thread_config = {
    "configurable": {
        "thread_id": "some_thread"
    }
}

# Run Time

Run time

graph.invoke(
    inputs, 
    config={"configurable": {"thread_id": "some_thread"}}, 
    interrupt_before=["node_a"], 
    interrupt_after=["node_b", "node_c"]
)

thread_config = {
    "configurable": {
        "thread_id": "some_thread"
    }
}

# Run the graph until the breakpoint
graph.invoke(inputs, config=thread_config)

# Optionally update the graph state based on user input
graph.update_state(update, config=thread_config)

# Resume the graph
graph.invoke(None, config=thread_config)

# Run the graph until the breakpoint
graph.invoke(inputs, config=thread_config)

# Optionally update the graph state based on user input
graph.update_state(update, config=thread_config)

# Resume the graph
graph.invoke(None, config=thread_config)

Static breakpoints can be especially useful for debugging if you want to step through the graph execution one node at a time or if you want to pause the graph execution at specific nodes.

NodeInterrupt exception¶
We recommend that you use the interrupt function instead of the NodeInterrupt exception if you're trying to implement human-in-the-loop workflows. The interrupt function is easier to use and more flexible.

NodeInterrupt exception
The developer can define some condition that must be met for a breakpoint to be triggered. This concept of dynamic breakpoints is useful when the developer wants to halt the graph under a particular condition. This uses a NodeInterrupt, which is a special type of exception that can be raised from within a node based upon some condition. As an example, we can define a dynamic breakpoint that triggers when the input is longer than 5 characters.


def my_node(state: State) -> State:
    if len(state['input']) > 5:
        raise NodeInterrupt(f"Received input that is longer than 5 characters: {state['input']}")

    return state
Let's assume we run the graph with an input that triggers the dynamic breakpoint and then attempt to resume the graph execution simply by passing in None for the input.


# Attempt to continue the graph execution with no change to state after we hit the dynamic breakpoint 
for event in graph.stream(None, thread_config, stream_mode="values"):
    print(event)
The graph will interrupt again because this node will be re-run with the same graph state. We need to change the graph state such that the condition that triggers the dynamic breakpoint is no longer met. So, we can simply edit the graph state to an input that meets the condition of our dynamic breakpoint (< 5 characters) and re-run the node.


# Update the state to pass the dynamic breakpoint
graph.update_state(config=thread_config, values={"input": "foo"})
for event in graph.stream(None, thread_config, stream_mode="values"):
    print(event)
Alternatively, what if we want to keep our current input and skip the node (my_node) that performs the check? To do this, we can simply perform the graph update with as_node="my_node" and pass in None for the values. This will make no update the graph state, but run the update as my_node, effectively skipping the node and bypassing the dynamic breakpoint.


# This update will skip the node `my_node` altogether
graph.update_state(config=thread_config, values=None, as_node="my_node")
for event in graph.stream(None, thread_config, stream_mode="values"):
    print(event)