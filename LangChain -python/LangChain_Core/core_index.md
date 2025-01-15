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

# langchain-core: 0.3.29#

`langchain-core` defines the base abstractions for the LangChain ecosystem.

The interfaces for core components like chat models, LLMs, vector stores,
retrievers, and more are defined here. The universal invocation protocol
(Runnables) along with a syntax for combining components (LangChain Expression
Language) are also defined here.

No third-party integrations are defined here. The dependencies are kept
purposefully very lightweight.

## agents#

**Classes**

`agents.AgentAction` | Represents a request to execute an action by an agent.  
---|---  
`agents.AgentActionMessageLog` | Representation of an action to be executed by an agent.  
`agents.AgentFinish` | Final return value of an ActionAgent.  
`agents.AgentStep` | Result of running an AgentAction.  
  
## beta#

**Classes**

`beta.runnables.context.Context`() | Context for a runnable.  
---|---  
`beta.runnables.context.ContextGet` |   
`beta.runnables.context.ContextSet` |   
`beta.runnables.context.PrefixContext`([prefix]) | Context for a runnable with a prefix.  
  
**Functions**

`beta.runnables.context.aconfig_with_context`(...) | Asynchronously patch a runnable config with context getters and setters.  
---|---  
`beta.runnables.context.config_with_context`(...) | Patch a runnable config with context getters and setters.  
  
## caches#

**Classes**

`caches.BaseCache`() | Interface for a caching layer for LLMs and Chat models.  
---|---  
`caches.InMemoryCache`(*[, maxsize]) | Cache that stores things in memory.  
  
## callbacks#

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
  
## chat_history#

**Classes**

`chat_history.BaseChatMessageHistory`() | Abstract base class for storing chat message history.  
---|---  
`chat_history.InMemoryChatMessageHistory` | In memory implementation of chat message history.  
  
## chat_loaders#

**Classes**

`chat_loaders.BaseChatLoader`() | Base class for chat loaders.  
---|---  
  
## chat_sessions#

**Classes**

`chat_sessions.ChatSession` | Chat Session represents a single conversation, channel, or other group of messages.  
---|---  
  
## document_loaders#

**Classes**

`document_loaders.base.BaseBlobParser`() | Abstract interface for blob parsers.  
---|---  
`document_loaders.base.BaseLoader`() | Interface for Document Loader.  
`document_loaders.blob_loaders.BlobLoader`() | Abstract interface for blob loaders implementation.  
`document_loaders.langsmith.LangSmithLoader`(*) | Load LangSmith Dataset examples as Documents.  
  
## documents#

**Classes**

`documents.base.BaseMedia` | Use to represent media content.  
---|---  
`documents.base.Blob` | Blob represents raw data by either reference or value.  
`documents.base.Document` | Class for storing a piece of text and associated metadata.  
`documents.compressor.BaseDocumentCompressor` | Base class for document compressors.  
`documents.transformers.BaseDocumentTransformer`() | Abstract base class for document transformation.  
  
## embeddings#

**Classes**

`embeddings.embeddings.Embeddings`() | Interface for embedding models.  
---|---  
`embeddings.fake.DeterministicFakeEmbedding` | Deterministic fake embedding model for unit testing purposes.  
`embeddings.fake.FakeEmbeddings` | Fake embedding model for unit testing purposes.  
  
## example_selectors#

**Classes**

`example_selectors.base.BaseExampleSelector`() | Interface for selecting examples to include in prompts.  
---|---  
`example_selectors.length_based.LengthBasedExampleSelector` | Select examples based on length.  
`example_selectors.semantic_similarity.MaxMarginalRelevanceExampleSelector` | Select examples based on Max Marginal Relevance.  
`example_selectors.semantic_similarity.SemanticSimilarityExampleSelector` | Select examples based on semantic similarity.  
  
**Functions**

`example_selectors.semantic_similarity.sorted_values`(values) | Return a list of values in dict sorted by key.  
---|---  
  
## exceptions#

**Classes**

`exceptions.ErrorCode`(value[, names, module, ...]) |   
---|---  
`exceptions.LangChainException` | General LangChain exception.  
`exceptions.OutputParserException`(error[, ...]) | Exception that output parsers should raise to signify a parsing error.  
`exceptions.TracerException` | Base class for exceptions in tracers module.  
  
**Functions**

`exceptions.create_message`(*, message, error_code) |   
---|---  
  
## globals#

**Functions**

