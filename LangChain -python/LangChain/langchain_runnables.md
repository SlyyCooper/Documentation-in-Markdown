# `runnables`#

LangChain **Runnable** and the **LangChain Expression Language (LCEL)**.

The LangChain Expression Language (LCEL) offers a declarative method to build
production-grade programs that harness the power of LLMs.

Programs created using LCEL and LangChain Runnables inherently support
synchronous, asynchronous, batch, and streaming operations.

Support for **async** allows servers hosting the LCEL based programs to scale
better for higher concurrent loads.

**Batch** operations allow for processing multiple inputs in parallel.

**Streaming** of intermediate outputs, as they’re being generated, allows for
creating more responsive UX.

This module contains non-core Runnable classes.

**Classes**

`runnables.hub.HubRunnable` | An instance of a runnable stored in the LangChain Hub.  
---|---  
`runnables.openai_functions.OpenAIFunction` | A function description for ChatOpenAI  
`runnables.openai_functions.OpenAIFunctionsRouter` | A runnable that routes to the selected function.  
  
© Copyright 2023, LangChain Inc.