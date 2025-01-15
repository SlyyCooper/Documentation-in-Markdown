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
    * `runnables` __
      * Runnable
      * RunnableBinding
      * RunnableBindingBase
      * RunnableEach
      * RunnableEachBase
      * RunnableGenerator
      * RunnableLambda
      * RunnableMap
      * RunnableParallel
      * RunnableSequence
      * RunnableSerializable
      * RunnableBranch
      * ContextThreadPoolExecutor
      * EmptyDict
      * RunnableConfig
      * DynamicRunnable
      * RunnableConfigurableAlternatives
      * RunnableConfigurableFields
      * StrEnum
      * RunnableWithFallbacks
      * Branch
      * CurveStyle
      * Edge
      * Graph
      * LabelsDict
      * MermaidDrawMethod
      * Node
      * NodeStyles
      * Stringifiable
      * AsciiCanvas
      * VertexViewer
      * PngDrawer
      * RunnableWithMessageHistory
      * RunnableAssign
      * RunnablePassthrough
      * RunnablePick
      * RunnableRetry
      * RouterInput
      * RouterRunnable
      * BaseStreamEvent
      * CustomStreamEvent
      * EventData
      * StandardStreamEvent
      * AddableDict
      * ConfigurableField
      * ConfigurableFieldMultiOption
      * ConfigurableFieldSingleOption
      * ConfigurableFieldSpec
      * FunctionNonLocals
      * GetLambdaSource
      * IsFunctionArgDict
      * IsLocalDict
      * NonLocals
      * SupportsAdd
      * chain
      * coerce_to_runnable
      * acall_func_with_variable_args
      * call_func_with_variable_args
      * ensure_config
      * get_async_callback_manager_for_config
      * get_callback_manager_for_config
      * get_config_list
      * get_executor_for_config
      * merge_configs
      * patch_config
      * run_in_executor
      * make_options_spec
      * prefix_config_spec
      * is_uuid
      * node_data_json
      * node_data_str
      * draw_ascii
      * draw_mermaid
      * draw_mermaid_png
      * aidentity
      * identity
      * aadd
      * accepts_config
      * accepts_context
      * accepts_run_manager
      * add
      * gated_coro
      * gather_with_concurrency
      * get_function_first_arg_dict_keys
      * get_lambda_source
      * get_unique_config_specs
      * indent_lines_after_first
      * is_async_callable
      * is_async_generator
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
  * `runnables`

# `runnables`#

LangChain **Runnable** and the **LangChain Expression Language (LCEL)**.

The LangChain Expression Language (LCEL) offers a declarative method to build
production-grade programs that harness the power of LLMs.

Programs created using LCEL and LangChain Runnables inherently support
synchronous, asynchronous, batch, and streaming operations.

Support for **async** allows servers hosting LCEL based programs to scale
better for higher concurrent loads.

**Batch** operations allow for processing multiple inputs in parallel.

**Streaming** of intermediate outputs, as they’re being generated, allows for
creating more responsive UX.

This module contains schema and implementation of LangChain Runnables
primitives.

**Classes**

