## Table of Contents

- [How to add semantic search to your LangGraph deployment¶](#how-to-add-semantic-search-to-your-langgraph-deployment)
  - [Prerequisites¶](#prerequisites)
  - [Steps¶](#steps)
  - [Usage¶](#usage)
  - [Custom Embeddings¶](#custom-embeddings)
  - [Querying via the API¶](#querying-via-the-api)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to add semantic search to your LangGraph deployment

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
        * How to add semantic search to your LangGraph deployment  How to add semantic search to your LangGraph deployment  Table of contents 
          * Prerequisites 
          * Steps 
          * Usage 
          * Custom Embeddings 
          * Querying via the API 
        * How to customize Dockerfile 
        * How to test a LangGraph app locally 
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

  * Prerequisites 
  * Steps 
  * Usage 
  * Custom Embeddings 
  * Querying via the API 

  1. Home 
  2. How-to Guides 
  3. LangGraph Platform 
  4. Application Structure 

# How to add semantic search to your LangGraph deployment¶

This guide explains how to add semantic search to your LangGraph deployment's
cross-thread store, so that your agent can search for memories and other
documents by semantic similarity.

## Prerequisites¶

  * A LangGraph deployment (see how to deploy)
  * API keys for your embedding provider (in this case, OpenAI)
  * `langchain >= 0.3.8` (if you specify using the string format below)

## Steps¶

  1. Update your `langgraph.json` configuration file to include the store configuration:

    
    
    {
        ...
        "store": {
            "index": {
                "embed": "openai:text-embeddings-3-small",
                "dims": 1536,
                "fields": ["$"]
            }
        }
    }
    

This configuration:

  * Uses OpenAI's text-embeddings-3-small model for generating embeddings
  * Sets the embedding dimension to 1536 (matching the model's output)
  * Indexes all fields in your stored data (`["$"]` means index everything, or specify specific fields like `["text", "metadata.title"]`)

  * To use the string embedding format above, make sure your dependencies include `langchain >= 0.3.8`:

    
    
    # In pyproject.toml
    [project]
    dependencies = [
        "langchain>=0.3.8"
    ]
    

Or if using requirements.txt:

    
    
    langchain>=0.3.8
    

## Usage¶

Once configured, you can use semantic search in your LangGraph nodes. The
store requires a namespace tuple to organize memories:

    
    
    def search_memory(state: State, *, store: BaseStore):
        # Search the store using semantic similarity
        # The namespace tuple helps organize different types of memories
        # e.g., ("user_facts", "preferences") or ("conversation", "summaries")
        results = store.search(
            namespace=("memory", "facts"),  # Organize memories by type
            query="your search query",
            limit=3  # number of results to return
        )
        return results
    

## Custom Embeddings¶

If you want to use custom embeddings, you can pass a path to a custom
embedding function:

    
    
    {
        ...
        "store": {
            "index": {
                "embed": "path/to/embedding_function.py:embed",
                "dims": 1536,
                "fields": ["$"]
            }
        }
    }
    

The deployment will look for the function in the specified path. The function
must be async and accept a list of strings:

    
    
    # path/to/embedding_function.py
    from openai import AsyncOpenAI
    
    client = AsyncOpenAI()
    
    async def aembed_texts(texts: list[str]) -> list[list[float]]:
        """Custom embedding function that must:
        1. Be async
        2. Accept a list of strings
        3. Return a list of float arrays (embeddings)
        """
        response = await client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        return [e.embedding for e in response.data]
    

## Querying via the API¶

You can also query the store using the LangGraph SDK. Since the SDK uses async
operations:

    
    
    from langgraph_sdk import get_client
    
    async def search_store():
        client = get_client()
        results = await client.store.search_items(
            ("memory", "facts"),
            query="your search query",
            limit=3  # number of results to return
        )
        return results
    
    # Use in an async context
    results = await search_store()
    

## Comments

Back to top

Previous

How to Set Up a LangGraph.js Application for Deployment

Next

How to customize Dockerfile

Made with  Material for MkDocs Insiders