`globals.get_debug`() | Get the value of the debug global setting.  
---|---  
`globals.get_llm_cache`() | Get the value of the llm_cache global setting.  
`globals.get_verbose`() | Get the value of the verbose global setting.  
`globals.set_debug`(value) | Set a new value for the debug global setting.  
`globals.set_llm_cache`(value) | Set a new LLM cache, overwriting the previous value, if any.  
`globals.set_verbose`(value) | Set a new value for the verbose global setting.  
  
## indexing#

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
  
## language_models#

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
  
## load#

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
  
## messages#

**Classes**

`messages.ai.AIMessage` | Message from an AI.  
---|---  
`messages.ai.AIMessageChunk` | Message chunk from an AI.  
`messages.ai.InputTokenDetails` | Breakdown of input token counts.  
`messages.ai.OutputTokenDetails` | Breakdown of output token counts.  
`messages.ai.UsageMetadata` | Usage metadata for a message, such as token counts.  
`messages.base.BaseMessage` | Base abstract message class.  
`messages.base.BaseMessageChunk` | Message chunk, which can be concatenated with other Message chunks.  
`messages.chat.ChatMessage` | Message that can be assigned an arbitrary speaker (i.e. role).  
`messages.chat.ChatMessageChunk` | Chat Message chunk.  
`messages.function.FunctionMessage` | Message for passing the result of executing a tool back to a model.  
`messages.function.FunctionMessageChunk` | Function Message chunk.  
`messages.human.HumanMessage` | Message from a human.  
`messages.human.HumanMessageChunk` | Human Message chunk.  
`messages.modifier.RemoveMessage` | Message responsible for deleting other messages.  
`messages.system.SystemMessage` | Message for priming AI behavior.  
`messages.system.SystemMessageChunk` | System Message chunk.  
`messages.tool.InvalidToolCall` | Allowance for errors made by LLM.  
`messages.tool.ToolCall` | Represents a request to call a tool.  
`messages.tool.ToolCallChunk` | A chunk of a tool call (e.g., as part of a stream).  
`messages.tool.ToolMessage` | Message for passing the result of executing a tool back to a model.  
`messages.tool.ToolMessageChunk` | Tool Message chunk.  
`messages.tool.ToolOutputMixin`() | Mixin for objects that tools can return directly.  
  
**Functions**

`messages.ai.add_ai_message_chunks`(left, *others) | Add multiple AIMessageChunks together.  
---|---  
`messages.ai.add_usage`(left, right) | Recursively add two UsageMetadata objects.  
`messages.ai.subtract_usage`(left, right) | Recursively subtract two UsageMetadata objects.  
`messages.base.get_msg_title_repr`(title, *[, ...]) | Get a title representation for a message.  
`messages.base.merge_content`(first_content, ...) | Merge two message contents.  
`messages.base.message_to_dict`(message) | Convert a Message to a dictionary.  
`messages.base.messages_to_dict`(messages) | Convert a sequence of Messages to a list of dictionaries.  
`messages.tool.default_tool_chunk_parser`(...) | Best-effort parsing of tool chunks.  
`messages.tool.default_tool_parser`(raw_tool_calls) | Best-effort parsing of tools.  
`messages.tool.invalid_tool_call`(*[, name, ...]) |   
`messages.tool.tool_call`(*, name, args, id) |   
`messages.tool.tool_call_chunk`(*[, name, ...]) |   
`messages.utils.convert_to_messages`(messages) | Convert a sequence of messages to a list of messages.  
`messages.utils.convert_to_openai_messages`(...) | Convert LangChain messages into OpenAI message dicts.  
`messages.utils.filter_messages`([messages]) | Filter messages based on name, type or id.  
`messages.utils.get_buffer_string`(messages[, ...]) | Convert a sequence of Messages to strings and concatenate them into one string.  
`messages.utils.merge_message_runs`([messages]) | Merge consecutive Messages of the same type.  
`messages.utils.message_chunk_to_message`(chunk) | Convert a message chunk to a message.  
`messages.utils.messages_from_dict`(messages) | Convert a sequence of messages from dicts to Message objects.  
`messages.utils.trim_messages`([messages]) | Trim messages to be below a token count.  
  
## output_parsers#

**Classes**

