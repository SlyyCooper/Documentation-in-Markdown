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
    * `utils` __
      * NoLock
      * Tee
      * aclosing
      * atee
      * StrictFormatter
      * FunctionDescription
      * ToolDescription
      * NoLock
      * Tee
      * safetee
      * ChevronError
      * abatch_iterate
      * py_anext
      * tee_peer
      * env_var_is_set
      * get_from_dict_or_env
      * get_from_env
      * convert_to_openai_function
      * convert_to_openai_tool
      * tool_example_to_messages
      * extract_sub_links
      * find_all_links
      * get_bolded_text
      * get_color_mapping
      * get_colored_text
      * print_text
      * is_interactive_env
      * batch_iterate
      * tee_peer
      * parse_and_check_json_markdown
      * parse_json_markdown
      * parse_partial_json
      * dereference_refs
      * grab_literal
      * l_sa_check
      * parse_tag
      * r_sa_check
      * render
      * tokenize
      * create_model
      * create_model_v2
      * get_fields
      * get_pydantic_major_version
      * is_basemodel_instance
      * is_basemodel_subclass
      * is_pydantic_v1_subclass
      * is_pydantic_v2_subclass
      * pre_init
      * comma_list
      * stringify_dict
      * stringify_value
      * build_extra_kwargs
      * check_package_version
      * convert_to_secret_str
      * from_env
      * get_pydantic_field_names
      * guard_import
      * mock_now
      * raise_for_status_with_text
      * secret_from_env
      * xor_args
      * convert_pydantic_to_openai_function
      * convert_pydantic_to_openai_tool
      * convert_python_function_to_openai_function
      * format_tool_to_openai_function
      * format_tool_to_openai_tool
      * try_load_from_hub
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
  * `utils`

# `utils`#

**Utility functions** for LangChain.

These functions do not depend on any other LangChain module.

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
  
© Copyright 2023, LangChain Inc.