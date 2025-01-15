Skip to main content

__Back to top __ `Ctrl`+`K`

  * Reference 

__ `Ctrl`+`K`

Docs

______

  * __ GitHub
  * __ X / Twitter

__ `Ctrl`+`K`

  * Reference 

Docs

______

  * __ GitHub
  * __ X / Twitter

Section Navigation

Base packages

  * Core __
    * ` agents` __
      * AgentAction
      * AgentActionMessageLog
      * AgentFinish
      * AgentStep
    * `beta`
    * `caches`
    * `callbacks`
    * `chat_history`
    * `chat_loaders`
    * `chat_sessions`
    * `document_loaders`
    * `documents`
    * `embeddings`
    * `example_selectors`
    * `exceptions`
    * `globals`
    * `indexing`
    * `language_models`
    * `load`
    * `messages`
    * `output_parsers`
    * `outputs`
    * `prompt_values`
    * `prompts`
    * `rate_limiters`
    * `retrievers`
    * `runnables`
    * `stores`
    * `structured_query`
    * `sys_info`
    * `tools`
    * `tracers`
    * `utils`
    * `vectorstores`
  * Langchain
  * Text Splitters
  * Community
  * Experimental

Integrations

  * AI21
  * Anthropic
  * AstraDB
  * AWS
  * Azure Dynamic Sessions
  * Cerebras
  * Chroma
  * Cohere
  * Couchbase
  * Databricks
  * Elasticsearch
  * Exa
  * Fireworks
  * Google Community
  * Google GenAI
  * Google VertexAI
  * Groq
  * Huggingface
  * IBM
  * Milvus
  * MistralAI
  * Neo4J
  * Nomic
  * Nvidia Ai Endpoints
  * Ollama
  * OpenAI
  * Pinecone
  * Postgres
  * Prompty
  * Qdrant
  * Redis
  * Sema4
  * Snowflake
  * Sqlserver
  * Standard Tests
  * Together
  * Unstructured
  * Upstage
  * VoyageAI
  * Weaviate
  * XAI

  * __
  * LangChain Python API Reference
  * langchain-core: 0.3.29
  * `agents`

# `agents`#

Schema definitions for representing agent actions, observations, and return
values.

**ATTENTION** The schema definitions are provided for backwards compatibility.

> New agents should be built using the langgraph library (langchain-
> ai/langgraph)), which provides a simpler and more flexible way to define
> agents.
>
> Please see the migration guide for information on how to migrate existing
> agents to modern langgraph agents:
> https://python.langchain.com/docs/how_to/migrate_agent/

Agents use language models to choose a sequence of actions to take.

A basic agent works in the following manner:

  1. Given a prompt an agent uses an LLM to request an action to take (e.g., a tool to run).

  2. The agent executes the action (e.g., runs the tool), and receives an observation.

  3. The agent returns the observation to the LLM, which can then be used to generate the next action.

  4. When the agent reaches a stopping condition, it returns a final return value.

The schemas for the agents themselves are defined in langchain.agents.agent.

**Classes**

`agents.AgentAction` | Represents a request to execute an action by an agent.  
---|---  
`agents.AgentActionMessageLog` | Representation of an action to be executed by an agent.  
`agents.AgentFinish` | Final return value of an ActionAgent.  
`agents.AgentStep` | Result of running an AgentAction.  
  
© Copyright 2023, LangChain Inc.