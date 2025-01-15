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
    * `callbacks` __
      * AsyncCallbackHandler
      * BaseCallbackHandler
      * BaseCallbackManager
      * CallbackManagerMixin
      * ChainManagerMixin
      * LLMManagerMixin
      * RetrieverManagerMixin
      * RunManagerMixin
      * ToolManagerMixin
      * FileCallbackHandler
      * AsyncCallbackManager
      * AsyncCallbackManagerForChainGroup
      * AsyncCallbackManagerForChainRun
      * AsyncCallbackManagerForLLMRun
      * AsyncCallbackManagerForRetrieverRun
      * AsyncCallbackManagerForToolRun
      * AsyncParentRunManager
      * AsyncRunManager
      * BaseRunManager
      * CallbackManager
      * CallbackManagerForChainGroup
      * CallbackManagerForChainRun
      * CallbackManagerForLLMRun
      * CallbackManagerForRetrieverRun
      * CallbackManagerForToolRun
      * ParentRunManager
      * RunManager
      * StdOutCallbackHandler
      * StreamingStdOutCallbackHandler
      * adispatch_custom_event
      * ahandle_event
      * atrace_as_chain_group
      * dispatch_custom_event
      * handle_event
      * shielded
      * trace_as_chain_group
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
  * `callbacks`

# `callbacks`#

**Callback handlers** allow listening to events in LangChain.

**Class hierarchy:**

    
    
    BaseCallbackHandler --> <name>CallbackHandler  # Example: AimCallbackHandler
    

**Classes**

`callbacks.base.AsyncCallbackHandler`() | Async callback handler for LangChain.  
---|---  
`callbacks.base.BaseCallbackHandler`() | Base callback handler for LangChain.  
`callbacks.base.BaseCallbackManager`(handlers) | Base callback manager for LangChain.  
`callbacks.base.CallbackManagerMixin`() | Mixin for callback manager.  
`callbacks.base.ChainManagerMixin`() | Mixin for chain callbacks.  
`callbacks.base.LLMManagerMixin`() | Mixin for LLM callbacks.  
`callbacks.base.RetrieverManagerMixin`() | Mixin for Retriever callbacks.  
`callbacks.base.RunManagerMixin`() | Mixin for run manager.  
`callbacks.base.ToolManagerMixin`() | Mixin for tool callbacks.  
`callbacks.file.FileCallbackHandler`(filename) | Callback Handler that writes to a file.  
`callbacks.manager.AsyncCallbackManager`(handlers) | Async callback manager that handles callbacks from LangChain.  
`callbacks.manager.AsyncCallbackManagerForChainGroup`(...) | Async callback manager for the chain group.  
`callbacks.manager.AsyncCallbackManagerForChainRun`(*, ...) | Async callback manager for chain run.  
`callbacks.manager.AsyncCallbackManagerForLLMRun`(*, ...) | Async callback manager for LLM run.  
`callbacks.manager.AsyncCallbackManagerForRetrieverRun`(*, ...) | Async callback manager for retriever run.  
`callbacks.manager.AsyncCallbackManagerForToolRun`(*, ...) | Async callback manager for tool run.  
`callbacks.manager.AsyncParentRunManager`(*, ...) | Async Parent Run Manager.  
`callbacks.manager.AsyncRunManager`(*, run_id, ...) | Async Run Manager.  
`callbacks.manager.BaseRunManager`(*, run_id, ...) | Base class for run manager (a bound callback manager).  
`callbacks.manager.CallbackManager`(handlers) | Callback manager for LangChain.  
`callbacks.manager.CallbackManagerForChainGroup`(...) | Callback manager for the chain group.  
`callbacks.manager.CallbackManagerForChainRun`(*, ...) | Callback manager for chain run.  
`callbacks.manager.CallbackManagerForLLMRun`(*, ...) | Callback manager for LLM run.  
`callbacks.manager.CallbackManagerForRetrieverRun`(*, ...) | Callback manager for retriever run.  
`callbacks.manager.CallbackManagerForToolRun`(*, ...) | Callback manager for tool run.  
`callbacks.manager.ParentRunManager`(*, ...[, ...]) | Sync Parent Run Manager.  
`callbacks.manager.RunManager`(*, run_id, ...) | Sync Run Manager.  
`callbacks.stdout.StdOutCallbackHandler`([color]) | Callback Handler that prints to std out.  
`callbacks.streaming_stdout.StreamingStdOutCallbackHandler`() | Callback handler for streaming.  
  
**Functions**

`callbacks.manager.adispatch_custom_event`(...) | Dispatch an adhoc event to the handlers.  
---|---  
`callbacks.manager.ahandle_event`(handlers, ...) | Async generic event handler for AsyncCallbackManager.  
`callbacks.manager.atrace_as_chain_group`(...) | Get an async callback manager for a chain group in a context manager.  
`callbacks.manager.dispatch_custom_event`(...) | Dispatch an adhoc event.  
`callbacks.manager.handle_event`(handlers, ...) | Generic event handler for CallbackManager.  
`callbacks.manager.shielded`(func) | Makes so an awaitable method is always shielded from cancellation.  
`callbacks.manager.trace_as_chain_group`(...) | Get a callback manager for a chain group in a context manager.  
  
© Copyright 2023, LangChain Inc.