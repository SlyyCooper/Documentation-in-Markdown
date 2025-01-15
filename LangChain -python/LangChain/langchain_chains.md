* `chains`

# `chains`#

**Chains** are easily reusable components linked together.

Chains encode a sequence of calls to components like models, document
retrievers, other Chains, etc., and provide a simple interface to this
sequence.

The Chain interface makes it easy to create apps that are:

>   * **Stateful:** add Memory to any Chain to give it state,
>
>   * **Observable:** pass Callbacks to a Chain to execute additional
> functionality, like logging, outside the main sequence of component calls,
>
>   * **Composable:** combine Chains with other components, including other
> Chains.
>
>

**Class hierarchy:**

    
    
    Chain --> <name>Chain  # Examples: LLMChain, MapReduceChain, RouterChain
    

**Classes**

`chains.base.Chain` | Abstract base class for creating structured sequences of calls to components.  
---|---  
`chains.combine_documents.base.BaseCombineDocumentsChain` | Base interface for chains combining documents.  
`chains.combine_documents.reduce.AsyncCombineDocsProtocol`(...) | Interface for the combine_docs method.  
`chains.combine_documents.reduce.CombineDocsProtocol`(...) | Interface for the combine_docs method.  
`chains.constitutional_ai.models.ConstitutionalPrinciple` | Class for a constitutional principle.  
`chains.conversational_retrieval.base.BaseConversationalRetrievalChain` | Chain for chatting with an index.  
`chains.conversational_retrieval.base.ChatVectorDBChain` | Chain for chatting with a vector database.  
`chains.conversational_retrieval.base.InputType` | Input type for ConversationalRetrievalChain.  
`chains.elasticsearch_database.base.ElasticsearchDatabaseChain` | Chain for interacting with Elasticsearch Database.  
`chains.flare.base.FlareChain` | Chain that combines a retriever, a question generator, and a response generator.  
`chains.flare.base.QuestionGeneratorChain` | Chain that generates questions from uncertain spans.  
`chains.flare.prompts.FinishedOutputParser` | Output parser that checks if the output is finished.  
`chains.hyde.base.HypotheticalDocumentEmbedder` | Generate hypothetical document for query, and then embed that.  
`chains.moderation.OpenAIModerationChain` | Pass input through a moderation endpoint.  
`chains.natbot.crawler.Crawler`() | A crawler for web pages.  
`chains.natbot.crawler.ElementInViewPort` | A typed dictionary containing information about elements in the viewport.  
`chains.openai_functions.citation_fuzzy_match.FactWithEvidence` | Class representing a single statement.  
`chains.openai_functions.citation_fuzzy_match.QuestionAnswer` | A question and its answer as a list of facts each one should have a source.  
`chains.openai_functions.openapi.SimpleRequestChain` | Chain for making a simple request to an API endpoint.  
`chains.openai_functions.qa_with_structure.AnswerWithSources` | An answer to the question, with sources.  
`chains.prompt_selector.BasePromptSelector` | Base class for prompt selectors.  
`chains.prompt_selector.ConditionalPromptSelector` | Prompt collection that goes through conditionals.  
`chains.qa_with_sources.loading.LoadingCallable`(...) | Interface for loading the combine documents chain.  
`chains.qa_with_sources.retrieval.RetrievalQAWithSourcesChain` | Question-answering with sources over an index.  
`chains.qa_with_sources.vector_db.VectorDBQAWithSourcesChain` | Question-answering with sources over a vector database.  
`chains.query_constructor.base.StructuredQueryOutputParser` | Output parser that parses a structured query.  
`chains.query_constructor.parser.ISO8601Date` | A date in ISO 8601 format (YYYY-MM-DD).  
`chains.query_constructor.parser.ISO8601DateTime` | A datetime in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).  
`chains.query_constructor.schema.AttributeInfo` | Information about a data source attribute.  
`chains.question_answering.chain.LoadingCallable`(...) | Interface for loading the combine documents chain.  
`chains.router.base.MultiRouteChain` | Use a single chain to route an input to one of multiple candidate chains.  
`chains.router.base.Route`(destination, ...) | Create new instance of Route(destination, next_inputs)  
`chains.router.base.RouterChain` | Chain that outputs the name of a destination chain and the inputs to it.  
`chains.router.embedding_router.EmbeddingRouterChain` | Chain that uses embeddings to route between options.  
`chains.router.llm_router.RouterOutputParser` | Parser for output of router chain in the multi-prompt chain.  
`chains.router.multi_retrieval_qa.MultiRetrievalQAChain` | A multi-route chain that uses an LLM router chain to choose amongst retrieval qa chains.  
`chains.sequential.SequentialChain` | Chain where the outputs of one chain feed directly into next.  
`chains.sequential.SimpleSequentialChain` | Simple chain where the outputs of one step feed directly into next.  
`chains.sql_database.query.SQLInput` | Input for a SQL Chain.  
`chains.sql_database.query.SQLInputWithTables` | Input for a SQL Chain.  
`chains.summarize.chain.LoadingCallable`(...) | Interface for loading the combine documents chain.  
`chains.transform.TransformChain` | Chain that transforms the chain output.  
  
**Functions**

