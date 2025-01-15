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
    * `load`
    * `messages`
    * `output_parsers`
    * `outputs` __
      * ChatGeneration
      * ChatGenerationChunk
      * ChatResult
      * Generation
      * GenerationChunk
      * LLMResult
      * RunInfo
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
  * `outputs`

# `outputs`#

**Output** classes are used to represent the output of a language model call
and the output of a chat.

The top container for information is the LLMResult object. LLMResult is used
by both chat models and LLMs. This object contains the output of the language
model and any additional information that the model provider wants to return.

When invoking models via the standard runnable methods (e.g. invoke, batch,
etc.): \- Chat models will return AIMessage objects. \- LLMs will return
regular text strings.

In addition, users can access the raw output of either LLMs or chat models via
callbacks. The on_chat_model_end and on_llm_end callbacks will return an
LLMResult object containing the generated outputs and any additional
information returned by the model provider.

In general, if information is already available in the AIMessage object, it is
recommended to access it from there rather than from the LLMResult object.

**Classes**

`outputs.chat_generation.ChatGeneration` | A single chat generation output.  
---|---  
`outputs.chat_generation.ChatGenerationChunk` | ChatGeneration chunk, which can be concatenated with other ChatGeneration chunks.  
`outputs.chat_result.ChatResult` | Use to represent the result of a chat model call with a single prompt.  
`outputs.generation.Generation` | A single text generation output.  
`outputs.generation.GenerationChunk` | Generation chunk, which can be concatenated with other Generation chunks.  
`outputs.llm_result.LLMResult` | A container for results of an LLM call.  
`outputs.run_info.RunInfo` | Class that contains metadata for a single execution of a Chain or model.  
  
© Copyright 2023, LangChain Inc.