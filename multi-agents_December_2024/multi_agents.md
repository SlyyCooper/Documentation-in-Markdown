└── multi_agents
    ├── README.md
    ├── __init__.py
    ├── agent.py
    ├── agents
        ├── __init__.py
        ├── editor.py
        ├── human.py
        ├── orchestrator.py
        ├── publisher.py
        ├── researcher.py
        ├── reviewer.py
        ├── reviser.py
        ├── utils
        │   ├── __init__.py
        │   ├── file_formats.py
        │   ├── llms.py
        │   ├── pdf_styles.css
        │   ├── utils.py
        │   └── views.py
        └── writer.py
    ├── langgraph.json
    ├── main.py
    ├── memory
        ├── __init__.py
        ├── draft.py
        └── research.py
    ├── package.json
    ├── requirements.txt
    └── task.json


/multi_agents/README.md:
--------------------------------------------------------------------------------
  1 | # LangGraph x GPT Researcher
  2 | [LangGraph](https://python.langchain.com/docs/langgraph) is a library for building stateful, multi-actor applications with LLMs. 
  3 | This example uses Langgraph to automate the process of an in depth research on any given topic.
  4 | 
  5 | ## Use case
  6 | By using Langgraph, the research process can be significantly improved in depth and quality by leveraging multiple agents with specialized skills. 
  7 | Inspired by the recent [STORM](https://arxiv.org/abs/2402.14207) paper, this example showcases how a team of AI agents can work together to conduct research on a given topic, from planning to publication.
  8 | 
  9 | An average run generates a 5-6 page research report in multiple formats such as PDF, Docx and Markdown.
 10 | 
 11 | Please note: This example uses the OpenAI API only for optimized performance.
 12 | 
 13 | ## The Multi Agent Team
 14 | The research team is made up of 8 agents:
 15 | - **Human** - The human in the loop that oversees the process and provides feedback to the agents.
 16 | - **Chief Editor** - Oversees the research process and manages the team. This is the "master" agent that coordinates the other agents using Langgraph.
 17 | - **Researcher** (gpt-researcher) - A specialized autonomous agent that conducts in depth research on a given topic.
 18 | - **Editor** - Responsible for planning the research outline and structure.
 19 | - **Reviewer** - Validates the correctness of the research results given a set of criteria.
 20 | - **Revisor** - Revises the research results based on the feedback from the reviewer.
 21 | - **Writer** - Responsible for compiling and writing the final report.
 22 | - **Publisher** - Responsible for publishing the final report in various formats.
 23 | 
 24 | ## How it works
 25 | Generally, the process is based on the following stages: 
 26 | 1. Planning stage
 27 | 2. Data collection and analysis
 28 | 3. Review and revision
 29 | 4. Writing and submission
 30 | 5. Publication
 31 | 
 32 | ### Architecture
 33 | <div align="center">
 34 | <img align="center" height="600" src="https://github.com/user-attachments/assets/ef561295-05f4-40a8-a57d-8178be687b18">
 35 | </div>
 36 | <br clear="all"/>
 37 | 
 38 | ### Steps
 39 | More specifically (as seen in the architecture diagram) the process is as follows:
 40 | - Browser (gpt-researcher) - Browses the internet for initial research based on the given research task.
 41 | - Editor - Plans the report outline and structure based on the initial research.
 42 | - For each outline topic (in parallel):
 43 |   - Researcher (gpt-researcher) - Runs an in depth research on the subtopics and writes a draft.
 44 |   - Reviewer - Validates the correctness of the draft given a set of criteria and provides feedback.
 45 |   - Revisor - Revises the draft until it is satisfactory based on the reviewer feedback.
 46 | - Writer - Compiles and writes the final report including an introduction, conclusion and references section from the given research findings.
 47 | - Publisher - Publishes the final report to multi formats such as PDF, Docx, Markdown, etc.
 48 | 
 49 | ## How to run
 50 | 1. Install required packages:
 51 |     ```bash
 52 |     pip install -r requirements.txt
 53 |     ```
 54 | 3. Update env variables
 55 |    ```bash
 56 |    export OPENAI_API_KEY={Your OpenAI API Key here}
 57 |    export TAVILY_API_KEY={Your Tavily API Key here}
 58 |    ```
 59 | 2. Run the application:
 60 |     ```bash
 61 |     python main.py
 62 |     ```
 63 | 
 64 | ## Usage
 65 | To change the research query and customize the report, edit the `task.json` file in the main directory.
 66 | #### Task.json contains the following fields:
 67 | - `query` - The research query or task.
 68 | - `model` - The OpenAI LLM to use for the agents.
 69 | - `max_sections` - The maximum number of sections in the report. Each section is a subtopic of the research query.
 70 | - `include_human_feedback` - If true, the user can provide feedback to the agents. If false, the agents will work autonomously.
 71 | - `publish_formats` - The formats to publish the report in. The reports will be written in the `output` directory.
 72 | - `source` - The location from which to conduct the research. Options: `web` or `local`. For local, please add `DOC_PATH` env var.
 73 | - `follow_guidelines` - If true, the research report will follow the guidelines below. It will take longer to complete. If false, the report will be generated faster but may not follow the guidelines.
 74 | - `guidelines` - A list of guidelines that the report must follow.
 75 | - `verbose` - If true, the application will print detailed logs to the console.
 76 | 
 77 | #### For example:
 78 | ```json
 79 | {
 80 |   "query": "Is AI in a hype cycle?",
 81 |   "model": "gpt-4o",
 82 |   "max_sections": 3, 
 83 |   "publish_formats": { 
 84 |     "markdown": true,
 85 |     "pdf": true,
 86 |     "docx": true
 87 |   },
 88 |   "include_human_feedback": false,
 89 |   "source": "web",
 90 |   "follow_guidelines": true,
 91 |   "guidelines": [
 92 |     "The report MUST fully answer the original question",
 93 |     "The report MUST be written in apa format",
 94 |     "The report MUST be written in english"
 95 |   ],
 96 |   "verbose": true
 97 | }
 98 | ```
 99 | 
100 | ## To Deploy
101 | 
102 | ```shell
103 | pip install langgraph-cli
104 | langgraph up
105 | ```
106 | 
107 | From there, see documentation [here](https://github.com/langchain-ai/langgraph-example) on how to use the streaming and async endpoints, as well as the playground.
108 | 


--------------------------------------------------------------------------------
/multi_agents/__init__.py:
--------------------------------------------------------------------------------
 1 | # multi_agents/__init__.py
 2 | 
 3 | from .agents import (
 4 |     ResearchAgent,
 5 |     WriterAgent,
 6 |     PublisherAgent,
 7 |     ReviserAgent,
 8 |     ReviewerAgent,
 9 |     EditorAgent,
10 |     ChiefEditorAgent
11 | )
12 | from .memory import (
13 |     DraftState,
14 |     ResearchState
15 | )
16 | 
17 | __all__ = [
18 |     "ResearchAgent",
19 |     "WriterAgent",
20 |     "PublisherAgent",
21 |     "ReviserAgent",
22 |     "ReviewerAgent",
23 |     "EditorAgent",
24 |     "ChiefEditorAgent",
25 |     "DraftState",
26 |     "ResearchState"
27 | ]


--------------------------------------------------------------------------------
/multi_agents/agent.py:
--------------------------------------------------------------------------------
 1 | from multi_agents.agents import ChiefEditorAgent
 2 | 
 3 | chief_editor = ChiefEditorAgent({
 4 |   "query": "Is AI in a hype cycle?",
 5 |   "max_sections": 3,
 6 |   "follow_guidelines": False,
 7 |   "model": "gpt-4o",
 8 |   "guidelines": [
 9 |     "The report MUST be written in APA format",
10 |     "Each sub section MUST include supporting sources using hyperlinks. If none exist, erase the sub section or rewrite it to be a part of the previous section",
11 |     "The report MUST be written in spanish"
12 |   ],
13 |   "verbose": False
14 | }, websocket=None, stream_output=None)
15 | graph = chief_editor.init_research_team()
16 | graph = graph.compile()


--------------------------------------------------------------------------------
/multi_agents/agents/__init__.py:
--------------------------------------------------------------------------------
 1 | from .researcher import ResearchAgent
 2 | from .writer import WriterAgent
 3 | from .publisher import PublisherAgent
 4 | from .reviser import ReviserAgent
 5 | from .reviewer import ReviewerAgent
 6 | from .editor import EditorAgent
 7 | from .human import HumanAgent
 8 | 
 9 | # Below import should remain last since it imports all of the above
10 | from .orchestrator import ChiefEditorAgent
11 | 
12 | __all__ = [
13 |     "ChiefEditorAgent",
14 |     "ResearchAgent",
15 |     "WriterAgent",
16 |     "EditorAgent",
17 |     "PublisherAgent",
18 |     "ReviserAgent",
19 |     "ReviewerAgent",
20 |     "HumanAgent"
21 | ]
22 | 


--------------------------------------------------------------------------------
/multi_agents/agents/editor.py:
--------------------------------------------------------------------------------
  1 | from datetime import datetime
  2 | import asyncio
  3 | from typing import Dict, List, Optional
  4 | 
  5 | from langgraph.graph import StateGraph, END
  6 | 
  7 | from .utils.views import print_agent_output
  8 | from .utils.llms import call_model
  9 | from ..memory.draft import DraftState
 10 | from . import ResearchAgent, ReviewerAgent, ReviserAgent
 11 | 
 12 | 
 13 | class EditorAgent:
 14 |     """Agent responsible for editing and managing code."""
 15 | 
 16 |     def __init__(self, websocket=None, stream_output=None, headers=None):
 17 |         self.websocket = websocket
 18 |         self.stream_output = stream_output
 19 |         self.headers = headers or {}
 20 | 
 21 |     async def plan_research(self, research_state: Dict[str, any]) -> Dict[str, any]:
 22 |         """
 23 |         Plan the research outline based on initial research and task parameters.
 24 | 
 25 |         :param research_state: Dictionary containing research state information
 26 |         :return: Dictionary with title, date, and planned sections
 27 |         """
 28 |         initial_research = research_state.get("initial_research")
 29 |         task = research_state.get("task")
 30 |         include_human_feedback = task.get("include_human_feedback")
 31 |         human_feedback = research_state.get("human_feedback")
 32 |         max_sections = task.get("max_sections")
 33 | 
 34 |         prompt = self._create_planning_prompt(
 35 |             initial_research, include_human_feedback, human_feedback, max_sections)
 36 | 
 37 |         print_agent_output(
 38 |             "Planning an outline layout based on initial research...", agent="EDITOR")
 39 |         plan = await call_model(
 40 |             prompt=prompt,
 41 |             model=task.get("model"),
 42 |             response_format="json",
 43 |         )
 44 | 
 45 |         return {
 46 |             "title": plan.get("title"),
 47 |             "date": plan.get("date"),
 48 |             "sections": plan.get("sections"),
 49 |         }
 50 | 
 51 |     async def run_parallel_research(self, research_state: Dict[str, any]) -> Dict[str, List[str]]:
 52 |         """
 53 |         Execute parallel research tasks for each section.
 54 | 
 55 |         :param research_state: Dictionary containing research state information
 56 |         :return: Dictionary with research results
 57 |         """
 58 |         agents = self._initialize_agents()
 59 |         workflow = self._create_workflow()
 60 |         chain = workflow.compile()
 61 | 
 62 |         queries = research_state.get("sections")
 63 |         title = research_state.get("title")
 64 | 
 65 |         self._log_parallel_research(queries)
 66 | 
 67 |         final_drafts = [
 68 |             chain.ainvoke(self._create_task_input(
 69 |                 research_state, query, title))
 70 |             for query in queries
 71 |         ]
 72 |         research_results = [
 73 |             result["draft"] for result in await asyncio.gather(*final_drafts)
 74 |         ]
 75 | 
 76 |         return {"research_data": research_results}
 77 | 
 78 |     def _create_planning_prompt(self, initial_research: str, include_human_feedback: bool,
 79 |                                 human_feedback: Optional[str], max_sections: int) -> List[Dict[str, str]]:
 80 |         """Create the prompt for research planning."""
 81 |         return [
 82 |             {
 83 |                 "role": "system",
 84 |                 "content": "You are a research editor. Your goal is to oversee the research project "
 85 |                            "from inception to completion. Your main task is to plan the article section "
 86 |                            "layout based on an initial research summary.\n ",
 87 |             },
 88 |             {
 89 |                 "role": "user",
 90 |                 "content": self._format_planning_instructions(initial_research, include_human_feedback,
 91 |                                                               human_feedback, max_sections),
 92 |             },
 93 |         ]
 94 | 
 95 |     def _format_planning_instructions(self, initial_research: str, include_human_feedback: bool,
 96 |                                       human_feedback: Optional[str], max_sections: int) -> str:
 97 |         """Format the instructions for research planning."""
 98 |         today = datetime.now().strftime('%d/%m/%Y')
 99 |         feedback_instruction = (
100 |             f"Human feedback: {human_feedback}. You must plan the sections based on the human feedback."
101 |             if include_human_feedback and human_feedback and human_feedback != 'no'
102 |             else ''
103 |         )
104 | 
105 |         return f"""Today's date is {today}
106 |                    Research summary report: '{initial_research}'
107 |                    {feedback_instruction}
108 |                    \nYour task is to generate an outline of sections headers for the research project
109 |                    based on the research summary report above.
110 |                    You must generate a maximum of {max_sections} section headers.
111 |                    You must focus ONLY on related research topics for subheaders and do NOT include introduction, conclusion and references.
112 |                    You must return nothing but a JSON with the fields 'title' (str) and 
113 |                    'sections' (maximum {max_sections} section headers) with the following structure:
114 |                    '{{title: string research title, date: today's date, 
115 |                    sections: ['section header 1', 'section header 2', 'section header 3' ...]}}'."""
116 | 
117 |     def _initialize_agents(self) -> Dict[str, any]:
118 |         """Initialize the research, reviewer, and reviser skills."""
119 |         return {
120 |             "research": ResearchAgent(self.websocket, self.stream_output, self.headers),
121 |             "reviewer": ReviewerAgent(self.websocket, self.stream_output, self.headers),
122 |             "reviser": ReviserAgent(self.websocket, self.stream_output, self.headers),
123 |         }
124 | 
125 |     def _create_workflow(self) -> StateGraph:
126 |         """Create the workflow for the research process."""
127 |         agents = self._initialize_agents()
128 |         workflow = StateGraph(DraftState)
129 | 
130 |         workflow.add_node("researcher", agents["research"].run_depth_research)
131 |         workflow.add_node("reviewer", agents["reviewer"].run)
132 |         workflow.add_node("reviser", agents["reviser"].run)
133 | 
134 |         workflow.set_entry_point("researcher")
135 |         workflow.add_edge("researcher", "reviewer")
136 |         workflow.add_edge("reviser", "reviewer")
137 |         workflow.add_conditional_edges(
138 |             "reviewer",
139 |             lambda draft: "accept" if draft["review"] is None else "revise",
140 |             {"accept": END, "revise": "reviser"},
141 |         )
142 | 
143 |         return workflow
144 | 
145 |     def _log_parallel_research(self, queries: List[str]) -> None:
146 |         """Log the start of parallel research tasks."""
147 |         if self.websocket and self.stream_output:
148 |             asyncio.create_task(self.stream_output(
149 |                 "logs",
150 |                 "parallel_research",
151 |                 f"Running parallel research for the following queries: {queries}",
152 |                 self.websocket,
153 |             ))
154 |         else:
155 |             print_agent_output(
156 |                 f"Running the following research tasks in parallel: {queries}...",
157 |                 agent="EDITOR",
158 |             )
159 | 
160 |     def _create_task_input(self, research_state: Dict[str, any], query: str, title: str) -> Dict[str, any]:
161 |         """Create the input for a single research task."""
162 |         return {
163 |             "task": research_state.get("task"),
164 |             "topic": query,
165 |             "title": title,
166 |             "headers": self.headers,
167 |         }
168 | 


--------------------------------------------------------------------------------
/multi_agents/agents/human.py:
--------------------------------------------------------------------------------
 1 | import json
 2 | 
 3 | 
 4 | class HumanAgent:
 5 |     def __init__(self, websocket=None, stream_output=None, headers=None):
 6 |         self.websocket = websocket
 7 |         self.stream_output = stream_output
 8 |         self.headers = headers or {}
 9 | 
10 |     async def review_plan(self, research_state: dict):
11 |         print(f"HumanAgent websocket: {self.websocket}")
12 |         print(f"HumanAgent stream_output: {self.stream_output}")
13 |         task = research_state.get("task")
14 |         layout = research_state.get("sections")
15 | 
16 |         user_feedback = None
17 | 
18 |         if task.get("include_human_feedback"):
19 |             # Stream response to the user if a websocket is provided (such as from web app)
20 |             if self.websocket and self.stream_output:
21 |                 try:
22 |                     await self.stream_output(
23 |                         "human_feedback",
24 |                         "request",
25 |                         f"Any feedback on this plan of topics to research? {layout}? If not, please reply with 'no'.",
26 |                         self.websocket,
27 |                     )
28 |                     response = await self.websocket.receive_text()
29 |                     print(f"Received response: {response}", flush=True)
30 |                     response_data = json.loads(response)
31 |                     if response_data.get("type") == "human_feedback":
32 |                         user_feedback = response_data.get("content")
33 |                     else:
34 |                         print(
35 |                             f"Unexpected response type: {response_data.get('type')}",
36 |                             flush=True,
37 |                         )
38 |                 except Exception as e:
39 |                     print(f"Error receiving human feedback: {e}", flush=True)
40 |             # Otherwise, prompt the user for feedback in the console
41 |             else:
42 |                 user_feedback = input(
43 |                     f"Any feedback on this plan? {layout}? If not, please reply with 'no'.\n>> "
44 |                 )
45 | 
46 |         if user_feedback and "no" in user_feedback.strip().lower():
47 |             user_feedback = None
48 | 
49 |         print(f"User feedback before return: {user_feedback}")
50 | 
51 |         return {"human_feedback": user_feedback}
52 | 


--------------------------------------------------------------------------------
/multi_agents/agents/orchestrator.py:
--------------------------------------------------------------------------------
  1 | import os
  2 | import time
  3 | import datetime
  4 | from langgraph.graph import StateGraph, END
  5 | # from langgraph.checkpoint.memory import MemorySaver
  6 | from .utils.views import print_agent_output
  7 | from ..memory.research import ResearchState
  8 | from .utils.utils import sanitize_filename
  9 | 
 10 | # Import agent classes
 11 | from . import \
 12 |     WriterAgent, \
 13 |     EditorAgent, \
 14 |     PublisherAgent, \
 15 |     ResearchAgent, \
 16 |     HumanAgent
 17 | 
 18 | 
 19 | class ChiefEditorAgent:
 20 |     """Agent responsible for managing and coordinating editing tasks."""
 21 | 
 22 |     def __init__(self, task: dict, websocket=None, stream_output=None, tone=None, headers=None):
 23 |         self.task = task
 24 |         self.websocket = websocket
 25 |         self.stream_output = stream_output
 26 |         self.headers = headers or {}
 27 |         self.tone = tone
 28 |         self.task_id = self._generate_task_id()
 29 |         self.output_dir = self._create_output_directory()
 30 | 
 31 |     def _generate_task_id(self):
 32 |         # Currently time based, but can be any unique identifier
 33 |         return int(time.time())
 34 | 
 35 |     def _create_output_directory(self):
 36 |         output_dir = "./outputs/" + \
 37 |             sanitize_filename(
 38 |                 f"run_{self.task_id}_{self.task.get('query')[0:40]}")
 39 | 
 40 |         os.makedirs(output_dir, exist_ok=True)
 41 |         return output_dir
 42 | 
 43 |     def _initialize_agents(self):
 44 |         return {
 45 |             "writer": WriterAgent(self.websocket, self.stream_output, self.headers),
 46 |             "editor": EditorAgent(self.websocket, self.stream_output, self.headers),
 47 |             "research": ResearchAgent(self.websocket, self.stream_output, self.tone, self.headers),
 48 |             "publisher": PublisherAgent(self.output_dir, self.websocket, self.stream_output, self.headers),
 49 |             "human": HumanAgent(self.websocket, self.stream_output, self.headers)
 50 |         }
 51 | 
 52 |     def _create_workflow(self, agents):
 53 |         workflow = StateGraph(ResearchState)
 54 | 
 55 |         # Add nodes for each agent
 56 |         workflow.add_node("browser", agents["research"].run_initial_research)
 57 |         workflow.add_node("planner", agents["editor"].plan_research)
 58 |         workflow.add_node("researcher", agents["editor"].run_parallel_research)
 59 |         workflow.add_node("writer", agents["writer"].run)
 60 |         workflow.add_node("publisher", agents["publisher"].run)
 61 |         workflow.add_node("human", agents["human"].review_plan)
 62 | 
 63 |         # Add edges
 64 |         self._add_workflow_edges(workflow)
 65 | 
 66 |         return workflow
 67 | 
 68 |     def _add_workflow_edges(self, workflow):
 69 |         workflow.add_edge('browser', 'planner')
 70 |         workflow.add_edge('planner', 'human')
 71 |         workflow.add_edge('researcher', 'writer')
 72 |         workflow.add_edge('writer', 'publisher')
 73 |         workflow.set_entry_point("browser")
 74 |         workflow.add_edge('publisher', END)
 75 | 
 76 |         # Add human in the loop
 77 |         workflow.add_conditional_edges(
 78 |             'human',
 79 |             lambda review: "accept" if review['human_feedback'] is None else "revise",
 80 |             {"accept": "researcher", "revise": "planner"}
 81 |         )
 82 | 
 83 |     def init_research_team(self):
 84 |         """Initialize and create a workflow for the research team."""
 85 |         agents = self._initialize_agents()
 86 |         return self._create_workflow(agents)
 87 | 
 88 |     async def _log_research_start(self):
 89 |         message = f"Starting the research process for query '{self.task.get('query')}'..."
 90 |         if self.websocket and self.stream_output:
 91 |             await self.stream_output("logs", "starting_research", message, self.websocket)
 92 |         else:
 93 |             print_agent_output(message, "MASTER")
 94 | 
 95 |     async def run_research_task(self, task_id=None):
 96 |         """
 97 |         Run a research task with the initialized research team.
 98 | 
 99 |         Args:
100 |             task_id (optional): The ID of the task to run.
101 | 
102 |         Returns:
103 |             The result of the research task.
104 |         """
105 |         research_team = self.init_research_team()
106 |         chain = research_team.compile()
107 | 
108 |         await self._log_research_start()
109 | 
110 |         config = {
111 |             "configurable": {
112 |                 "thread_id": task_id,
113 |                 "thread_ts": datetime.datetime.utcnow()
114 |             }
115 |         }
116 | 
117 |         result = await chain.ainvoke({"task": self.task}, config=config)
118 |         return result
119 | 


--------------------------------------------------------------------------------
/multi_agents/agents/publisher.py:
--------------------------------------------------------------------------------
 1 | from .utils.file_formats import \
 2 |     write_md_to_pdf, \
 3 |     write_md_to_word, \
 4 |     write_text_to_md
 5 | 
 6 | from .utils.views import print_agent_output
 7 | 
 8 | 
 9 | class PublisherAgent:
10 |     def __init__(self, output_dir: str, websocket=None, stream_output=None, headers=None):
11 |         self.websocket = websocket
12 |         self.stream_output = stream_output
13 |         self.output_dir = output_dir
14 |         self.headers = headers or {}
15 |         
16 |     async def publish_research_report(self, research_state: dict, publish_formats: dict):
17 |         layout = self.generate_layout(research_state)
18 |         await self.write_report_by_formats(layout, publish_formats)
19 | 
20 |         return layout
21 | 
22 |     def generate_layout(self, research_state: dict):
23 |         sections = '\n\n'.join(f"{value}"
24 |                                  for subheader in research_state.get("research_data")
25 |                                  for key, value in subheader.items())
26 |         references = '\n'.join(f"{reference}" for reference in research_state.get("sources"))
27 |         headers = research_state.get("headers")
28 |         layout = f"""# {headers.get('title')}
29 | #### {headers.get("date")}: {research_state.get('date')}
30 | 
31 | ## {headers.get("introduction")}
32 | {research_state.get('introduction')}
33 | 
34 | ## {headers.get("table_of_contents")}
35 | {research_state.get('table_of_contents')}
36 | 
37 | {sections}
38 | 
39 | ## {headers.get("conclusion")}
40 | {research_state.get('conclusion')}
41 | 
42 | ## {headers.get("references")}
43 | {references}
44 | """
45 |         return layout
46 | 
47 |     async def write_report_by_formats(self, layout:str, publish_formats: dict):
48 |         if publish_formats.get("pdf"):
49 |             await write_md_to_pdf(layout, self.output_dir)
50 |         if publish_formats.get("docx"):
51 |             await write_md_to_word(layout, self.output_dir)
52 |         if publish_formats.get("markdown"):
53 |             await write_text_to_md(layout, self.output_dir)
54 | 
55 |     async def run(self, research_state: dict):
56 |         task = research_state.get("task")
57 |         publish_formats = task.get("publish_formats")
58 |         if self.websocket and self.stream_output:
59 |             await self.stream_output("logs", "publishing", f"Publishing final research report based on retrieved data...", self.websocket)
60 |         else:
61 |             print_agent_output(output="Publishing final research report based on retrieved data...", agent="PUBLISHER")
62 |         final_research_report = await self.publish_research_report(research_state, publish_formats)
63 |         return {"report": final_research_report}
64 | 


--------------------------------------------------------------------------------
/multi_agents/agents/researcher.py:
--------------------------------------------------------------------------------
 1 | from gpt_researcher import GPTResearcher
 2 | from colorama import Fore, Style
 3 | from .utils.views import print_agent_output
 4 | 
 5 | 
 6 | class ResearchAgent:
 7 |     def __init__(self, websocket=None, stream_output=None, tone=None, headers=None):
 8 |         self.websocket = websocket
 9 |         self.stream_output = stream_output
10 |         self.headers = headers or {}
11 |         self.tone = tone
12 | 
13 |     async def research(self, query: str, research_report: str = "research_report",
14 |                        parent_query: str = "", verbose=True, source="web", tone=None, headers=None):
15 |         # Initialize the researcher
16 |         researcher = GPTResearcher(query=query, report_type=research_report, parent_query=parent_query,
17 |                                    verbose=verbose, report_source=source, tone=tone, websocket=self.websocket, headers=self.headers)
18 |         # Conduct research on the given query
19 |         await researcher.conduct_research()
20 |         # Write the report
21 |         report = await researcher.write_report()
22 | 
23 |         return report
24 | 
25 |     async def run_subtopic_research(self, parent_query: str, subtopic: str, verbose: bool = True, source="web", headers=None):
26 |         try:
27 |             report = await self.research(parent_query=parent_query, query=subtopic,
28 |                                          research_report="subtopic_report", verbose=verbose, source=source, tone=self.tone, headers=None)
29 |         except Exception as e:
30 |             print(f"{Fore.RED}Error in researching topic {subtopic}: {e}{Style.RESET_ALL}")
31 |             report = None
32 |         return {subtopic: report}
33 | 
34 |     async def run_initial_research(self, research_state: dict):
35 |         task = research_state.get("task")
36 |         query = task.get("query")
37 |         source = task.get("source", "web")
38 | 
39 |         if self.websocket and self.stream_output:
40 |             await self.stream_output("logs", "initial_research", f"Running initial research on the following query: {query}", self.websocket)
41 |         else:
42 |             print_agent_output(f"Running initial research on the following query: {query}", agent="RESEARCHER")
43 |         return {"task": task, "initial_research": await self.research(query=query, verbose=task.get("verbose"),
44 |                                                                       source=source, tone=self.tone, headers=self.headers)}
45 | 
46 |     async def run_depth_research(self, draft_state: dict):
47 |         task = draft_state.get("task")
48 |         topic = draft_state.get("topic")
49 |         parent_query = task.get("query")
50 |         source = task.get("source", "web")
51 |         verbose = task.get("verbose")
52 |         if self.websocket and self.stream_output:
53 |             await self.stream_output("logs", "depth_research", f"Running in depth research on the following report topic: {topic}", self.websocket)
54 |         else:
55 |             print_agent_output(f"Running in depth research on the following report topic: {topic}", agent="RESEARCHER")
56 |         research_draft = await self.run_subtopic_research(parent_query=parent_query, subtopic=topic,
57 |                                                           verbose=verbose, source=source, headers=self.headers)
58 |         return {"draft": research_draft}


--------------------------------------------------------------------------------
/multi_agents/agents/reviewer.py:
--------------------------------------------------------------------------------
 1 | from .utils.views import print_agent_output
 2 | from .utils.llms import call_model
 3 | 
 4 | TEMPLATE = """You are an expert research article reviewer. \
 5 | Your goal is to review research drafts and provide feedback to the reviser only based on specific guidelines. \
 6 | """
 7 | 
 8 | 
 9 | class ReviewerAgent:
10 |     def __init__(self, websocket=None, stream_output=None, headers=None):
11 |         self.websocket = websocket
12 |         self.stream_output = stream_output
13 |         self.headers = headers or {}
14 | 
15 |     async def review_draft(self, draft_state: dict):
16 |         """
17 |         Review a draft article
18 |         :param draft_state:
19 |         :return:
20 |         """
21 |         task = draft_state.get("task")
22 |         guidelines = "- ".join(guideline for guideline in task.get("guidelines"))
23 |         revision_notes = draft_state.get("revision_notes")
24 | 
25 |         revise_prompt = f"""The reviser has already revised the draft based on your previous review notes with the following feedback:
26 | {revision_notes}\n
27 | Please provide additional feedback ONLY if critical since the reviser has already made changes based on your previous feedback.
28 | If you think the article is sufficient or that non critical revisions are required, please aim to return None.
29 | """
30 | 
31 |         review_prompt = f"""You have been tasked with reviewing the draft which was written by a non-expert based on specific guidelines.
32 | Please accept the draft if it is good enough to publish, or send it for revision, along with your notes to guide the revision.
33 | If not all of the guideline criteria are met, you should send appropriate revision notes.
34 | If the draft meets all the guidelines, please return None.
35 | {revise_prompt if revision_notes else ""}
36 | 
37 | Guidelines: {guidelines}\nDraft: {draft_state.get("draft")}\n
38 | """
39 |         prompt = [
40 |             {"role": "system", "content": TEMPLATE},
41 |             {"role": "user", "content": review_prompt},
42 |         ]
43 | 
44 |         response = await call_model(prompt, model=task.get("model"))
45 | 
46 |         if task.get("verbose"):
47 |             if self.websocket and self.stream_output:
48 |                 await self.stream_output(
49 |                     "logs",
50 |                     "review_feedback",
51 |                     f"Review feedback is: {response}...",
52 |                     self.websocket,
53 |                 )
54 |             else:
55 |                 print_agent_output(
56 |                     f"Review feedback is: {response}...", agent="REVIEWER"
57 |                 )
58 | 
59 |         if "None" in response:
60 |             return None
61 |         return response
62 | 
63 |     async def run(self, draft_state: dict):
64 |         task = draft_state.get("task")
65 |         guidelines = task.get("guidelines")
66 |         to_follow_guidelines = task.get("follow_guidelines")
67 |         review = None
68 |         if to_follow_guidelines:
69 |             print_agent_output(f"Reviewing draft...", agent="REVIEWER")
70 | 
71 |             if task.get("verbose"):
72 |                 print_agent_output(
73 |                     f"Following guidelines {guidelines}...", agent="REVIEWER"
74 |                 )
75 | 
76 |             review = await self.review_draft(draft_state)
77 |         else:
78 |             print_agent_output(f"Ignoring guidelines...", agent="REVIEWER")
79 |         return {"review": review}
80 | 


--------------------------------------------------------------------------------
/multi_agents/agents/reviser.py:
--------------------------------------------------------------------------------
 1 | from .utils.views import print_agent_output
 2 | from .utils.llms import call_model
 3 | import json
 4 | 
 5 | sample_revision_notes = """
 6 | {
 7 |   "draft": { 
 8 |     draft title: The revised draft that you are submitting for review 
 9 |   },
10 |   "revision_notes": Your message to the reviewer about the changes you made to the draft based on their feedback
11 | }
12 | """
13 | 
14 | 
15 | class ReviserAgent:
16 |     def __init__(self, websocket=None, stream_output=None, headers=None):
17 |         self.websocket = websocket
18 |         self.stream_output = stream_output
19 |         self.headers = headers or {}
20 | 
21 |     async def revise_draft(self, draft_state: dict):
22 |         """
23 |         Review a draft article
24 |         :param draft_state:
25 |         :return:
26 |         """
27 |         review = draft_state.get("review")
28 |         task = draft_state.get("task")
29 |         draft_report = draft_state.get("draft")
30 |         prompt = [
31 |             {
32 |                 "role": "system",
33 |                 "content": "You are an expert writer. Your goal is to revise drafts based on reviewer notes.",
34 |             },
35 |             {
36 |                 "role": "user",
37 |                 "content": f"""Draft:\n{draft_report}" + "Reviewer's notes:\n{review}\n\n
38 | You have been tasked by your reviewer with revising the following draft, which was written by a non-expert.
39 | If you decide to follow the reviewer's notes, please write a new draft and make sure to address all of the points they raised.
40 | Please keep all other aspects of the draft the same.
41 | You MUST return nothing but a JSON in the following format:
42 | {sample_revision_notes}
43 | """,
44 |             },
45 |         ]
46 | 
47 |         response = await call_model(
48 |             prompt,
49 |             model=task.get("model"),
50 |             response_format="json",
51 |         )
52 |         return response
53 | 
54 |     async def run(self, draft_state: dict):
55 |         print_agent_output(f"Rewriting draft based on feedback...", agent="REVISOR")
56 |         revision = await self.revise_draft(draft_state)
57 | 
58 |         if draft_state.get("task").get("verbose"):
59 |             if self.websocket and self.stream_output:
60 |                 await self.stream_output(
61 |                     "logs",
62 |                     "revision_notes",
63 |                     f"Revision notes: {revision.get('revision_notes')}",
64 |                     self.websocket,
65 |                 )
66 |             else:
67 |                 print_agent_output(
68 |                     f"Revision notes: {revision.get('revision_notes')}", agent="REVISOR"
69 |                 )
70 | 
71 |         return {
72 |             "draft": revision.get("draft"),
73 |             "revision_notes": revision.get("revision_notes"),
74 |         }
75 | 


--------------------------------------------------------------------------------
/multi_agents/agents/utils/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/master/multi_agents/agents/utils/__init__.py


--------------------------------------------------------------------------------
/multi_agents/agents/utils/file_formats.py:
--------------------------------------------------------------------------------
 1 | import aiofiles
 2 | import urllib
 3 | import uuid
 4 | import mistune
 5 | 
 6 | 
 7 | async def write_to_file(filename: str, text: str) -> None:
 8 |     """Asynchronously write text to a file in UTF-8 encoding.
 9 | 
10 |     Args:
11 |         filename (str): The filename to write to.
12 |         text (str): The text to write.
13 |     """
14 |     # Convert text to UTF-8, replacing any problematic characters
15 |     text_utf8 = text.encode('utf-8', errors='replace').decode('utf-8')
16 | 
17 |     async with aiofiles.open(filename, "w", encoding='utf-8') as file:
18 |         await file.write(text_utf8)
19 | 
20 | 
21 | async def write_text_to_md(text: str, path: str) -> str:
22 |     """Writes text to a Markdown file and returns the file path.
23 | 
24 |     Args:
25 |         text (str): Text to write to the Markdown file.
26 | 
27 |     Returns:
28 |         str: The file path of the generated Markdown file.
29 |     """
30 |     task = uuid.uuid4().hex
31 |     file_path = f"{path}/{task}.md"
32 |     await write_to_file(file_path, text)
33 |     print(f"Report written to {file_path}")
34 |     return file_path
35 | 
36 | 
37 | async def write_md_to_pdf(text: str, path: str) -> str:
38 |     """Converts Markdown text to a PDF file and returns the file path.
39 | 
40 |     Args:
41 |         text (str): Markdown text to convert.
42 | 
43 |     Returns:
44 |         str: The encoded file path of the generated PDF.
45 |     """
46 |     task = uuid.uuid4().hex
47 |     file_path = f"{path}/{task}.pdf"
48 | 
49 |     try:
50 |         # Moved imports to inner function to avoid known import errors with gobject-2.0
51 |         from md2pdf.core import md2pdf
52 |         md2pdf(file_path,
53 |                md_content=text,
54 |                # md_file_path=f"{file_path}.md",
55 |                css_file_path="./multi_agents/skills/utils/pdf_styles.css",  # Updated path
56 |                base_url=None)
57 |         print(f"Report written to {file_path}")
58 |     except Exception as e:
59 |         print(f"Error in converting Markdown to PDF: {e}")
60 |         return ""
61 | 
62 |     encoded_file_path = urllib.parse.quote(file_path)
63 |     return encoded_file_path
64 | 
65 | 
66 | async def write_md_to_word(text: str, path: str) -> str:
67 |     """Converts Markdown text to a DOCX file and returns the file path.
68 | 
69 |     Args:
70 |         text (str): Markdown text to convert.
71 | 
72 |     Returns:
73 |         str: The encoded file path of the generated DOCX.
74 |     """
75 |     task = uuid.uuid4().hex
76 |     file_path = f"{path}/{task}.docx"
77 | 
78 |     try:
79 |         from htmldocx import HtmlToDocx
80 |         from docx import Document
81 |         # Convert report markdown to HTML
82 |         html = mistune.html(text)
83 |         # Create a document object
84 |         doc = Document()
85 |         # Convert the html generated from the report to document format
86 |         HtmlToDocx().add_html_to_document(html, doc)
87 | 
88 |         # Saving the docx document to file_path
89 |         doc.save(file_path)
90 | 
91 |         print(f"Report written to {file_path}")
92 | 
93 |         encoded_file_path = urllib.parse.quote(f"{file_path}.docx")
94 |         return encoded_file_path
95 | 
96 |     except Exception as e:
97 |         print(f"Error in converting Markdown to DOCX: {e}")
98 |         return ""
99 | 


--------------------------------------------------------------------------------
/multi_agents/agents/utils/llms.py:
--------------------------------------------------------------------------------
 1 | import json5 as json
 2 | import json_repair
 3 | from langchain_community.adapters.openai import convert_openai_messages
 4 | 
 5 | from gpt_researcher.config.config import Config
 6 | from gpt_researcher.utils.llm import create_chat_completion
 7 | 
 8 | from loguru import logger
 9 | 
10 | 
11 | async def call_model(
12 |     prompt: list,
13 |     model: str,
14 |     response_format: str = None,
15 | ):
16 | 
17 |     optional_params = {}
18 |     if response_format == "json":
19 |         optional_params = {"response_format": {"type": "json_object"}}
20 | 
21 |     cfg = Config()
22 |     lc_messages = convert_openai_messages(prompt)
23 | 
24 |     try:
25 |         response = await create_chat_completion(
26 |             model=model,
27 |             messages=lc_messages,
28 |             temperature=0,
29 |             llm_provider=cfg.smart_llm_provider,
30 |             llm_kwargs=cfg.llm_kwargs,
31 |             # cost_callback=cost_callback,
32 |         )
33 | 
34 |         if response_format == "json":
35 |             try:
36 |                 cleaned_json_string = response.strip("```json\n")
37 |                 return json.loads(cleaned_json_string)
38 |             except Exception as e:
39 |                 print("⚠️ Error in reading JSON, attempting to repair JSON")
40 |                 logger.error(
41 |                     f"Error in reading JSON, attempting to repair reponse: {response}"
42 |                 )
43 |                 return json_repair.loads(response)
44 |         else:
45 |             return response
46 | 
47 |     except Exception as e:
48 |         print("⚠️ Error in calling model")
49 |         logger.error(f"Error in calling model: {e}")
50 | 


--------------------------------------------------------------------------------
/multi_agents/agents/utils/pdf_styles.css:
--------------------------------------------------------------------------------
 1 | body {
 2 |     font-family: 'Libre Baskerville', serif;
 3 |     font-size: 12pt; /* standard size for academic papers */
 4 |     line-height: 1.6; /* for readability */
 5 |     color: #333; /* softer on the eyes than black */
 6 |     background-color: #fff; /* white background */
 7 |     margin: 0;
 8 |     padding: 0;
 9 | }
10 | 
11 | h1, h2, h3, h4, h5, h6 {
12 |     font-family: 'Libre Baskerville', serif;
13 |     color: #000; /* darker than the body text */
14 |     margin-top: 1em; /* space above headers */
15 | }
16 | 
17 | h1 {
18 |     font-size: 2em; /* make h1 twice the size of the body text */
19 | }
20 | 
21 | h2 {
22 |     font-size: 1.5em;
23 | }
24 | 
25 | /* Add some space between paragraphs */
26 | p {
27 |     margin-bottom: 1em;
28 | }
29 | 
30 | /* Style for blockquotes, often used in academic papers */
31 | blockquote {
32 |     font-style: italic;
33 |     margin: 1em 0;
34 |     padding: 1em;
35 |     background-color: #f9f9f9; /* a light grey background */
36 | }
37 | 
38 | /* You might want to style tables, figures, etc. too */
39 | table {
40 |     border-collapse: collapse;
41 |     width: 100%;
42 | }
43 | 
44 | table, th, td {
45 |     border: 1px solid #ddd;
46 |     text-align: left;
47 |     padding: 8px;
48 | }
49 | 
50 | th {
51 |     background-color: #f2f2f2;
52 |     color: black;
53 | }


--------------------------------------------------------------------------------
/multi_agents/agents/utils/utils.py:
--------------------------------------------------------------------------------
 1 | import re
 2 | 
 3 | def sanitize_filename(filename: str) -> str:
 4 |     """
 5 |     Sanitize a given filename by replacing characters that are invalid 
 6 |     in Windows file paths with an underscore ('_').
 7 | 
 8 |     This function ensures that the filename is compatible with all 
 9 |     operating systems by removing or replacing characters that are 
10 |     not allowed in Windows file paths. Specifically, it replaces 
11 |     the following characters: < > : " / \\ | ? *
12 | 
13 |     Parameters:
14 |     filename (str): The original filename to be sanitized.
15 | 
16 |     Returns:
17 |     str: The sanitized filename with invalid characters replaced by an underscore.
18 |     
19 |     Examples:
20 |     >>> sanitize_filename('invalid:file/name*example?.txt')
21 |     'invalid_file_name_example_.txt'
22 |     
23 |     >>> sanitize_filename('valid_filename.txt')
24 |     'valid_filename.txt'
25 |     """
26 |     return re.sub(r'[<>:"/\\|?*]', '_', filename)
27 | 


--------------------------------------------------------------------------------
/multi_agents/agents/utils/views.py:
--------------------------------------------------------------------------------
 1 | from colorama import Fore, Style
 2 | from enum import Enum
 3 | 
 4 | 
 5 | class AgentColor(Enum):
 6 |     RESEARCHER = Fore.LIGHTBLUE_EX
 7 |     EDITOR = Fore.YELLOW
 8 |     WRITER = Fore.LIGHTGREEN_EX
 9 |     PUBLISHER = Fore.MAGENTA
10 |     REVIEWER = Fore.CYAN
11 |     REVISOR = Fore.LIGHTWHITE_EX
12 |     MASTER = Fore.LIGHTYELLOW_EX
13 | 
14 | 
15 | def print_agent_output(output:str, agent: str="RESEARCHER"):
16 |     print(f"{AgentColor[agent].value}{agent}: {output}{Style.RESET_ALL}")


--------------------------------------------------------------------------------
/multi_agents/agents/writer.py:
--------------------------------------------------------------------------------
  1 | from datetime import datetime
  2 | import json5 as json
  3 | from .utils.views import print_agent_output
  4 | from .utils.llms import call_model
  5 | 
  6 | sample_json = """
  7 | {
  8 |   "table_of_contents": A table of contents in markdown syntax (using '-') based on the research headers and subheaders,
  9 |   "introduction": An indepth introduction to the topic in markdown syntax and hyperlink references to relevant sources,
 10 |   "conclusion": A conclusion to the entire research based on all research data in markdown syntax and hyperlink references to relevant sources,
 11 |   "sources": A list with strings of all used source links in the entire research data in markdown syntax and apa citation format. For example: ['-  Title, year, Author [source url](source)', ...]
 12 | }
 13 | """
 14 | 
 15 | 
 16 | class WriterAgent:
 17 |     def __init__(self, websocket=None, stream_output=None, headers=None):
 18 |         self.websocket = websocket
 19 |         self.stream_output = stream_output
 20 |         self.headers = headers
 21 | 
 22 |     def get_headers(self, research_state: dict):
 23 |         return {
 24 |             "title": research_state.get("title"),
 25 |             "date": "Date",
 26 |             "introduction": "Introduction",
 27 |             "table_of_contents": "Table of Contents",
 28 |             "conclusion": "Conclusion",
 29 |             "references": "References",
 30 |         }
 31 | 
 32 |     async def write_sections(self, research_state: dict):
 33 |         query = research_state.get("title")
 34 |         data = research_state.get("research_data")
 35 |         task = research_state.get("task")
 36 |         follow_guidelines = task.get("follow_guidelines")
 37 |         guidelines = task.get("guidelines")
 38 | 
 39 |         prompt = [
 40 |             {
 41 |                 "role": "system",
 42 |                 "content": "You are a research writer. Your sole purpose is to write a well-written "
 43 |                 "research reports about a "
 44 |                 "topic based on research findings and information.\n ",
 45 |             },
 46 |             {
 47 |                 "role": "user",
 48 |                 "content": f"Today's date is {datetime.now().strftime('%d/%m/%Y')}\n."
 49 |                 f"Query or Topic: {query}\n"
 50 |                 f"Research data: {str(data)}\n"
 51 |                 f"Your task is to write an in depth, well written and detailed "
 52 |                 f"introduction and conclusion to the research report based on the provided research data. "
 53 |                 f"Do not include headers in the results.\n"
 54 |                 f"You MUST include any relevant sources to the introduction and conclusion as markdown hyperlinks -"
 55 |                 f"For example: 'This is a sample text. ([url website](url))'\n\n"
 56 |                 f"{f'You must follow the guidelines provided: {guidelines}' if follow_guidelines else ''}\n"
 57 |                 f"You MUST return nothing but a JSON in the following format (without json markdown):\n"
 58 |                 f"{sample_json}\n\n",
 59 |             },
 60 |         ]
 61 | 
 62 |         response = await call_model(
 63 |             prompt,
 64 |             task.get("model"),
 65 |             response_format="json",
 66 |         )
 67 |         return response
 68 | 
 69 |     async def revise_headers(self, task: dict, headers: dict):
 70 |         prompt = [
 71 |             {
 72 |                 "role": "system",
 73 |                 "content": """You are a research writer. 
 74 | Your sole purpose is to revise the headers data based on the given guidelines.""",
 75 |             },
 76 |             {
 77 |                 "role": "user",
 78 |                 "content": f"""Your task is to revise the given headers JSON based on the guidelines given.
 79 | You are to follow the guidelines but the values should be in simple strings, ignoring all markdown syntax.
 80 | You must return nothing but a JSON in the same format as given in headers data.
 81 | Guidelines: {task.get("guidelines")}\n
 82 | Headers Data: {headers}\n
 83 | """,
 84 |             },
 85 |         ]
 86 | 
 87 |         response = await call_model(
 88 |             prompt,
 89 |             task.get("model"),
 90 |             response_format="json",
 91 |         )
 92 |         return {"headers": response}
 93 | 
 94 |     async def run(self, research_state: dict):
 95 |         if self.websocket and self.stream_output:
 96 |             await self.stream_output(
 97 |                 "logs",
 98 |                 "writing_report",
 99 |                 f"Writing final research report based on research data...",
100 |                 self.websocket,
101 |             )
102 |         else:
103 |             print_agent_output(
104 |                 f"Writing final research report based on research data...",
105 |                 agent="WRITER",
106 |             )
107 | 
108 |         research_layout_content = await self.write_sections(research_state)
109 | 
110 |         if research_state.get("task").get("verbose"):
111 |             if self.websocket and self.stream_output:
112 |                 research_layout_content_str = json.dumps(
113 |                     research_layout_content, indent=2
114 |                 )
115 |                 await self.stream_output(
116 |                     "logs",
117 |                     "research_layout_content",
118 |                     research_layout_content_str,
119 |                     self.websocket,
120 |                 )
121 |             else:
122 |                 print_agent_output(research_layout_content, agent="WRITER")
123 | 
124 |         headers = self.get_headers(research_state)
125 |         if research_state.get("task").get("follow_guidelines"):
126 |             if self.websocket and self.stream_output:
127 |                 await self.stream_output(
128 |                     "logs",
129 |                     "rewriting_layout",
130 |                     "Rewriting layout based on guidelines...",
131 |                     self.websocket,
132 |                 )
133 |             else:
134 |                 print_agent_output(
135 |                     "Rewriting layout based on guidelines...", agent="WRITER"
136 |                 )
137 |             headers = await self.revise_headers(
138 |                 task=research_state.get("task"), headers=headers
139 |             )
140 |             headers = headers.get("headers")
141 | 
142 |         return {**research_layout_content, "headers": headers}
143 | 


--------------------------------------------------------------------------------
/multi_agents/langgraph.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "python_version": "3.11",
 3 |   "dependencies": [
 4 |     "."
 5 |   ],
 6 |   "graphs": {
 7 |     "agent": "./agent.py:graph"
 8 |   },
 9 |   "env": ".env"
10 | }


--------------------------------------------------------------------------------
/multi_agents/main.py:
--------------------------------------------------------------------------------
 1 | from dotenv import load_dotenv
 2 | import sys
 3 | import os
 4 | import uuid
 5 | sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 6 | 
 7 | from multi_agents.agents import ChiefEditorAgent
 8 | import asyncio
 9 | import json
10 | from gpt_researcher.utils.enum import Tone
11 | 
12 | # Run with LangSmith if API key is set
13 | if os.environ.get("LANGCHAIN_API_KEY"):
14 |     os.environ["LANGCHAIN_TRACING_V2"] = "true"
15 | load_dotenv()
16 | 
17 | def open_task():
18 |     # Get the directory of the current script
19 |     current_dir = os.path.dirname(os.path.abspath(__file__))
20 |     # Construct the absolute path to task.json
21 |     task_json_path = os.path.join(current_dir, 'task.json')
22 |     
23 |     with open(task_json_path, 'r') as f:
24 |         task = json.load(f)
25 | 
26 |     if not task:
27 |         raise Exception("No task found. Please ensure a valid task.json file is present in the multi_agents directory and contains the necessary task information.")
28 | 
29 |     return task
30 | 
31 | async def run_research_task(query, websocket=None, stream_output=None, tone=Tone.Objective, headers=None):
32 |     task = open_task()
33 |     task["query"] = query
34 | 
35 |     chief_editor = ChiefEditorAgent(task, websocket, stream_output, tone, headers)
36 |     research_report = await chief_editor.run_research_task()
37 | 
38 |     if websocket and stream_output:
39 |         await stream_output("logs", "research_report", research_report, websocket)
40 | 
41 |     return research_report
42 | 
43 | async def main():
44 |     task = open_task()
45 | 
46 |     chief_editor = ChiefEditorAgent(task)
47 |     research_report = await chief_editor.run_research_task(task_id=uuid.uuid4())
48 | 
49 |     return research_report
50 | 
51 | if __name__ == "__main__":
52 |     asyncio.run(main())


--------------------------------------------------------------------------------
/multi_agents/memory/__init__.py:
--------------------------------------------------------------------------------
1 | from .draft import DraftState
2 | from .research import ResearchState
3 | 
4 | __all__ = [
5 |     "DraftState",
6 |     "ResearchState"
7 | ]


--------------------------------------------------------------------------------
/multi_agents/memory/draft.py:
--------------------------------------------------------------------------------
 1 | from typing import TypedDict, List, Annotated
 2 | import operator
 3 | 
 4 | 
 5 | class DraftState(TypedDict):
 6 |     task: dict
 7 |     topic: str
 8 |     draft: dict
 9 |     review: str
10 |     revision_notes: str


--------------------------------------------------------------------------------
/multi_agents/memory/research.py:
--------------------------------------------------------------------------------
 1 | from typing import TypedDict, List, Annotated
 2 | import operator
 3 | 
 4 | 
 5 | class ResearchState(TypedDict):
 6 |     task: dict
 7 |     initial_research: str
 8 |     sections: List[str]
 9 |     research_data: List[dict]
10 |     human_feedback: str
11 |     # Report layout
12 |     title: str
13 |     headers: dict
14 |     date: str
15 |     table_of_contents: str
16 |     introduction: str
17 |     conclusion: str
18 |     sources: List[str]
19 |     report: str
20 | 
21 | 
22 | 


--------------------------------------------------------------------------------
/multi_agents/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "simple_js_test",
 3 |   "version": "1.0.0",
 4 |   "description": "",
 5 |   "main": "server.js",
 6 |   "type": "module",
 7 |   "scripts": {
 8 |     "test": "echo \"Error: no test specified\" && exit 1"
 9 |   },
10 |   "author": "",
11 |   "license": "ISC",
12 |   "dependencies": {
13 |     "@langchain/langgraph-sdk": "^0.0.1-rc.13"
14 |   }
15 | }
16 | 


--------------------------------------------------------------------------------
/multi_agents/requirements.txt:
--------------------------------------------------------------------------------
1 | langgraph
2 | gpt_researcher
3 | langgraph-cli
4 | python-dotenv
5 | weasyprint
6 | json5
7 | loguru
8 | 


--------------------------------------------------------------------------------
/multi_agents/task.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "query": "Is AI in a hype cycle?",
 3 |   "max_sections": 3,
 4 |   "publish_formats": {
 5 |     "markdown": true,
 6 |     "pdf": true,
 7 |     "docx": true
 8 |   },
 9 |   "include_human_feedback": false,
10 |   "follow_guidelines": false,
11 |   "model": "gpt-4o",
12 |   "guidelines": [
13 |     "The report MUST be written in APA format",
14 |     "Each sub section MUST include supporting sources using hyperlinks. If none exist, erase the sub section or rewrite it to be a part of the previous section",
15 |     "The report MUST be written in spanish"
16 |   ],
17 |   "verbose": true
18 | }