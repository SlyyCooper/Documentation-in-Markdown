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
    * `messages` __
      * AIMessage
      * AIMessageChunk
      * InputTokenDetails
      * OutputTokenDetails
      * UsageMetadata
      * BaseMessage
      * BaseMessageChunk
      * ChatMessage
      * ChatMessageChunk
      * FunctionMessage
      * FunctionMessageChunk
      * HumanMessage
      * HumanMessageChunk
      * RemoveMessage
      * SystemMessage
      * SystemMessageChunk
      * InvalidToolCall
      * ToolCall
      * ToolCallChunk
      * ToolMessage
      * ToolMessageChunk
      * ToolOutputMixin
      * add_ai_message_chunks
      * add_usage
      * subtract_usage
      * get_msg_title_repr
      * merge_content
      * message_to_dict
      * messages_to_dict
      * default_tool_chunk_parser
      * default_tool_parser
      * invalid_tool_call
      * tool_call
      * tool_call_chunk
      * convert_to_messages
      * convert_to_openai_messages
      * filter_messages
      * get_buffer_string
      * merge_message_runs
      * message_chunk_to_message
      * messages_from_dict
      * trim_messages
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
  * `messages`

# `messages`#

**Messages** are objects used in prompts and chat conversations.

**Class hierarchy:**

    
    
    BaseMessage --> SystemMessage, AIMessage, HumanMessage, ChatMessage, FunctionMessage, ToolMessage
                --> BaseMessageChunk --> SystemMessageChunk, AIMessageChunk, HumanMessageChunk, ChatMessageChunk, FunctionMessageChunk, ToolMessageChunk
    

**Main helpers:**

    
    
    ChatPromptTemplate
    

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
  
© Copyright 2023, LangChain Inc.