`output_parsers.base.BaseGenerationOutputParser` | Base class to parse the output of an LLM call.  
---|---  
`output_parsers.base.BaseLLMOutputParser`() | Abstract base class for parsing the outputs of a model.  
`output_parsers.base.BaseOutputParser` | Base class to parse the output of an LLM call.  
`output_parsers.json.JsonOutputParser` | Parse the output of an LLM call to a JSON object.  
`output_parsers.json.SimpleJsonOutputParser` | alias of `JsonOutputParser`  
`output_parsers.list.CommaSeparatedListOutputParser` | Parse the output of an LLM call to a comma-separated list.  
`output_parsers.list.ListOutputParser` | Parse the output of an LLM call to a list.  
`output_parsers.list.MarkdownListOutputParser` | Parse a Markdown list.  
`output_parsers.list.NumberedListOutputParser` | Parse a numbered list.  
`output_parsers.openai_functions.JsonKeyOutputFunctionsParser` | Parse an output as the element of the Json object.  
`output_parsers.openai_functions.JsonOutputFunctionsParser` | Parse an output as the Json object.  
`output_parsers.openai_functions.OutputFunctionsParser` | Parse an output that is one of sets of values.  
`output_parsers.openai_functions.PydanticAttrOutputFunctionsParser` | Parse an output as an attribute of a pydantic object.  
`output_parsers.openai_functions.PydanticOutputFunctionsParser` | Parse an output as a pydantic object.  
`output_parsers.openai_tools.JsonOutputKeyToolsParser` | Parse tools from OpenAI response.  
`output_parsers.openai_tools.JsonOutputToolsParser` | Parse tools from OpenAI response.  
`output_parsers.openai_tools.PydanticToolsParser` | Parse tools from OpenAI response.  
`output_parsers.pydantic.PydanticOutputParser` | Parse an output using a pydantic model.  
`output_parsers.string.StrOutputParser` | OutputParser that parses LLMResult into the top likely string.  
`output_parsers.transform.BaseCumulativeTransformOutputParser` | Base class for an output parser that can handle streaming input.  
`output_parsers.transform.BaseCumulativeTransformOutputParser[Any]` | Base class for an output parser that can handle streaming input.  
`output_parsers.transform.BaseTransformOutputParser` | Base class for an output parser that can handle streaming input.  
`output_parsers.transform.BaseTransformOutputParser[list[str]]` | Base class for an output parser that can handle streaming input.  
`output_parsers.transform.BaseTransformOutputParser[str]` | Base class for an output parser that can handle streaming input.  
`output_parsers.xml.XMLOutputParser` | Parse an output using xml format.  
  
**Functions**

`output_parsers.list.droplastn`(iter, n) | Drop the last n elements of an iterator.  
---|---  
`output_parsers.openai_tools.make_invalid_tool_call`(...) | Create an InvalidToolCall from a raw tool call.  
`output_parsers.openai_tools.parse_tool_call`(...) | Parse a single tool call.  
`output_parsers.openai_tools.parse_tool_calls`(...) | Parse a list of tool calls.  
`output_parsers.xml.nested_element`(path, elem) | Get nested element from path.  
  
## outputs#

**Classes**

`outputs.chat_generation.ChatGeneration` | A single chat generation output.  
---|---  
`outputs.chat_generation.ChatGenerationChunk` | ChatGeneration chunk, which can be concatenated with other ChatGeneration chunks.  
`outputs.chat_result.ChatResult` | Use to represent the result of a chat model call with a single prompt.  
`outputs.generation.Generation` | A single text generation output.  
`outputs.generation.GenerationChunk` | Generation chunk, which can be concatenated with other Generation chunks.  
`outputs.llm_result.LLMResult` | A container for results of an LLM call.  
`outputs.run_info.RunInfo` | Class that contains metadata for a single execution of a Chain or model.  
  
## prompt_values#

**Classes**

`prompt_values.ChatPromptValue` | Chat prompt value.  
---|---  
`prompt_values.ChatPromptValueConcrete` | Chat prompt value which explicitly lists out the message types it accepts.  
`prompt_values.ImagePromptValue` | Image prompt value.  
`prompt_values.ImageURL` | Image URL.  
`prompt_values.PromptValue` | Base abstract class for inputs to any language model.  
`prompt_values.StringPromptValue` | String prompt value.  
  
## prompts#

**Classes**