`runnables.base.Runnable`() | A unit of work that can be invoked, batched, streamed, transformed and composed.  
---|---  
`runnables.base.RunnableBinding` | Wrap a Runnable with additional functionality.  
`runnables.base.RunnableBindingBase` | Runnable that delegates calls to another Runnable with a set of kwargs.  
`runnables.base.RunnableEach` | Runnable that delegates calls to another Runnable with each element of the input sequence.  
`runnables.base.RunnableEachBase` | Runnable that delegates calls to another Runnable with each element of the input sequence.  
`runnables.base.RunnableGenerator`(transform) | Runnable that runs a generator function.  
`runnables.base.RunnableLambda`(func[, afunc, ...]) | RunnableLambda converts a python callable into a Runnable.  
`runnables.base.RunnableMap` | alias of `RunnableParallel`  
`runnables.base.RunnableParallel` | Runnable that runs a mapping of Runnables in parallel, and returns a mapping of their outputs.  
`runnables.base.RunnableSequence` | Sequence of Runnables, where the output of each is the input of the next.  
`runnables.base.RunnableSerializable` | Runnable that can be serialized to JSON.  
`runnables.branch.RunnableBranch` | Runnable that selects which branch to run based on a condition.  
`runnables.config.ContextThreadPoolExecutor`([...]) | ThreadPoolExecutor that copies the context to the child thread.  
`runnables.config.EmptyDict` | Empty dict type.  
`runnables.config.RunnableConfig` | Configuration for a Runnable.  
`runnables.configurable.DynamicRunnable` | Serializable Runnable that can be dynamically configured.  
`runnables.configurable.RunnableConfigurableAlternatives` | Runnable that can be dynamically configured.  
`runnables.configurable.RunnableConfigurableFields` | Runnable that can be dynamically configured.  
`runnables.configurable.StrEnum`(value[, ...]) | String enum.  
`runnables.fallbacks.RunnableWithFallbacks` | Runnable that can fallback to other Runnables if it fails.  
`runnables.graph.Branch`(condition, ends) | Branch in a graph.  
`runnables.graph.CurveStyle`(value[, names, ...]) | Enum for different curve styles supported by Mermaid  
`runnables.graph.Edge`(source, target[, data, ...]) | Edge in a graph.  
`runnables.graph.Graph`(nodes, ...) | Graph of nodes and edges.  
`runnables.graph.LabelsDict` | Dictionary of labels for nodes and edges in a graph.  
`runnables.graph.MermaidDrawMethod`(value[, ...]) | Enum for different draw methods supported by Mermaid  
`runnables.graph.Node`(id, name, data, metadata) | Node in a graph.  
`runnables.graph.NodeStyles`([default, first, ...]) | Schema for Hexadecimal color codes for different node types.  
`runnables.graph.Stringifiable`(*args, **kwargs) |   
`runnables.graph_ascii.AsciiCanvas`(cols, lines) | Class for drawing in ASCII.  
`runnables.graph_ascii.VertexViewer`(name) | Class to define vertex box boundaries that will be accounted for during graph building by grandalf.  
`runnables.graph_png.PngDrawer`([fontname, labels]) | Helper class to draw a state graph into a PNG file.  
`runnables.history.RunnableWithMessageHistory` | Runnable that manages chat message history for another Runnable.  
`runnables.passthrough.RunnableAssign` | Runnable that assigns key-value pairs to Dict[str, Any] inputs.  
`runnables.passthrough.RunnablePassthrough` | Runnable to passthrough inputs unchanged or with additional keys.  
`runnables.passthrough.RunnablePick` | Runnable that picks keys from Dict[str, Any] inputs.  
`runnables.retry.RunnableRetry` | Retry a Runnable if it fails.  
`runnables.router.RouterInput` | Router input.  
`runnables.router.RouterRunnable` | Runnable that routes to a set of Runnables based on Input['key'].  
`runnables.schema.BaseStreamEvent` | Streaming event.  
`runnables.schema.CustomStreamEvent` | Custom stream event created by the user.  
`runnables.schema.EventData` | Data associated with a streaming event.  
`runnables.schema.StandardStreamEvent` | A standard stream event that follows LangChain convention for event data.  
`runnables.utils.AddableDict` | Dictionary that can be added to another dictionary.  
`runnables.utils.ConfigurableField`(id[, ...]) | Field that can be configured by the user.  
`runnables.utils.ConfigurableFieldMultiOption`(id, ...) | Field that can be configured by the user with multiple default values.  
`runnables.utils.ConfigurableFieldSingleOption`(id, ...) | Field that can be configured by the user with a default value.  
`runnables.utils.ConfigurableFieldSpec`(id, ...) | Field that can be configured by the user.  
`runnables.utils.FunctionNonLocals`() | Get the nonlocal variables accessed of a function.  
`runnables.utils.GetLambdaSource`() | Get the source code of a lambda function.  
`runnables.utils.IsFunctionArgDict`() | Check if the first argument of a function is a dict.  
`runnables.utils.IsLocalDict`(name, keys) | Check if a name is a local dict.  
`runnables.utils.NonLocals`() | Get nonlocal variables accessed.  
`runnables.utils.SupportsAdd`(*args, **kwargs) | Protocol for objects that support addition.  
  
