## Table of Contents

- [How to test a LangGraph app locally¶](#how-to-test-a-langgraph-app-locally)
  - [Setup¶](#setup)
  - [Start the API server¶](#start-the-api-server)
    - [Interact with the server¶](#interact-with-the-server)
      - [Initialize with authentication¶](#initialize-with-authentication)
      - [Initialize with environment variables¶](#initialize-with-environment-variables)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to test a LangGraph app locally

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
      * Controllability 
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
      * Application Structure  Application Structure 
        * Application Structure 
        * How to Set Up a LangGraph Application for Deployment 
        * How to Set Up a LangGraph Application for Deployment 
        * How to Set Up a LangGraph.js Application for Deployment 
        * How to add semantic search to your LangGraph deployment 
        * How to customize Dockerfile 
        * How to test a LangGraph app locally  How to test a LangGraph app locally  Table of contents 
          * Setup 
          * Start the API server 
            * Interact with the server 
              * Initialize with authentication 
              * Initialize with environment variables 
        * Rebuild Graph at Runtime 
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
  * Start the API server 
    * Interact with the server 
      * Initialize with authentication 
      * Initialize with environment variables 

  1. Home 
  2. How-to Guides 
  3. LangGraph Platform 
  4. Application Structure 

# How to test a LangGraph app locally¶

This guide assumes you have a LangGraph app correctly set up with a proper
configuration file and a corresponding compiled graph, and that you have a
proper LangChain API key.

Testing locally ensures that there are no errors or conflicts with Python
dependencies and confirms that the configuration file is specified correctly.

## Setup¶

Install the LangGraph CLI package:

    
    
    pip install -U "langgraph-cli[inmem]"
    

Ensure you have an API key, which you can create from the LangSmith UI
(Settings > API Keys). This is required to authenticate that you have
LangGraph Cloud access. After you have saved the key to a safe place, place
the following line in your `.env` file:

    
    
    LANGSMITH_API_KEY = *********
    

## Start the API server¶

Once you have installed the CLI, you can run the following command to start
the API server for local testing:

    
    
    langgraph dev
    

This will start up the LangGraph API server locally. If this runs
successfully, you should see something like:

> Ready!
>
>   * API: http://localhost:2024
>
>   * Docs: http://localhost:2024/docs
>
>   * LangGraph Studio Web UI:
> https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
>
>

In-Memory Mode

The `langgraph dev` command starts LangGraph Server in an in-memory mode. This
mode is suitable for development and testing purposes. For production use, you
should deploy LangGraph Server with access to a persistent storage backend.

If you want to test your application with a persistent storage backend, you
can use the `langgraph up` command instead of `langgraph dev`. You will need
to have `docker` installed on your machine to use this command.

### Interact with the server¶

We can now interact with the API server using the LangGraph SDK. First, we
need to start our client, select our assistant (in this case a graph we called
"agent", make sure to select the proper assistant you wish to test).

You can either initialize by passing authentication or by setting an
environment variable.

#### Initialize with authentication¶

PythonJavascriptCURL

    
    
    from langgraph_sdk import get_client
    
    # only pass the url argument to get_client() if you changed the default port when calling langgraph dev
    client = get_client(url=<DEPLOYMENT_URL>,api_key=<LANGSMITH_API_KEY>)
    # Using the graph deployed with the name "agent"
    assistant_id = "agent"
    thread = await client.threads.create()
    
    
    
    import { Client } from "@langchain/langgraph-sdk";
    
    // only set the apiUrl if you changed the default port when calling langgraph dev
    const client = new Client({ apiUrl: <DEPLOYMENT_URL>, apiKey: <LANGSMITH_API_KEY> });
    // Using the graph deployed with the name "agent"
    const assistantId = "agent";
    const thread = await client.threads.create();
    
    
    
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads \
      --header 'Content-Type: application/json'
      --header 'x-api-key: <LANGSMITH_API_KEY>'
    

#### Initialize with environment variables¶

If you have a `LANGSMITH_API_KEY` set in your environment, you do not need to
explicitly pass authentication to the client

PythonJavascriptCURL

    
    
    from langgraph_sdk import get_client
    
    # only pass the url argument to get_client() if you changed the default port when calling langgraph dev
    client = get_client()
    # Using the graph deployed with the name "agent"
    assistant_id = "agent"
    thread = await client.threads.create()
    
    
    
    import { Client } from "@langchain/langgraph-sdk";
    
    // only set the apiUrl if you changed the default port when calling langgraph dev
    const client = new Client();
    // Using the graph deployed with the name "agent"
    const assistantId = "agent";
    const thread = await client.threads.create();
    
    
    
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads \
      --header 'Content-Type: application/json'
    

Now we can invoke our graph to ensure it is working. Make sure to change the
input to match the proper schema for your graph.

PythonJavascriptCURL

    
    
    input = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
    async for chunk in client.runs.stream(
        thread["thread_id"],
        assistant_id,
        input=input,
        stream_mode="updates",
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")
    
    
    
    const input = { "messages": [{ "role": "user", "content": "what's the weather in sf"}] }
    
    const streamResponse = client.runs.stream(
      thread["thread_id"],
      assistantId,
      {
        input: input,
        streamMode: "updates",
      }
    );
    for await (const chunk of streamResponse) {
      console.log(`Receiving new event of type: ${chunk.event}...`);
      console.log(chunk.data);
      console.log("\n\n");
    }
    
    
    
    curl --request POST \
     --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream \
     --header 'Content-Type: application/json' \
     --data "{
       \"assistant_id\": \"agent\",
       \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in sf\"}]},
       \"stream_mode\": [
         \"events\"
       ]
     }" | \
     sed 's/\r$//' | \
     awk '
     /^event:/ {
         if (data_content != "") {
             print data_content "\n"
         }
         sub(/^event: /, "Receiving event of type: ", $0)
         printf "%s...\n", $0
         data_content = ""
     }
     /^data:/ {
         sub(/^data: /, "", $0)
         data_content = $0
     }
     END {
         if (data_content != "") {
             print data_content "\n"
         }
     }
     ' 
    

If your graph works correctly, you should see your graph output displayed in
the console. Of course, there are many more ways you might need to test your
graph, for a full list of commands you can send with the SDK, see the Python
and JS/TS references.

## Comments

Back to top

Previous

How to customize Dockerfile

Next

Rebuild Graph at Runtime

Made with  Material for MkDocs Insiders