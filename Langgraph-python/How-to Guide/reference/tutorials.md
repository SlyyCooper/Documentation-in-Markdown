## Table of Contents

- [Tutorials¶](#tutorials)
  - [Get Started 🚀¶](#get-started-)
  - [Use cases 🛠️¶](#use-cases-)
    - [Chatbots¶](#chatbots)
    - [RAG¶](#rag)
    - [Agent Architectures¶](#agent-architectures)
      - [Multi-Agent Systems¶](#multi-agent-systems)
      - [Planning Agents¶](#planning-agents)
      - [Reflection & Critique¶](#reflection--critique)
    - [Evaluation¶](#evaluation)
    - [Experimental¶](#experimental)
  - [LangGraph Platform 🧱¶](#langgraph-platform-)
    - [Authentication & Access Control¶](#authentication--access-control)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

Tutorials

Initializing search

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 
  * Conceptual Guides 
  * Reference 

GitHub

  * Home 
  * Tutorials 

Tutorials

    * Quick Start  Quick Start 
      * Quick Start 
      * 🚀 LangGraph Quick Start 
      * QuickStart: Launch Local LangGraph Server 
      * Quickstart: Deploy on LangGraph Cloud 
    * Chatbots  Chatbots 
      * Chatbots 
      * Build a Customer Support Bot 
      * Prompt Generation from User Requirements 
      * Code generation with RAG and self-correction 
    * RAG  RAG 
      * RAG 
      * Adaptive RAG 
      * Langgraph adaptive rag local 
      * Agentic RAG 
      * Corrective RAG (CRAG) 
      * Corrective RAG (CRAG) using local LLMs 
      * Self-RAG 
      * Self-RAG using local LLMs 
      * An agent for interacting with a SQL database 
    * Agent Architectures  Agent Architectures 
      * Agent Architectures 
      * Multi-Agent Systems 
      * Planning Agents 
      * Reflection & Critique 
    * Evaluation & Analysis  Evaluation & Analysis 
      * Evaluation & Analysis 
      * Chat Bot Evaluation as Multi-agent Simulation 
      * Chat Bot Benchmarking using Simulation 
    * Experimental  Experimental 
      * Experimental 
      * Web Research (STORM) 
      * TNT-LLM: Text Mining at Scale 
      * Web Voyager 
      * Competitive Programming 
      * Complex data extraction with function calling 
    * LangGraph Platform  LangGraph Platform 
      * LangGraph Platform 
      * Setting up Custom Authentication (Part ⅓) 
      * Making Conversations Private (Part ⅔) 
      * Connecting an Authentication Provider (Part 3/3) 
  * How-to Guides 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Get Started 🚀 
  * Use cases 🛠️ 
    * Chatbots 
    * RAG 
    * Agent Architectures 
      * Multi-Agent Systems 
      * Planning Agents 
      * Reflection & Critique 
    * Evaluation 
    * Experimental 
  * LangGraph Platform 🧱 
    * Authentication & Access Control 

  1. Home 
  2. Tutorials 

# Tutorials¶

New to LangGraph or LLM app development? Read this material to get up and
running building your first applications.

## Get Started 🚀¶

  * LangGraph Quickstart: Build a chatbot that can use tools and keep track of conversation history. Add human-in-the-loop capabilities and explore how time-travel works.
  * LangGraph Server Quickstart: Launch a LangGraph server locally and interact with it using REST API and LangGraph Studio Web UI.
  * LangGraph Template Quickstart: Start building with LangGraph Platform using a template application.
  * Deploy with LangGraph Cloud Quickstart: Deploy a LangGraph app using LangGraph Cloud.

## Use cases 🛠️¶

Explore practical implementations tailored for specific scenarios:

### Chatbots¶

  * Customer Support: Build a multi-functional support bot for flights, hotels, and car rentals.
  * Prompt Generation from User Requirements: Build an information gathering chatbot.
  * Code Assistant: Build a code analysis and generation assistant.

### RAG¶

  * Agentic RAG: Use an agent to figure out how to retrieve the most relevant information before using the retrieved information to answer the user's question.
  * Adaptive RAG: Adaptive RAG is a strategy for RAG that unites (1) query analysis with (2) active / self-corrective RAG. Implementation of: https://arxiv.org/abs/2403.14403
    * For a version that uses a local LLM: Adaptive RAG using local LLMs
  * Corrective RAG: Uses an LLM to grade the quality of the retrieved information from the given source, and if the quality is low, it will try to retrieve the information from another source. Implementation of: https://arxiv.org/pdf/2401.15884.pdf
    * For a version that uses a local LLM: Corrective RAG using local LLMs
  * Self-RAG: Self-RAG is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents and generations. Implementation of https://arxiv.org/abs/2310.11511.
    * For a version that uses a local LLM: Self-RAG using local LLMs
  * SQL Agent: Build a SQL agent that can answer questions about a SQL database.

### Agent Architectures¶

#### Multi-Agent Systems¶

  * Network: Enable two or more agents to collaborate on a task
  * Supervisor: Use an LLM to orchestrate and delegate to individual agents
  * Hierarchical Teams: Orchestrate nested teams of agents to solve problems

#### Planning Agents¶

  * Plan-and-Execute: Implement a basic planning and execution agent
  * Reasoning without Observation: Reduce re-planning by saving observations as variables
  * LLMCompiler: Stream and eagerly execute a DAG of tasks from a planner

#### Reflection & Critique¶

  * Basic Reflection: Prompt the agent to reflect on and revise its outputs
  * Reflexion: Critique missing and superfluous details to guide next steps
  * Tree of Thoughts: Search over candidate solutions to a problem using a scored tree
  * Language Agent Tree Search: Use reflection and rewards to drive a monte-carlo tree search over agents
  * Self-Discover Agent: Analyze an agent that learns about its own capabilities

### Evaluation¶

  * Agent-based: Evaluate chatbots via simulated user interactions
  * In LangSmith: Evaluate chatbots in LangSmith over a dialog dataset

### Experimental¶

  * Web Research (STORM): Generate Wikipedia-like articles via research and multi-perspective QA
  * TNT-LLM: Build rich, interpretable taxonomies of user intentand using the classification system developed by Microsoft for their Bing Copilot application.
  * Web Navigation: Build an agent that can navigate and interact with websites
  * Competitive Programming: Build an agent with few-shot "episodic memory" and human-in-the-loop collaboration to solve problems from the USA Computing Olympiad; adapted from the "Can Language Models Solve Olympiad Programming?" paper by Shi, Tang, Narasimhan, and Yao.
  * Complex data extraction: Build an agent that can use function calling to do complex extraction tasks

## LangGraph Platform 🧱¶

### Authentication & Access Control¶

Add custom authentication and authorization to an existing LangGraph Platform
deployment in the following three-part guide:

  1. Setting Up Custom Authentication: Implement OAuth2 authentication to authorize users on your deployment
  2. Resource Authorization: Let users have private conversations
  3. Connecting an Authentication Provider: Add real user accounts and validate using OAuth2

## Comments

Back to top

Previous

Home

Next

🚀 LangGraph Quick Start

Made with  Material for MkDocs Insiders