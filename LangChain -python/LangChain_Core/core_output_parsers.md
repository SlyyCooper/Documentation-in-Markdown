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
    * `output_parsers` __
      * BaseGenerationOutputParser
      * BaseLLMOutputParser
      * BaseOutputParser
      * JsonOutputParser
      * SimpleJsonOutputParser
      * CommaSeparatedListOutputParser
      * ListOutputParser
      * MarkdownListOutputParser
      * NumberedListOutputParser
      * JsonKeyOutputFunctionsParser
      * JsonOutputFunctionsParser
      * OutputFunctionsParser
      * PydanticAttrOutputFunctionsParser
      * PydanticOutputFunctionsParser
      * JsonOutputKeyToolsParser
      * JsonOutputToolsParser
      * PydanticToolsParser
      * PydanticOutputParser
      * StrOutputParser
      * BaseCumulativeTransformOutputParser
      * BaseTransformOutputParser
      * XMLOutputParser
      * droplastn
      * make_invalid_tool_call
      * parse_tool_call
      * parse_tool_calls
      * nested_element
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
  * `output_parsers`

# `output_parsers`#

**OutputParser** classes parse the output of an LLM call.

**Class hierarchy:**

    
    
    BaseLLMOutputParser --> BaseOutputParser --> <name>OutputParser  # ListOutputParser, PydanticOutputParser
    

**Main helpers:**

    
    
    Serializable, Generation, PromptValue
    

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
  
© Copyright 2023, LangChain Inc.