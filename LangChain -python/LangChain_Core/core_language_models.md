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
    * `language_models` __
      * BaseLanguageModel
      * LangSmithParams
      * BaseChatModel
      * SimpleChatModel
      * FakeListLLM
      * FakeListLLMError
      * FakeStreamingListLLM
      * FakeChatModel
      * FakeListChatModel
      * FakeListChatModelError
      * FakeMessagesListChatModel
      * GenericFakeChatModel
      * ParrotFakeChatModel
      * BaseLLM
      * LLM
      * agenerate_from_stream
      * generate_from_stream
      * aget_prompts
      * aupdate_cache
      * create_base_retry_decorator
      * get_prompts
      * update_cache
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
  * `language_models`

# `language_models`#

**Language Model** is a type of model that can generate text or complete text
prompts.

LangChain has two main classes to work with language models: **Chat Models**
and “old-fashioned” **LLMs**.

**Chat Models**

Language models that use a sequence of messages as inputs and return chat
messages as outputs (as opposed to using plain text). These are traditionally
newer models ( older models are generally LLMs, see below). Chat models
support the assignment of distinct roles to conversation messages, helping to
distinguish messages from the AI, users, and instructions such as system
messages.

The key abstraction for chat models is BaseChatModel. Implementations should
inherit from this class. Please see LangChain how-to guides with more
information on how to implement a custom chat model.

To implement a custom Chat Model, inherit from BaseChatModel. See the
following guide for more information on how to implement a custom Chat Model:

https://python.langchain.com/docs/how_to/custom_chat_model/

**LLMs**

Language models that takes a string as input and returns a string. These are
traditionally older models (newer models generally are Chat Models, see
below).

Although the underlying models are string in, string out, the LangChain
wrappers also allow these models to take messages as input. This gives them
the same interface as Chat Models. When messages are passed in as input, they
will be formatted into a string under the hood before being passed to the
underlying model.

To implement a custom LLM, inherit from BaseLLM or LLM. Please see the
following guide for more information on how to implement a custom LLM:

https://python.langchain.com/docs/how_to/custom_llm/

**Classes**

`language_models.base.BaseLanguageModel` | Abstract base class for interfacing with language models.  
---|---  
`language_models.base.BaseLanguageModel[BaseMessage]` | Abstract base class for interfacing with language models.  
`language_models.base.BaseLanguageModel[str]` | Abstract base class for interfacing with language models.  
`language_models.base.LangSmithParams` | LangSmith parameters for tracing.  
`language_models.chat_models.BaseChatModel` | Base class for chat models.  
`language_models.chat_models.SimpleChatModel` | Simplified implementation for a chat model to inherit from.  
`language_models.fake.FakeListLLM` | Fake LLM for testing purposes.  
`language_models.fake.FakeListLLMError` | Fake error for testing purposes.  
`language_models.fake.FakeStreamingListLLM` | Fake streaming list LLM for testing purposes.  
`language_models.fake_chat_models.FakeChatModel` | Fake Chat Model wrapper for testing purposes.  
`language_models.fake_chat_models.FakeListChatModel` | Fake ChatModel for testing purposes.  
`language_models.fake_chat_models.FakeListChatModelError` |   
`language_models.fake_chat_models.FakeMessagesListChatModel` | Fake ChatModel for testing purposes.  
`language_models.fake_chat_models.GenericFakeChatModel` | Generic fake chat model that can be used to test the chat model interface.  
`language_models.fake_chat_models.ParrotFakeChatModel` | Generic fake chat model that can be used to test the chat model interface.  
`language_models.llms.BaseLLM` | Base LLM abstract interface.  
`language_models.llms.LLM` | Simple interface for implementing a custom LLM.  
  
**Functions**

`language_models.chat_models.agenerate_from_stream`(stream) | Async generate from a stream.  
---|---  
`language_models.chat_models.generate_from_stream`(stream) | Generate from a stream.  
`language_models.llms.aget_prompts`(params, ...) | Get prompts that are already cached.  
`language_models.llms.aupdate_cache`(cache, ...) | Update the cache and get the LLM output.  
`language_models.llms.create_base_retry_decorator`(...) | Create a retry decorator for a given LLM and provided  
`language_models.llms.get_prompts`(params, prompts) | Get prompts that are already cached.  
`language_models.llms.update_cache`(cache, ...) | Update the cache and get the LLM output.  
  
© Copyright 2023, LangChain Inc.