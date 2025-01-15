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
    * `tracers` __
      * AsyncBaseTracer
      * BaseTracer
      * EvaluatorCallbackHandler
      * RunInfo
      * LangChainTracer
      * LogEntry
      * LogStreamCallbackHandler
      * RunLog
      * RunLogPatch
      * RunState
      * AsyncRootListenersTracer
      * RootListenersTracer
      * RunCollectorCallbackHandler
      * ConsoleCallbackHandler
      * FunctionCallbackHandler
      * collect_runs
      * register_configure_hook
      * tracing_enabled
      * tracing_v2_enabled
      * wait_for_all_evaluators
      * get_client
      * log_error_once
      * wait_for_all_tracers
      * LangChainTracerV1
      * get_headers
      * elapsed
      * try_json_stringify
      * BaseRun
      * ChainRun
      * LLMRun
      * ToolRun
      * TracerSession
      * TracerSessionBase
      * TracerSessionV1
      * TracerSessionV1Base
      * TracerSessionV1Create
      * RunTypeEnum
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
  * `tracers`

# `tracers`#

**Tracers** are classes for tracing runs.

**Class hierarchy:**

    
    
    BaseCallbackHandler --> BaseTracer --> <name>Tracer  # Examples: LangChainTracer, RootListenersTracer
                                       --> <name>  # Examples: LogStreamCallbackHandler
    

**Classes**

`tracers.base.AsyncBaseTracer`(*[, _schema_format]) | Async Base interface for tracers.  
---|---  
`tracers.base.BaseTracer`(*[, _schema_format]) | Base interface for tracers.  
`tracers.evaluation.EvaluatorCallbackHandler`(...) | Tracer that runs a run evaluator whenever a run is persisted.  
`tracers.event_stream.RunInfo` | Information about a run.  
`tracers.langchain.LangChainTracer`([...]) | Implementation of the SharedTracer that POSTS to the LangChain endpoint.  
`tracers.log_stream.LogEntry` | A single entry in the run log.  
`tracers.log_stream.LogStreamCallbackHandler`(*) | Tracer that streams run logs to a stream.  
`tracers.log_stream.RunLog`(*ops, state) | Run log.  
`tracers.log_stream.RunLogPatch`(*ops) | Patch to the run log.  
`tracers.log_stream.RunState` | State of the run.  
`tracers.root_listeners.AsyncRootListenersTracer`(*, ...) | Async Tracer that calls listeners on run start, end, and error.  
`tracers.root_listeners.RootListenersTracer`(*, ...) | Tracer that calls listeners on run start, end, and error.  
`tracers.run_collector.RunCollectorCallbackHandler`([...]) | Tracer that collects all nested runs in a list.  
`tracers.stdout.ConsoleCallbackHandler`(**kwargs) | Tracer that prints to the console.  
`tracers.stdout.FunctionCallbackHandler`(...) | Tracer that calls a function with a single str parameter.  
  
**Functions**

`tracers.context.collect_runs`() | Collect all run traces in context.  
---|---  
`tracers.context.register_configure_hook`(...) | Register a configure hook.  
`tracers.context.tracing_enabled`([session_name]) | Throw an error because this has been replaced by tracing_v2_enabled.  
`tracers.context.tracing_v2_enabled`([...]) | Instruct LangChain to log all runs in context to LangSmith.  
`tracers.evaluation.wait_for_all_evaluators`() | Wait for all tracers to finish.  
`tracers.langchain.get_client`() | Get the client.  
`tracers.langchain.log_error_once`(method, ...) | Log an error once.  
`tracers.langchain.wait_for_all_tracers`() | Wait for all tracers to finish.  
`tracers.langchain_v1.LangChainTracerV1`(...) | Throw an error because this has been replaced by LangChainTracer.  
`tracers.langchain_v1.get_headers`(*args, **kwargs) | Throw an error because this has been replaced by get_headers.  
`tracers.stdout.elapsed`(run) | Get the elapsed time of a run.  
`tracers.stdout.try_json_stringify`(obj, fallback) | Try to stringify an object to JSON.  
  
**Deprecated classes**

`tracers.schemas.BaseRun`(*, uuid[, ...]) |   
---|---  
`tracers.schemas.ChainRun`(*, uuid[, ...]) |   
`tracers.schemas.LLMRun`(*, uuid[, ...]) |   
`tracers.schemas.ToolRun`(*, uuid[, ...]) |   
`tracers.schemas.TracerSession`(*[, ...]) |   
`tracers.schemas.TracerSessionBase`(*[, ...]) |   
`tracers.schemas.TracerSessionV1`(*[, ...]) |   
`tracers.schemas.TracerSessionV1Base`(*[, ...]) |   
`tracers.schemas.TracerSessionV1Create`(*[, ...]) |   
  
**Deprecated functions**

`tracers.schemas.RunTypeEnum`() |   
---|---  
  
© Copyright 2023, LangChain Inc.