`prompts.base.BasePromptTemplate` | Base class for all prompt templates, returning a prompt.  
---|---  
`prompts.base.BasePromptTemplate[ImageURL]` | Base class for all prompt templates, returning a prompt.  
`prompts.chat.AIMessagePromptTemplate` | AI message prompt template.  
`prompts.chat.BaseChatPromptTemplate` | Base class for chat prompt templates.  
`prompts.chat.BaseMessagePromptTemplate` | Base class for message prompt templates.  
`prompts.chat.BaseStringMessagePromptTemplate` | Base class for message prompt templates that use a string prompt template.  
`prompts.chat.ChatMessagePromptTemplate` | Chat message prompt template.  
`prompts.chat.ChatPromptTemplate` | Prompt template for chat models.  
`prompts.chat.HumanMessagePromptTemplate` | Human message prompt template.  
`prompts.chat.MessagesPlaceholder` | Prompt template that assumes variable is already list of messages.  
`prompts.chat.SystemMessagePromptTemplate` | System message prompt template.  
`prompts.few_shot.FewShotChatMessagePromptTemplate` | Chat prompt template that supports few-shot examples.  
`prompts.few_shot.FewShotPromptTemplate` | Prompt template that contains few shot examples.  
`prompts.few_shot_with_templates.FewShotPromptWithTemplates` | Prompt template that contains few shot examples.  
`prompts.image.ImagePromptTemplate` | Image prompt template for a multimodal model.  
`prompts.prompt.PromptTemplate` | Prompt template for a language model.  
`prompts.string.StringPromptTemplate` | String prompt that exposes the format method, returning a prompt.  
`prompts.structured.StructuredPrompt` |   
  
**Functions**

`prompts.base.aformat_document`(doc, prompt) | Async format a document into a string based on a prompt template.  
---|---  
`prompts.base.format_document`(doc, prompt) | Format a document into a string based on a prompt template.  
`prompts.loading.load_prompt`(path[, encoding]) | Unified method for loading a prompt from LangChainHub or local fs.  
`prompts.loading.load_prompt_from_config`(config) | Load prompt from Config Dict.  
`prompts.string.check_valid_template`(...) | Check that template string is valid.  
`prompts.string.get_template_variables`(...) | Get the variables from the template.  
`prompts.string.jinja2_formatter`(template, /, ...) | Format a template using jinja2.  
`prompts.string.mustache_formatter`(template, ...) | Format a template using mustache.  
`prompts.string.mustache_schema`(template) | Get the variables from a mustache template.  
`prompts.string.mustache_template_vars`(template) | Get the variables from a mustache template.  
`prompts.string.validate_jinja2`(template, ...) | Validate that the input variables are valid for the template.  
  
**Deprecated classes**

`prompts.pipeline.PipelinePromptTemplate` |   
---|---  
  
## rate_limiters#

**Classes**

`rate_limiters.BaseRateLimiter`(*args, **kwargs) |   
---|---  
`rate_limiters.InMemoryRateLimiter`(*[, ...]) |   
  
## retrievers#

**Classes**

`retrievers.BaseRetriever` | Abstract base class for a Document retrieval system.  
---|---  
`retrievers.LangSmithRetrieverParams` | LangSmith parameters for tracing.  
  
## runnables#

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
  
## stores#

**Classes**

`stores.BaseStore`() | Abstract interface for a key-value store.  
---|---  
`stores.InMemoryBaseStore`() | In-memory implementation of the BaseStore using a dictionary.  
`stores.InMemoryByteStore`() | In-memory store for bytes.  
`stores.InMemoryStore`() | In-memory store for any type of data.  
`stores.InvalidKeyException` | Raised when a key is invalid; e.g., uses incorrect characters.  
  
## structured_query#

**Classes**

`structured_query.Comparator`(value[, names, ...]) | Enumerator of the comparison operators.  
---|---  
`structured_query.Comparison` | Comparison to a value.  
`structured_query.Expr` | Base class for all expressions.  
`structured_query.FilterDirective` | Filtering expression.  
`structured_query.Operation` | Logical operation over other directives.  
`structured_query.Operator`(value[, names, ...]) | Enumerator of the operations.  
`structured_query.StructuredQuery` | Structured query.  
`structured_query.Visitor`() | Defines interface for IR translation using a visitor pattern.  
  
## sys_info#

**Functions**

`sys_info.print_sys_info`(*[, additional_pkgs]) | Print information about the environment for debugging purposes.  
---|---  
  
## tools#

**Classes**

