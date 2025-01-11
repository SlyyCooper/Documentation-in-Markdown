## Table of Contents

- [How to stream full state of your graph¶](#how-to-stream-full-state-of-your-graph)
  - [Setup¶](#setup)
  - [Stream graph in values mode¶](#stream-graph-in-values-mode)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to stream full state of your graph

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
      * Application Structure 
      * Deployment 
      * Authentication & Access Control 
      * Assistants 
      * Threads 
      * Runs 
      * Streaming  Streaming 
        * Streaming 
        * How to stream full state of your graph  How to stream full state of your graph  Table of contents 
          * Setup 
          * Stream graph in values mode 
        * How to stream state updates of your graph 
        * How to stream messages from your graph 
        * How to stream events 
        * How to stream debug events 
        * How to configure multiple streaming modes at the same time 
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
  * Stream graph in values mode 

  1. Home 
  2. How-to Guides 
  3. LangGraph Platform 
  4. Streaming 

# How to stream full state of your graph¶

Prerequisites

  * Streaming

This guide covers how to use `stream_mode="values"`, which streams the value
of the state at each superstep. This differs from using
`stream_mode="updates"`: instead of streaming just the updates to the state
from each node, it streams the entire graph state at that superstep.

## Setup¶

First let's set up our client and thread:

PythonJavascriptCURL

    
    
    from langgraph_sdk import get_client
    
    client = get_client(url=<DEPLOYMENT_URL>)
    # Using the graph deployed with the name "agent"
    assistant_id = "agent"
    # create thread
    thread = await client.threads.create()
    print(thread)
    
    
    
    import { Client } from "@langchain/langgraph-sdk";
    
    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
    // Using the graph deployed with the name "agent"
    const assistantID = "agent";
    // create thread
    const thread = await client.threads.create();
    console.log(thread);
    
    
    
    curl --request POST \
      --url <DEPLOYMENT_URL>/threads \
      --header 'Content-Type: application/json' \
      --data '{}'
    

Output:

    
    
    {
      'thread_id': 'bfc68029-1f7b-400f-beab-6f9032a52da4',
      'created_at': '2024-06-24T21:30:07.980789+00:00',
      'updated_at': '2024-06-24T21:30:07.980789+00:00',
      'metadata': {},
      'status': 'idle',
      'config': {},
      'values': None
    }
    

## Stream graph in values mode¶

Now we can stream by values, which streams the full state of the graph after
each node has finished executing:

PythonJavascriptCURL

    
    
    input = {"messages": [{"role": "user", "content": "what's the weather in la"}]}
    
    # stream values
    async for chunk in client.runs.stream(
        thread["thread_id"],
        assistant_id, 
        input=input,
        stream_mode="values"
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")
    
    
    
    const input = {"messages": [{"role": "user", "content": "what's the weather in la"}]}
    
    const streamResponse = client.runs.stream(
      thread["thread_id"],
      assistantID,
      {
        input,
        streamMode: "values"
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
       \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in la\"}]},
       \"stream_mode\": [
         \"values\"
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
    

Output:

    
    
    Receiving new event of type: metadata...
    {"run_id": "f08791ce-0a3d-44e0-836c-ff62cd2e2786"}
    
    
    
    Receiving new event of type: values...
    {
      "messages": [
        {
          "role": "human",
          "content": "what's the weather in la"
        }
      ]
    }
    
    
    
    Receiving new event of type: values...
    {
      "messages": [
        {
          "content": "what's the weather in la",
          "type": "human",
          ...
        },
        {
          "content": "",
          "type": "ai",
          "tool_calls": [
            {
              "name": "tavily_search_results_json",
              "args": {
                "query": "weather in los angeles"
              },
              "id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
            }
          ],
          ...
        }
      ]
    }
    
    ...
    
    Receiving new event of type: values...
    {
      "messages": [
        {
          "content": "what's the weather in la",
          "type": "human",
          ...
        },
        {
          "content": "",
          "type": "ai",
          "tool_calls": [
            {
              "name": "tavily_search_results_json",
              "args": {
                "query": "weather in los angeles"
              },
              "id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
            }
          ],
          ...
        }
        {
          "content": [
            {
              "url": "https://www.weatherapi.com/",
              "content": "{\"location\": {\"name\": \"Los Angeles\", \"region\": \"California\", \"country\": \"United States of America\", \"lat\": 34.05, \"lon\": -118.24, \"tz_id\": \"America/Los_Angeles\", \"localtime_epoch\": 1716310320, \"localtime\": \"2024-05-21 9:52\"}, \"current\": {\"last_updated_epoch\": 1716309900, \"last_updated\": \"2024-05-21 09:45\", \"temp_c\": 16.7, \"temp_f\": 62.1, \"is_day\": 1, \"condition\": {\"text\": \"Overcast\", \"icon\": \"//cdn.weatherapi.com/weather/64x64/day/122.png\", \"code\": 1009}, \"wind_mph\": 8.1, \"wind_kph\": 13.0, \"wind_degree\": 250, \"wind_dir\": \"WSW\", \"pressure_mb\": 1015.0, \"pressure_in\": 29.97, \"precip_mm\": 0.0, \"precip_in\": 0.0, \"humidity\": 65, \"cloud\": 100, \"feelslike_c\": 16.7, \"feelslike_f\": 62.1, \"vis_km\": 16.0, \"vis_miles\": 9.0, \"uv\": 5.0, \"gust_mph\": 12.5, \"gust_kph\": 20.2}}"
            }
          ],
          "type": "tool",
          "name": "tavily_search_results_json",
          "tool_call_id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
          ...
        },
        {
          "content": "Based on the weather API results, the current weather in Los Angeles is overcast with a temperature of around 62°F (17°C). There are light winds from the west-southwest around 8-13 mph. The humidity is 65% and visibility is good at 9 miles. Overall, mild spring weather conditions in LA.",
          "type": "ai",
          ...
        }
      ]
    }
    
    
    
    Receiving new event of type: end...
    None
    

If we want to just get the final result, we can use this endpoint and just
keep track of the last value we received

PythonJavascriptCURL

    
    
    final_answer = None
    async for chunk in client.runs.stream(
        thread["thread_id"],
        assistant_id,
        input=input,
        stream_mode="values"
    ):
        if chunk.event == "values":
            final_answer = chunk.data
    
    
    
    let finalAnswer;
    const streamResponse = client.runs.stream(
      thread["thread_id"],
      assistantID,
      {
        input,
        streamMode: "values"
      }
    );
    for await (const chunk of streamResponse) {
      finalAnswer = chunk.data;
    }
    
    
    
    curl --request POST \
     --url <DEPLOYMENT_URL>/threads/<THREAD_ID>/runs/stream \
     --header 'Content-Type: application/json' \
     --data "{
       \"assistant_id\": \"agent\",
       \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"what's the weather in la\"}]},
       \"stream_mode\": [
         \"values\"
       ]
     }" | \
     sed 's/\r$//' | \
     awk '
     /^data:/ { 
         sub(/^data: /, "", $0)   
         data_content = $0          
     }    
     END {                                               
         if (data_content != "") {
             print data_content
         }
     }         
     '
    

Output:

    
    
    {
      "messages": [
        {
          "content": "what's the weather in la",
          "type": "human",
          ...
        },
        {
          "type": "ai",
          "tool_calls": [
            {
              "name": "tavily_search_results_json",
              "args": {
                "query": "weather in los angeles"
              },
              "id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
            }
          ],
          ...
        }
        {
          "content": [
            {
              "url": "https://www.weatherapi.com/",
              "content": "{\"location\": {\"name\": \"Los Angeles\", \"region\": \"California\", \"country\": \"United States of America\", \"lat\": 34.05, \"lon\": -118.24, \"tz_id\": \"America/Los_Angeles\", \"localtime_epoch\": 1716310320, \"localtime\": \"2024-05-21 9:52\"}, \"current\": {\"last_updated_epoch\": 1716309900, \"last_updated\": \"2024-05-21 09:45\", \"temp_c\": 16.7, \"temp_f\": 62.1, \"is_day\": 1, \"condition\": {\"text\": \"Overcast\", \"icon\": \"//cdn.weatherapi.com/weather/64x64/day/122.png\", \"code\": 1009}, \"wind_mph\": 8.1, \"wind_kph\": 13.0, \"wind_degree\": 250, \"wind_dir\": \"WSW\", \"pressure_mb\": 1015.0, \"pressure_in\": 29.97, \"precip_mm\": 0.0, \"precip_in\": 0.0, \"humidity\": 65, \"cloud\": 100, \"feelslike_c\": 16.7, \"feelslike_f\": 62.1, \"vis_km\": 16.0, \"vis_miles\": 9.0, \"uv\": 5.0, \"gust_mph\": 12.5, \"gust_kph\": 20.2}}"
            }
          ],
          "type": "tool",
          "name": "tavily_search_results_json",
          "tool_call_id": "toolu_01E5mSaZWm5rWJnCqmt63v4g"
          ...
        },
        {
          "content": "Based on the weather API results, the current weather in Los Angeles is overcast with a temperature of around 62°F (17°C). There are light winds from the west-southwest around 8-13 mph. The humidity is 65% and visibility is good at 9 miles. Overall, mild spring weather conditions in LA.",
          "type": "ai",
          ...
        }
      ]
    }
    

## Comments

Back to top

Previous

Stateless Runs

Next

How to stream state updates of your graph

Made with  Material for MkDocs Insiders