`chains.combine_documents.reduce.acollapse_docs`(...) | Execute a collapse function on a set of documents and merge their metadatas.  
---|---  
`chains.combine_documents.reduce.collapse_docs`(...) | Execute a collapse function on a set of documents and merge their metadatas.  
`chains.combine_documents.reduce.split_list_of_docs`(...) | Split Documents into subsets that each meet a cumulative length constraint.  
`chains.combine_documents.stuff.create_stuff_documents_chain`(...) | Create a chain for passing a list of Documents to a model.  
`chains.example_generator.generate_example`(...) | Return another example given a list of examples for a prompt.  
`chains.history_aware_retriever.create_history_aware_retriever`(...) | Create a chain that takes conversation history and returns documents.  
`chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable`(llm) | Create a citation fuzzy match Runnable.  
`chains.openai_functions.openapi.openapi_spec_to_openai_fn`(spec) | Convert a valid OpenAPI spec to the JSON Schema format expected for OpenAI  
`chains.openai_functions.utils.get_llm_kwargs`(...) | Return the kwargs for the LLMChain constructor.  
`chains.prompt_selector.is_chat_model`(llm) | Check if the language model is a chat model.  
`chains.prompt_selector.is_llm`(llm) | Check if the language model is a LLM.  
`chains.query_constructor.base.construct_examples`(...) | Construct examples from input-output pairs.  
`chains.query_constructor.base.fix_filter_directive`(...) | Fix invalid filter directive.  
`chains.query_constructor.base.get_query_constructor_prompt`(...) | Create query construction prompt.  
`chains.query_constructor.base.load_query_constructor_runnable`(...) | Load a query constructor runnable chain.  
`chains.query_constructor.parser.get_parser`([...]) | Return a parser for the query language.  
`chains.query_constructor.parser.v_args`(...) | Dummy decorator for when lark is not installed.  
`chains.retrieval.create_retrieval_chain`(...) | Create retrieval chain that retrieves documents and then passes them on.  
`chains.sql_database.query.create_sql_query_chain`(llm, db) | Create a chain that generates SQL queries.  
`chains.structured_output.base.get_openai_output_parser`(...) | Get the appropriate function output parser given the user functions.  
`chains.summarize.chain.load_summarize_chain`(llm) | Load summarizing chain.  
  
**Deprecated classes**

`chains.api.base.APIChain` |   
---|---  
`chains.combine_documents.base.AnalyzeDocumentChain` |   
`chains.combine_documents.map_reduce.MapReduceDocumentsChain` |   
`chains.combine_documents.map_rerank.MapRerankDocumentsChain` |   
`chains.combine_documents.reduce.ReduceDocumentsChain` |   
`chains.combine_documents.refine.RefineDocumentsChain` |   
`chains.combine_documents.stuff.StuffDocumentsChain` |   
`chains.constitutional_ai.base.ConstitutionalChain` |   
`chains.conversation.base.ConversationChain` |   
`chains.conversational_retrieval.base.ConversationalRetrievalChain` |   
`chains.llm.LLMChain` |   
`chains.llm_checker.base.LLMCheckerChain` |   
`chains.llm_math.base.LLMMathChain` |   
`chains.llm_summarization_checker.base.LLMSummarizationCheckerChain` |   
`chains.mapreduce.MapReduceChain` |   
`chains.natbot.base.NatBotChain` |   
`chains.qa_generation.base.QAGenerationChain` |   
`chains.qa_with_sources.base.BaseQAWithSourcesChain` |   
`chains.qa_with_sources.base.QAWithSourcesChain` |   
`chains.retrieval_qa.base.BaseRetrievalQA` |   
`chains.retrieval_qa.base.RetrievalQA` |   
`chains.retrieval_qa.base.VectorDBQA` |   
`chains.router.llm_router.LLMRouterChain` |   
`chains.router.multi_prompt.MultiPromptChain` |   
  
**Deprecated functions**

`chains.loading.load_chain`(path, **kwargs) |   
---|---  
`chains.loading.load_chain_from_config`(...) |   
`chains.openai_functions.base.create_openai_fn_chain`(...) |   
`chains.openai_functions.base.create_structured_output_chain`(...) |   
`chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_chain`(llm) |   
`chains.openai_functions.extraction.create_extraction_chain`(...) |   
`chains.openai_functions.extraction.create_extraction_chain_pydantic`(...) |   
`chains.openai_functions.openapi.get_openapi_chain`(spec) |   
`chains.openai_functions.qa_with_structure.create_qa_with_sources_chain`(llm) |   
`chains.openai_functions.qa_with_structure.create_qa_with_structure_chain`(...) |   
`chains.openai_functions.tagging.create_tagging_chain`(...) |   
`chains.openai_functions.tagging.create_tagging_chain_pydantic`(...) |   
`chains.openai_tools.extraction.create_extraction_chain_pydantic`(...) |   
`chains.qa_with_sources.loading.load_qa_with_sources_chain`(llm) |   
`chains.query_constructor.base.load_query_constructor_chain`(...) |   
`chains.question_answering.chain.load_qa_chain`(llm) |   
`chains.structured_output.base.create_openai_fn_runnable`(...) |   
`chains.structured_output.base.create_structured_output_runnable`(...) |   
  
© Copyright 2023, LangChain Inc.