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
    * `indexing` __
      * IndexingException
      * IndexingResult
      * DeleteResponse
      * DocumentIndex
      * InMemoryRecordManager
      * RecordManager
      * UpsertResponse
      * InMemoryDocumentIndex
      * aindex
      * index
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
  * `indexing`

# `indexing`#

Code to help indexing data into a vectorstore.

This package contains helper logic to help deal with indexing data into a
vectorstore while avoiding duplicated content and over-writing content if it’s
unchanged.

**Classes**

`indexing.api.IndexingException` | Raised when an indexing operation fails.  
---|---  
`indexing.api.IndexingResult` | Return a detailed a breakdown of the result of the indexing operation.  
`indexing.base.DeleteResponse` | A generic response for delete operation.  
`indexing.base.DocumentIndex` |   
`indexing.base.InMemoryRecordManager`(namespace) | An in-memory record manager for testing purposes.  
`indexing.base.RecordManager`(namespace) | Abstract base class representing the interface for a record manager.  
`indexing.base.UpsertResponse` | A generic response for upsert operations.  
`indexing.in_memory.InMemoryDocumentIndex` |   
  
**Functions**

`indexing.api.aindex`(docs_source, ...[, ...]) | Async index data from the loader into the vector store.  
---|---  
`indexing.api.index`(docs_source, ...[, ...]) | Index data from the loader into the vector store.  
  
© Copyright 2023, LangChain Inc.