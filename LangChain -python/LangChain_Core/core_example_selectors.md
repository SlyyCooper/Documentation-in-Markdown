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
    * `example_selectors` __
      * BaseExampleSelector
      * LengthBasedExampleSelector
      * MaxMarginalRelevanceExampleSelector
      * SemanticSimilarityExampleSelector
      * sorted_values
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
  * `example_selectors`

# `example_selectors`#

**Example selector** implements logic for selecting examples to include them
in prompts. This allows us to select examples that are most relevant to the
input.

**Classes**

`example_selectors.base.BaseExampleSelector`() | Interface for selecting examples to include in prompts.  
---|---  
`example_selectors.length_based.LengthBasedExampleSelector` | Select examples based on length.  
`example_selectors.semantic_similarity.MaxMarginalRelevanceExampleSelector` | Select examples based on Max Marginal Relevance.  
`example_selectors.semantic_similarity.SemanticSimilarityExampleSelector` | Select examples based on semantic similarity.  
  
**Functions**

`example_selectors.semantic_similarity.sorted_values`(values) | Return a list of values in dict sorted by key.  
---|---  
  
© Copyright 2023, LangChain Inc.