Template Applications¶
Templates are open source reference applications designed to help you get started quickly when building with LangGraph. They provide working examples of common agentic workflows that can be customized to your needs.

You can create an application from a template using the LangGraph CLI.

Requirements

Python >= 3.11
LangGraph CLI: Requires langchain-cli[inmem] >= 0.1.58
Install the LangGraph CLI¶

pip install "langgraph-cli[inmem]" --upgrade
Available Templates¶
Template	Description	Python	JS/TS
New LangGraph Project	A simple, minimal chatbot with memory.	Repo	Repo
ReAct Agent	A simple agent that can be flexibly extended to many tools.	Repo	Repo
Memory Agent	A ReAct-style agent with an additional tool to store memories for use across threads.	Repo	Repo
Retrieval Agent	An agent that includes a retrieval-based question-answering system.	Repo	Repo
Data-Enrichment Agent	An agent that performs web searches and organizes its findings into a structured format.	Repo	Repo
🌱 Create a LangGraph App¶
To create a new app from a template, use the langgraph new command.


langgraph new
Next Steps¶
Review the README.md file in the root of your new LangGraph app for more information about the template and how to customize it.

After configuring the app properly and adding your API keys, you can start the app using the LangGraph CLI:

langgraph dev 