**Functions**

`runnables.base.chain`() | Decorate a function to make it a Runnable.  
---|---  
`runnables.base.coerce_to_runnable`(thing) | Coerce a Runnable-like object into a Runnable.  
`runnables.config.acall_func_with_variable_args`(...) | Async call function that may optionally accept a run_manager and/or config.  
`runnables.config.call_func_with_variable_args`(...) | Call function that may optionally accept a run_manager and/or config.  
`runnables.config.ensure_config`([config]) | Ensure that a config is a dict with all keys present.  
`runnables.config.get_async_callback_manager_for_config`(config) | Get an async callback manager for a config.  
`runnables.config.get_callback_manager_for_config`(config) | Get a callback manager for a config.  
`runnables.config.get_config_list`(config, length) | Get a list of configs from a single config or a list of configs.  
`runnables.config.get_executor_for_config`(config) | Get an executor for a config.  
`runnables.config.merge_configs`(*configs) | Merge multiple configs into one.  
`runnables.config.patch_config`(config, *[, ...]) | Patch a config with new values.  
`runnables.config.run_in_executor`(...) | Run a function in an executor.  
`runnables.configurable.make_options_spec`(...) | Make a ConfigurableFieldSpec for a ConfigurableFieldSingleOption or ConfigurableFieldMultiOption.  
`runnables.configurable.prefix_config_spec`(...) | Prefix the id of a ConfigurableFieldSpec.  
`runnables.graph.is_uuid`(value) | Check if a string is a valid UUID.  
`runnables.graph.node_data_json`(node, *[, ...]) | Convert the data of a node to a JSON-serializable format.  
`runnables.graph.node_data_str`(id, data) | Convert the data of a node to a string.  
`runnables.graph_ascii.draw_ascii`(vertices, edges) | Build a DAG and draw it in ASCII.  
`runnables.graph_mermaid.draw_mermaid`(nodes, ...) | Draws a Mermaid graph using the provided graph data.  
`runnables.graph_mermaid.draw_mermaid_png`(...) | Draws a Mermaid graph as PNG using provided syntax.  
`runnables.passthrough.aidentity`(x) | Async identity function.  
`runnables.passthrough.identity`(x) | Identity function.  
`runnables.utils.aadd`(addables) | Asynchronously add a sequence of addable objects together.  
`runnables.utils.accepts_config`(callable) | Check if a callable accepts a config argument.  
`runnables.utils.accepts_context`(callable) | Check if a callable accepts a context argument.  
`runnables.utils.accepts_run_manager`(callable) | Check if a callable accepts a run_manager argument.  
`runnables.utils.add`(addables) | Add a sequence of addable objects together.  
`runnables.utils.gated_coro`(semaphore, coro) | Run a coroutine with a semaphore.  
`runnables.utils.gather_with_concurrency`(n, ...) | Gather coroutines with a limit on the number of concurrent coroutines.  
`runnables.utils.get_function_first_arg_dict_keys`(func) | Get the keys of the first argument of a function if it is a dict.  
`runnables.utils.get_lambda_source`(func) | Get the source code of a lambda function.  
`runnables.utils.get_unique_config_specs`(specs) | Get the unique config specs from a sequence of config specs.  
`runnables.utils.indent_lines_after_first`(...) | Indent all lines of text after the first line.  
`runnables.utils.is_async_callable`(func) | Check if a function is async.  
`runnables.utils.is_async_generator`(func) | Check if a function is an async generator.  
  
© Copyright 2023, LangChain Inc.