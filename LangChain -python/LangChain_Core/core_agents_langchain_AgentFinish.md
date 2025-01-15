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
  * AgentFinish

# AgentFinish#

_class _langchain_core.agents.AgentFinish[source]#

    

Bases: `Serializable`

Final return value of an ActionAgent.

Agents return an AgentFinish when they have reached a stopping condition.

Override init to support instantiation by position for backward compat.

_param _log _: str_ _[Required]_#

    

Additional information to log about the return value. This is used to pass
along the full LLM prediction, not just the parsed out return value. For
example, if the full LLM prediction was Final Answer: 2 you may want to just
return 2 as a return value, but pass along the full string as a log (for
debugging or observability purposes).

_param _return_values _: dict_ _[Required]_#

    

Dictionary of return values.

_param _type _: Literal['AgentFinish']__ = 'AgentFinish'_#

    

_property _messages _: Sequence[BaseMessage]_#

    

Messages that correspond to this observation.

__On this page

  * `AgentFinish`
    * `log`
    * `return_values`
    * `type`
    * `messages`

© Copyright 2023, LangChain Inc.