`tools.base.BaseTool` | Interface LangChain tools must implement.  
---|---  
`tools.base.BaseToolkit` | Base Toolkit representing a collection of related tools.  
`tools.base.InjectedToolArg`() | Annotation for a Tool arg that is **not** meant to be generated by a model.  
`tools.base.InjectedToolCallId`() | Annotation for injecting the tool_call_id.  
`tools.base.SchemaAnnotationError` | Raised when 'args_schema' is missing or has an incorrect type annotation.  
`tools.base.ToolException` | Optional exception that tool throws when execution error occurs.  
`tools.retriever.RetrieverInput` | Input to the retriever.  
`tools.simple.Tool` | Tool that takes in function or coroutine directly.  
`tools.structured.StructuredTool` | Tool that can operate on any number of inputs.  
  
**Functions**

`tools.base.create_schema_from_function`(...) | Create a pydantic schema from a function's signature.  
---|---  
`tools.base.get_all_basemodel_annotations`(cls, *) |   
`tools.convert.convert_runnable_to_tool`(runnable) | Convert a Runnable into a BaseTool.  
`tools.convert.tool`() | Make tools out of functions, can be used with or without arguments.  
`tools.render.render_text_description`(tools) | Render the tool name and description in plain text.  
`tools.render.render_text_description_and_args`(tools) | Render the tool name, description, and args in plain text.  
`tools.retriever.create_retriever_tool`(...[, ...]) | Create a tool to do retrieval of documents.  
  
## tracers#

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
  
## utils#

**Classes**

`utils.aiter.NoLock`() | Dummy lock that provides the proper interface but no protection.  
---|---  
`utils.aiter.Tee`(iterable[, n, lock]) | Create `n` separate asynchronous iterators over `iterable`.  
`utils.aiter.aclosing`(thing) | Async context manager for safely finalizing an asynchronously cleaned-up resource such as an async generator, calling its `aclose()` method.  
`utils.aiter.atee` | alias of `Tee`  
`utils.formatting.StrictFormatter`() | Formatter that checks for extra keys.  
`utils.function_calling.FunctionDescription` | Representation of a callable function to send to an LLM.  
`utils.function_calling.ToolDescription` | Representation of a callable function to the OpenAI API.  
`utils.iter.NoLock`() | Dummy lock that provides the proper interface but no protection.  
`utils.iter.Tee`(iterable[, n, lock]) | Create `n` separate asynchronous iterators over `iterable`  
`utils.iter.safetee` | alias of `Tee`  
`utils.mustache.ChevronError` | Custom exception for Chevron errors.  
  
**Functions**

