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
  * AgentActionMessageLog

# AgentActionMessageLog#

_class _langchain_core.agents.AgentActionMessageLog[source]#

    

Bases: `AgentAction`

Representation of an action to be executed by an agent.

This is similar to AgentAction, but includes a message log consisting of chat
messages. This is useful when working with ChatModels, and is used to
reconstruct conversation history from the agent’s perspective.

_param _log _: str_ _[Required]_#

    

Additional information to log about the action. This log can be used in a few
ways. First, it can be used to audit what exactly the LLM predicted to lead to
this (tool, tool_input). Second, it can be used in future iterations to show
the LLMs prior thoughts. This is useful when (tool, tool_input) does not
contain full information about the LLM prediction (for example, any thought
before the tool/tool_input).

_param _message_log _: Sequence[BaseMessage]__[Required]_#

    

Similar to log, this can be used to pass along extra information about what
exact messages were predicted by the LLM before parsing out the (tool,
tool_input). This is again useful if (tool, tool_input) cannot be used to
fully recreate the LLM prediction, and you need that LLM prediction (for
future agent iteration). Compared to log, this is useful when the underlying
LLM is a ChatModel (and therefore returns messages rather than a string).

_param _tool _: str_ _[Required]_#

    

The name of the Tool to execute.

_param _tool_input _: str | dict_ _[Required]_#
    

The input to pass in to the Tool.

_param _type _: Literal['AgentActionMessageLog']__ = 'AgentActionMessageLog'_#

    

_property _messages _: Sequence[BaseMessage]_#

    

Return the messages that correspond to this action.

__On this page

  * `AgentActionMessageLog`
    * `log`
    * `message_log`
    * `tool`
    * `tool_input`
    * `type`
    * `messages`

© Copyright 2023, LangChain Inc.