* `retrievers`

# `retrievers`#

**Retriever** class returns Documents given a text **query**.

It is more general than a vector store. A retriever does not need to be able
to store documents, only to return (or retrieve) it. Vector stores can be used
as the backbone of a retriever, but there are other types of retrievers as
well.

**Class hierarchy:**

    
    
    BaseRetriever --> <name>Retriever  # Examples: ArxivRetriever, MergerRetriever
    

**Main helpers:**

    
    
    Document, Serializable, Callbacks,
    CallbackManagerForRetrieverRun, AsyncCallbackManagerForRetrieverRun
    

**Classes**

`retrievers.contextual_compression.ContextualCompressionRetriever` | Retriever that wraps a base retriever and compresses the results.  
---|---  
`retrievers.document_compressors.base.DocumentCompressorPipeline` | Document compressor that uses a pipeline of Transformers.  
`retrievers.document_compressors.chain_extract.LLMChainExtractor` | Document compressor that uses an LLM chain to extract the relevant parts of documents.  
`retrievers.document_compressors.chain_extract.NoOutputParser` | Parse outputs that could return a null string of some sort.  
`retrievers.document_compressors.chain_filter.LLMChainFilter` | Filter that drops documents that aren't relevant to the query.  
`retrievers.document_compressors.cross_encoder.BaseCrossEncoder`() | Interface for cross encoder models.  
`retrievers.document_compressors.cross_encoder_rerank.CrossEncoderReranker` | Document compressor that uses CrossEncoder for reranking.  
`retrievers.document_compressors.embeddings_filter.EmbeddingsFilter` | Document compressor that uses embeddings to drop documents unrelated to the query.  
`retrievers.document_compressors.listwise_rerank.LLMListwiseRerank` | Document compressor that uses Zero-Shot Listwise Document Reranking.  
`retrievers.ensemble.EnsembleRetriever` | Retriever that ensembles the multiple retrievers.  
`retrievers.merger_retriever.MergerRetriever` | Retriever that merges the results of multiple retrievers.  
`retrievers.multi_query.LineListOutputParser` | Output parser for a list of lines.  
`retrievers.multi_query.MultiQueryRetriever` | Given a query, use an LLM to write a set of queries.  
`retrievers.multi_vector.MultiVectorRetriever` | Retrieve from a set of multiple embeddings for the same document.  
`retrievers.multi_vector.SearchType`(value[, ...]) | Enumerator of the types of search to perform.  
`retrievers.parent_document_retriever.ParentDocumentRetriever` | Retrieve small chunks then retrieve their parent documents.  
`retrievers.re_phraser.RePhraseQueryRetriever` | Given a query, use an LLM to re-phrase it.  
`retrievers.self_query.base.SelfQueryRetriever` | Retriever that uses a vector store and an LLM to generate the vector store queries.  
`retrievers.time_weighted_retriever.TimeWeightedVectorStoreRetriever` | Retriever that combines embedding similarity with recency in retrieving values.  
  
**Functions**

`retrievers.document_compressors.chain_extract.default_get_input`(...) | Return the compression chain input.  
---|---  
`retrievers.document_compressors.chain_filter.default_get_input`(...) | Return the compression chain input.  
`retrievers.ensemble.unique_by_key`(iterable, key) | Yield unique elements of an iterable based on a key function.  
  
**Deprecated classes**

`retrievers.document_compressors.cohere_rerank.CohereRerank` |   
---|---  
  
© Copyright 2023, LangChain Inc.