`utils.aiter.abatch_iterate`(size, iterable) | Utility batching function for async iterables.  
---|---  
`utils.aiter.py_anext`(iterator[, default]) | Pure-Python implementation of anext() for testing purposes.  
`utils.aiter.tee_peer`(iterator, buffer, ...) | An individual iterator of a `tee()`.  
`utils.env.env_var_is_set`(env_var) | Check if an environment variable is set.  
`utils.env.get_from_dict_or_env`(data, key, ...) | Get a value from a dictionary or an environment variable.  
`utils.env.get_from_env`(key, env_key[, default]) | Get a value from a dictionary or an environment variable.  
`utils.function_calling.convert_to_openai_function`(...) | Convert a raw function/class to an OpenAI function. :param function: A dictionary, Pydantic BaseModel class, TypedDict class, a LangChain Tool object, or a Python function. If a dictionary is passed in, it is assumed to already be a valid OpenAI function, a JSON schema with top-level 'title' key specified, an Anthropic format tool, or an Amazon Bedrock Converse format tool. :param strict: If True, model output is guaranteed to exactly match the JSON Schema provided in the function definition. If None, `strict` argument will not be included in function definition.  
`utils.function_calling.convert_to_openai_tool`(tool, *) | Convert a tool-like object to an OpenAI tool schema.  
`utils.function_calling.tool_example_to_messages`(...) |   
`utils.html.extract_sub_links`(raw_html, url, *) | Extract all links from a raw HTML string and convert into absolute paths.  
`utils.html.find_all_links`(raw_html, *[, pattern]) | Extract all links from a raw HTML string.  
`utils.input.get_bolded_text`(text) | Get bolded text.  
`utils.input.get_color_mapping`(items[, ...]) | Get mapping for items to a support color.  
`utils.input.get_colored_text`(text, color) | Get colored text.  
`utils.input.print_text`(text[, color, end, file]) | Print text with highlighting and no end characters.  
`utils.interactive_env.is_interactive_env`() | Determine if running within IPython or Jupyter.  
`utils.iter.batch_iterate`(size, iterable) | Utility batching function.  
`utils.iter.tee_peer`(iterator, buffer, peers, ...) | An individual iterator of a `tee()`.  
`utils.json.parse_and_check_json_markdown`(...) | Parse a JSON string from a Markdown string and check that it contains the expected keys.  
`utils.json.parse_json_markdown`(json_string, *) | Parse a JSON string from a Markdown string.  
`utils.json.parse_partial_json`(s, *[, strict]) | Parse a JSON string that may be missing closing braces.  
`utils.json_schema.dereference_refs`(schema_obj, *) | Try to substitute $refs in JSON Schema.  
`utils.mustache.grab_literal`(template, l_del) | Parse a literal from the template.  
`utils.mustache.l_sa_check`(template, literal, ...) | Do a preliminary check to see if a tag could be a standalone.  
`utils.mustache.parse_tag`(template, l_del, r_del) | Parse a tag from a template.  
`utils.mustache.r_sa_check`(template, ...) | Do a final check to see if a tag could be a standalone.  
`utils.mustache.render`([template, data, ...]) | Render a mustache template.  
`utils.mustache.tokenize`(template[, ...]) | Tokenize a mustache template.  
`utils.pydantic.create_model`(__model_name[, ...]) | Create a pydantic model with the given field definitions.  
`utils.pydantic.create_model_v2`(model_name, *) | Create a pydantic model with the given field definitions.  
`utils.pydantic.get_fields`() | Get the field names of a Pydantic model.  
`utils.pydantic.get_pydantic_major_version`() | Get the major version of Pydantic.  
`utils.pydantic.is_basemodel_instance`(obj) | Check if the given class is an instance of Pydantic BaseModel.  
`utils.pydantic.is_basemodel_subclass`(cls) | Check if the given class is a subclass of Pydantic BaseModel.  
`utils.pydantic.is_pydantic_v1_subclass`(cls) | Check if the installed Pydantic version is 1.x-like.  
`utils.pydantic.is_pydantic_v2_subclass`(cls) | Check if the installed Pydantic version is 1.x-like.  
`utils.pydantic.pre_init`(func) | Decorator to run a function before model initialization.  
`utils.strings.comma_list`(items) | Convert a list to a comma-separated string.  
`utils.strings.stringify_dict`(data) | Stringify a dictionary.  
`utils.strings.stringify_value`(val) | Stringify a value.  
`utils.utils.build_extra_kwargs`(extra_kwargs, ...) | Build extra kwargs from values and extra_kwargs.  
`utils.utils.check_package_version`(package[, ...]) | Check the version of a package.  
`utils.utils.convert_to_secret_str`(value) | Convert a string to a SecretStr if needed.  
`utils.utils.from_env`() | Create a factory method that gets a value from an environment variable.  
`utils.utils.get_pydantic_field_names`(...) | Get field names, including aliases, for a pydantic class.  
`utils.utils.guard_import`(module_name, *[, ...]) | Dynamically import a module and raise an exception if the module is not installed.  
`utils.utils.mock_now`(dt_value) | Context manager for mocking out datetime.now() in unit tests.  
`utils.utils.raise_for_status_with_text`(response) | Raise an error with the response text.  
`utils.utils.secret_from_env`() | Secret from env.  
`utils.utils.xor_args`(*arg_groups) | Validate specified keyword args are mutually exclusive."  
  
**Deprecated functions**

`utils.function_calling.convert_pydantic_to_openai_function`(...) |   
---|---  
`utils.function_calling.convert_pydantic_to_openai_tool`(...) |   
`utils.function_calling.convert_python_function_to_openai_function`(...) |   
`utils.function_calling.format_tool_to_openai_function`(tool) |   
`utils.function_calling.format_tool_to_openai_tool`(tool) |   
`utils.loading.try_load_from_hub`(*args, **kwargs) |   
  
## vectorstores#

**Classes**

`vectorstores.base.VectorStore`() | Interface for vector store.  
---|---  
`vectorstores.base.VectorStoreRetriever` | Base Retriever class for VectorStore.  
`vectorstores.in_memory.InMemoryVectorStore`(...) | In-memory vector store implementation.  
  
**Functions**

`vectorstores.utils.maximal_marginal_relevance`(...) | Calculate maximal marginal relevance.  
---|---  
  
© Copyright 2023, LangChain Inc.