# Introduction

**LangChain** is a framework for developing applications powered by large
language models (LLMs).

LangChain simplifies every stage of the LLM application lifecycle:

  * **Development** : Build your applications using LangChain's open-source components and third-party integrations. Use LangGraph to build stateful agents with first-class streaming and human-in-the-loop support.
  * **Productionization** : Use LangSmith to inspect, monitor and evaluate your applications, so that you can continuously optimize and deploy with confidence.
  * **Deployment** : Turn your LangGraph applications into production-ready APIs and Assistants with LangGraph Platform.

LangChain implements a standard interface for large language models and
related technologies, such as embedding models and vector stores, and
integrates with hundreds of providers. See the integrations page for more.

Select chat model:

# **OpenAI**

```
    pip install -qU langchain-openai  
```
    
```python  
    import getpass  
    import os  
      
    if not os.environ.get("OPENAI_API_KEY"):  
      os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")  
      
    from langchain_openai import ChatOpenAI  
      
    model = ChatOpenAI(model="gpt-4o-mini")  
    
    
    
    model.invoke("Hello, world!")  
```

# **Anthropic**

```
    pip install -qU langchain-anthropic
```
```python
import getpass
import os

if not os.environ.get("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter API key for Anthropic: ")

from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-5-sonnet-20240620")

model.invoke("Hello, world!")
```

# **Google**

```
    pip install -qU langchain-google-vertexai
```

```python
# Ensure your VertexAI credentials are configured

from langchain_google_vertexai import ChatVertexAI

model = ChatVertexAI(model="gemini-2.0-flash-exp")
model.invoke("Hello, world!")
```

## Architecture​

The LangChain framework consists of multiple open-source libraries. Read more
in the Architecture page.

  * **`langchain-core`** : Base abstractions for chat models and other components.
  * **Integration packages** (e.g. `langchain-openai`, `langchain-anthropic`, etc.): Important integrations have been split into lightweight packages that are co-maintained by the LangChain team and the integration developers.
  * **`langchain`** : Chains, agents, and retrieval strategies that make up an application's cognitive architecture.
  * **`langchain-community`** : Third-party integrations that are community maintained.
  * **`langgraph`** : Orchestration framework for combining LangChain components into production-ready applications with persistence, streaming, and other key features. See LangGraph documentation.


