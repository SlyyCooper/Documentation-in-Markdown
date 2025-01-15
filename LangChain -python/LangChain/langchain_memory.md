* `memory`

# `memory`#

**Memory** maintains Chain state, incorporating context from past runs.

**Class hierarchy for Memory:**

    
    
    BaseMemory --> BaseChatMemory --> <name>Memory  # Examples: ZepMemory, MotorheadMemory
    

**Main helpers:**

    
    
    BaseChatMessageHistory
    

**Chat Message History** stores the chat message history in different stores.

**Class hierarchy for ChatMessageHistory:**

    
    
    BaseChatMessageHistory --> <name>ChatMessageHistory  # Example: ZepChatMessageHistory
    

**Main helpers:**

    
    
    AIMessage, BaseMessage, HumanMessage
    

**Classes**

`memory.combined.CombinedMemory` | Combining multiple memories' data together.  
---|---  
`memory.readonly.ReadOnlySharedMemory` | Memory wrapper that is read-only and cannot be changed.  
`memory.simple.SimpleMemory` | Simple memory for storing context or other information that shouldn't ever change between prompts.  
`memory.vectorstore_token_buffer_memory.ConversationVectorStoreTokenBufferMemory` | Conversation chat memory with token limit and vectordb backing.  
  
**Functions**

`memory.utils.get_prompt_input_key`(inputs, ...) | Get the prompt input key.  
---|---  
  
**Deprecated classes**

`memory.buffer.ConversationBufferMemory` |   
---|---  
`memory.buffer.ConversationStringBufferMemory` |   
`memory.buffer_window.ConversationBufferWindowMemory` |   
`memory.chat_memory.BaseChatMemory` |   
`memory.entity.BaseEntityStore` |   
`memory.entity.ConversationEntityMemory` |   
`memory.entity.InMemoryEntityStore` |   
`memory.entity.RedisEntityStore` |   
`memory.entity.SQLiteEntityStore` |   
`memory.entity.UpstashRedisEntityStore` |   
`memory.summary.ConversationSummaryMemory` |   
`memory.summary.SummarizerMixin` |   
`memory.summary_buffer.ConversationSummaryBufferMemory` |   
`memory.token_buffer.ConversationTokenBufferMemory` |   
`memory.vectorstore.VectorStoreRetrieverMemory` |   
  
© Copyright 2023, LangChain Inc.