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
    * ` agents`
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
    * `load` __
      * Reviver
      * BaseSerialized
      * Serializable
      * SerializedConstructor
      * SerializedNotImplemented
      * SerializedSecret
      * default
      * dumpd
      * dumps
      * load
      * loads
      * to_json_not_implemented
      * try_neq_default
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
  * `load`

# `load`#

**Load** module helps with serialization and deserialization.

**Classes**

`load.load.Reviver`([secrets_map, ...]) | Reviver for JSON objects.  
---|---  
`load.serializable.BaseSerialized` | Base class for serialized objects.  
`load.serializable.Serializable` | Serializable base class.  
`load.serializable.SerializedConstructor` | Serialized constructor.  
`load.serializable.SerializedNotImplemented` | Serialized not implemented.  
`load.serializable.SerializedSecret` | Serialized secret.  
  
**Functions**

`load.dump.default`(obj) | Return a default value for a Serializable object or a SerializedNotImplemented object.  
---|---  
`load.dump.dumpd`(obj) | Return a dict representation of an object.  
`load.dump.dumps`(obj, *[, pretty]) | Return a json string representation of an object.  
`load.load.load`(obj, *[, secrets_map, ...]) |   
`load.load.loads`(text, *[, secrets_map, ...]) |   
`load.serializable.to_json_not_implemented`(obj) | Serialize a "not implemented" object.  
`load.serializable.try_neq_default`(value, ...) | Try to determine if a value is different from the default.  
  
© Copyright 2023, LangChain Inc.