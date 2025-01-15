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
  * AgentAction

# AgentAction#

_class _langchain_core.agents.AgentAction[source]#

    

Bases: `Serializable`

Represents a request to execute an action by an agent.

The action consists of the name of the tool to execute and the input to pass
to the tool. The log is used to pass along extra information about the action.

_param _log _: str_ _[Required]_#

    

Additional information to log about the action. This log can be used in a few
ways. First, it can be used to audit what exactly the LLM predicted to lead to
this (tool, tool_input). Second, it can be used in future iterations to show
the LLMs prior thoughts. This is useful when (tool, tool_input) does not
contain full information about the LLM prediction (for example, any thought
before the tool/tool_input).

_param _tool _: str_ _[Required]_#

    

The name of the Tool to execute.

_param _tool_input _: str | dict_ _[Required]_#
    

The input to pass in to the Tool.

_param _type _: Literal['AgentAction']__ = 'AgentAction'_#

    

_property _messages _: Sequence[BaseMessage]_#

    

Return the messages that correspond to this action.

__On this page

  * `AgentAction`
    * `log`
    * `tool`
    * `tool_input`
    * `type`
    * `messages`

© Copyright 2023, LangChain Inc.