* `embeddings`

# `embeddings`#

**Embedding models** are wrappers around embedding models from different APIs
and services.

**Embedding models** can be LLMs or not.

**Class hierarchy:**

    
    
    Embeddings --> <name>Embeddings  # Examples: OpenAIEmbeddings, HuggingFaceEmbeddings
    

**Classes**

`embeddings.cache.CacheBackedEmbeddings`(...) | Interface for caching results from embedding models.  
---|---  
  
**Functions**

`embeddings.base.init_embeddings`(model, *[, ...]) |   
---|---  
  
© Copyright 2023, LangChain Inc.