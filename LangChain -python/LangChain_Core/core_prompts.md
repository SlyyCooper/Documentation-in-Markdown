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
    * `prompts` __
      * BasePromptTemplate
      * AIMessagePromptTemplate
      * BaseChatPromptTemplate
      * BaseMessagePromptTemplate
      * BaseStringMessagePromptTemplate
      * ChatMessagePromptTemplate
      * ChatPromptTemplate
      * HumanMessagePromptTemplate
      * MessagesPlaceholder
      * SystemMessagePromptTemplate
      * FewShotChatMessagePromptTemplate
      * FewShotPromptTemplate
      * FewShotPromptWithTemplates
      * ImagePromptTemplate
      * PromptTemplate
      * StringPromptTemplate
      * StructuredPrompt
      * aformat_document
      * format_document
      * load_prompt
      * load_prompt_from_config
      * check_valid_template
      * get_template_variables
      * jinja2_formatter
      * mustache_formatter
      * mustache_schema
      * mustache_template_vars
      * validate_jinja2
      * PipelinePromptTemplate
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
  * `prompts`

# `prompts`#

**Prompt** is the input to the model.

Prompt is often constructed from multiple components and prompt values. Prompt
classes and functions make constructing

> and working with prompts easy.

**Class hierarchy:**

    
    
    BasePromptTemplate --> PipelinePromptTemplate
                           StringPromptTemplate --> PromptTemplate
                                                    FewShotPromptTemplate
                                                    FewShotPromptWithTemplates
                           BaseChatPromptTemplate --> AutoGPTPrompt
                                                      ChatPromptTemplate --> AgentScratchPadChatPromptTemplate
    
    
    
    BaseMessagePromptTemplate --> MessagesPlaceholder
                                  BaseStringMessagePromptTemplate --> ChatMessagePromptTemplate
                                                                      HumanMessagePromptTemplate
                                                                      AIMessagePromptTemplate
                                                                      SystemMessagePromptTemplate
    

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
  
© Copyright 2023, LangChain Inc.