├── .dockerignore
├── .env.example
├── .github
    ├── ISSUE_TEMPLATE
    │   ├── bug_report.md
    │   └── feature_request.md
    ├── dependabot.yml
    └── workflows
    │   └── docker-build.yml
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── README-ja_JP.md
├── README-ko_KR.md
├── README-zh_CN.md
├── README.md
├── backend
    ├── __init__.py
    ├── chat
    │   ├── __init__.py
    │   └── chat.py
    ├── memory
    │   ├── __init__.py
    │   ├── draft.py
    │   └── research.py
    ├── report_type
    │   ├── __init__.py
    │   ├── basic_report
    │   │   ├── __init__.py
    │   │   └── basic_report.py
    │   └── detailed_report
    │   │   ├── README.md
    │   │   ├── __init__.py
    │   │   └── detailed_report.py
    ├── server
    │   ├── __init__.py
    │   ├── app.py
    │   ├── logging_config.py
    │   ├── server.py
    │   ├── server_utils.py
    │   └── websocket_manager.py
    └── utils.py
├── citation.cff
├── cli.py
├── docker-compose.yml
├── docs
    ├── CNAME
    ├── README.md
    ├── babel.config.js
    ├── blog
    │   ├── 2023-09-22-gpt-researcher
    │   │   ├── architecture.png
    │   │   ├── index.md
    │   │   └── planner.jpeg
    │   ├── 2023-11-12-openai-assistant
    │   │   ├── diagram-1.png
    │   │   ├── diagram-assistant.jpeg
    │   │   └── index.md
    │   ├── 2024-05-19-gptr-langgraph
    │   │   ├── architecture.jpeg
    │   │   ├── blog-langgraph.jpeg
    │   │   └── index.md
    │   ├── 2024-09-7-hybrid-research
    │   │   ├── gptr-hybrid.png
    │   │   └── index.md
    │   └── authors.yml
    ├── docs
    │   ├── contribute.md
    │   ├── examples
    │   │   ├── detailed_report.md
    │   │   ├── examples.ipynb
    │   │   ├── examples.md
    │   │   ├── hybrid_research.md
    │   │   ├── pip-run.ipynb
    │   │   ├── sample_report.py
    │   │   └── sample_sources_only.py
    │   ├── faq.md
    │   ├── gpt-researcher
    │   │   ├── context
    │   │   │   ├── filtering-by-domain.md
    │   │   │   ├── gptr-hybrid.png
    │   │   │   ├── local-docs.md
    │   │   │   ├── tailored-research.md
    │   │   │   └── vector-stores.md
    │   │   ├── frontend
    │   │   │   ├── frontend.md
    │   │   │   ├── logs.md
    │   │   │   └── playing-with-webhooks.md
    │   │   ├── getting-started
    │   │   │   ├── cli.md
    │   │   │   ├── getting-started-with-docker.md
    │   │   │   ├── getting-started.md
    │   │   │   ├── how-to-choose.md
    │   │   │   ├── introduction.md
    │   │   │   └── linux-deployment.md
    │   │   ├── gptr
    │   │   │   ├── automated-tests.md
    │   │   │   ├── config.md
    │   │   │   ├── example.md
    │   │   │   ├── handling-logs-as-they-stream.md
    │   │   │   ├── pip-package.md
    │   │   │   ├── querying-the-backend.md
    │   │   │   ├── scraping.md
    │   │   │   └── troubleshooting.md
    │   │   ├── llms
    │   │   │   ├── llms.md
    │   │   │   ├── running-with-ollama.md
    │   │   │   └── testing-your-llm.md
    │   │   ├── multi_agents
    │   │   │   └── langgraph.md
    │   │   └── search-engines
    │   │   │   ├── retrievers.md
    │   │   │   └── test-your-retriever.md
    │   ├── reference
    │   │   ├── config
    │   │   │   ├── config.md
    │   │   │   └── singleton.md
    │   │   ├── processing
    │   │   │   ├── html.md
    │   │   │   └── text.md
    │   │   └── sidebar.json
    │   ├── roadmap.md
    │   └── welcome.md
    ├── docusaurus.config.js
    ├── package.json
    ├── pydoc-markdown.yml
    ├── sidebars.js
    ├── src
    │   ├── components
    │   │   ├── HomepageFeatures.js
    │   │   └── HomepageFeatures.module.css
    │   ├── css
    │   │   └── custom.css
    │   └── pages
    │   │   ├── index.js
    │   │   └── index.module.css
    ├── static
    │   ├── .nojekyll
    │   ├── CNAME
    │   └── img
    │   │   ├── architecture.png
    │   │   ├── banner1.jpg
    │   │   ├── examples.png
    │   │   ├── gptr-logo.png
    │   │   ├── leaderboard.png
    │   │   └── multi-agent.png
    └── yarn.lock
├── frontend
    ├── README.md
    ├── index.html
    ├── nextjs
    │   ├── .dockerignore
    │   ├── .eslintrc.json
    │   ├── .example.env
    │   ├── .gitignore
    │   ├── .prettierrc
    │   ├── Dockerfile
    │   ├── Dockerfile.dev
    │   ├── README.md
    │   ├── actions
    │   │   └── apiActions.ts
    │   ├── app
    │   │   ├── globals.css
    │   │   ├── layout.tsx
    │   │   └── page.tsx
    │   ├── components
    │   │   ├── Footer.tsx
    │   │   ├── Header.tsx
    │   │   ├── Hero.tsx
    │   │   ├── HumanFeedback.tsx
    │   │   ├── Images
    │   │   │   ├── ImageModal.jsx
    │   │   │   └── ImagesAlbum.jsx
    │   │   ├── Langgraph
    │   │   │   └── Langgraph.js
    │   │   ├── LoadingDots.tsx
    │   │   ├── ResearchBlocks
    │   │   │   ├── AccessReport.tsx
    │   │   │   ├── Answer.tsx
    │   │   │   ├── ImageSection.tsx
    │   │   │   ├── LogsSection.tsx
    │   │   │   ├── Question.tsx
    │   │   │   ├── Sources.tsx
    │   │   │   └── elements
    │   │   │   │   ├── InputArea.tsx
    │   │   │   │   ├── LogMessage.tsx
    │   │   │   │   ├── SourceCard.tsx
    │   │   │   │   └── SubQuestions.tsx
    │   │   ├── ResearchResults.tsx
    │   │   ├── Settings
    │   │   │   ├── App.css
    │   │   │   ├── ChatBox.tsx
    │   │   │   ├── FileUpload.tsx
    │   │   │   ├── Modal.tsx
    │   │   │   └── ToneSelector.tsx
    │   │   ├── SimilarTopics.tsx
    │   │   ├── Task
    │   │   │   ├── Accordion.tsx
    │   │   │   ├── AgentLogs.tsx
    │   │   │   ├── Report.tsx
    │   │   │   └── ResearchForm.tsx
    │   │   └── TypeAnimation.tsx
    │   ├── config
    │   │   └── task.ts
    │   ├── helpers
    │   │   ├── findDifferences.ts
    │   │   └── getHost.ts
    │   ├── hooks
    │   │   └── useWebSocket.ts
    │   ├── next.config.mjs
    │   ├── nginx
    │   │   └── default.conf
    │   ├── package.json
    │   ├── postcss.config.mjs
    │   ├── public
    │   │   ├── favicon.ico
    │   │   ├── img
    │   │   │   ├── F.svg
    │   │   │   ├── Info.svg
    │   │   │   ├── W.svg
    │   │   │   ├── agents
    │   │   │   │   ├── academicResearchAgentAvatar.png
    │   │   │   │   ├── businessAnalystAgentAvatar.png
    │   │   │   │   ├── computerSecurityanalystAvatar.png
    │   │   │   │   ├── defaultAgentAvatar.JPG
    │   │   │   │   ├── financeAgentAvatar.png
    │   │   │   │   ├── mathAgentAvatar.png
    │   │   │   │   └── travelAgentAvatar.png
    │   │   │   ├── arrow-circle-up-right.svg
    │   │   │   ├── arrow-narrow-right.svg
    │   │   │   ├── browser.svg
    │   │   │   ├── chat-check.svg
    │   │   │   ├── chat.svg
    │   │   │   ├── copy-white.svg
    │   │   │   ├── copy.svg
    │   │   │   ├── dinosaur.svg
    │   │   │   ├── discord.svg
    │   │   │   ├── docker-blue.svg
    │   │   │   ├── docker.svg
    │   │   │   ├── dunk.svg
    │   │   │   ├── github-blue.svg
    │   │   │   ├── github-footer.svg
    │   │   │   ├── github.svg
    │   │   │   ├── globe.svg
    │   │   │   ├── gptr-logo.png
    │   │   │   ├── hiker.svg
    │   │   │   ├── icon _atom_.svg
    │   │   │   ├── icon _dumbell_.svg
    │   │   │   ├── icon _leaf_.svg
    │   │   │   ├── image.svg
    │   │   │   ├── indeed.svg
    │   │   │   ├── link.svg
    │   │   │   ├── message-question-circle.svg
    │   │   │   ├── news.svg
    │   │   │   ├── search.svg
    │   │   │   ├── share.svg
    │   │   │   ├── similarTopics.svg
    │   │   │   ├── sources.svg
    │   │   │   ├── stock.svg
    │   │   │   ├── stock2.svg
    │   │   │   ├── thinking.svg
    │   │   │   ├── white-books.svg
    │   │   │   └── x.svg
    │   │   ├── next.svg
    │   │   └── vercel.svg
    │   ├── styles
    │   │   └── markdown.css
    │   ├── tailwind.config.ts
    │   ├── tsconfig.json
    │   ├── types
    │   │   └── data.ts
    │   └── utils
    │   │   ├── consolidateBlocks.ts
    │   │   └── dataProcessing.ts
    ├── pdf_styles.css
    ├── scripts.js
    ├── static
    │   ├── academicResearchAgentAvatar.png
    │   ├── businessAnalystAgentAvatar.png
    │   ├── computerSecurityanalystAvatar.png
    │   ├── defaultAgentAvatar.JPG
    │   ├── favicon.ico
    │   ├── financeAgentAvatar.png
    │   ├── gptr-logo.png
    │   ├── mathAgentAvatar.png
    │   └── travelAgentAvatar.png
    └── styles.css
├── gpt_researcher
    ├── README.md
    ├── __init__.py
    ├── actions
    │   ├── __init__.py
    │   ├── agent_creator.py
    │   ├── markdown_processing.py
    │   ├── query_processing.py
    │   ├── report_generation.py
    │   ├── retriever.py
    │   ├── utils.py
    │   └── web_scraping.py
    ├── agent.py
    ├── config
    │   ├── __init__.py
    │   ├── config.py
    │   └── variables
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── default.py
    │   │   └── test_local.json
    ├── context
    │   ├── __init__.py
    │   ├── compression.py
    │   └── retriever.py
    ├── document
    │   ├── __init__.py
    │   ├── document.py
    │   └── langchain_document.py
    ├── llm_provider
    │   ├── __init__.py
    │   └── generic
    │   │   ├── __init__.py
    │   │   └── base.py
    ├── memory
    │   ├── __init__.py
    │   └── embeddings.py
    ├── prompts.py
    ├── retrievers
    │   ├── __init__.py
    │   ├── arxiv
    │   │   ├── __init__.py
    │   │   └── arxiv.py
    │   ├── bing
    │   │   ├── __init__.py
    │   │   └── bing.py
    │   ├── custom
    │   │   ├── __init__.py
    │   │   └── custom.py
    │   ├── duckduckgo
    │   │   ├── __init__.py
    │   │   └── duckduckgo.py
    │   ├── exa
    │   │   ├── __init__.py
    │   │   └── exa.py
    │   ├── google
    │   │   ├── __init__.py
    │   │   └── google.py
    │   ├── pubmed_central
    │   │   ├── __init__.py
    │   │   └── pubmed_central.py
    │   ├── searchapi
    │   │   ├── __init__.py
    │   │   └── searchapi.py
    │   ├── searx
    │   │   ├── __init__.py
    │   │   └── searx.py
    │   ├── semantic_scholar
    │   │   ├── __init__.py
    │   │   └── semantic_scholar.py
    │   ├── serpapi
    │   │   ├── __init__.py
    │   │   └── serpapi.py
    │   ├── serper
    │   │   ├── __init__.py
    │   │   └── serper.py
    │   ├── tavily
    │   │   ├── __init__.py
    │   │   └── tavily_search.py
    │   └── utils.py
    ├── scraper
    │   ├── __init__.py
    │   ├── arxiv
    │   │   ├── __init__.py
    │   │   └── arxiv.py
    │   ├── beautiful_soup
    │   │   ├── __init__.py
    │   │   └── beautiful_soup.py
    │   ├── browser
    │   │   ├── __init__.py
    │   │   ├── browser.py
    │   │   ├── js
    │   │   │   └── overlay.js
    │   │   └── processing
    │   │   │   ├── __init__.py
    │   │   │   ├── html.py
    │   │   │   └── scrape_skills.py
    │   ├── pymupdf
    │   │   ├── __init__.py
    │   │   └── pymupdf.py
    │   ├── scraper.py
    │   ├── utils.py
    │   └── web_base_loader
    │   │   ├── __init__.py
    │   │   └── web_base_loader.py
    ├── skills
    │   ├── __init__.py
    │   ├── browser.py
    │   ├── context_manager.py
    │   ├── curator.py
    │   ├── researcher.py
    │   └── writer.py
    ├── utils
    │   ├── __init__.py
    │   ├── costs.py
    │   ├── enum.py
    │   ├── llm.py
    │   ├── logger.py
    │   ├── logging_config.py
    │   └── validators.py
    └── vector_store
    │   ├── __init__.py
    │   └── vector_store.py
├── langgraph.json
├── main.py
├── multi_agents
    ├── README.md
    ├── __init__.py
    ├── agent.py
    ├── agents
    │   ├── __init__.py
    │   ├── editor.py
    │   ├── human.py
    │   ├── orchestrator.py
    │   ├── publisher.py
    │   ├── researcher.py
    │   ├── reviewer.py
    │   ├── reviser.py
    │   ├── utils
    │   │   ├── __init__.py
    │   │   ├── file_formats.py
    │   │   ├── llms.py
    │   │   ├── pdf_styles.css
    │   │   ├── utils.py
    │   │   └── views.py
    │   └── writer.py
    ├── langgraph.json
    ├── main.py
    ├── memory
    │   ├── __init__.py
    │   ├── draft.py
    │   └── research.py
    ├── package.json
    ├── requirements.txt
    └── task.json
├── poetry.toml
├── pyproject.toml
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── docs
        └── doc.pdf
    ├── documents-report-source.py
    ├── gptr-logs-handler.py
    ├── report-types.py
    ├── research_test.py
    ├── test-loaders.py
    ├── test-openai-llm.py
    ├── test-your-llm.py
    ├── test-your-retriever.py
    ├── test_logging.py
    ├── test_logs.py
    ├── test_researcher_logging.py
    └── vector-store.py


/.dockerignore:
--------------------------------------------------------------------------------
1 | .git
2 | output/
3 | 


--------------------------------------------------------------------------------
/.env.example:
--------------------------------------------------------------------------------
1 | OPENAI_API_KEY=
2 | TAVILY_API_KEY=
3 | DOC_PATH=./my-docs


--------------------------------------------------------------------------------
/.github/ISSUE_TEMPLATE/bug_report.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | name: Bug report
 3 | about: Create a report to help us improve
 4 | title: ''
 5 | labels: ''
 6 | assignees: ''
 7 | 
 8 | ---
 9 | 
10 | **Describe the bug**
11 | A clear and concise description of what the bug is.
12 | 
13 | **To Reproduce**
14 | Steps to reproduce the behavior:
15 | 1. Go to '...'
16 | 2. Click on '....'
17 | 3. Scroll down to '....'
18 | 4. See error
19 | 
20 | **Expected behavior**
21 | A clear and concise description of what you expected to happen.
22 | 
23 | **Screenshots**
24 | If applicable, add screenshots to help explain your problem.
25 | 
26 | **Desktop (please complete the following information):**
27 |  - OS: [e.g. iOS]
28 |  - Browser [e.g. chrome, safari]
29 |  - Version [e.g. 22]
30 | 
31 | **Smartphone (please complete the following information):**
32 |  - Device: [e.g. iPhone6]
33 |  - OS: [e.g. iOS8.1]
34 |  - Browser [e.g. stock browser, safari]
35 |  - Version [e.g. 22]
36 | 
37 | **Additional context**
38 | Add any other context about the problem here.
39 | 


--------------------------------------------------------------------------------
/.github/ISSUE_TEMPLATE/feature_request.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | name: Feature request
 3 | about: Suggest an idea for this project
 4 | title: ''
 5 | labels: ''
 6 | assignees: ''
 7 | 
 8 | ---
 9 | 
10 | **Is your feature request related to a problem? Please describe.**
11 | A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]
12 | 
13 | **Describe the solution you'd like**
14 | A clear and concise description of what you want to happen.
15 | 
16 | **Describe alternatives you've considered**
17 | A clear and concise description of any alternative solutions or features you've considered.
18 | 
19 | **Additional context**
20 | Add any other context or screenshots about the feature request here.
21 | 


--------------------------------------------------------------------------------
/.github/dependabot.yml:
--------------------------------------------------------------------------------
 1 | # To get started with Dependabot version updates, you'll need to specify which
 2 | # package ecosystems to update and where the package manifests are located.
 3 | # Please see the documentation for all configuration options:
 4 | # https://docs.github.com/github/administering-a-repository/configuration-options-for-dependency-updates
 5 | 
 6 | version: 2
 7 | updates:
 8 |   - package-ecosystem: "pip" # See documentation for possible values
 9 |     directory: "/" # Location of package manifests
10 |     schedule:
11 |       interval: "weekly"
12 |   - package-ecosystem: "docker"
13 |     directory: "/"
14 |     schedule:
15 |       interval: "weekly"
16 | 


--------------------------------------------------------------------------------
/.github/workflows/docker-build.yml:
--------------------------------------------------------------------------------
 1 | name: GPTR tests
 2 | run-name: ${{ github.actor }} ran the GPTR tests flow
 3 | permissions:
 4 |   contents: read
 5 |   pull-requests: write
 6 | on:
 7 |   workflow_dispatch:  # Add this line to enable manual triggering
 8 |   # pull_request:
 9 |   #   types: [opened, synchronize]
10 | 
11 | jobs:
12 |   docker:
13 |     runs-on: ubuntu-latest
14 |     environment: tests  # Specify the environment to use for this job
15 |     env:
16 |       # Ensure these environment variables are set for the entire job
17 |       OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
18 |       TAVILY_API_KEY: ${{ secrets.TAVILY_API_KEY }}
19 |       LANGCHAIN_API_KEY: ${{ secrets.LANGCHAIN_API_KEY }}
20 |     steps:
21 |       - name: Git checkout
22 |         uses: actions/checkout@v3
23 | 
24 |       - name: Set up QEMU
25 |         uses: docker/setup-qemu-action@v2
26 | 
27 |       - name: Set up Docker Buildx
28 |         uses: docker/setup-buildx-action@v2
29 |         with:
30 |           driver: docker
31 | 
32 |       # - name: Build Docker images
33 |       #   uses: docker/build-push-action@v4
34 |       #   with:
35 |       #     push: false
36 |       #     tags: gptresearcher/gpt-researcher:latest
37 |       #     file: Dockerfile          
38 | 
39 |       - name: Set up Docker Compose
40 |         run: |
41 |           sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
42 |           sudo chmod +x /usr/local/bin/docker-compose
43 |       - name: Run tests with Docker Compose
44 |         run: |
45 |           docker-compose --profile test run --rm gpt-researcher-tests


--------------------------------------------------------------------------------
/.gitignore:
--------------------------------------------------------------------------------
 1 | #Ignore env containing secrets
 2 | .env
 3 | .venv
 4 | .envrc
 5 | 
 6 | #Ignore Virtual Env
 7 | env/
 8 | venv/
 9 | .venv/
10 | 
11 | # Other Environments
12 | ENV/
13 | env.bak/
14 | venv.bak/
15 | 
16 | #Ignore generated outputs
17 | outputs/
18 | *.lock
19 | dist/
20 | gpt_researcher.egg-info/
21 | 
22 | #Ignore my local docs
23 | my-docs/
24 | 
25 | #Ignore pycache
26 | **/__pycache__/
27 | 
28 | #Ignore mypy cache
29 | .mypy_cache/
30 | node_modules
31 | .idea
32 | .DS_Store
33 | .docusaurus
34 | build
35 | docs/build
36 | 
37 | .vscode/launch.json
38 | .langgraph-data/
39 | .next/
40 | package-lock.json
41 | 
42 | #Vim swp files
43 | *.swp
44 | 
45 | # Log files
46 | logs/
47 | *.orig


--------------------------------------------------------------------------------
/CONTRIBUTING.md:
--------------------------------------------------------------------------------
 1 | # Contributing to GPT Researcher
 2 | 
 3 | First off, we'd like to welcome you and thank you for your interest and effort in contributing to our open-source project ❤️. Contributions of all forms are welcome—from new features and bug fixes to documentation and more.
 4 | 
 5 | We are on a mission to build the #1 AI agent for comprehensive, unbiased, and factual research online, and we need your support to achieve this grand vision.
 6 | 
 7 | Please take a moment to review this document to make the contribution process easy and effective for everyone involved.
 8 | 
 9 | ## Reporting Issues
10 | 
11 | If you come across any issue or have an idea for an improvement, don't hesitate to create an issue on GitHub. Describe your problem in sufficient detail, providing as much relevant information as possible. This way, we can reproduce the issue before attempting to fix it or respond appropriately.
12 | 
13 | ## Contributing Code
14 | 
15 | 1. **Fork the repository and create your branch from `master`.**  
16 |    If it’s not an urgent bug fix, branch from `master` and work on the feature or fix there.
17 | 
18 | 2. **Make your changes.**  
19 |    Implement your changes following best practices for coding in the project's language.
20 | 
21 | 3. **Test your changes.**  
22 |    Ensure that your changes pass all tests if any exist. If the project doesn’t have automated tests, test your changes manually to confirm they behave as expected.
23 | 
24 | 4. **Follow the coding style.**  
25 |    Ensure your code adheres to the coding conventions used throughout the project, including indentation, accurate comments, etc.
26 | 
27 | 5. **Commit your changes.**  
28 |    Make your Git commits informative and concise. This is very helpful for others when they look at the Git log.
29 | 
30 | 6. **Push to your fork and submit a pull request.**  
31 |    When your work is ready and passes tests, push your branch to your fork of the repository and submit a pull request from there.
32 | 
33 | 7. **Pat yourself on the back and wait for review.**  
34 |    Your work is done, congratulations! Now sit tight. The project maintainers will review your submission as soon as possible. They might suggest changes or ask for improvements. Both constructive conversation and patience are key to the collaboration process.
35 | 
36 | ## Documentation
37 | 
38 | If you would like to contribute to the project's documentation, please follow the same steps: fork the repository, make your changes, test them, and submit a pull request.
39 | 
40 | Documentation is a vital part of any software. It's not just about having good code; ensuring that users and contributors understand what's going on, how to use the software, or how to contribute is crucial.
41 | 
42 | We're grateful for all our contributors, and we look forward to building the world's leading AI research agent hand-in-hand with you. Let's harness the power of open source and AI to change the world together!
43 | 


--------------------------------------------------------------------------------
/Dockerfile:
--------------------------------------------------------------------------------
 1 | # Stage 1: Browser and build tools installation
 2 | FROM python:3.11.4-slim-bullseye AS install-browser
 3 | 
 4 | # Install Chromium, Chromedriver, Firefox, Geckodriver, and build tools in one layer
 5 | RUN apt-get update && \
 6 |     apt-get satisfy -y "chromium, chromium-driver (>= 115.0)" && \
 7 |     apt-get install -y --no-install-recommends firefox-esr wget build-essential && \
 8 |     wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz && \
 9 |     tar -xvzf geckodriver-v0.33.0-linux64.tar.gz && \
10 |     chmod +x geckodriver && \
11 |     mv geckodriver /usr/local/bin/ && \
12 |     rm geckodriver-v0.33.0-linux64.tar.gz && \
13 |     chromium --version && chromedriver --version && \
14 |     rm -rf /var/lib/apt/lists/*  # Clean up apt lists to reduce image size
15 | 
16 | # Stage 2: Python dependencies installation
17 | FROM install-browser AS gpt-researcher-install
18 | 
19 | ENV PIP_ROOT_USER_ACTION=ignore
20 | WORKDIR /usr/src/app
21 | 
22 | # Copy and install Python dependencies in a single layer to optimize cache usage
23 | COPY ./requirements.txt ./requirements.txt
24 | COPY ./multi_agents/requirements.txt ./multi_agents/requirements.txt
25 | 
26 | RUN pip install --no-cache-dir -r requirements.txt && \
27 |     pip install --no-cache-dir -r multi_agents/requirements.txt
28 | 
29 | # Stage 3: Final stage with non-root user and app
30 | FROM gpt-researcher-install AS gpt-researcher
31 | 
32 | # Create a non-root user for security
33 | RUN useradd -ms /bin/bash gpt-researcher && \
34 |     chown -R gpt-researcher:gpt-researcher /usr/src/app
35 | 
36 | USER gpt-researcher
37 | WORKDIR /usr/src/app
38 | 
39 | # Copy the rest of the application files with proper ownership
40 | COPY --chown=gpt-researcher:gpt-researcher ./ ./
41 | 
42 | # Expose the application's port
43 | EXPOSE 8000
44 | 
45 | # Define the default command to run the application
46 | CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
47 | 


--------------------------------------------------------------------------------
/backend/__init__.py:
--------------------------------------------------------------------------------
1 | from multi_agents import agents


--------------------------------------------------------------------------------
/backend/chat/__init__.py:
--------------------------------------------------------------------------------
1 | from .chat import ChatAgentWithMemory


--------------------------------------------------------------------------------
/backend/memory/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/backend/memory/__init__.py


--------------------------------------------------------------------------------
/backend/memory/draft.py:
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
/backend/memory/research.py:
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
10 |     # Report layout
11 |     title: str
12 |     headers: dict
13 |     date: str
14 |     table_of_contents: str
15 |     introduction: str
16 |     conclusion: str
17 |     sources: List[str]
18 |     report: str
19 | 
20 | 
21 | 


--------------------------------------------------------------------------------
/backend/report_type/__init__.py:
--------------------------------------------------------------------------------
1 | from .basic_report.basic_report import BasicReport
2 | from .detailed_report.detailed_report import DetailedReport
3 | 
4 | __all__ = [
5 |     "BasicReport",
6 |     "DetailedReport"
7 | ]


--------------------------------------------------------------------------------
/backend/report_type/basic_report/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/backend/report_type/basic_report/__init__.py


--------------------------------------------------------------------------------
/backend/report_type/basic_report/basic_report.py:
--------------------------------------------------------------------------------
 1 | from fastapi import WebSocket
 2 | from typing import Any
 3 | 
 4 | from gpt_researcher import GPTResearcher
 5 | 
 6 | 
 7 | class BasicReport:
 8 |     def __init__(
 9 |         self,
10 |         query: str,
11 |         report_type: str,
12 |         report_source: str,
13 |         source_urls,
14 |         tone: Any,
15 |         config_path: str,
16 |         websocket: WebSocket,
17 |         headers=None
18 |     ):
19 |         self.query = query
20 |         self.report_type = report_type
21 |         self.report_source = report_source
22 |         self.source_urls = source_urls
23 |         self.tone = tone
24 |         self.config_path = config_path
25 |         self.websocket = websocket
26 |         self.headers = headers or {}
27 | 
28 |     async def run(self):
29 |         # Initialize researcher
30 |         researcher = GPTResearcher(
31 |             query=self.query,
32 |             report_type=self.report_type,
33 |             report_source=self.report_source,
34 |             source_urls=self.source_urls,
35 |             tone=self.tone,
36 |             config_path=self.config_path,
37 |             websocket=self.websocket,
38 |             headers=self.headers
39 |         )
40 | 
41 |         await researcher.conduct_research()
42 |         report = await researcher.write_report()
43 |         return report
44 | 


--------------------------------------------------------------------------------
/backend/report_type/detailed_report/README.md:
--------------------------------------------------------------------------------
 1 | ## Detailed Reports
 2 | 
 3 | Introducing long and detailed reports, with a completely new architecture inspired by the latest [STORM](https://arxiv.org/abs/2402.14207) paper.
 4 | 
 5 | In this method we do the following:
 6 | 
 7 | 1. Trigger Initial GPT Researcher report based on task
 8 | 2. Generate subtopics from research summary
 9 | 3. For each subtopic the headers of the subtopic report are extracted and accumulated
10 | 4. For each subtopic a report is generated making sure that any information about the headers accumulated until now are not re-generated.
11 | 5. An additional introduction section is written along with a table of contents constructed from the entire report.
12 | 6. The final report is constructed by appending these : Intro + Table of contents + Subsection reports


--------------------------------------------------------------------------------
/backend/report_type/detailed_report/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/backend/report_type/detailed_report/__init__.py


--------------------------------------------------------------------------------
/backend/server/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/backend/server/__init__.py


--------------------------------------------------------------------------------
/backend/server/app.py:
--------------------------------------------------------------------------------
 1 | from fastapi import FastAPI
 2 | from fastapi.middleware.cors import CORSMiddleware
 3 | import logging
 4 | 
 5 | logger = logging.getLogger(__name__)
 6 | 
 7 | app = FastAPI()
 8 | 
 9 | # Add CORS middleware
10 | app.add_middleware(
11 |     CORSMiddleware,
12 |     allow_origins=["*"],  # In production, replace with your frontend domain
13 |     allow_credentials=True,
14 |     allow_methods=["*"],
15 |     allow_headers=["*"],
16 | )


--------------------------------------------------------------------------------
/backend/server/logging_config.py:
--------------------------------------------------------------------------------
 1 | import logging
 2 | import json
 3 | import os
 4 | from datetime import datetime
 5 | from pathlib import Path
 6 | 
 7 | class JSONResearchHandler:
 8 |     def __init__(self, json_file):
 9 |         self.json_file = json_file
10 |         self.research_data = {
11 |             "timestamp": datetime.now().isoformat(),
12 |             "events": [],
13 |             "content": {
14 |                 "query": "",
15 |                 "sources": [],
16 |                 "context": [],
17 |                 "report": "",
18 |                 "costs": 0.0
19 |             }
20 |         }
21 | 
22 |     def log_event(self, event_type: str, data: dict):
23 |         self.research_data["events"].append({
24 |             "timestamp": datetime.now().isoformat(),
25 |             "type": event_type,
26 |             "data": data
27 |         })
28 |         self._save_json()
29 | 
30 |     def update_content(self, key: str, value):
31 |         self.research_data["content"][key] = value
32 |         self._save_json()
33 | 
34 |     def _save_json(self):
35 |         with open(self.json_file, 'w') as f:
36 |             json.dump(self.research_data, f, indent=2)
37 | 
38 | def setup_research_logging():
39 |     # Create logs directory if it doesn't exist
40 |     logs_dir = Path("logs")
41 |     logs_dir.mkdir(exist_ok=True)
42 |     
43 |     # Generate timestamp for log files
44 |     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
45 |     
46 |     # Create log file paths
47 |     log_file = logs_dir / f"research_{timestamp}.log"
48 |     json_file = logs_dir / f"research_{timestamp}.json"
49 |     
50 |     # Configure file handler for research logs
51 |     file_handler = logging.FileHandler(log_file)
52 |     file_handler.setLevel(logging.INFO)
53 |     file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
54 |     
55 |     # Get research logger and configure it
56 |     research_logger = logging.getLogger('research')
57 |     research_logger.setLevel(logging.INFO)
58 |     
59 |     # Remove any existing handlers to avoid duplicates
60 |     research_logger.handlers.clear()
61 |     
62 |     # Add file handler
63 |     research_logger.addHandler(file_handler)
64 |     
65 |     # Add stream handler for console output
66 |     console_handler = logging.StreamHandler()
67 |     console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
68 |     research_logger.addHandler(console_handler)
69 |     
70 |     # Prevent propagation to root logger to avoid duplicate logs
71 |     research_logger.propagate = False
72 |     
73 |     # Create JSON handler
74 |     json_handler = JSONResearchHandler(json_file)
75 |     
76 |     return str(log_file), str(json_file), research_logger, json_handler
77 | 
78 | # Create a function to get the logger and JSON handler
79 | def get_research_logger():
80 |     return logging.getLogger('research')
81 | 
82 | def get_json_handler():
83 |     return getattr(logging.getLogger('research'), 'json_handler', None)


--------------------------------------------------------------------------------
/citation.cff:
--------------------------------------------------------------------------------
 1 | cff-version: 1.0.0
 2 | message: "If you use this software, please cite it as below."
 3 | authors:
 4 |   - family-names: Elovic
 5 |     given-names: Assaf
 6 | title: gpt-researcher
 7 | version: 0.5.4
 8 | date-released: 2023-07-23
 9 | repository-code: https://github.com/assafelovic/gpt-researcher
10 | url: https://gptr.dev


--------------------------------------------------------------------------------
/docker-compose.yml:
--------------------------------------------------------------------------------
 1 | services:
 2 |   gpt-researcher:
 3 |     pull_policy: build
 4 |     image: gptresearcher/gpt-researcher
 5 |     build: ./
 6 |     environment: 
 7 |       OPENAI_API_KEY: ${OPENAI_API_KEY}
 8 |       TAVILY_API_KEY: ${TAVILY_API_KEY}
 9 |       LANGCHAIN_API_KEY: ${LANGCHAIN_API_KEY}
10 |     restart: always
11 |     ports:
12 |       - 8000:8000
13 |   gptr-nextjs:
14 |     pull_policy: build
15 |     image: gptresearcher/gptr-nextjs
16 |     stdin_open: true
17 |     environment:
18 |       - CHOKIDAR_USEPOLLING=true
19 |     build:
20 |       dockerfile: Dockerfile.dev
21 |       context: frontend/nextjs
22 |     volumes:
23 |       - /app/node_modules
24 |       - ./frontend/nextjs:/app
25 |     restart: always
26 |     ports:
27 |       - 3000:3000
28 | 
29 |   gpt-researcher-tests:
30 |     image: gptresearcher/gpt-researcher-tests
31 |     build: ./
32 |     environment: 
33 |       OPENAI_API_KEY: ${OPENAI_API_KEY}
34 |       TAVILY_API_KEY: ${TAVILY_API_KEY}
35 |       LANGCHAIN_API_KEY: ${LANGCHAIN_API_KEY}
36 |     profiles: ["test"]
37 |     command: >
38 |       /bin/sh -c "
39 |       pip install pytest pytest-asyncio faiss-cpu &&
40 |       python -m pytest tests/report-types.py &&
41 |       python -m pytest tests/vector-store.py
42 |       "
43 | 


--------------------------------------------------------------------------------
/docs/CNAME:
--------------------------------------------------------------------------------
1 | docs.gptr.dev


--------------------------------------------------------------------------------
/docs/README.md:
--------------------------------------------------------------------------------
 1 | # Website
 2 | 
 3 | This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.
 4 | 
 5 | ## Prerequisites
 6 | 
 7 | To build and test documentation locally, begin by downloading and installing [Node.js](https://nodejs.org/en/download/), and then installing [Yarn](https://classic.yarnpkg.com/en/).
 8 | On Windows, you can install via the npm package manager (npm) which comes bundled with Node.js:
 9 | 
10 | ```console
11 | npm install --global yarn
12 | ```
13 | 
14 | ## Installation
15 | 
16 | ```console
17 | pip install pydoc-markdown
18 | cd website
19 | yarn install
20 | ```
21 | 
22 | ## Local Development
23 | 
24 | Navigate to the website folder and run:
25 | 
26 | ```console
27 | pydoc-markdown
28 | yarn start
29 | ```
30 | 
31 | This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.
32 | 


--------------------------------------------------------------------------------
/docs/babel.config.js:
--------------------------------------------------------------------------------
1 | module.exports = {
2 |   presets: [require.resolve('@docusaurus/core/lib/babel/preset')],
3 | };
4 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/blog/2023-09-22-gpt-researcher/architecture.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/blog/2023-09-22-gpt-researcher/planner.jpeg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/blog/2023-11-12-openai-assistant/diagram-1.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/blog/2023-11-12-openai-assistant/diagram-assistant.jpeg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/blog/2024-05-19-gptr-langgraph/architecture.jpeg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/blog/2024-05-19-gptr-langgraph/blog-langgraph.jpeg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/blog/2024-09-7-hybrid-research/gptr-hybrid.png


--------------------------------------------------------------------------------
/docs/blog/authors.yml:
--------------------------------------------------------------------------------
1 | assafe:
2 |   name: Assaf Elovic
3 |   title: Creator @ GPT Researcher and Tavily
4 |   url: https://github.com/assafelovic
5 |   image_url: https://lh3.googleusercontent.com/a/ACg8ocJtrLku69VG_2Y0sJa5mt66gIGNaEBX5r_mgE6CRPEb7A=s96-c
6 | 


--------------------------------------------------------------------------------
/docs/docs/contribute.md:
--------------------------------------------------------------------------------
1 | # Contribute
2 | 
3 | We highly welcome contributions! Please check out [contributing](https://github.com/assafelovic/gpt-researcher/blob/master/CONTRIBUTING.md) if you're interested.
4 | 
5 | Please check out our [roadmap](https://trello.com/b/3O7KBePw/gpt-researcher-roadmap) page and reach out to us via our [Discord community](https://discord.gg/QgZXvJAccX) if you're interested in joining our mission.


--------------------------------------------------------------------------------
/docs/docs/examples/examples.md:
--------------------------------------------------------------------------------
 1 | # Simple Run
 2 | 
 3 | ### Run PIP Package
 4 | ```python
 5 | from gpt_researcher import GPTResearcher
 6 | import asyncio
 7 | 
 8 | 
 9 | async def main():
10 |     """
11 |     This is a sample script that shows how to run a research report.
12 |     """
13 |     # Query
14 |     query = "What happened in the latest burning man floods?"
15 | 
16 |     # Report Type
17 |     report_type = "research_report"
18 | 
19 |     # Initialize the researcher
20 |     researcher = GPTResearcher(query=query, report_type=report_type, config_path=None)
21 |     # Conduct research on the given query
22 |     await researcher.conduct_research()
23 |     # Write the report
24 |     report = await researcher.write_report()
25 |     
26 |     return report
27 | 
28 | 
29 | if __name__ == "__main__":
30 |     asyncio.run(main())
31 | ```


--------------------------------------------------------------------------------
/docs/docs/examples/pip-run.ipynb:
--------------------------------------------------------------------------------
 1 | {
 2 |   "nbformat": 4,
 3 |   "nbformat_minor": 0,
 4 |   "metadata": {
 5 |     "colab": {
 6 |       "provenance": []
 7 |     },
 8 |     "kernelspec": {
 9 |       "name": "python3",
10 |       "display_name": "Python 3"
11 |     },
12 |     "language_info": {
13 |       "name": "python"
14 |     }
15 |   },
16 |   "cells": [
17 |     {
18 |       "cell_type": "code",
19 |       "execution_count": 1,
20 |       "metadata": {
21 |         "id": "byPgKYhAE6gn"
22 |       },
23 |       "outputs": [],
24 |       "source": [
25 |         "import os\n",
26 |         "os.environ['OPENAI_API_KEY'] = 'your_openai_api_key'\n",
27 |         "os.environ['TAVILY_API_KEY'] = 'your_tavily_api_key' # Get a free key here: https://app.tavily.com"
28 |       ]
29 |     },
30 |     {
31 |       "cell_type": "code",
32 |       "source": [
33 |         "!pip install -U gpt-researcher nest_asyncio"
34 |       ],
35 |       "metadata": {
36 |         "id": "-rXET3OZLxwH"
37 |       },
38 |       "execution_count": null,
39 |       "outputs": []
40 |     },
41 |     {
42 |       "cell_type": "code",
43 |       "source": [
44 |         "import nest_asyncio # required for notebooks\n",
45 |         "nest_asyncio.apply()\n",
46 |         "\n",
47 |         "from gpt_researcher import GPTResearcher\n",
48 |         "import asyncio\n",
49 |         "\n",
50 |         "async def get_report(query: str, report_type: str) -> str:\n",
51 |         "    researcher = GPTResearcher(query, report_type)\n",
52 |         "    research_result = await researcher.conduct_research()\n",
53 |         "    report = await researcher.write_report()\n",
54 |         "    \n",
55 |         "    # Get additional information\n",
56 |         "    research_context = researcher.get_research_context()\n",
57 |         "    research_costs = researcher.get_costs()\n",
58 |         "    research_images = researcher.get_research_images()\n",
59 |         "    research_sources = researcher.get_research_sources()\n",
60 |         "    \n",
61 |         "    return report, research_context, research_costs, research_images, research_sources\n",
62 |         "\n",
63 |         "if __name__ == \"__main__\":\n",
64 |         "    query = \"Should I invest in Nvidia?\"\n",
65 |         "    report_type = \"research_report\"\n",
66 |         "\n",
67 |         "    report, context, costs, images, sources = asyncio.run(get_report(query, report_type))\n",
68 |         "    \n",
69 |         "    print(\"Report:\")\n",
70 |         "    print(report)\n",
71 |         "    print(\"\\nResearch Costs:\")\n",
72 |         "    print(costs)\n",
73 |         "    print(\"\\nResearch Images:\")\n",
74 |         "    print(images)\n",
75 |         "    print(\"\\nResearch Sources:\")\n",
76 |         "    print(sources)"
77 |       ],
78 |       "metadata": {
79 |         "id": "KWZe2InrL0ji"
80 |       },
81 |       "execution_count": null,
82 |       "outputs": []
83 |     }
84 |   ]
85 | }


--------------------------------------------------------------------------------
/docs/docs/examples/sample_report.py:
--------------------------------------------------------------------------------
 1 | import nest_asyncio  # required for notebooks
 2 | 
 3 | nest_asyncio.apply()
 4 | 
 5 | from gpt_researcher import GPTResearcher
 6 | import asyncio
 7 | 
 8 | 
 9 | async def get_report(query: str, report_type: str):
10 |     researcher = GPTResearcher(query, report_type)
11 |     research_result = await researcher.conduct_research()
12 |     report = await researcher.write_report()
13 | 
14 |     # Get additional information
15 |     research_context = researcher.get_research_context()
16 |     research_costs = researcher.get_costs()
17 |     research_images = researcher.get_research_images()
18 |     research_sources = researcher.get_research_sources()
19 | 
20 |     return report, research_context, research_costs, research_images, research_sources
21 | 
22 | 
23 | if __name__ == "__main__":
24 |     query = "Should I invest in Nvidia?"
25 |     report_type = "research_report"
26 | 
27 |     report, context, costs, images, sources = asyncio.run(get_report(query, report_type))
28 | 
29 |     print("Report:")
30 |     print(report)
31 |     print("\nResearch Costs:")
32 |     print(costs)
33 |     print("\nResearch Images:")
34 |     print(images)
35 |     print("\nResearch Sources:")
36 |     print(sources)


--------------------------------------------------------------------------------
/docs/docs/examples/sample_sources_only.py:
--------------------------------------------------------------------------------
 1 | from gpt_researcher import GPTResearcher
 2 | import asyncio
 3 | 
 4 | 
 5 | async def get_report(query: str, report_source: str, sources: list) -> str:
 6 |     researcher = GPTResearcher(query=query, report_source=report_source, source_urls=sources)
 7 |     research_context = await researcher.conduct_research()
 8 |     return await researcher.write_report()
 9 | 
10 | if __name__ == "__main__":
11 |     query = "What are the biggest trends in AI lately?"
12 |     report_source = "static"
13 |     sources = [
14 |         "https://en.wikipedia.org/wiki/Artificial_intelligence",
15 |         "https://www.ibm.com/think/insights/artificial-intelligence-trends",
16 |         "https://www.forbes.com/advisor/business/ai-statistics"
17 |     ]
18 | 
19 |     report = asyncio.run(get_report(query=query, report_source=report_source, sources=sources))
20 |     print(report)
21 | 


--------------------------------------------------------------------------------
/docs/docs/faq.md:
--------------------------------------------------------------------------------
 1 | # FAQ
 2 | 
 3 | ### How do I get started?
 4 | It really depends on what you're aiming for. 
 5 | 
 6 | If you're looking to connect your AI application to the internet with Tavily tailored API, check out the [Tavily API](https://docs.tavily.com/docs/tavily-api/introductionn) documentation. 
 7 | If you're looking to build and deploy our open source autonomous research agent GPT Researcher, please see [GPT Researcher](/docs/gpt-researcher/getting-started/introduction) documentation.
 8 | You can also check out demos and examples for inspiration [here](/docs/examples/examples).
 9 | 
10 | ### What is GPT Researcher?
11 | 
12 | GPT Researcher is a popular open source autonomous research agent that takes care of the tedious task of research for you, by scraping, filtering and aggregating over 20+ web sources per a single research task.
13 | 
14 | GPT Researcher is built with best practices for leveraging LLMs (prompt engineering, RAG, chains, embeddings, etc), and is optimized for quick and efficient research. It is also fully customizable and can be tailored to your specific needs.
15 | 
16 | To learn more about GPT Researcher, check out the [documentation page](/docs/gpt-researcher/getting-started/introduction).
17 | 
18 | ### How much does each research run cost?
19 | 
20 | A research task using GPT Researcher costs around $0.01 per a single run (for GPT-4 usage). We're constantly optimizing LLM calls to reduce costs and improve performance. 
21 | 
22 | ### How do you ensure the report is factual and accurate?
23 | 
24 | we do our best to ensure that the information we provide is factual and accurate. We do this by using multiple sources, and by using proprietary AI to score and rank the most relevant and accurate information. We also use proprietary AI to filter out irrelevant information and sources.
25 | 
26 | Lastly, by using RAG and other techniques, we ensure that the information is relevant to the context of the research task, leading to more accurate generative AI content and reduced hallucinations.
27 | 
28 | ### What are your plans for the future?
29 | 
30 | We're constantly working on improving our products and services. We're currently working on improving our search API together with design partners, and adding more data sources to our search engine. We're also working on improving our research agent GPT Researcher, and adding more features to it while growing our amazing open source community.
31 | 
32 | If you're interested in our roadmap or looking to collaborate, check out our [roadmap page](https://trello.com/b/3O7KBePw/gpt-researcher-roadmap). 
33 | 
34 | Feel free to [contact us](mailto:assafelovic@gmail.com) if you have any further questions or suggestions!


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/context/filtering-by-domain.md:
--------------------------------------------------------------------------------
 1 | # Filtering by Domain
 2 | 
 3 | If you set Google as a Retriever, you can filter web results by site.
 4 | 
 5 | For example, set in the query param you pass the GPTResearcher class instance: `query="site:linkedin.com a python web developer to implement my custom gpt-researcher flow"` will limit the results to linkedin.com
 6 | 
 7 | > **Step 1** -  Set these environment variables with a .env file in the root folder
 8 | 
 9 | ```bash
10 | TAVILY_API_KEY=
11 | LANGCHAIN_TRACING_V2=true
12 | LANGCHAIN_API_KEY=
13 | OPENAI_API_KEY=
14 | DOC_PATH=./my-docs
15 | RETRIEVER=google
16 | GOOGLE_API_KEY=
17 | GOOGLE_CX_KEY=
18 | ```
19 | 
20 | > **Step 2** -  from the root project run:
21 | 
22 | docker-compose up -- build
23 | 
24 | > **Step 3** -  from the frontend input box in localhost:3000, you can append any google search filter (such as filtering by domain names)
25 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/docs/gpt-researcher/context/gptr-hybrid.png


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/context/local-docs.md:
--------------------------------------------------------------------------------
 1 | # Research on Local Documents
 2 | 
 3 | ## Just Local Docs
 4 | 
 5 | You can instruct the GPT Researcher to run research tasks based on your local documents. Currently supported file formats are: PDF, plain text, CSV, Excel, Markdown, PowerPoint, and Word documents.
 6 | 
 7 | Step 1: Add the env variable `DOC_PATH` pointing to the folder where your documents are located.
 8 | 
 9 | ```bash
10 | export DOC_PATH="./my-docs"
11 | ```
12 | 
13 | Step 2: 
14 |  - If you're running the frontend app on localhost:8000, simply select "My Documents" from the "Report Source" Dropdown Options.
15 |  - If you're running GPT Researcher with the [PIP package](https://docs.tavily.com/docs/gpt-researcher/gptr/pip-package), pass the `report_source` argument as "local" when you instantiate the `GPTResearcher` class [code sample here](https://docs.gptr.dev/docs/gpt-researcher/context/tailored-research).
16 | 
17 | ## Local Docs + Web (Hybrid)
18 | 
19 | ![GPT Researcher hybrid research](./gptr-hybrid.png)
20 | 
21 | Check out the blog post on [Hybrid Research](https://docs.gptr.dev/blog/gptr-hybrid) to learn more about how to combine local documents with web research.
22 | ```
23 | 


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/frontend/playing-with-webhooks.md:
--------------------------------------------------------------------------------
 1 | # Playing with Webhooks
 2 | 
 3 | The GPTR Frontend is powered by Webhooks streaming back from the Backend. This allows for real-time updates on the status of your research tasks, as well as the ability to interact with the Backend directly from the Frontend.
 4 | 
 5 | 
 6 | ## Inspecting Webhooks
 7 | 
 8 | When running reports via the frontend, you can inspect the websocket messages in the Network Tab.
 9 | 
10 | Here's how: 
11 | 
12 | ![image](https://github.com/user-attachments/assets/15fcb5a4-77ea-4b3b-87d7-55d4b6f80095)
13 | 
14 | 
15 | ### Am I polling the right URL?
16 | 
17 | If you're concerned that your frontend isn't hitting the right API Endpoint, you can check the URL in the Network Tab.
18 | 
19 | Click into the WS request & go to the "Headers" tab
20 | 
21 | ![image](https://github.com/user-attachments/assets/dbd58c1d-3506-411a-852b-e1b133b6f5c8)
22 | 
23 | For debugging, have a look at the <a href="https://github.com/assafelovic/gpt-researcher/blob/master/frontend/nextjs/helpers/getHost.ts">getHost function.</a>


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/getting-started/cli.md:
--------------------------------------------------------------------------------
 1 | # Run with CLI
 2 | 
 3 | This command-line interface (CLI) tool allows you to generate research reports using the GPTResearcher class. It provides an easy way to conduct research on various topics and generate different types of reports.
 4 | 
 5 | ## Installation
 6 | 
 7 | 1. Clone the repository:
 8 |    ```
 9 |    git clone https://github.com/yourusername/gpt-researcher.git
10 |    cd gpt-researcher
11 |    ```
12 | 
13 | 2. Install the required dependencies:
14 |    ```
15 |    pip install -r requirements.txt
16 |    ```
17 | 
18 | 3. Set up your environment variables:
19 |    Create a `.env` file in the project root and add your API keys or other necessary configurations.
20 | 
21 | ## Usage
22 | 
23 | The basic syntax for using the CLI is:
24 | 
25 | ```
26 | python cli.py "<query>" --report_type <report_type>
27 | ```
28 | 
29 | ### Arguments
30 | 
31 | - `query` (required): The research query you want to investigate.
32 | - `--report_type` (required): The type of report to generate. Options include:
33 |   - `research_report`: Summary - Short and fast (~2 min)
34 |   - `detailed_report`: Detailed - In depth and longer (~5 min)
35 |   - `resource_report`
36 |   - `outline_report`
37 |   - `custom_report`
38 |   - `subtopic_report`
39 | 
40 | ## Examples
41 | 
42 | 1. Generate a quick research report on climate change:
43 |    ```
44 |    python cli.py "What are the main causes of climate change?" --report_type research_report
45 |    ```
46 | 
47 | 2. Create a detailed report on artificial intelligence:
48 |    ```
49 |    python cli.py "The impact of artificial intelligence on job markets" --report_type detailed_report
50 |    ```
51 | 
52 | 3. Generate an outline report on renewable energy:
53 |    ```
54 |    python cli.py "Renewable energy sources and their potential" --report_type outline_report
55 |    ```
56 | 
57 | ## Output
58 | 
59 | The generated report will be saved as a Markdown file in the `outputs` directory. The filename will be a unique UUID.
60 | 
61 | ## Note
62 | 
63 | - The execution time may vary depending on the complexity of the query and the type of report requested.
64 | - Make sure you have the necessary API keys and permissions set up in your `.env` file for the tool to function correctly.


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/getting-started/getting-started-with-docker.md:
--------------------------------------------------------------------------------
 1 | # Docker: Quickstart
 2 | 
 3 | > **Step 1** - Install & Open Docker Desktop
 4 | 
 5 | Follow instructions at https://www.docker.com/products/docker-desktop/
 6 | 
 7 | 
 8 | > **Step 2** - [Follow this flow](https://www.youtube.com/watch?v=x1gKFt_6Us4)
 9 | 
10 | This mainly includes cloning the '.env.example' file, adding your API Keys to the cloned file and saving the file as '.env'
11 | 
12 | > **Step 3** - Within root, run with Docker.
13 | 
14 | ```bash
15 | docker-compose up --build
16 | ```
17 | 
18 | If that doesn't work, try running it without the dash:
19 | ```bash
20 | docker compose up --build
21 | ```
22 | 
23 | > **Step 4** - By default, if you haven't uncommented anything in your docker-compose file, this flow will start 2 processes:
24 |  - the Python server running on localhost:8000
25 |  - the React app running on localhost:3000
26 | 
27 | Visit localhost:3000 on any browser and enjoy researching!
28 | 
29 | 


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/gptr/automated-tests.md:
--------------------------------------------------------------------------------
 1 | # Automated Tests
 2 | 
 3 | ## Automated Testing with Github Actions
 4 | 
 5 | This repository contains the code for the automated testing of the GPT-Researcher Repo using Github Actions. 
 6 | 
 7 | The tests are triggered in a docker container which runs the tests via the `pytest` module.
 8 | 
 9 | ## Running the Tests
10 | 
11 | You can run the tests:
12 | 
13 | ### Via a docker command
14 | 
15 | ```bash
16 | docker-compose --profile test run --rm gpt-researcher-tests
17 | ```
18 | 
19 | ### Via a Github Action
20 | 
21 | ![image](https://github.com/user-attachments/assets/721fca20-01bb-4c10-9cf9-19d823bebbb0)
22 | 
23 | Attaching here the required settings & screenshots on the github repo level:
24 | 
25 | Step 1: Within the repo, press the "Settings" tab
26 | 
27 | Step 2: Create a new environment named "tests" (all lowercase)
28 | 
29 | Step 3: Click into the "tests" environment & add environment secrets of ```OPENAI_API_KEY``` & ```TAVILY_API_KEY```
30 | 
31 | Get the keys from here:
32 | 
33 | https://app.tavily.com/sign-in
34 | 
35 | https://platform.openai.com/api-keys
36 | 
37 | 
38 | ![Screen Shot 2024-07-28 at 9 00 19](https://github.com/user-attachments/assets/7cd341c6-d8d4-461f-ab5e-325abc9fe509)
39 | ![Screen Shot 2024-07-28 at 9 02 55](https://github.com/user-attachments/assets/a3744f01-06a6-4c9d-8aa0-1fc742d3e866)
40 | 
41 | If configured correctly, here's what the Github action should look like when opening a new PR or committing to an open PR:
42 | 
43 | ![Screen Shot 2024-07-28 at 8 57 02](https://github.com/user-attachments/assets/30dbc668-4e6a-4b3b-a02e-dc859fc9bd3d)


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/gptr/example.md:
--------------------------------------------------------------------------------
 1 | # Agent Example
 2 | 
 3 | If you're interested in using GPT Researcher as a standalone agent, you can easily import it into any existing Python project. Below, is an example of calling the agent to generate a research report:
 4 | 
 5 | ```python
 6 | from gpt_researcher import GPTResearcher
 7 | import asyncio
 8 | 
 9 | async def fetch_report(query):
10 |     """
11 |     Fetch a research report based on the provided query and report type.
12 |     """
13 |     researcher = GPTResearcher(query=query)
14 |     await researcher.conduct_research()
15 |     report = await researcher.write_report()
16 |     return report
17 | 
18 | async def generate_research_report(query):
19 |     """
20 |     This is a sample script that executes an async main function to run a research report.
21 |     """
22 |     report = await fetch_report(query)
23 |     print(report)
24 | 
25 | if __name__ == "__main__":
26 |     QUERY = "What happened in the latest burning man floods?"
27 |     asyncio.run(generate_research_report(query=QUERY))
28 | ```
29 | 
30 | You can further enhance this example to use the returned report as context for generating valuable content such as news article, marketing content, email templates, newsletters, etc.
31 | 
32 | You can also use GPT Researcher to gather information about code documentation, business analysis, financial information and more. All of which can be used to complete much more complex tasks that require factual and high quality realtime information.
33 | 


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/gptr/handling-logs-as-they-stream.md:
--------------------------------------------------------------------------------
 1 | # Handling Logs
 2 | 
 3 | Here is a snippet of code to help you handle the streaming logs of your Research tasks.
 4 | 
 5 | ```python
 6 | from typing import Dict, Any
 7 | import asyncio
 8 | from gpt_researcher import GPTResearcher
 9 | 
10 | class CustomLogsHandler:
11 |     """A custom Logs handler class to handle JSON data."""
12 |     def __init__(self):
13 |         self.logs = []  # Initialize logs to store data
14 | 
15 |     async def send_json(self, data: Dict[str, Any]) -> None:
16 |         """Send JSON data and log it."""
17 |         self.logs.append(data)  # Append data to logs
18 |         print(f"My custom Log: {data}")  # For demonstration, print the log
19 | 
20 | async def run():
21 |     # Define the necessary parameters with sample values
22 |     
23 |     query = "What happened in the latest burning man floods?"
24 |     report_type = "research_report"  # Type of report to generate
25 |     report_source = "online"  # Could specify source like 'online', 'books', etc.
26 |     tone = "informative"  # Tone of the report ('informative', 'casual', etc.)
27 |     config_path = None  # Path to a config file, if needed
28 |     
29 |     # Initialize researcher with a custom WebSocket
30 |     custom_logs_handler = CustomLogsHandler()
31 | 
32 |     researcher = GPTResearcher(
33 |         query=query,
34 |         report_type=report_type,
35 |         report_source=report_source,
36 |         tone=tone,
37 |         config_path=config_path,
38 |         websocket=custom_logs_handler
39 |     )
40 | 
41 |     await researcher.conduct_research()  # Conduct the research
42 |     report = await researcher.write_report()  # Write the research report
43 | 
44 |     return report
45 | 
46 | # Run the asynchronous function using asyncio
47 | if __name__ == "__main__":
48 |     asyncio.run(run())
49 | ```
50 | 
51 | The data from the research process will be logged and stored in the `CustomLogsHandler` instance. You can customize the logging behavior as needed for your application.
52 | 
53 | Here's a sample of the output:
54 | 
55 | ```
56 | {
57 |     "type": "logs",
58 |     "content": "added_source_url",
59 |     "output": "✅ Added source url to research: https://www.npr.org/2023/09/28/1202110410/how-rumors-and-conspiracy-theories-got-in-the-way-of-mauis-fire-recovery\n",
60 |     "metadata": "https://www.npr.org/2023/09/28/1202110410/how-rumors-and-conspiracy-theories-got-in-the-way-of-mauis-fire-recovery"
61 | }
62 | ```
63 | 
64 | The `metadata` field will include whatever metadata is relevant to the log entry. Let the script above run to completion for the full logs output of a given research task.


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/llms/testing-your-llm.md:
--------------------------------------------------------------------------------
 1 | # Testing your LLM
 2 | 
 3 | Here is a snippet of code to help you verify that your LLM-related environment variables are set up correctly.
 4 | 
 5 | ```python
 6 | from gpt_researcher.config.config import Config
 7 | from gpt_researcher.utils.llm import create_chat_completion
 8 | import asyncio
 9 | from dotenv import load_dotenv
10 | load_dotenv()
11 | 
12 | async def main():
13 |     cfg = Config()
14 | 
15 |     try:
16 |         report = await create_chat_completion(
17 |             model=cfg.smart_llm_model,
18 |             messages = [{"role": "user", "content": "sup?"}],
19 |             temperature=0.35,
20 |             llm_provider=cfg.smart_llm_provider,
21 |             stream=True,
22 |             max_tokens=cfg.smart_token_limit,
23 |             llm_kwargs=cfg.llm_kwargs
24 |         )
25 |     except Exception as e:
26 |         print(f"Error in calling LLM: {e}")
27 | 
28 | # Run the async function
29 | asyncio.run(main())
30 | ```


--------------------------------------------------------------------------------
/docs/docs/gpt-researcher/search-engines/test-your-retriever.md:
--------------------------------------------------------------------------------
 1 | # Testing your Retriever
 2 | 
 3 | To test your retriever, you can use the following code snippet. The script will search for a sub-query and display the search results.
 4 | 
 5 | ```python
 6 | import asyncio
 7 | from dotenv import load_dotenv
 8 | from gpt_researcher.config.config import Config
 9 | from gpt_researcher.actions.retriever import get_retrievers
10 | from gpt_researcher.skills.researcher import ResearchConductor
11 | import pprint
12 | # Load environment variables from .env file
13 | load_dotenv()
14 | 
15 | async def test_scrape_data_by_query():
16 |     # Initialize the Config object
17 |     config = Config()
18 | 
19 |     # Retrieve the retrievers based on the current configuration
20 |     retrievers = get_retrievers({}, config)
21 |     print("Retrievers:", retrievers)
22 | 
23 |     # Create a mock researcher object with necessary attributes
24 |     class MockResearcher:
25 |         def init(self):
26 |             self.retrievers = retrievers
27 |             self.cfg = config
28 |             self.verbose = True
29 |             self.websocket = None
30 |             self.scraper_manager = None  # Mock or implement scraper manager
31 |             self.vector_store = None  # Mock or implement vector store
32 | 
33 |     researcher = MockResearcher()
34 |     research_conductor = ResearchConductor(researcher)
35 |     # print('research_conductor',dir(research_conductor))
36 |     # print('MockResearcher',dir(researcher))
37 |     # Define a sub-query to test
38 |     sub_query = "design patterns for autonomous ai agents"
39 | 
40 |     # Iterate through all retrievers
41 |     for retriever_class in retrievers:
42 |         # Instantiate the retriever with the sub-query
43 |         retriever = retriever_class(sub_query)
44 | 
45 |         # Perform the search using the current retriever
46 |         search_results = await asyncio.to_thread(
47 |             retriever.search, max_results=10
48 |         )
49 | 
50 |         print("\033[35mSearch results:\033[0m")
51 |         pprint.pprint(search_results, indent=4, width=80)
52 | 
53 | if __name__ == "__main__":
54 |     asyncio.run(test_scrape_data_by_query())
55 | ```
56 | 
57 | The output of the search results will include the title, body, and href of each search result. For example:
58 |     
59 | ```json
60 | [{   
61 |     "body": "Jun 5, 2024 ... Three AI Design Patterns of Autonomous "
62 |                 "Agents. Overview of the Three Patterns. Three notable AI "
63 |                 "design patterns for autonomous agents include:.",
64 |     "href": "https://accredianpublication.medium.com/building-smarter-systems-the-role-of-agentic-design-patterns-in-genai-13617492f5df",
65 |     "title": "Building Smarter Systems: The Role of Agentic Design "
66 |                 "Patterns in ..."},
67 |     ...]
68 | ```


--------------------------------------------------------------------------------
/docs/docs/reference/config/config.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_label: config
  3 | title: config.config
  4 | ---
  5 | 
  6 | Configuration class to store the state of bools for different scripts access.
  7 | 
  8 | ## Config Objects
  9 | 
 10 | ```python
 11 | class Config(metaclass=Singleton)
 12 | ```
 13 | 
 14 | Configuration class to store the state of bools for different scripts access.
 15 | 
 16 | #### \_\_init\_\_
 17 | 
 18 | ```python
 19 | def __init__() -> None
 20 | ```
 21 | 
 22 | Initialize the Config class
 23 | 
 24 | #### set\_fast\_llm\_model
 25 | 
 26 | ```python
 27 | def set_fast_llm_model(value: str) -> None
 28 | ```
 29 | 
 30 | Set the fast LLM model value.
 31 | 
 32 | #### set\_smart\_llm\_model
 33 | 
 34 | ```python
 35 | def set_smart_llm_model(value: str) -> None
 36 | ```
 37 | 
 38 | Set the smart LLM model value.
 39 | 
 40 | #### set\_fast\_token\_limit
 41 | 
 42 | ```python
 43 | def set_fast_token_limit(value: int) -> None
 44 | ```
 45 | 
 46 | Set the fast token limit value.
 47 | 
 48 | #### set\_smart\_token\_limit
 49 | 
 50 | ```python
 51 | def set_smart_token_limit(value: int) -> None
 52 | ```
 53 | 
 54 | Set the smart token limit value.
 55 | 
 56 | #### set\_browse\_chunk\_max\_length
 57 | 
 58 | ```python
 59 | def set_browse_chunk_max_length(value: int) -> None
 60 | ```
 61 | 
 62 | Set the browse_website command chunk max length value.
 63 | 
 64 | #### set\_openai\_api\_key
 65 | 
 66 | ```python
 67 | def set_openai_api_key(value: str) -> None
 68 | ```
 69 | 
 70 | Set the OpenAI API key value.
 71 | 
 72 | #### set\_debug\_mode
 73 | 
 74 | ```python
 75 | def set_debug_mode(value: bool) -> None
 76 | ```
 77 | 
 78 | Set the debug mode value.
 79 | 
 80 | ## APIKeyError Objects
 81 | 
 82 | ```python
 83 | class APIKeyError(Exception)
 84 | ```
 85 | 
 86 | Exception raised when an API key is not set in config.py or as an environment variable.
 87 | 
 88 | #### check\_openai\_api\_key
 89 | 
 90 | ```python
 91 | def check_openai_api_key(cfg) -> None
 92 | ```
 93 | 
 94 | Check if the OpenAI API key is set in config.py or as an environment variable.
 95 | 
 96 | #### check\_tavily\_api\_key
 97 | 
 98 | ```python
 99 | def check_tavily_api_key(cfg) -> None
100 | ```
101 | 
102 | Check if the Tavily Search API key is set in config.py or as an environment variable.
103 | 
104 | #### check\_google\_api\_key
105 | 
106 | ```python
107 | def check_google_api_key(cfg) -> None
108 | ```
109 | 
110 | Check if the Google API key is set in config.py or as an environment variable.
111 | 
112 | #### check\_serp\_api\_key
113 | 
114 | ```python
115 | def check_serp_api_key(cfg) -> None
116 | ```
117 | 
118 | Check if the SERP API key is set in config.py or as an environment variable.
119 | 
120 | #### check\_searx\_url
121 | 
122 | ```python
123 | def check_searx_url(cfg) -> None
124 | ```
125 | 
126 | Check if the Searx URL is set in config.py or as an environment variable.
127 | 
128 | 


--------------------------------------------------------------------------------
/docs/docs/reference/config/singleton.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_label: singleton
 3 | title: config.singleton
 4 | ---
 5 | 
 6 | The singleton metaclass for ensuring only one instance of a class.
 7 | 
 8 | ## Singleton Objects
 9 | 
10 | ```python
11 | class Singleton(abc.ABCMeta, type)
12 | ```
13 | 
14 | Singleton metaclass for ensuring only one instance of a class.
15 | 
16 | #### \_\_call\_\_
17 | 
18 | ```python
19 | def __call__(cls, *args, **kwargs)
20 | ```
21 | 
22 | Call method for the singleton metaclass.
23 | 
24 | ## AbstractSingleton Objects
25 | 
26 | ```python
27 | class AbstractSingleton(abc.ABC, metaclass=Singleton)
28 | ```
29 | 
30 | Abstract singleton class for ensuring only one instance of a class.
31 | 
32 | 


--------------------------------------------------------------------------------
/docs/docs/reference/processing/html.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | sidebar_label: html
 3 | title: processing.html
 4 | ---
 5 | 
 6 | HTML processing functions
 7 | 
 8 | #### extract\_hyperlinks
 9 | 
10 | ```python
11 | def extract_hyperlinks(soup: BeautifulSoup,
12 |                        base_url: str) -> list[tuple[str, str]]
13 | ```
14 | 
15 | Extract hyperlinks from a BeautifulSoup object
16 | 
17 | **Arguments**:
18 | 
19 | - `soup` _BeautifulSoup_ - The BeautifulSoup object
20 | - `base_url` _str_ - The base URL
21 |   
22 | 
23 | **Returns**:
24 | 
25 |   List[Tuple[str, str]]: The extracted hyperlinks
26 | 
27 | #### format\_hyperlinks
28 | 
29 | ```python
30 | def format_hyperlinks(hyperlinks: list[tuple[str, str]]) -> list[str]
31 | ```
32 | 
33 | Format hyperlinks to be displayed to the user
34 | 
35 | **Arguments**:
36 | 
37 | - `hyperlinks` _List[Tuple[str, str]]_ - The hyperlinks to format
38 |   
39 | 
40 | **Returns**:
41 | 
42 | - `List[str]` - The formatted hyperlinks
43 | 
44 | 


--------------------------------------------------------------------------------
/docs/docs/reference/processing/text.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | sidebar_label: text
  3 | title: processing.text
  4 | ---
  5 | 
  6 | Text processing functions
  7 | 
  8 | #### split\_text
  9 | 
 10 | ```python
 11 | def split_text(text: str,
 12 |                max_length: int = 8192) -> Generator[str, None, None]
 13 | ```
 14 | 
 15 | Split text into chunks of a maximum length
 16 | 
 17 | **Arguments**:
 18 | 
 19 | - `text` _str_ - The text to split
 20 | - `max_length` _int, optional_ - The maximum length of each chunk. Defaults to 8192.
 21 |   
 22 | 
 23 | **Yields**:
 24 | 
 25 | - `str` - The next chunk of text
 26 |   
 27 | 
 28 | **Raises**:
 29 | 
 30 | - `ValueError` - If the text is longer than the maximum length
 31 | 
 32 | #### summarize\_text
 33 | 
 34 | ```python
 35 | def summarize_text(url: str,
 36 |                    text: str,
 37 |                    question: str,
 38 |                    driver: Optional[WebDriver] = None) -> str
 39 | ```
 40 | 
 41 | Summarize text using the OpenAI API
 42 | 
 43 | **Arguments**:
 44 | 
 45 | - `url` _str_ - The url of the text
 46 | - `text` _str_ - The text to summarize
 47 | - `question` _str_ - The question to ask the model
 48 | - `driver` _WebDriver_ - The webdriver to use to scroll the page
 49 |   
 50 | 
 51 | **Returns**:
 52 | 
 53 | - `str` - The summary of the text
 54 | 
 55 | #### scroll\_to\_percentage
 56 | 
 57 | ```python
 58 | def scroll_to_percentage(driver: WebDriver, ratio: float) -> None
 59 | ```
 60 | 
 61 | Scroll to a percentage of the page
 62 | 
 63 | **Arguments**:
 64 | 
 65 | - `driver` _WebDriver_ - The webdriver to use
 66 | - `ratio` _float_ - The percentage to scroll to
 67 |   
 68 | 
 69 | **Raises**:
 70 | 
 71 | - `ValueError` - If the ratio is not between 0 and 1
 72 | 
 73 | #### create\_message
 74 | 
 75 | ```python
 76 | def create_message(chunk: str, question: str) -> Dict[str, str]
 77 | ```
 78 | 
 79 | Create a message for the chat completion
 80 | 
 81 | **Arguments**:
 82 | 
 83 | - `chunk` _str_ - The chunk of text to summarize
 84 | - `question` _str_ - The question to answer
 85 |   
 86 | 
 87 | **Returns**:
 88 | 
 89 |   Dict[str, str]: The message to send to the chat completion
 90 | 
 91 | #### write\_to\_file
 92 | 
 93 | ```python
 94 | def write_to_file(filename: str, text: str) -> None
 95 | ```
 96 | 
 97 | Write text to a file
 98 | 
 99 | **Arguments**:
100 | 
101 | - `text` _str_ - The text to write
102 | - `filename` _str_ - The filename to write to
103 | 
104 | 


--------------------------------------------------------------------------------
/docs/docs/reference/sidebar.json:
--------------------------------------------------------------------------------
1 | {
2 |   "items": [],
3 |   "label": "Reference",
4 |   "type": "category"
5 | }


--------------------------------------------------------------------------------
/docs/docs/roadmap.md:
--------------------------------------------------------------------------------
1 | # Roadmap
2 | 
3 | We're constantly working on additional features and improvements to our products and services. We're also working on new products and services to help you build better AI applications using [GPT Researcher](https://gptr.dev).
4 | 
5 | Our vision is to build the #1 autonomous research agent for AI developers and researchers, and we're excited to have you join us on this journey!
6 | 
7 | The roadmap is prioritized based on the following goals: Performance, Quality, Modularity and Conversational flexibility. The roadmap is public and can be found [here](https://trello.com/b/3O7KBePw/gpt-researcher-roadmap). 
8 | 
9 | Interested in collaborating or contributing? Check out our [contributing page](/docs/contribute) for more information.


--------------------------------------------------------------------------------
/docs/docs/welcome.md:
--------------------------------------------------------------------------------
 1 | # Welcome
 2 | 
 3 | Hey there! 👋
 4 | 
 5 | We're a team of AI researchers and developers who are passionate about building the next generation of AI assistants. 
 6 | Our mission is to empower individuals and organizations with accurate, unbiased, and factual information.
 7 | 
 8 | ### GPT Researcher
 9 | Quickly accessing relevant and trustworthy information is more crucial than ever. However, we've learned that none of today's search engines provide a suitable tool that provides factual, explicit and objective answers without the need to continuously click and explore multiple sites for a given research task. 
10 | 
11 | This is why we've built the trending open source **[GPT Researcher](https://github.com/assafelovic/gpt-researcher)**. GPT Researcher is an autonomous agent that takes care of the tedious task of research for you, by scraping, filtering and aggregating over 20+ web sources per a single research task. 
12 | 
13 | To learn more about GPT Researcher, check out the [documentation page](/docs/gpt-researcher/getting-started/introduction).
14 | 


--------------------------------------------------------------------------------
/docs/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "website",
 3 |   "version": "0.0.0",
 4 |   "private": true,
 5 |   "resolutions" :{
 6 |     "nth-check":"2.0.1",
 7 |     "trim":"0.0.3",
 8 |     "got": "11.8.5",
 9 |     "node-forge": "1.3.0",
10 |     "minimatch": "3.0.5",
11 |     "loader-utils": "2.0.4",
12 |     "eta": "2.0.0",
13 |     "@sideway/formula": "3.0.1",
14 |     "http-cache-semantics": "4.1.1"
15 |    },
16 |   "scripts": {
17 |     "docusaurus": "docusaurus",
18 |     "start": "docusaurus start",
19 |     "build": "docusaurus build",
20 |     "swizzle": "docusaurus swizzle",
21 |     "deploy": "docusaurus deploy",
22 |     "clear": "docusaurus clear",
23 |     "serve": "docusaurus serve",
24 |     "write-translations": "docusaurus write-translations",
25 |     "write-heading-ids": "docusaurus write-heading-ids"
26 |   },
27 |   "dependencies": {
28 |     "@docusaurus/core": "0.0.0-4193",
29 |     "@docusaurus/preset-classic": "0.0.0-4193",
30 |     "@easyops-cn/docusaurus-search-local": "^0.21.1",
31 |     "@mdx-js/react": "^1.6.21",
32 |     "@svgr/webpack": "^5.5.0",
33 |     "clsx": "^1.1.1",
34 |     "file-loader": "^6.2.0",
35 |     "hast-util-is-element": "1.1.0",
36 |     "react": "^17.0.1",
37 |     "react-dom": "^17.0.1",
38 |     "rehype-katex": "4",
39 |     "remark-math": "3",
40 |     "trim": "^0.0.3",
41 |     "url-loader": "^4.1.1",
42 |     "minimatch": "3.0.5"
43 |   },
44 |   "browserslist": {
45 |     "production": [
46 |       ">0.5%",
47 |       "not dead",
48 |       "not op_mini all"
49 |     ],
50 |     "development": [
51 |       "last 1 chrome version",
52 |       "last 1 firefox version",
53 |       "last 1 safari version"
54 |     ]
55 |   }
56 | }
57 | 


--------------------------------------------------------------------------------
/docs/pydoc-markdown.yml:
--------------------------------------------------------------------------------
 1 | loaders:
 2 |    - type: python
 3 |      search_path: [../docs]
 4 | processors:
 5 |   - type: filter
 6 |     skip_empty_modules: true
 7 |   - type: smart
 8 |   - type: crossref
 9 | renderer:
10 |   type: docusaurus
11 |   docs_base_path: docs
12 |   relative_output_path: reference
13 |   relative_sidebar_path: sidebar.json
14 |   sidebar_top_level_label: Reference
15 |   markdown:
16 |     escape_html_in_docstring: false
17 | 


--------------------------------------------------------------------------------
/docs/src/components/HomepageFeatures.js:
--------------------------------------------------------------------------------
 1 | import React from 'react';
 2 | import clsx from 'clsx';
 3 | import { Link } from 'react-router-dom';
 4 | import styles from './HomepageFeatures.module.css';
 5 | 
 6 | const FeatureList = [
 7 |   {
 8 |     title: 'GPT Researcher',
 9 |     Svg: require('../../static/img/gptr-logo.png').default,
10 |     docLink: './docs/gpt-researcher/getting-started/getting-started',
11 |     description: (
12 |       <>
13 |         GPT Researcher is an open source autonomous agent designed for comprehensive online research on a variety of tasks.
14 |       </>
15 |     ),
16 |   },
17 |   /*{
18 |     title: 'Tavily Search API',
19 |     Svg: require('../../static/img/tavily.png').default,
20 |     docLink: './docs/tavily-api/introduction',
21 |     description: (
22 |       <>
23 |         Tavily Search API is a search engine optimized for LLMs, optimized for a factual, efficient, and persistent search experience
24 |       </>
25 |     ),
26 |   },*/
27 |   {
28 |     title: 'Multi-Agent Assistant',
29 |     Svg: require('../../static/img/multi-agent.png').default,
30 |     docLink: './docs/gpt-researcher/multi_agents/langgraph',
31 |     description: (
32 |       <>
33 |         Learn how a team of AI agents can work together to conduct research on a given topic, from planning to publication.
34 |       </>
35 |     ),
36 |   },
37 |   {
38 |     title: 'Examples and Demos',
39 |     Svg: require('../../static/img/examples.png').default,
40 |     docLink: './docs/examples/examples',
41 |     description: (
42 |       <>
43 |           Check out GPT Researcher in action across multiple frameworks and use cases such as hybrid research and long detailed reports.
44 |       </>
45 |     ),
46 |   },
47 | ];
48 | 
49 | function Feature({Svg, title, description, docLink}) {
50 |   return (
51 |     <div className={clsx('col col--4')}>
52 |       <div className="text--center">
53 |         {/*<Svg className={styles.featureSvg} alt={title} />*/}
54 |         <img src={Svg} alt={title} height="60"/>
55 |       </div>
56 |       <div className="text--center padding-horiz--md">
57 |         <Link to={docLink}>
58 |             <h3>{title}</h3>
59 |         </Link>
60 |         <p>{description}</p>
61 |       </div>
62 |     </div>
63 |   );
64 | }
65 | 
66 | export default function HomepageFeatures() {
67 |   return (
68 |     <section className={styles.features}>
69 |       <div className="container" style={{marginTop: 30}}>
70 |         <div className="row" style={{justifyContent: 'center'}}>
71 |           {FeatureList.map((props, idx) => (
72 |             <Feature key={idx} {...props} />
73 |           ))}
74 |         </div>
75 |       </div>
76 |     </section>
77 |   );
78 | }
79 | 


--------------------------------------------------------------------------------
/docs/src/components/HomepageFeatures.module.css:
--------------------------------------------------------------------------------
 1 | /* stylelint-disable docusaurus/copyright-header */
 2 | 
 3 | .features {
 4 |   display: flex;
 5 |   align-items: center;
 6 |   padding: 2rem 0;
 7 |   width: 100%;
 8 | }
 9 | 
10 | .featureSvg {
11 |   height: 120px;
12 |   width: 200px;
13 | }
14 | 


--------------------------------------------------------------------------------
/docs/src/pages/index.js:
--------------------------------------------------------------------------------
 1 | import React from 'react';
 2 | import clsx from 'clsx';
 3 | import Layout from '@theme/Layout';
 4 | import Link from '@docusaurus/Link';
 5 | import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
 6 | import styles from './index.module.css';
 7 | import HomepageFeatures from '../components/HomepageFeatures';
 8 | 
 9 | function HomepageHeader() {
10 |   const {siteConfig} = useDocusaurusContext();
11 |   return (
12 |     <header className={clsx('hero hero--primary', styles.heroBanner)} style={{backgroundImage: "linear-gradient(to right, #f472b6, #a78bfa, #22d3ee)"}}>
13 |       <div className="container">
14 |         <h1 className="hero__title">{siteConfig.title}</h1>
15 |         <p className="hero__subtitle">{siteConfig.tagline}</p>
16 |         <div className={styles.buttons}>
17 |           <Link
18 |             className="button button--secondary button--lg"
19 |             to="/docs/gpt-researcher/getting-started/getting-started">
20 |             Getting Started - 5 min ⏱️
21 |           </Link>
22 |         </div>
23 |       </div>
24 |     </header>
25 |   );
26 | }
27 | 
28 | export default function Home() {
29 |   const {siteConfig} = useDocusaurusContext();
30 |   return (
31 |     <Layout
32 |       title={`Documentation`}
33 |       description="GPT Researcher is the leading autonomous agent designed for comprehensive online research on a variety of tasks.">
34 |       <HomepageHeader />
35 |       <main>
36 |         <HomepageFeatures />
37 |       </main>
38 |     </Layout>
39 |   );
40 | }
41 | 


--------------------------------------------------------------------------------
/docs/src/pages/index.module.css:
--------------------------------------------------------------------------------
 1 | /* stylelint-disable docusaurus/copyright-header */
 2 | 
 3 | /**
 4 |  * CSS files with the .module.css suffix will be treated as CSS modules
 5 |  * and scoped locally.
 6 |  */
 7 | 
 8 | .heroBanner {
 9 |   padding: 5rem 0;
10 |   text-align: center;
11 |   position: relative;
12 |   overflow: hidden;
13 | }
14 | 
15 | @media screen and (max-width: 966px) {
16 |   .heroBanner {
17 |     padding: 2rem;
18 |   }
19 | }
20 | 
21 | .buttons {
22 |   display: flex;
23 |   align-items: center;
24 |   justify-content: center;
25 | }
26 | 


--------------------------------------------------------------------------------
/docs/static/.nojekyll:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/static/.nojekyll


--------------------------------------------------------------------------------
/docs/static/CNAME:
--------------------------------------------------------------------------------
1 | docs.gptr.dev


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/static/img/architecture.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/static/img/banner1.jpg


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/static/img/examples.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/static/img/gptr-logo.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/static/img/leaderboard.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/docs/static/img/multi-agent.png


--------------------------------------------------------------------------------
/frontend/README.md:
--------------------------------------------------------------------------------
 1 | # Frontend Application
 2 | 
 3 | This frontend project aims to enhance the user experience of GPT-Researcher, providing an intuitive and efficient interface for automated research. It offers two deployment options to suit different needs and environments.
 4 | 
 5 | ## Option 1: Static Frontend (FastAPI)
 6 | 
 7 | A lightweight solution using FastAPI to serve static files.
 8 | 
 9 | #### Prerequisites
10 | - Python 3.11+
11 | - pip
12 | 
13 | #### Setup and Running
14 | 
15 | 1. Install required packages:
16 |    ```
17 |    pip install -r requirements.txt
18 |    ```
19 | 
20 | 2. Start the server:
21 |    ```
22 |    python -m uvicorn main:app
23 |    ```
24 | 
25 | 3. Access at `http://localhost:8000`
26 | 
27 | #### Demo
28 | https://github.com/assafelovic/gpt-researcher/assets/13554167/dd6cf08f-b31e-40c6-9907-1915f52a7110
29 | 
30 | ## Option 2: NextJS Frontend
31 | 
32 | A more robust solution with enhanced features and performance.
33 | 
34 | #### Prerequisites
35 | - Node.js (v18.17.0 recommended)
36 | - npm
37 | 
38 | #### Setup and Running
39 | 
40 | 1. Navigate to NextJS directory:
41 |    ```
42 |    cd nextjs
43 |    ```
44 | 
45 | 2. Set up Node.js:
46 |    ```
47 |    nvm install 18.17.0
48 |    nvm use v18.17.0
49 |    ```
50 | 
51 | 3. Install dependencies:
52 |    ```
53 |    npm install --legacy-peer-deps
54 |    ```
55 | 
56 | 4. Start development server:
57 |    ```
58 |    npm run dev
59 |    ```
60 | 
61 | 5. Access at `http://localhost:3000`
62 | 
63 | Note: Requires backend server on `localhost:8000` as detailed in option 1.
64 | 
65 | #### Demo
66 | https://github.com/user-attachments/assets/092e9e71-7e27-475d-8c4f-9dddd28934a3
67 | 
68 | ## Choosing an Option
69 | 
70 | - Static Frontend: Quick setup, lightweight deployment.
71 | - NextJS Frontend: Feature-rich, scalable, better performance and SEO.
72 | 
73 | For production, NextJS is recommended.
74 | 
75 | ## Frontend Features
76 | 
77 | Our frontend enhances GPT-Researcher by providing:
78 | 
79 | 1. Intuitive Research Interface: Streamlined input for research queries.
80 | 2. Real-time Progress Tracking: Visual feedback on ongoing research tasks.
81 | 3. Interactive Results Display: Easy-to-navigate presentation of findings.
82 | 4. Customizable Settings: Adjust research parameters to suit specific needs.
83 | 5. Responsive Design: Optimal experience across various devices.
84 | 
85 | These features aim to make the research process more efficient and user-friendly, complementing GPT-Researcher's powerful agent capabilities.


--------------------------------------------------------------------------------
 1 | .git
 2 | 
 3 | # Ignore env containing secrets
 4 | .env
 5 | .venv
 6 | .envrc
 7 | 
 8 | # Ignore Virtual Env
 9 | env/
10 | venv/
11 | .venv/
12 | 
13 | # Other Environments
14 | ENV/
15 | env.bak/
16 | venv.bak/
17 | 
18 | # Ignore generated outputs
19 | outputs/
20 | 
21 | # Ignore my local docs
22 | my-docs/
23 | 
24 | # Ignore pycache
25 | **/__pycache__/
26 | 
27 | # Ignore mypy cache
28 | .mypy_cache/
29 | 
30 | # Node modules
31 | node_modules
32 | 
33 | # Ignore IDE config
34 | .idea
35 | 
36 | # macOS specific files
37 | .DS_Store
38 | 
39 | # Docusaurus build artifacts
40 | .docusaurus
41 | 
42 | # Build directories
43 | build
44 | docs/build
45 | 
46 | # Language graph data
47 | .langgraph-data/
48 | 
49 | # Next.js build artifacts
50 | .next/
51 | 
52 | # Package lock file
53 | package-lock.json
54 | 
55 | # Docker-specific exclusions (if any)
56 | Dockerfile
57 | docker-compose.yml
58 | 


--------------------------------------------------------------------------------
/frontend/nextjs/.eslintrc.json:
--------------------------------------------------------------------------------
1 | {
2 |   "extends": "next/core-web-vitals"
3 | }
4 | 


--------------------------------------------------------------------------------
/frontend/nextjs/.example.env:
--------------------------------------------------------------------------------
1 | TOGETHER_API_KEY=
2 | BING_API_KEY=
3 | HELICONE_API_KEY=
4 | 


--------------------------------------------------------------------------------
/frontend/nextjs/.gitignore:
--------------------------------------------------------------------------------
 1 | # See https://help.github.com/articles/ignoring-files/ for more about ignoring files.
 2 | .env
 3 | package-lock.json
 4 | 
 5 | # dependencies
 6 | /node_modules
 7 | /.pnp
 8 | .pnp.js
 9 | .yarn/install-state.gz
10 | 
11 | # testing
12 | /coverage
13 | 
14 | # next.js
15 | /.next/
16 | /out/
17 | 
18 | # production
19 | /build
20 | 
21 | # misc
22 | .DS_Store
23 | *.pem
24 | 
25 | # debug
26 | npm-debug.log*
27 | yarn-debug.log*
28 | yarn-error.log*
29 | 
30 | # local env files
31 | .env*.local
32 | 
33 | # vercel
34 | .vercel
35 | 
36 | # typescript
37 | *.tsbuildinfo
38 | next-env.d.ts
39 | 


--------------------------------------------------------------------------------
/frontend/nextjs/.prettierrc:
--------------------------------------------------------------------------------
1 | { "plugins": ["prettier-plugin-tailwindcss"] }
2 | 


--------------------------------------------------------------------------------
/frontend/nextjs/Dockerfile:
--------------------------------------------------------------------------------
 1 | FROM node:18.17.0-alpine as builder
 2 | WORKDIR /app
 3 | COPY ./package.json ./
 4 | RUN npm install --legacy-peer-deps
 5 | COPY . .
 6 | RUN npm run build
 7 | 
 8 | FROM nginx
 9 | EXPOSE 3000
10 | COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
11 | COPY --from=builder /app/build /usr/share/nginx/html
12 | 


--------------------------------------------------------------------------------
/frontend/nextjs/Dockerfile.dev:
--------------------------------------------------------------------------------
1 | FROM node:18.17.0-alpine
2 | WORKDIR /app
3 | COPY ./package.json ./
4 | RUN npm install --legacy-peer-deps
5 | COPY . .
6 | CMD ["npm", "run", "dev"]


--------------------------------------------------------------------------------
/frontend/nextjs/README.md:
--------------------------------------------------------------------------------
1 | ## Cloning & running
2 | 
3 | 1. Create a `.env` (use the `.example.env` for reference) and replace the API keys
4 | 2. Run `npm install --legacy-peer-deps` and `npm run dev` to install dependencies and run locally
5 | 


--------------------------------------------------------------------------------
/frontend/nextjs/actions/apiActions.ts:
--------------------------------------------------------------------------------
  1 | import { createParser, ParsedEvent, ReconnectInterval } from "eventsource-parser";
  2 | 
  3 | export async function handleSourcesAndAnswer(question: string) {
  4 |   let sourcesResponse = await fetch("/api/getSources", {
  5 |     method: "POST",
  6 |     body: JSON.stringify({ question }),
  7 |   });
  8 |   let sources = await sourcesResponse.json();
  9 | 
 10 |   const response = await fetch("/api/getAnswer", {
 11 |     method: "POST",
 12 |     headers: {
 13 |       "Content-Type": "application/json",
 14 |     },
 15 |     body: JSON.stringify({ question, sources }),
 16 |   });
 17 | 
 18 |   if (!response.ok) {
 19 |     throw new Error(response.statusText);
 20 |   }
 21 | 
 22 |   if (response.status === 202) {
 23 |     const fullAnswer = await response.text();
 24 |     return fullAnswer;
 25 |   }
 26 | 
 27 |   // This data is a ReadableStream
 28 |   const data = response.body;
 29 |   if (!data) {
 30 |     return;
 31 |   }
 32 | 
 33 |   const onParse = (event: ParsedEvent | ReconnectInterval) => {
 34 |     if (event.type === "event") {
 35 |       const data = event.data;
 36 |       try {
 37 |         const text = JSON.parse(data).text ?? "";
 38 |         return text;
 39 |       } catch (e) {
 40 |         console.error(e);
 41 |       }
 42 |     }
 43 |   };
 44 | 
 45 |   // https://web.dev/streams/#the-getreader-and-read-methods
 46 |   const reader = data.getReader();
 47 |   const decoder = new TextDecoder();
 48 |   const parser = createParser(onParse);
 49 |   let done = false;
 50 |   while (!done) {
 51 |     const { value, done: doneReading } = await reader.read();
 52 |     done = doneReading;
 53 |     const chunkValue = decoder.decode(value);
 54 |     parser.feed(chunkValue);
 55 |   }
 56 | }
 57 | 
 58 | export async function handleSimilarQuestions(question: string) {
 59 |   let res = await fetch("/api/getSimilarQuestions", {
 60 |     method: "POST",
 61 |     body: JSON.stringify({ question }),
 62 |   });
 63 |   let questions = await res.json();
 64 |   return questions;
 65 | }
 66 | 
 67 | export async function handleLanggraphAnswer(question: string) {
 68 |   const response = await fetch("/api/generateLanggraph", {
 69 |     method: "POST",
 70 |     headers: {
 71 |       "Content-Type": "application/json",
 72 |     },
 73 |     body: JSON.stringify({ question }),
 74 |   });
 75 | 
 76 |   if (!response.ok) {
 77 |     throw new Error(response.statusText);
 78 |   }
 79 | 
 80 |   // This data is a ReadableStream
 81 |   const data = response.body;
 82 |   if (!data) {
 83 |     return;
 84 |   }
 85 | 
 86 |   const onParse = (event: ParsedEvent | ReconnectInterval) => {
 87 |     if (event.type === "event") {
 88 |       const data = event.data;
 89 |       try {
 90 |         const text = JSON.parse(data).text ?? "";
 91 |         return text;
 92 |       } catch (e) {
 93 |         console.error(e);
 94 |       }
 95 |     }
 96 |   };
 97 | 
 98 |   const reader = data.getReader();
 99 |   const decoder = new TextDecoder();
100 |   const parser = createParser(onParse);
101 |   let done = false;
102 |   while (!done) {
103 |     const { value, done: doneReading } = await reader.read();
104 |     done = doneReading;
105 |     const chunkValue = decoder.decode(value);
106 |     parser.feed(chunkValue);
107 |   }
108 | }


--------------------------------------------------------------------------------
/frontend/nextjs/app/globals.css:
--------------------------------------------------------------------------------
  1 | @tailwind base;
  2 | @tailwind components;
  3 | @tailwind utilities;
  4 | 
  5 | @keyframes gradientBG {
  6 |   0% {background-position: 0% 50%;}
  7 |   50% {background-position: 100% 50%;}
  8 |   100% {background-position: 0% 50%;}
  9 | }
 10 | 
 11 | html {
 12 |   scroll-behavior: smooth;
 13 | }
 14 | 
 15 | textarea {
 16 |   max-height: 300px; /* Set an appropriate max height */
 17 |   overflow-y: auto;  /* Enable internal scrolling */
 18 |   /* transition: height 0.2s ease-in-out; */
 19 | }
 20 | 
 21 | .log-message {
 22 |   word-wrap: break-word; /* For handling long URLs or text */
 23 |   overflow-wrap: break-word; /* For handling overflow in modern browsers */
 24 |   overflow-x: hidden; /* Hide horizontal overflow */
 25 |   word-break: break-word; /* Break long words if needed */
 26 | }
 27 | 
 28 | body {
 29 |   font-family: 'Montserrat', sans-serif;
 30 |   line-height: 1.6;
 31 |   background-size: 200% 200%;
 32 |   background-image: linear-gradient(170deg, #151A2D, #036f73, #151A2D);
 33 |   /*animation: gradientBG 10s ease infinite;*/
 34 | }
 35 | 
 36 | .landing {
 37 |   display: flex;
 38 |   justify-content: center;
 39 |   align-items: center;
 40 |   height: 30vh;
 41 |   text-align: center;
 42 |   color: white;
 43 | }
 44 | 
 45 | .landing h1 {
 46 |   font-size: 3.5rem;
 47 |   font-weight: 700;
 48 |   margin-bottom: 2rem;
 49 | }
 50 | 
 51 | @layer utilities {
 52 |   .text-balance {
 53 |     text-wrap: balance;
 54 |   }
 55 |   /* Hide scrollbar for Chrome, Safari and Opera */
 56 |   .no-scrollbar::-webkit-scrollbar {
 57 |     display: none;
 58 |   }
 59 |   /* Hide scrollbar for IE, Edge and Firefox */
 60 |   .no-scrollbar {
 61 |     -ms-overflow-style: none; /* IE and Edge */
 62 |     scrollbar-width: none; /* Firefox */
 63 |   }
 64 |   .loader {
 65 |     text-align: left;
 66 |     display: flex;
 67 |     gap: 3px;
 68 |   }
 69 | 
 70 |   .loader span {
 71 |     display: inline-block;
 72 |     vertical-align: middle;
 73 |     width: 7px;
 74 |     height: 7px;
 75 |     /* background: #4b4b4b; */
 76 |     background: white;
 77 |     border-radius: 50%;
 78 |     animation: loader 0.6s infinite alternate;
 79 |   }
 80 | 
 81 |   .loader span:nth-of-type(2) {
 82 |     animation-delay: 0.2s;
 83 |   }
 84 | 
 85 |   .loader span:nth-of-type(3) {
 86 |     animation-delay: 0.6s;
 87 |   }
 88 | 
 89 |   @keyframes loader {
 90 |     0% {
 91 |       opacity: 1;
 92 |       transform: scale(0.6);
 93 |     }
 94 | 
 95 |     100% {
 96 |       opacity: 0.3;
 97 |       transform: scale(1);
 98 |     }
 99 |   }
100 | }
101 | 
102 | body {
103 |   margin: 0px !important;
104 | }
105 | 
106 | /* Add these styles for the scrollbar */
107 | .scrollbar-thin {
108 |   scrollbar-width: thin;
109 | }
110 | 
111 | .scrollbar-thumb-gray-600::-webkit-scrollbar-thumb {
112 |   background-color: #4B5563;
113 |   border-radius: 6px;
114 | }
115 | 
116 | .scrollbar-track-gray-300::-webkit-scrollbar-track {
117 |   background-color: #D1D5DB;
118 | }
119 | 
120 | .scrollbar-thin::-webkit-scrollbar {
121 |   width: 6px;
122 | }
123 | 


--------------------------------------------------------------------------------
/frontend/nextjs/app/layout.tsx:
--------------------------------------------------------------------------------
 1 | import type { Metadata } from "next";
 2 | import { Lexend } from "next/font/google";
 3 | import PlausibleProvider from "next-plausible";
 4 | import "./globals.css";
 5 | 
 6 | const inter = Lexend({ subsets: ["latin"] });
 7 | 
 8 | let title = "GPT Researcher";
 9 | let description =
10 |   "A research assistant vanquishing hallucinations";
11 | let url = "https://github.com/assafelovic/gpt-researcher";
12 | let ogimage = "/favicon.ico";
13 | let sitename = "GPT Researcher";
14 | 
15 | export const metadata: Metadata = {
16 |   metadataBase: new URL(url),
17 |   title,
18 |   description,
19 |   icons: {
20 |     icon: "/favicon.ico",
21 |   },
22 |   openGraph: {
23 |     images: [ogimage],
24 |     title,
25 |     description,
26 |     url: url,
27 |     siteName: sitename,
28 |     locale: "en_US",
29 |     type: "website",
30 |   },
31 |   twitter: {
32 |     card: "summary_large_image",
33 |     images: [ogimage],
34 |     title,
35 |     description,
36 |   },
37 | };
38 | 
39 | export default function RootLayout({
40 |   children,
41 | }: Readonly<{
42 |   children: React.ReactNode;
43 | }>) {
44 |   return (
45 |     <html lang="en">
46 |       <head>
47 |         <PlausibleProvider domain="localhost:3000" />
48 |       </head>
49 |       <body
50 |         className={`${inter.className} flex min-h-screen flex-col justify-between`}
51 |       >
52 |         {children}
53 |       </body>
54 |     </html>
55 |   );
56 | }
57 | 


--------------------------------------------------------------------------------
/frontend/nextjs/components/Footer.tsx:
--------------------------------------------------------------------------------
/frontend/nextjs/components/Header.tsx:
--------------------------------------------------------------------------------
 1 | import Image from "next/image";
 2 | 
 3 | interface HeaderProps {
 4 |   loading?: boolean;      // Indicates if research is currently in progress
 5 |   isStopped?: boolean;    // Indicates if research was manually stopped
 6 |   showResult?: boolean;   // Controls if research results are being displayed
 7 |   onStop?: () => void;    // Handler for stopping ongoing research
 8 |   onNewResearch?: () => void;  // Handler for starting fresh research
 9 | }
10 | 
11 | const Header = ({ loading, isStopped, showResult, onStop, onNewResearch }: HeaderProps) => {
12 |   return (
13 |     <div className="fixed top-0 left-0 right-0 z-50">
14 |       {/* Original gradient background with blur effect */}
15 |       <div className="absolute inset-0 backdrop-blur-sm bg-gradient-to-b to-transparent"></div>
16 |       
17 |       {/* Header container */}
18 |       <div className="container relative h-[60px] px-4 lg:h-[80px] lg:px-0 pt-4 pb-4">
19 |         <div className="flex flex-col items-center">
20 |           {/* Logo/Home link */}
21 |           <a href="/">
22 |             <Image
23 |               src="/img/gptr-logo.png"
24 |               alt="logo"
25 |               width={60}
26 |               height={60}
27 |               className="lg:h-16 lg:w-16"
28 |             />
29 |           </a>
30 |           
31 |           {/* Action buttons container */}
32 |           <div className="flex gap-2 mt-2 transition-all duration-300 ease-in-out">
33 |             {/* Stop button - shown only during active research */}
34 |             {loading && !isStopped && (
35 |               <button
36 |                 onClick={onStop}
37 |                 className="flex items-center justify-center px-6 h-8 text-sm text-white bg-red-500 rounded-full hover:bg-red-600 transform hover:scale-105 transition-all duration-200 shadow-lg whitespace-nowrap"
38 |               >
39 |                 Stop
40 |               </button>
41 |             )}
42 |             {/* New Research button - shown after stopping or completing research */}
43 |             {(isStopped || !loading) && showResult && (
44 |               <button
45 |                 onClick={onNewResearch}
46 |                 className="flex items-center justify-center px-6 h-8 text-sm text-white bg-[rgb(168,85,247)] rounded-full hover:bg-[rgb(147,51,234)] transform hover:scale-105 transition-all duration-200 shadow-lg whitespace-nowrap"
47 |               >
48 |                 New Research
49 |               </button>
50 |             )}
51 |           </div>
52 |         </div>
53 |       </div>
54 |     </div>
55 |   );
56 | };
57 | 
58 | export default Header;
59 | 


--------------------------------------------------------------------------------
/frontend/nextjs/components/HumanFeedback.tsx:
--------------------------------------------------------------------------------
 1 | // /multi_agents/frontend/components/HumanFeedback.tsx
 2 | 
 3 | import React, { useState, useEffect } from 'react';
 4 | 
 5 | interface HumanFeedbackProps {
 6 |   websocket: WebSocket | null;
 7 |   onFeedbackSubmit: (feedback: string | null) => void;
 8 |   questionForHuman: boolean;
 9 | }
10 | 
11 | const HumanFeedback: React.FC<HumanFeedbackProps> = ({ questionForHuman, websocket, onFeedbackSubmit }) => {
12 |   const [feedbackRequest, setFeedbackRequest] = useState<string | null>(null);
13 |   const [userFeedback, setUserFeedback] = useState<string>('');
14 | 
15 |   const handleSubmit = (e: React.FormEvent) => {
16 |     e.preventDefault();
17 |     onFeedbackSubmit(userFeedback === '' ? null : userFeedback);
18 |     setFeedbackRequest(null);
19 |     setUserFeedback('');
20 |   };
21 | 
22 |   return (
23 |     <div className="bg-gray-100 p-4 rounded-lg shadow-md">
24 |       <h3 className="text-lg font-semibold mb-2">Human Feedback Required</h3>
25 |       <p className="mb-4">{questionForHuman}</p>
26 |       <form onSubmit={handleSubmit}>
27 |         <textarea
28 |           className="w-full p-2 border rounded-md"
29 |           value={userFeedback}
30 |           onChange={(e) => setUserFeedback(e.target.value)}
31 |           placeholder="Enter your feedback here (or leave blank for 'no')"
32 |         />
33 |         <button
34 |           type="submit"
35 |           className="mt-2 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
36 |         >
37 |           Submit Feedback
38 |         </button>
39 |       </form>
40 |     </div>
41 |   );
42 | };
43 | 
44 | export default HumanFeedback;


--------------------------------------------------------------------------------
/frontend/nextjs/components/Images/ImageModal.jsx:
--------------------------------------------------------------------------------
/frontend/nextjs/components/Langgraph/Langgraph.js:
--------------------------------------------------------------------------------
 1 | import { Client } from "@langchain/langgraph-sdk";
 2 | import { task } from '../../config/task';
 3 | 
 4 | export async function startLanggraphResearch(newQuestion, report_source, langgraphHostUrl) {
 5 |     // Update the task query with the new question
 6 |     task.task.query = newQuestion;
 7 |     task.task.source = report_source;
 8 |     const host = langgraphHostUrl;
 9 |     
10 |     // Add your Langgraph Cloud Authentication token here
11 |     const authToken = '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';
12 | 
13 |     const client = new Client({
14 |         apiUrl: host,
15 |         defaultHeaders: {
16 |             'Content-Type': 'application/json',
17 |             'X-Api-Key': authToken
18 |         }
19 |     });
20 |   
21 |     // List all assistants
22 |     const assistants = await client.assistants.search({
23 |       metadata: null,
24 |       offset: 0,
25 |       limit: 10,
26 |     });
27 |   
28 |     console.log('assistants: ', assistants);
29 |   
30 |     // We auto-create an assistant for each graph you register in config.
31 |     const agent = assistants[0];
32 |   
33 |     // Start a new thread
34 |     const thread = await client.threads.create();
35 |   
36 |     // Start a streaming run
37 |     const input = task;
38 |   
39 |     const streamResponse = client.runs.stream(
40 |       thread["thread_id"],
41 |       agent["assistant_id"],
42 |       {
43 |         input,
44 |       },
45 |     );
46 | 
47 |     return {streamResponse, host, thread_id: thread["thread_id"]};
48 | }


--------------------------------------------------------------------------------
/frontend/nextjs/components/LoadingDots.tsx:
--------------------------------------------------------------------------------
 1 | const LoadingDots = () => {
 2 |   return (
 3 |     <div className="flex justify-center py-4">
 4 |       <div className="animate-pulse flex space-x-2">
 5 |         <div className="w-2 h-2 bg-gray-300 rounded-full"></div>
 6 |         <div className="w-2 h-2 bg-gray-300 rounded-full"></div>
 7 |         <div className="w-2 h-2 bg-gray-300 rounded-full"></div>
 8 |       </div>
 9 |     </div>
10 |   );
11 | };
12 | 
13 | export default LoadingDots; 


--------------------------------------------------------------------------------
/frontend/nextjs/components/ResearchBlocks/AccessReport.tsx:
--------------------------------------------------------------------------------
 1 | import React from 'react';
 2 | import {getHost} from '../../helpers/getHost'
 3 | 
 4 | interface AccessReportProps {
 5 |   accessData: {
 6 |     pdf?: string;
 7 |     docx?: string;
 8 |     json?: string;
 9 |   };
10 |   chatBoxSettings: {
11 |     report_type?: string;
12 |   };
13 |   report: string;
14 | }
15 | 
16 | const AccessReport: React.FC<AccessReportProps> = ({ accessData, chatBoxSettings, report }) => {
17 |   const host = getHost();
18 | 
19 |   const getReportLink = (dataType: 'pdf' | 'docx' | 'json'): string => {
20 |     // Early return if path is not available
21 |     if (!accessData?.[dataType]) {
22 |       console.warn(`No ${dataType} path provided`);
23 |       return '#';
24 |     }
25 | 
26 |     const path = accessData[dataType] as string;
27 |     
28 |     // Clean the path - remove leading/trailing slashes and handle outputs/ prefix
29 |     const cleanPath = path
30 |       .trim()
31 |       .replace(/^\/+|\/+$/g, ''); // Remove leading/trailing slashes
32 |     
33 |     // Only prepend outputs/ if it's not already there
34 |     const finalPath = cleanPath.startsWith('outputs/') 
35 |       ? cleanPath 
36 |       : `outputs/${cleanPath}`;
37 |     
38 |     return `${host}/${finalPath}`;
39 |   };
40 | 
41 |   // Safety check for accessData
42 |   if (!accessData || typeof accessData !== 'object') {
43 |     return null;
44 |   }
45 | 
46 |   return (
47 |     <div className="flex justify-center mt-4">
48 |       <a 
49 |         href={getReportLink('pdf')} 
50 |         className="bg-purple-500 text-white active:bg-purple-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
51 |         target="_blank"
52 |         rel="noopener noreferrer">
53 |         View as PDF
54 |       </a>
55 |       <a 
56 |         href={getReportLink('docx')} 
57 |         className="bg-purple-500 text-white active:bg-purple-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
58 |         target="_blank"
59 |         rel="noopener noreferrer">
60 |         Download DocX
61 |       </a>
62 |       {chatBoxSettings?.report_type === 'research_report' && (
63 |         <a
64 |           href={getReportLink('json')}
65 |           className="bg-purple-500 text-white active:bg-purple-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
66 |           target="_blank"
67 |           rel="noopener noreferrer">
68 |           Download Logs
69 |         </a>
70 |       )}
71 |     </div>
72 |   );
73 | };
74 | 
75 | export default AccessReport;


--------------------------------------------------------------------------------
/frontend/nextjs/components/ResearchBlocks/ImageSection.tsx:
--------------------------------------------------------------------------------
 1 | import Image from "next/image";
 2 | import ImagesAlbum from '../Images/ImagesAlbum';
 3 | 
 4 | interface ImageSectionProps {
 5 |   metadata: any;
 6 | }
 7 | 
 8 | const ImageSection = ({ metadata }: ImageSectionProps) => {
 9 |   return (
10 |     <div className="container h-auto w-full shrink-0 rounded-lg border border-solid border-[#C2C2C2] bg-gray-800 shadow-md p-5">
11 |       <div className="flex items-start gap-4 pb-3 lg:pb-3.5">
12 |         <Image src="/img/image.svg" alt="images" width={24} height={24} />
13 |         <h3 className="text-base font-bold uppercase leading-[152.5%] text-white">
14 |           Related Images
15 |         </h3>
16 |       </div>
17 |       <div className="overflow-y-auto max-h-[500px] scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-gray-300">
18 |         <ImagesAlbum images={metadata} />
19 |       </div>
20 |     </div>
21 |   );
22 | };
23 | 
24 | export default ImageSection; 


--------------------------------------------------------------------------------
/frontend/nextjs/components/ResearchBlocks/LogsSection.tsx:
--------------------------------------------------------------------------------
 1 | import Image from "next/image";
 2 | import LogMessage from './elements/LogMessage';
 3 | import { useEffect, useRef } from 'react';
 4 | 
 5 | interface Log {
 6 |   header: string;
 7 |   text: string;
 8 |   metadata: any;
 9 |   key: string;
10 | }
11 | 
12 | interface OrderedLogsProps {
13 |   logs: Log[];
14 | }
15 | 
16 | const LogsSection = ({ logs }: OrderedLogsProps) => {
17 |   const logsContainerRef = useRef<HTMLDivElement>(null);
18 | 
19 |   useEffect(() => {
20 |     // Scroll to bottom whenever logs change
21 |     if (logsContainerRef.current) {
22 |       logsContainerRef.current.scrollTop = logsContainerRef.current.scrollHeight;
23 |     }
24 |   }, [logs]); // Dependency on logs array ensures this runs when new logs are added
25 | 
26 |   return (
27 |     <div className="container h-auto w-full shrink-0 rounded-lg border border-solid border-[#C2C2C2] bg-gray-800 shadow-md p-5">
28 |       <div className="flex items-start gap-4 pb-3 lg:pb-3.5">
29 |         <Image src="/img/chat-check.svg" alt="logs" width={24} height={24} />
30 |         <h3 className="text-base font-bold uppercase leading-[152.5%] text-white">
31 |           Agent Work
32 |         </h3>
33 |       </div>
34 |       <div 
35 |         ref={logsContainerRef}
36 |         className="overflow-y-auto min-h-[200px] max-h-[500px] scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-gray-300"
37 |       >
38 |         <LogMessage logs={logs} />
39 |       </div>
40 |     </div>
41 |   );
42 | };
43 | 
44 | export default LogsSection; 


--------------------------------------------------------------------------------
/frontend/nextjs/components/ResearchBlocks/Question.tsx:
--------------------------------------------------------------------------------
 1 | import Image from "next/image";
 2 | 
 3 | interface QuestionProps {
 4 |   question: string;
 5 | }
 6 | 
 7 | const Question: React.FC<QuestionProps> = ({ question }) => {
 8 |   return (
 9 |     <div className="container w-full flex flex-col sm:flex-row items-start gap-3 pt-2 mb-2">
10 |       <div className="flex items-center gap-2 sm:gap-4">
11 |         <Image
12 |           src={"/img/message-question-circle.svg"}
13 |           alt="message"
14 |           width={24}
15 |           height={24}
16 |           className="w-6 h-6"
17 |         />
18 |         <p className="font-bold uppercase leading-[152%] text-white">
19 |           Research Task:
20 |         </p><br/>
21 |       </div>
22 |       <div className="grow text-white break-words max-w-full log-message">&quot;{question}&quot;</div>
23 |     </div>
24 |   );
25 | };
26 | 
27 | export default Question;
28 | 


--------------------------------------------------------------------------------
/frontend/nextjs/components/ResearchBlocks/Sources.tsx:
--------------------------------------------------------------------------------
 1 | import Image from "next/image";
 2 | import SourceCard from "./elements/SourceCard";
 3 | 
 4 | export default function Sources({
 5 |   sources,
 6 | }: {
 7 |   sources: { name: string; url: string }[];
 8 | }) {
 9 |   return (
10 |     <div className="container h-auto w-full shrink-0 rounded-lg border border-solid border-[#C2C2C2] bg-gray-800 shadow-md p-5">
11 |       <div className="flex items-start gap-4 pb-3 lg:pb-3.5">
12 |         <Image src="/img/browser.svg" alt="footer" width={24} height={24} />
13 |         <h3 className="text-base font-bold uppercase leading-[152.5%] text-white">
14 |           sources{" "}
15 |         </h3>
16 |       </div>
17 |       <div className="overflow-y-auto max-h-[250px] scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-gray-300">
18 |         <div className="flex w-full max-w-[890px] flex-wrap content-center items-center gap-[15px] pb-2">
19 |           {sources.length > 0 ? (
20 |             sources.map((source) => (
21 |               <SourceCard source={source} key={source.url} />
22 |             ))
23 |           ) : (
24 |             <>
25 |               <div className="h-20 w-[260px] max-w-sm animate-pulse rounded-md bg-gray-300" />
26 |               <div className="h-20 w-[260px] max-w-sm animate-pulse rounded-md bg-gray-300" />
27 |               <div className="h-20 w-[260px] max-w-sm animate-pulse rounded-md bg-gray-300" />
28 |               <div className="h-20 w-[260px] max-w-sm animate-pulse rounded-md bg-gray-300" />
29 |               <div className="h-20 w-[260px] max-w-sm animate-pulse rounded-md bg-gray-300" />
30 |               <div className="h-20 w-[260px] max-w-sm animate-pulse rounded-md bg-gray-300" />
31 |             </>
32 |           )}
33 |         </div>
34 |       </div>
35 |     </div>
36 |   );
37 | }
38 | 


--------------------------------------------------------------------------------
/frontend/nextjs/components/ResearchBlocks/elements/SourceCard.tsx:
--------------------------------------------------------------------------------
 1 | import Image from "next/image";
 2 | import { useState } from "react";
 3 | 
 4 | const SourceCard = ({ source }: { source: { name: string; url: string } }) => {
 5 |   const [imageSrc, setImageSrc] = useState(`https://www.google.com/s2/favicons?domain=${source.url}&sz=128`);
 6 | 
 7 |   const handleImageError = () => {
 8 |     setImageSrc("/img/globe.svg");
 9 |   };
10 | 
11 |   return (
12 |     <div className="flex h-[79px] w-full items-center gap-2.5 rounded border border-solid border-[#C1C1C1] bg-neutral-50 px-1.5 py-1 md:w-auto">
13 |       <div className="">
14 |         <Image
15 |           src={imageSrc}
16 |           alt={source.url}
17 |           className="p-1"
18 |           width={44}
19 |           height={44}
20 |           onError={handleImageError}  // Update src on error
21 |         />
22 |       </div>
23 |       <div className="flex max-w-[192px] flex-col justify-center gap-[7px]">
24 |         <h6 className="line-clamp-2 text-sm font-light leading-[normal] text-[#1B1B16]">
25 |           {source.name}
26 |         </h6>
27 |         <a
28 |           target="_blank"
29 |           rel="noopener noreferrer"
30 |           href={source.url}
31 |           className="truncate text-sm font-light text-[#1B1B16]/30"
32 |         >
33 |           {source.url}
34 |         </a>
35 |       </div>
36 |     </div>
37 |   );
38 | };
39 | 
40 | export default SourceCard;
41 | 


--------------------------------------------------------------------------------
/frontend/nextjs/components/ResearchBlocks/elements/SubQuestions.tsx:
--------------------------------------------------------------------------------
 1 | import Image from "next/image";
 2 | 
 3 | interface SubQuestionsProps {
 4 |   metadata: string[];
 5 |   handleClickSuggestion: (value: string) => void;
 6 | }
 7 | 
 8 | const SubQuestions: React.FC<SubQuestionsProps> = ({ metadata, handleClickSuggestion }) => {
 9 |   return (
10 |     <div className="container flex w-full items-start gap-3 pt-5 pb-2">
11 |       <div className="flex w-fit items-center gap-4">
12 |         <Image
13 |           src={"/img/thinking.svg"}
14 |           alt="thinking"
15 |           width={30}
16 |           height={30}
17 |           className="size-[24px]"
18 |         />
19 |       </div>
20 |       <div className="grow text-white">
21 |         <p className="pr-5 font-bold leading-[152%] text-white pb-[20px]">
22 |           Pondering your question from several angles
23 |         </p>
24 |         <div className="flex flex-row flex-wrap items-center gap-2.5 pb-[20px]">
25 |           {metadata.map((item, subIndex) => (
26 |             <div
27 |               className="flex cursor-pointer items-center justify-center gap-[5px] rounded-full border border-solid border-[#C1C1C1] bg-[#EDEDEA] px-2.5 py-2"
28 |               onClick={() => handleClickSuggestion(item)}
29 |               key={`${item}-${subIndex}`}
30 |             >
31 |               <span className="text-sm font-light leading-[normal] text-[#1B1B16]">
32 |                 {item}
33 |               </span>
34 |             </div>
35 |           ))}
36 |         </div>
37 |       </div>
38 |     </div>
39 |   );
40 | };
41 | 
42 | export default SubQuestions;


--------------------------------------------------------------------------------
/frontend/nextjs/components/Settings/ChatBox.tsx:
--------------------------------------------------------------------------------
 1 | import React, { useState, useEffect } from 'react';
 2 | import ResearchForm from '../Task/ResearchForm';
 3 | import Report from '../Task/Report';
 4 | import AgentLogs from '../Task/AgentLogs';
 5 | import AccessReport from '../ResearchBlocks/AccessReport';
 6 | 
 7 | interface ChatBoxSettings {
 8 |   report_source: string;
 9 |   report_type: string;
10 |   tone: string;
11 | }
12 | 
13 | interface ChatBoxProps {
14 |   chatBoxSettings: ChatBoxSettings;
15 |   setChatBoxSettings: React.Dispatch<React.SetStateAction<ChatBoxSettings>>;
16 | }
17 | 
18 | interface OutputData {
19 |   pdf?: string;
20 |   docx?: string;
21 |   json?: string;
22 | }
23 | 
24 | interface WebSocketMessage {
25 |   type: 'logs' | 'report' | 'path';
26 |   output: string | OutputData;
27 | }
28 | 
29 | export default function ChatBox({ chatBoxSettings, setChatBoxSettings }: ChatBoxProps) {
30 | 
31 |   const [agentLogs, setAgentLogs] = useState<any[]>([]);
32 |   const [report, setReport] = useState("");
33 |   const [accessData, setAccessData] = useState({});
34 |   const [socket, setSocket] = useState<WebSocket | null>(null);
35 | 
36 |   useEffect(() => {
37 |     if (typeof window !== 'undefined') {
38 |       const { protocol, pathname } = window.location;
39 |       let { host } = window.location;
40 |       host = host.includes('localhost') ? 'localhost:8000' : host;
41 |       const ws_uri = `${protocol === 'https:' ? 'wss:' : 'ws:'}//${host}${pathname}ws`;
42 |       const newSocket = new WebSocket(ws_uri);
43 |       setSocket(newSocket);
44 | 
45 |       newSocket.onmessage = (event) => {
46 |         const data = JSON.parse(event.data) as WebSocketMessage;
47 |         
48 |         if (data.type === 'logs') {
49 |           setAgentLogs((prevLogs: any[]) => [...prevLogs, data]);
50 |         } else if (data.type === 'report') {
51 |           setReport((prevReport: string) => prevReport + (data.output as string));
52 |         } else if (data.type === 'path') {
53 |           const output = data.output as OutputData;
54 |           setAccessData({
55 |             ...(output.pdf && { pdf: `outputs/${output.pdf}` }),
56 |             ...(output.docx && { docx: `outputs/${output.docx}` }),
57 |             ...(output.json && { json: `outputs/${output.json}` })
58 |           });
59 |         }
60 |       };
61 | 
62 |       return () => {
63 |         newSocket.close();
64 |       };
65 |     }
66 |   }, []);
67 | 
68 |   return (
69 |     <div>
70 |       <main className="container" id="form">
71 |         <ResearchForm 
72 |           chatBoxSettings={chatBoxSettings} 
73 |           setChatBoxSettings={setChatBoxSettings}
74 |         />
75 | 
76 |         {agentLogs?.length > 0 ? <AgentLogs agentLogs={agentLogs} /> : ''}
77 |         <div className="margin-div">
78 |           {report ? <Report report={report} /> : ''}
79 |           {Object.keys(accessData).length > 0 && 
80 |             <AccessReport 
81 |               accessData={accessData} 
82 |               chatBoxSettings={chatBoxSettings} 
83 |               report={report}
84 |             />
85 |           }
86 |         </div>
87 |       </main>
88 |     </div>
89 |   );
90 | }


--------------------------------------------------------------------------------
/frontend/nextjs/components/Settings/ToneSelector.tsx:
--------------------------------------------------------------------------------
 1 | import React, { ChangeEvent } from 'react';
 2 | 
 3 | interface ToneSelectorProps {
 4 |   tone: string;
 5 |   onToneChange: (event: ChangeEvent<HTMLSelectElement>) => void;
 6 | }
 7 | export default function ToneSelector({ tone, onToneChange }: ToneSelectorProps) {
 8 |   return (
 9 |     <div className="form-group">
10 |       <label htmlFor="tone" className="agent_question">Tone </label>
11 |       <select name="tone" id="tone" value={tone} onChange={onToneChange} className="form-control" required>
12 |         <option value="Objective">Objective - Impartial and unbiased presentation of facts and findings</option>
13 |         <option value="Formal">Formal - Adheres to academic standards with sophisticated language and structure</option>
14 |         <option value="Analytical">Analytical - Critical evaluation and detailed examination of data and theories</option>
15 |         <option value="Persuasive">Persuasive - Convincing the audience of a particular viewpoint or argument</option>
16 |         <option value="Informative">Informative - Providing clear and comprehensive information on a topic</option>
17 |         <option value="Explanatory">Explanatory - Clarifying complex concepts and processes</option>
18 |         <option value="Descriptive">Descriptive - Detailed depiction of phenomena, experiments, or case studies</option>
19 |         <option value="Critical">Critical - Judging the validity and relevance of the research and its conclusions</option>
20 |         <option value="Comparative">Comparative - Juxtaposing different theories, data, or methods to highlight differences and similarities</option>
21 |         <option value="Speculative">Speculative - Exploring hypotheses and potential implications or future research directions</option>
22 |         <option value="Reflective">Reflective - Considering the research process and personal insights or experiences</option>
23 |         <option value="Narrative">Narrative - Telling a story to illustrate research findings or methodologies</option>
24 |         <option value="Humorous">Humorous - Light-hearted and engaging, usually to make the content more relatable</option>
25 |         <option value="Optimistic">Optimistic - Highlighting positive findings and potential benefits</option>
26 |         <option value="Pessimistic">Pessimistic - Focusing on limitations, challenges, or negative outcomes</option>
27 |       </select>
28 |     </div>
29 |   );
30 | }


--------------------------------------------------------------------------------
/frontend/nextjs/components/SimilarTopics.tsx:
--------------------------------------------------------------------------------
 1 | import Image from "next/image";
 2 | 
 3 | const SimilarTopics = ({
 4 |   similarQuestions,
 5 |   handleDisplayResult,
 6 |   reset,
 7 | }: {
 8 |   similarQuestions: string[];
 9 |   handleDisplayResult: (item: string) => void;
10 |   reset: () => void;
11 | }) => {
12 |   return (
13 |     <div className="container flex h-auto w-full shrink-0 gap-4 rounded-lg border border-solid border-[#C2C2C2] bg-white p-5 lg:p-10">
14 |       <div className="hidden lg:block">
15 |         <Image
16 |           src="/img/similarTopics.svg"
17 |           alt="footer"
18 |           width={24}
19 |           height={24}
20 |         />
21 |       </div>
22 |       <div className="flex-1 divide-y divide-[#E5E5E5]">
23 |         <div className="flex gap-4 pb-3">
24 |           <Image
25 |             src="/img/similarTopics.svg"
26 |             alt="footer"
27 |             width={24}
28 |             height={24}
29 |             className="block lg:hidden"
30 |           />
31 |           <h3 className="text-base font-bold uppercase text-black">
32 |             Similar topics:{" "}
33 |           </h3>
34 |         </div>
35 | 
36 |         <div className="max-w-[890px] space-y-[15px] divide-y divide-[#E5E5E5]">
37 |           {similarQuestions.length > 0 ? (
38 |             similarQuestions.map((item) => (
39 |               <button
40 |                 className="flex cursor-pointer items-center gap-4 pt-3.5"
41 |                 key={item}
42 |                 onClick={() => {
43 |                   reset();
44 |                   handleDisplayResult(item);
45 |                 }}
46 |               >
47 |                 <div className="flex items-center">
48 |                   <Image
49 |                     src="/img/arrow-circle-up-right.svg"
50 |                     alt="footer"
51 |                     width={24}
52 |                     height={24}
53 |                   />
54 |                 </div>
55 |                 <p className="text-sm font-light leading-[normal] text-[#1B1B16] [leading-trim:both] [text-edge:cap]">
56 |                   {item}
57 |                 </p>
58 |               </button>
59 |             ))
60 |           ) : (
61 |             <>
62 |               <div className="h-10 w-full animate-pulse rounded-md bg-gray-300" />
63 |               <div className="h-10 w-full animate-pulse rounded-md bg-gray-300" />
64 |               <div className="h-10 w-full animate-pulse rounded-md bg-gray-300" />
65 |             </>
66 |           )}
67 |         </div>
68 |       </div>
69 |     </div>
70 |   );
71 | };
72 | 
73 | export default SimilarTopics;
74 | 


--------------------------------------------------------------------------------
/frontend/nextjs/components/Task/AgentLogs.tsx:
--------------------------------------------------------------------------------
 1 | export default function AgentLogs({agentLogs}:any){  
 2 |   const renderAgentLogs = (agentLogs:any)=>{
 3 |     return agentLogs && agentLogs.map((agentLog:any, index:number)=>{
 4 |       return (<div key={index}>{agentLog.output}</div>)
 5 |     })
 6 |   }
 7 | 
 8 |   return (
 9 |     <div className="margin-div">
10 |         <h2>Agent Output</h2>
11 |         <div id="output">
12 |           {renderAgentLogs(agentLogs)}
13 |         </div>
14 |     </div>
15 |   );
16 | }


--------------------------------------------------------------------------------
/frontend/nextjs/components/Task/Report.tsx:
--------------------------------------------------------------------------------
 1 | import React from 'react';
 2 | 
 3 | export default function Report({report}:any) {
 4 | 
 5 |     return (
 6 |         <div>
 7 |             <h2>Research Report</h2>
 8 |             <div id="reportContainer">
 9 |                 {/* <MarkdownView
10 |                     markdown={report}
11 |                     options={{ tables: true, emoji: true }}
12 |                 /> */}
13 |             </div>
14 |         </div>
15 |     );
16 | };


--------------------------------------------------------------------------------
/frontend/nextjs/components/TypeAnimation.tsx:
--------------------------------------------------------------------------------
 1 | const TypeAnimation = () => {
 2 |   return (
 3 |     <div className="loader pb-1">
 4 |       <span></span>
 5 |       <span></span>
 6 |       <span></span>
 7 |     </div>
 8 |   );
 9 | };
10 | 
11 | export default TypeAnimation;
12 | 


--------------------------------------------------------------------------------
/frontend/nextjs/config/task.ts:
--------------------------------------------------------------------------------
 1 | export const task = {
 2 |   "task": {
 3 |     "query": "Is AI in a hype cycle?",
 4 |     "include_human_feedback": false,
 5 |     "model": "gpt-4o",
 6 |     "max_sections": 3,
 7 |     "publish_formats": {
 8 |       "markdown": true,
 9 |       "pdf": true,
10 |       "docx": true
11 |     },
12 |     "source": "web",
13 |     "follow_guidelines": true,
14 |     "guidelines": [
15 |       "The report MUST fully answer the original question",
16 |       "The report MUST be written in apa format",
17 |       "The report MUST be written in english"
18 |     ],
19 |     "verbose": true
20 |   },
21 |   "initial_research": "Initial research data here",
22 |   "sections": ["Section 1", "Section 2"],
23 |   "research_data": "Research data here",
24 |   "title": "Research Title",
25 |   "headers": {
26 |     "introduction": "Introduction header",
27 |     "table_of_contents": "Table of Contents header",
28 |     "conclusion": "Conclusion header",
29 |     "sources": "Sources header"
30 |   },
31 |   "date": "2023-10-01",
32 |   "table_of_contents": "- Introduction\n- Section 1\n- Section 2\n- Conclusion",
33 |   "introduction": "Introduction content here",
34 |   "conclusion": "Conclusion content here",
35 |   "sources": ["Source 1", "Source 2"],
36 |   "report": "Full report content here"
37 | }


--------------------------------------------------------------------------------
/frontend/nextjs/helpers/findDifferences.ts:
--------------------------------------------------------------------------------
 1 | type Value = string | number | boolean | null | undefined | object | Value[]; // Possible value types
 2 | type Changes = { [key: string]: { before: Value; after: Value } | Changes }; // Recursive changes type
 3 | 
 4 | function findDifferences<T extends Record<string, any>>(obj1: T, obj2: T): Changes {
 5 |     // Helper function to check if a value is an object (excluding arrays)
 6 |     function isObject(obj: any): obj is Record<string, any> {
 7 |         return obj && typeof obj === 'object' && !Array.isArray(obj);
 8 |     }
 9 | 
10 |     // Recursive function to compare two objects and return the differences
11 |     function compareObjects(o1: Record<string, any>, o2: Record<string, any>): Changes {
12 |         const changes: Changes = {};
13 | 
14 |         // Iterate over keys in the first object (o1)
15 |         for (const key in o1) {
16 |             if (isObject(o1[key]) && isObject(o2[key])) {
17 |                 // Recursively compare nested objects
18 |                 const nestedChanges = compareObjects(o1[key], o2[key]);
19 |                 if (Object.keys(nestedChanges).length > 0) {
20 |                     changes[key] = nestedChanges; // Add nested changes if any
21 |                 }
22 |             } else if (Array.isArray(o1[key]) && Array.isArray(o2[key])) {
23 |                 // Compare arrays
24 |                 if (o1[key].length !== o2[key].length || o1[key].some((val, index) => val !== o2[key][index])) {
25 |                     changes[key] = { before: o1[key], after: o2[key] };
26 |                 }
27 |             } else {
28 |                 // Compare primitive values (or any non-object, non-array values)
29 |                 if (o1[key] !== o2[key]) {
30 |                     changes[key] = { before: o1[key], after: o2[key] };
31 |                 }
32 |             }
33 |         }
34 | 
35 |         // Iterate over keys in the second object (o2) to detect new keys
36 |         for (const key in o2) {
37 |             if (!(key in o1)) {
38 |                 changes[key] = { before: undefined, after: o2[key] };
39 |             }
40 |         }
41 | 
42 |         return changes; // Return the collected changes
43 |     }
44 | 
45 |     return compareObjects(obj1, obj2); // Compare the two input objects
46 | }
47 | 
48 | export default findDifferences;


--------------------------------------------------------------------------------
/frontend/nextjs/helpers/getHost.ts:
--------------------------------------------------------------------------------
 1 | interface GetHostParams {
 2 |   purpose?: string;
 3 | }
 4 | 
 5 | export const getHost = ({ purpose }: GetHostParams = {}): string => {
 6 |   if (typeof window !== 'undefined') {
 7 |     let { host } = window.location;
 8 |     if (purpose === 'langgraph-gui') {
 9 |       return host.includes('localhost') ? 'http%3A%2F%2F127.0.0.1%3A8123' : `https://${host}`;
10 |     } else {
11 |       return host.includes('localhost') ? 'http://localhost:8000' : `https://${host}`;
12 |     }
13 |   }
14 |   return '';
15 | };


--------------------------------------------------------------------------------
/frontend/nextjs/next.config.mjs:
--------------------------------------------------------------------------------
 1 | /** @type {import('next').NextConfig} */
 2 | const nextConfig = {
 3 |   images: {
 4 |     remotePatterns: [
 5 |       {
 6 |         hostname: 'www.google.com',
 7 |       },
 8 |     ],
 9 |   },
10 | };
11 | 
12 | export default nextConfig;
13 | 


--------------------------------------------------------------------------------
/frontend/nextjs/nginx/default.conf:
--------------------------------------------------------------------------------
1 | server{
2 |     listen 3000;
3 | 
4 |     location / {
5 |         root /usr/share/nginx/html;
6 |         index index.html index.htm;
7 |         try_files $uri $uri/ /index.html;
8 |     }
9 | }


--------------------------------------------------------------------------------
/frontend/nextjs/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "gpt-researcher",
 3 |   "version": "0.1.0",
 4 |   "private": true,
 5 |   "scripts": {
 6 |     "dev": "next dev",
 7 |     "build": "next build",
 8 |     "start": "next start",
 9 |     "lint": "next lint"
10 |   },
11 |   "dependencies": {
12 |     "@chakra-ui/react": "^2.4.9",
13 |     "@emotion/react": "^11.10.5",
14 |     "@emotion/styled": "^11.10.5",
15 |     "@langchain/langgraph-sdk": "^0.0.1-rc.12",
16 |     "@mozilla/readability": "^0.5.0",
17 |     "@testing-library/jest-dom": "^5.16.5",
18 |     "@testing-library/react": "^13.4.0",
19 |     "@testing-library/user-event": "^13.5.0",
20 |     "axios": "^1.3.2",
21 |     "eventsource-parser": "^1.1.2",
22 |     "framer-motion": "^9.0.2",
23 |     "jsdom": "^24.1.0",
24 |     "next": "14.2.3",
25 |     "next-plausible": "^3.12.0",
26 |     "react": "^18",
27 |     "react-dom": "^18",
28 |     "react-dropzone": "^14.2.3",
29 |     "react-hot-toast": "^2.4.1",
30 |     "react-scripts": "5.0.1",
31 |     "remark": "^15.0.1",
32 |     "remark-html": "^16.0.1",
33 |     "remark-parse": "^11.0.0",
34 |     "together-ai": "^0.6.0-alpha.3",
35 |     "web-vitals": "^2.1.4",
36 |     "zod": "^3.0.0",
37 |     "zod-to-json-schema": "^3.23.0"
38 |   },
39 |   "devDependencies": {
40 |     "@types/jsdom": "^21.1.6",
41 |     "@types/node": "^20",
42 |     "@types/react": "^18",
43 |     "@types/react-dom": "^18",
44 |     "eslint": "^8",
45 |     "eslint-config-next": "14.2.3",
46 |     "postcss": "^8",
47 |     "prettier": "^3.2.5",
48 |     "prettier-plugin-tailwindcss": "^0.6.0",
49 |     "tailwindcss": "^3.4.1",
50 |     "typescript": "^5"
51 |   }
52 | }
53 | 


--------------------------------------------------------------------------------
/frontend/nextjs/postcss.config.mjs:
--------------------------------------------------------------------------------
1 | /** @type {import('postcss-load-config').Config} */
2 | const config = {
3 |   plugins: {
4 |     tailwindcss: {},
5 |   },
6 | };
7 | 
8 | export default config;
9 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/favicon.ico


--------------------------------------------------------------------------------
 1 | <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
 2 | <g id="Info" clip-path="url(#clip0_14_6243)">
 3 | <path id="Vector" d="M12 0C15.1826 0 18.2348 1.26428 20.4853 3.51472C22.7357 5.76516 24 8.8174 24 12C24 15.1826 22.7357 18.2348 20.4853 20.4853C18.2348 22.7357 15.1826 24 12 24C8.8174 24 5.76516 22.7357 3.51472 20.4853C1.26428 18.2348 0 15.1826 0 12C0 8.8174 1.26428 5.76516 3.51472 3.51472C5.76516 1.26428 8.8174 0 12 0ZM14.25 11.25H9.75V19.5H14.25V11.25ZM12 4.5C11.4033 4.5 10.831 4.73705 10.409 5.15901C9.98705 5.58097 9.75 6.15326 9.75 6.75C9.75 7.34674 9.98705 7.91903 10.409 8.34099C10.831 8.76295 11.4033 9 12 9C12.5967 9 13.169 8.76295 13.591 8.34099C14.0129 7.91903 14.25 7.34674 14.25 6.75C14.25 6.15326 14.0129 5.58097 13.591 5.15901C13.169 4.73705 12.5967 4.5 12 4.5Z" fill="url(#paint0_linear_14_6243)"/>
 4 | </g>
 5 | <defs>
 6 | <linearGradient id="paint0_linear_14_6243" x1="0.827587" y1="-2.27913e-07" x2="15.7188" y2="25.3405" gradientUnits="userSpaceOnUse">
 7 | <stop stop-color="#1B1B16"/>
 8 | <stop offset="1" stop-color="#565646"/>
 9 | </linearGradient>
10 | <clipPath id="clip0_14_6243">
11 | <rect width="24" height="24" fill="white"/>
12 | </clipPath>
13 | </defs>
14 | </svg>
15 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/img/agents/academicResearchAgentAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/img/agents/businessAnalystAgentAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/img/agents/computerSecurityanalystAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/img/agents/defaultAgentAvatar.JPG


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/img/agents/financeAgentAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/img/agents/mathAgentAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/img/agents/travelAgentAvatar.png


--------------------------------------------------------------------------------
1 |  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <g id="arrow-circle-up-right">
3 | <path id="Icon" d="M16.5 14.5L16.5005 7.5M16.5005 7.5H9.5M16.5005 7.5L7.50049 16.4998" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
4 | </g>
5 | </svg>
6 | 


--------------------------------------------------------------------------------
1 | <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <g id="arrow-narrow-right">
3 | <path id="Icon" d="M4 12H20M20 12L14 6M20 12L14 18" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
4 | </g>
5 | </svg>
6 | 


--------------------------------------------------------------------------------
1 | <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
2 | <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
3 | <svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
4 | <g id="SVGRepo_bgCarrier" stroke-width="0"/>
5 | <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
6 | <g id="SVGRepo_iconCarrier"> <path d="M14 19C17.7712 19 19.6569 19 20.8284 17.8284C22 16.6569 22 14.7712 22 11C22 7.22876 22 5.34315 20.8284 4.17157C19.6569 3 17.7712 3 14 3H10C6.22876 3 4.34315 3 3.17157 4.17157C2 5.34315 2 7.22876 2 11C2 14.7712 2 16.6569 3.17157 17.8284C3.82475 18.4816 4.69989 18.7706 6 18.8985" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> <path d="M9 11L11.25 13L15 9" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> <path d="M14 19C12.7635 19 11.4022 19.4992 10.1586 20.145C8.16119 21.1821 7.16249 21.7007 6.67035 21.3703C6.1782 21.0398 6.27135 20.0151 6.45766 17.9657L6.5 17.5" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/> </g>
7 | </svg>


--------------------------------------------------------------------------------
1 | <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
2 | <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
3 | <svg fill="#ffffff" width="800px" height="800px" viewBox="0 0 24 24" role="img" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff">
4 | <g id="SVGRepo_bgCarrier" stroke-width="0"/>
5 | <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
6 | <g id="SVGRepo_iconCarrier">
7 | <path d="M22.365 8.729c.9 0 1.635-.735 1.635-1.635s-.735-1.636-1.635-1.636-1.636.735-1.636 1.636.723 1.635 1.636 1.635m-4.907 5.452a3.27 3.27 0 1 0 0-6.542 3.27 3.27 0 0 0 0 6.542m0 8.722c2.105 0 3.816-1.711 3.816-3.829s-1.711-3.816-3.829-3.816a3.82 3.82 0 0 0-3.816 3.816 3.825 3.825 0 0 0 3.829 3.83M6.542 14.18a6.542 6.542 0 1 0 0-13.084 6.542 6.542 0 1 0 0 13.084"/>
8 | </g>
9 | </svg>


--------------------------------------------------------------------------------
1 | <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-whiteidth="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M6 11C6 8.17157 6 6.75736 6.87868 5.87868C7.75736 5 9.17157 5 12 5H15C17.8284 5 19.2426 5 20.1213 5.87868C21 6.75736 21 8.17157 21 11V16C21 18.8284 21 20.2426 20.1213 21.1213C19.2426 22 17.8284 22 15 22H12C9.17157 22 7.75736 22 6.87868 21.1213C6 20.2426 6 18.8284 6 16V11Z" stroke="white" stroke-whiteidth="1.5"></path> <path d="M6 19C4.34315 19 3 17.6569 3 16V10C3 6.22876 3 4.34315 4.17157 3.17157C5.34315 2 7.22876 2 11 2H15C16.6569 2 18 3.34315 18 5" stroke="white" stroke-whiteidth="1.5"></path> </g></svg>


--------------------------------------------------------------------------------
 1 | <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
 2 | <g id="copy-03" opacity="0.6" clip-path="url(#clip0_14_6250)">
 3 | <path id="Icon" d="M6.66675 6.66663V4.33329C6.66675 3.39987 6.66675 2.93316 6.8484 2.57664C7.00819 2.26304 7.26316 2.00807 7.57676 1.84828C7.93328 1.66663 8.39999 1.66663 9.33341 1.66663H15.6667C16.6002 1.66663 17.0669 1.66663 17.4234 1.84828C17.737 2.00807 17.992 2.26304 18.1518 2.57664C18.3334 2.93316 18.3334 3.39987 18.3334 4.33329V10.6666C18.3334 11.6 18.3334 12.0668 18.1518 12.4233C17.992 12.7369 17.737 12.9918 17.4234 13.1516C17.0669 13.3333 16.6002 13.3333 15.6667 13.3333H13.3334M4.33341 18.3333H10.6667C11.6002 18.3333 12.0669 18.3333 12.4234 18.1516C12.737 17.9918 12.992 17.7369 13.1518 17.4233C13.3334 17.0668 13.3334 16.6 13.3334 15.6666V9.33329C13.3334 8.39987 13.3334 7.93316 13.1518 7.57664C12.992 7.26304 12.737 7.00807 12.4234 6.84828C12.0669 6.66663 11.6002 6.66663 10.6667 6.66663H4.33341C3.39999 6.66663 2.93328 6.66663 2.57676 6.84828C2.26316 7.00807 2.00819 7.26304 1.8484 7.57664C1.66675 7.93316 1.66675 8.39987 1.66675 9.33329V15.6666C1.66675 16.6 1.66675 17.0668 1.8484 17.4233C2.00819 17.7369 2.26316 17.9918 2.57676 18.1516C2.93328 18.3333 3.39999 18.3333 4.33341 18.3333Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
 4 | </g>
 5 | <defs>
 6 | <clipPath id="clip0_14_6250">
 7 | <rect width="20" height="20" fill="white"/>
 8 | </clipPath>
 9 | </defs>
10 | </svg>
11 | 


--------------------------------------------------------------------------------
1 | <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
2 | <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
3 | <svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
4 | <g id="SVGRepo_bgCarrier" stroke-width="0"/>
5 | <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
6 | <g id="SVGRepo_iconCarrier"> <path d="M18.59 5.88997C17.36 5.31997 16.05 4.89997 14.67 4.65997C14.5 4.95997 14.3 5.36997 14.17 5.69997C12.71 5.47997 11.26 5.47997 9.83001 5.69997C9.69001 5.36997 9.49001 4.95997 9.32001 4.65997C7.94001 4.89997 6.63001 5.31997 5.40001 5.88997C2.92001 9.62997 2.25001 13.28 2.58001 16.87C4.23001 18.1 5.82001 18.84 7.39001 19.33C7.78001 18.8 8.12001 18.23 8.42001 17.64C7.85001 17.43 7.31001 17.16 6.80001 16.85C6.94001 16.75 7.07001 16.64 7.20001 16.54C10.33 18 13.72 18 16.81 16.54C16.94 16.65 17.07 16.75 17.21 16.85C16.7 17.16 16.15 17.42 15.59 17.64C15.89 18.23 16.23 18.8 16.62 19.33C18.19 18.84 19.79 18.1 21.43 16.87C21.82 12.7 20.76 9.08997 18.61 5.88997H18.59ZM8.84001 14.67C7.90001 14.67 7.13001 13.8 7.13001 12.73C7.13001 11.66 7.88001 10.79 8.84001 10.79C9.80001 10.79 10.56 11.66 10.55 12.73C10.55 13.79 9.80001 14.67 8.84001 14.67ZM15.15 14.67C14.21 14.67 13.44 13.8 13.44 12.73C13.44 11.66 14.19 10.79 15.15 10.79C16.11 10.79 16.87 11.66 16.86 12.73C16.86 13.79 16.11 14.67 15.15 14.67Z" fill="#ffffff"/> </g>
7 | </svg>


--------------------------------------------------------------------------------
1 | <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
2 | <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
3 | <svg width="800px" height="800px" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="none">
4 | <g id="SVGRepo_bgCarrier" stroke-width="0"/>
5 | <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
6 | <g id="SVGRepo_iconCarrier">
7 | <path fill="#ffffff" d="M12.342 4.536l.15-.227.262.159.116.083c.28.216.869.768.996 1.684.223-.04.448-.06.673-.06.534 0 .893.124 1.097.227l.105.057.068.045.191.156-.066.2a2.044 2.044 0 01-.47.73c-.29.299-.8.652-1.609.698l-.178.005h-.148c-.37.977-.867 2.078-1.702 3.066a7.081 7.081 0 01-1.74 1.488 7.941 7.941 0 01-2.549.968c-.644.125-1.298.187-1.953.185-1.45 0-2.73-.288-3.517-.792-.703-.449-1.243-1.182-1.606-2.177a8.25 8.25 0 01-.461-2.83.516.516 0 01.432-.516l.068-.005h10.54l.092-.007.149-.016c.256-.034.646-.11.92-.27-.328-.543-.421-1.178-.268-1.854a3.3 3.3 0 01.3-.81l.108-.187zM2.89 5.784l.04.007a.127.127 0 01.077.082l.006.04v1.315l-.006.041a.127.127 0 01-.078.082l-.039.006H1.478a.124.124 0 01-.117-.088l-.007-.04V5.912l.007-.04a.127.127 0 01.078-.083l.039-.006H2.89zm1.947 0l.039.007a.127.127 0 01.078.082l.006.04v1.315l-.007.041a.127.127 0 01-.078.082l-.039.006H3.424a.125.125 0 01-.117-.088L3.3 7.23V5.913a.13.13 0 01.085-.123l.039-.007h1.413zm1.976 0l.039.007a.127.127 0 01.077.082l.007.04v1.315l-.007.041a.127.127 0 01-.078.082l-.039.006H5.4a.124.124 0 01-.117-.088l-.006-.04V5.912l.006-.04a.127.127 0 01.078-.083l.039-.006h1.413zm1.952 0l.039.007a.127.127 0 01.078.082l.007.04v1.315a.13.13 0 01-.085.123l-.04.006H7.353a.124.124 0 01-.117-.088l-.006-.04V5.912l.006-.04a.127.127 0 01.078-.083l.04-.006h1.412zm1.97 0l.039.007a.127.127 0 01.078.082l.006.04v1.315a.13.13 0 01-.085.123l-.039.006H9.322a.124.124 0 01-.117-.088l-.006-.04V5.912l.006-.04a.127.127 0 01.078-.083l.04-.006h1.411zM4.835 3.892l.04.007a.127.127 0 01.077.081l.007.041v1.315a.13.13 0 01-.085.123l-.039.007H3.424a.125.125 0 01-.117-.09l-.007-.04V4.021a.13.13 0 01.085-.122l.039-.007h1.412zm1.976 0l.04.007a.127.127 0 01.077.081l.007.041v1.315a.13.13 0 01-.085.123l-.039.007H5.4a.125.125 0 01-.117-.09l-.006-.04V4.021l.006-.04a.127.127 0 01.078-.082l.039-.007h1.412zm1.953 0c.054 0 .1.037.117.088l.007.041v1.315a.13.13 0 01-.085.123l-.04.007H7.353a.125.125 0 01-.117-.09l-.006-.04V4.021l.006-.04a.127.127 0 01.078-.082l.04-.007h1.412zm0-1.892c.054 0 .1.037.117.088l.007.04v1.316a.13.13 0 01-.085.123l-.04.006H7.353a.124.124 0 01-.117-.088l-.006-.04V2.128l.006-.04a.127.127 0 01.078-.082L7.353 2h1.412z"/>
8 | </g>
9 | </svg>


--------------------------------------------------------------------------------
1 | <svg viewBox="0 -0.5 48 48" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>Github-color</title> <desc>Created with Sketch.</desc> <defs> </defs> <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"> <g id="Color-" transform="translate(-700.000000, -560.000000)" fill="#3E75C3"> <path d="M723.9985,560 C710.746,560 700,570.787092 700,584.096644 C700,594.740671 706.876,603.77183 716.4145,606.958412 C717.6145,607.179786 718.0525,606.435849 718.0525,605.797328 C718.0525,605.225068 718.0315,603.710086 718.0195,601.699648 C711.343,603.155898 709.9345,598.469394 709.9345,598.469394 C708.844,595.686405 707.2705,594.94548 707.2705,594.94548 C705.091,593.450075 707.4355,593.480194 707.4355,593.480194 C709.843,593.650366 711.1105,595.963499 711.1105,595.963499 C713.2525,599.645538 716.728,598.58234 718.096,597.964902 C718.3135,596.407754 718.9345,595.346062 719.62,594.743683 C714.2905,594.135281 708.688,592.069123 708.688,582.836167 C708.688,580.205279 709.6225,578.054788 711.1585,576.369634 C710.911,575.759726 710.0875,573.311058 711.3925,569.993458 C711.3925,569.993458 713.4085,569.345902 717.9925,572.46321 C719.908,571.928599 721.96,571.662047 724.0015,571.651505 C726.04,571.662047 728.0935,571.928599 730.0105,572.46321 C734.5915,569.345902 736.603,569.993458 736.603,569.993458 C737.9125,573.311058 737.089,575.759726 736.8415,576.369634 C738.3805,578.054788 739.309,580.205279 739.309,582.836167 C739.309,592.091712 733.6975,594.129257 728.3515,594.725612 C729.2125,595.469549 729.9805,596.939353 729.9805,599.18773 C729.9805,602.408949 729.9505,605.006706 729.9505,605.797328 C729.9505,606.441873 730.3825,607.191834 731.6005,606.9554 C741.13,603.762794 748,594.737659 748,584.096644 C748,570.787092 737.254,560 723.9985,560" id="Github"> </path> </g> </g> </g></svg>


--------------------------------------------------------------------------------
 1 | <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
 2 | <g id="Social icon" opacity="0.7" clip-path="url(#clip0_14_6286)">
 3 | <path id="Icon" fill-rule="evenodd" clip-rule="evenodd" d="M8 0C3.5816 0 0 3.5872 0 8.0136C0 11.5536 2.292 14.5576 5.4712 15.6168C5.8712 15.6904 6.0168 15.4432 6.0168 15.2304C6.0168 15.0408 6.0104 14.536 6.0064 13.868C3.7808 14.352 3.3112 12.7936 3.3112 12.7936C2.948 11.8672 2.4232 11.6208 2.4232 11.6208C1.6968 11.1248 2.4784 11.1344 2.4784 11.1344C3.2808 11.1904 3.7032 11.96 3.7032 11.96C4.4168 13.184 5.576 12.8304 6.0312 12.6256C6.1048 12.108 6.3112 11.7552 6.54 11.5552C4.764 11.3528 2.896 10.6648 2.896 7.5944C2.896 6.72 3.208 6.004 3.7192 5.444C3.6368 5.2416 3.3624 4.4264 3.7976 3.324C3.7976 3.324 4.4696 3.108 5.9976 4.1448C6.65021 3.96681 7.32355 3.87615 8 3.8752C8.68 3.8784 9.364 3.9672 10.0032 4.1448C11.5304 3.108 12.2008 3.3232 12.2008 3.3232C12.6376 4.4264 12.3624 5.2416 12.2808 5.444C12.7928 6.004 13.1032 6.72 13.1032 7.5944C13.1032 10.6728 11.232 11.3504 9.4504 11.5488C9.7376 11.796 9.9928 12.2848 9.9928 13.0328C9.9928 14.1032 9.9832 14.968 9.9832 15.2304C9.9832 15.4448 10.1272 15.6944 10.5336 15.616C12.1266 15.0817 13.5115 14.0602 14.4924 12.696C15.4733 11.3318 16.0007 9.69385 16 8.0136C16 3.5872 12.4176 0 8 0Z" fill="#242E36"/>
 4 | </g>
 5 | <defs>
 6 | <clipPath id="clip0_14_6286">
 7 | <rect width="16" height="16" fill="white"/>
 8 | </clipPath>
 9 | </defs>
10 | </svg>
11 | 


--------------------------------------------------------------------------------
1 | <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
2 | <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
3 | <svg width="800px" height="800px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000">
4 | <g id="SVGRepo_bgCarrier" stroke-width="0"/>
5 | <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
6 | <g id="SVGRepo_iconCarrier"> <title>github [#142]</title> <desc>Created with Sketch.</desc> <defs> </defs> <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"> <g id="Dribbble-Light-Preview" transform="translate(-140.000000, -7559.000000)" fill="#ffffff"> <g id="icons" transform="translate(56.000000, 160.000000)"> <path d="M94,7399 C99.523,7399 104,7403.59 104,7409.253 C104,7413.782 101.138,7417.624 97.167,7418.981 C96.66,7419.082 96.48,7418.762 96.48,7418.489 C96.48,7418.151 96.492,7417.047 96.492,7415.675 C96.492,7414.719 96.172,7414.095 95.813,7413.777 C98.04,7413.523 100.38,7412.656 100.38,7408.718 C100.38,7407.598 99.992,7406.684 99.35,7405.966 C99.454,7405.707 99.797,7404.664 99.252,7403.252 C99.252,7403.252 98.414,7402.977 96.505,7404.303 C95.706,7404.076 94.85,7403.962 94,7403.958 C93.15,7403.962 92.295,7404.076 91.497,7404.303 C89.586,7402.977 88.746,7403.252 88.746,7403.252 C88.203,7404.664 88.546,7405.707 88.649,7405.966 C88.01,7406.684 87.619,7407.598 87.619,7408.718 C87.619,7412.646 89.954,7413.526 92.175,7413.785 C91.889,7414.041 91.63,7414.493 91.54,7415.156 C90.97,7415.418 89.522,7415.871 88.63,7414.304 C88.63,7414.304 88.101,7413.319 87.097,7413.247 C87.097,7413.247 86.122,7413.234 87.029,7413.87 C87.029,7413.87 87.684,7414.185 88.139,7415.37 C88.139,7415.37 88.726,7417.2 91.508,7416.58 C91.513,7417.437 91.522,7418.245 91.522,7418.489 C91.522,7418.76 91.338,7419.077 90.839,7418.982 C86.865,7417.627 84,7413.783 84,7409.253 C84,7403.59 88.478,7399 94,7399" id="github-[#142]"> </path> </g> </g> </g> </g>
7 | </svg>


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/nextjs/public/img/gptr-logo.png


--------------------------------------------------------------------------------
1 | <svg width="19" height="19" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <g id="&#240;&#159;&#166;&#134; icon &#34;atom&#34;">
3 | <path id="Vector" fill-rule="evenodd" clip-rule="evenodd" d="M14.4258 9.49998C13.7961 8.61084 13.0394 7.70704 12.1662 6.8338C11.2929 5.96056 10.3891 5.20385 9.49998 4.57419C8.61084 5.20385 7.70704 5.96056 6.8338 6.8338C5.96056 7.70704 5.20385 8.61084 4.57419 9.49998C5.20385 10.3891 5.96056 11.2929 6.8338 12.1662C7.70704 13.0394 8.61084 13.7961 9.49998 14.4258C10.3891 13.7961 11.2929 13.0394 12.1662 12.1662C13.0394 11.2929 13.7961 10.3891 14.4258 9.49998ZM15.5013 7.77557C16.6942 5.56024 16.9775 3.64659 16.1654 2.83453C15.3534 2.02246 13.4397 2.30579 11.2244 3.49861C11.996 4.09137 12.7604 4.76183 13.4993 5.50071C14.2381 6.23958 14.9086 7.00399 15.5013 7.77557ZM7.77557 15.5013C7.00399 14.9086 6.23958 14.2381 5.50071 13.4993C4.76183 12.7604 4.09137 11.996 3.49861 11.2244C2.30579 13.4397 2.02246 15.3534 2.83453 16.1654C3.64659 16.9775 5.56024 16.6942 7.77557 15.5013ZM16.6902 9.49998C18.6629 12.7259 19.1584 15.8387 17.4985 17.4985C15.8387 19.1584 12.7259 18.6629 9.49998 16.6902C6.27403 18.6629 3.16126 19.1584 1.50143 17.4985C-0.158396 15.8387 0.337048 12.7259 2.30973 9.49998C0.337048 6.27403 -0.158396 3.16126 1.50143 1.50143C3.16126 -0.158396 6.27403 0.337048 9.49998 2.30973C12.7259 0.337048 15.8387 -0.158396 17.4985 1.50143C19.1584 3.16126 18.6629 6.27403 16.6902 9.49998ZM15.5013 11.2244C14.9086 11.996 14.2381 12.7604 13.4993 13.4993C12.7604 14.2381 11.996 14.9086 11.2244 15.5013C13.4397 16.6942 15.3534 16.9775 16.1654 16.1654C16.9775 15.3534 16.6942 13.4397 15.5013 11.2244ZM3.49861 7.77557C4.09137 7.00399 4.76183 6.23958 5.50071 5.50071C6.23958 4.76183 7.00399 4.09137 7.77557 3.49861C5.56024 2.30579 3.64659 2.02246 2.83453 2.83453C2.02246 3.64659 2.30579 5.56024 3.49861 7.77557ZM9.49998 8.55734C10.0206 8.55734 10.4426 8.97938 10.4426 9.49998C10.4426 10.0206 10.0206 10.4426 9.49998 10.4426C8.97938 10.4426 8.55734 10.0206 8.55734 9.49998C8.55734 8.97938 8.97938 8.55734 9.49998 8.55734Z" fill="black"/>
4 | </g>
5 | </svg>
6 | 


--------------------------------------------------------------------------------
1 | <svg width="21" height="13" viewBox="0 0 21 13" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <g id="&#240;&#159;&#166;&#134; icon &#34;dumbell&#34;">
3 | <path id="Vector" fill-rule="evenodd" clip-rule="evenodd" d="M5.47427 1.3573H7.11094C7.57345 1.36852 7.93946 1.75232 7.92866 2.21485V10.7852C7.93946 11.2476 7.57345 11.6316 7.11094 11.6427H5.47427C5.01176 11.6316 4.6458 11.2476 4.65658 10.7852V9.07138H2.31792C1.85541 9.06019 1.48946 8.67629 1.50023 8.21383V4.78621C1.48946 4.32375 1.85541 3.93984 2.31792 3.92866H4.65658V2.21485C4.6458 1.75232 5.01176 1.36852 5.47427 1.3573Z" stroke="black" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
4 | <path id="Vector_2" fill-rule="evenodd" clip-rule="evenodd" d="M15.5258 11.6427H13.8891C13.4265 11.6316 13.0606 11.2476 13.0714 10.7852V2.21485C13.0606 1.75232 13.4265 1.36852 13.8891 1.3573H15.5258C15.9882 1.36852 16.3543 1.75232 16.3435 2.21485V3.92866H18.6808C18.9031 3.93367 19.1144 4.02688 19.268 4.18772C19.4215 4.34856 19.5049 4.56391 19.4998 4.78621V8.21383C19.5106 8.67629 19.1446 9.06019 18.6821 9.07138H16.3435V10.7852C16.3543 11.2476 15.9882 11.6316 15.5258 11.6427Z" stroke="black" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
5 | <path id="Vector_3" d="M3.69263 9.07145C3.69263 9.60398 4.12435 10.0357 4.65689 10.0357C5.18943 10.0357 5.62115 9.60398 5.62115 9.07145H3.69263ZM5.62115 3.92874C5.62115 3.3962 5.18943 2.96448 4.65689 2.96448C4.12435 2.96448 3.69263 3.3962 3.69263 3.92874H5.62115ZM17.3093 3.92874C17.3093 3.3962 16.8775 2.96448 16.345 2.96448C15.8125 2.96448 15.3807 3.3962 15.3807 3.92874H17.3093ZM15.3807 9.07145C15.3807 9.60398 15.8125 10.0357 16.345 10.0357C16.8775 10.0357 17.3093 9.60398 17.3093 9.07145H15.3807ZM7.92894 5.53584C7.3964 5.53584 6.96468 5.96757 6.96468 6.5001C6.96468 7.03262 7.3964 7.46436 7.92894 7.46436V5.53584ZM13.0717 7.46436C13.6042 7.46436 14.0359 7.03262 14.0359 6.5001C14.0359 5.96757 13.6042 5.53584 13.0717 5.53584V7.46436ZM5.62115 9.07145V3.92874H3.69263V9.07145H5.62115ZM15.3807 3.92874V9.07145H17.3093V3.92874H15.3807ZM7.92894 7.46436H13.0717V5.53584H7.92894V7.46436Z" fill="black"/>
6 | </g>
7 | </svg>
8 | 


--------------------------------------------------------------------------------
1 | <svg width="19" height="17" viewBox="0 0 19 17" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <g id="&#240;&#159;&#166;&#134; icon &#34;leaf&#34;">
3 | <path id="Vector" d="M17.5687 0.802062C17.3936 0.4114 16.8936 0.395773 16.6842 0.764558C15.7154 2.44909 13.9808 3.49919 11.9994 3.49919H9.49914C6.18633 3.49919 3.49858 6.18695 3.49858 9.49976C3.49858 9.71853 3.52358 9.92793 3.54545 10.1404C5.53939 8.71219 8.41779 7.49957 12.4994 7.49957C12.7745 7.49957 12.9995 7.72459 12.9995 7.99962C12.9995 8.27465 12.7745 8.49967 12.4994 8.49967C4.64243 8.49967 1.31087 13.3158 0.573297 15.1253C0.367028 15.6347 0.610801 16.216 1.12022 16.4254C1.63277 16.6379 2.21408 16.391 2.4266 15.8847C2.47348 15.7722 3.07979 14.3877 4.67369 13.0532C5.68628 14.4252 7.61147 15.7347 10.1398 15.466C15.0465 15.1097 18.5 10.7093 18.5 5.32124C18.5 3.75234 18.1625 2.12719 17.5687 0.802062Z" fill="black"/>
4 | </g>
5 | </svg>
6 | 


--------------------------------------------------------------------------------
1 | <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
2 | <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
3 | <svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff">
4 | <g id="SVGRepo_bgCarrier" stroke-width="0"/>
5 | <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
6 | <g id="SVGRepo_iconCarrier"> <path d="M14.2639 15.9375L12.5958 14.2834C11.7909 13.4851 11.3884 13.086 10.9266 12.9401C10.5204 12.8118 10.0838 12.8165 9.68048 12.9536C9.22188 13.1095 8.82814 13.5172 8.04068 14.3326L4.04409 18.2801M14.2639 15.9375L14.6053 15.599C15.4112 14.7998 15.8141 14.4002 16.2765 14.2543C16.6831 14.126 17.12 14.1311 17.5236 14.2687C17.9824 14.4251 18.3761 14.8339 19.1634 15.6514L20 16.4934M14.2639 15.9375L18.275 19.9565M18.275 19.9565C17.9176 20 17.4543 20 16.8 20H7.2C6.07989 20 5.51984 20 5.09202 19.782C4.71569 19.5903 4.40973 19.2843 4.21799 18.908C4.12796 18.7313 4.07512 18.5321 4.04409 18.2801M18.275 19.9565C18.5293 19.9256 18.7301 19.8727 18.908 19.782C19.2843 19.5903 19.5903 19.2843 19.782 18.908C20 18.4802 20 17.9201 20 16.8V16.4934M4.04409 18.2801C4 17.9221 4 17.4575 4 16.8V7.2C4 6.0799 4 5.51984 4.21799 5.09202C4.40973 4.71569 4.71569 4.40973 5.09202 4.21799C5.51984 4 6.07989 4 7.2 4H16.8C17.9201 4 18.4802 4 18.908 4.21799C19.2843 4.40973 19.5903 4.71569 19.782 5.09202C20 5.51984 20 6.0799 20 7.2V16.4934M17 8.99989C17 10.1045 16.1046 10.9999 15 10.9999C13.8954 10.9999 13 10.1045 13 8.99989C13 7.89532 13.8954 6.99989 15 6.99989C16.1046 6.99989 17 7.89532 17 8.99989Z" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> </g>
7 | </svg>


--------------------------------------------------------------------------------
 1 | <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
 2 | <g id="link-03" opacity="0.6" clip-path="url(#clip0_14_6251)">
 3 | <path id="Icon" d="M8.33326 10.8333C8.69113 11.3118 9.14772 11.7077 9.67205 11.9941C10.1964 12.2806 10.7762 12.4509 11.3721 12.4936C11.9681 12.5363 12.5662 12.4503 13.126 12.2415C13.6858 12.0327 14.1942 11.7059 14.6166 11.2833L17.1166 8.78334C17.8756 7.9975 18.2956 6.94499 18.2861 5.85251C18.2766 4.76002 17.8384 3.71497 17.0658 2.94243C16.2933 2.1699 15.2482 1.7317 14.1558 1.7222C13.0633 1.71271 12.0108 2.13269 11.2249 2.89168L9.79159 4.31668M11.6666 9.16668C11.3087 8.68824 10.8521 8.29236 10.3278 8.00589C9.80347 7.71943 9.22367 7.54908 8.62771 7.5064C8.03176 7.46372 7.4336 7.54971 6.8738 7.75853C6.314 7.96735 5.80566 8.29412 5.38326 8.71668L2.88326 11.2167C2.12426 12.0025 1.70429 13.055 1.71378 14.1475C1.72327 15.24 2.16148 16.2851 2.93401 17.0576C3.70655 17.8301 4.7516 18.2683 5.84408 18.2778C6.93657 18.2873 7.98908 17.8673 8.77492 17.1083L10.1999 15.6833" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
 4 | </g>
 5 | <defs>
 6 | <clipPath id="clip0_14_6251">
 7 | <rect width="20" height="20" fill="white"/>
 8 | </clipPath>
 9 | </defs>
10 | </svg>
11 | 


--------------------------------------------------------------------------------
1 | <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-whiteidth="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M4 21V19.5C4 16.4624 6.46243 14 9.5 14H12.5C15.5376 14 18 16.4624 18 19.5V21M7 21V18M15 21V18M16.5 6L16.8367 5.49493C17.1969 4.95461 17.9371 4.82782 18.4566 5.21745C19.0073 5.63047 19.0645 6.43549 18.5778 6.92224L17.8536 7.64645C17.6272 7.87282 17.5 8.17986 17.5 8.5M17.5 10V10.2M13.8281 4.89801C14.6435 3.74945 15.9842 3 17.5 3C19.9853 3 22 5.01472 22 7.5C22 9.98528 19.9853 12 17.5 12C16.2549 12 15.1279 11.4943 14.3131 10.6771M15 8.00001C15 5.79086 13.2091 4 11 4C8.79086 4 7 5.79086 7 8.00001C7 10.2092 8.79086 12 11 12C11.8312 12 12.6032 11.7465 13.2429 11.3125C14.3033 10.5931 15 9.37794 15 8.00001Z" stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-whiteidth="1.4"></path></g></svg>


--------------------------------------------------------------------------------
1 | <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-search"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>


--------------------------------------------------------------------------------
1 | <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <g id="share-01" opacity="0.6">
3 | <path id="Icon" d="M17.5 10V13.5C17.5 14.9001 17.5 15.6002 17.2275 16.135C16.9878 16.6054 16.6054 16.9878 16.135 17.2275C15.6002 17.5 14.9001 17.5 13.5 17.5H6.5C5.09987 17.5 4.3998 17.5 3.86502 17.2275C3.39462 16.9878 3.01217 16.6054 2.77248 16.135C2.5 15.6002 2.5 14.9001 2.5 13.5V10M13.3333 5.83333L10 2.5M10 2.5L6.66667 5.83333M10 2.5V12.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
4 | </g>
5 | </svg>
6 | 


--------------------------------------------------------------------------------
1 | <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <path id="Layer 58" d="M12 0C9.62663 0 7.30655 0.703787 5.33316 2.02236C3.35977 3.34094 1.8217 5.21508 0.913451 7.4078C0.00519945 9.60051 -0.232441 12.0133 0.230582 14.3411C0.693604 16.6689 1.83649 18.807 3.51472 20.4853C5.19295 22.1635 7.33115 23.3064 9.65892 23.7694C11.9867 24.2324 14.3995 23.9948 16.5922 23.0865C18.7849 22.1783 20.6591 20.6402 21.9776 18.6668C23.2962 16.6935 24 14.3734 24 12C24 8.8174 22.7357 5.76515 20.4853 3.51472C18.2348 1.26428 15.1826 0 12 0ZM6.54546 13.0909C6.3297 13.0909 6.11878 13.0269 5.93938 12.9071C5.75998 12.7872 5.62016 12.6168 5.53759 12.4175C5.45502 12.2181 5.43342 11.9988 5.47551 11.7872C5.5176 11.5756 5.6215 11.3812 5.77407 11.2286C5.92664 11.076 6.12102 10.9721 6.33263 10.93C6.54425 10.888 6.76359 10.9096 6.96293 10.9921C7.16227 11.0747 7.33264 11.2145 7.45252 11.3939C7.57239 11.5733 7.63637 11.7842 7.63637 12C7.63637 12.2893 7.52143 12.5668 7.31685 12.7714C7.11226 12.976 6.83478 13.0909 6.54546 13.0909ZM12 13.0909C11.7842 13.0909 11.5733 13.0269 11.3939 12.9071C11.2145 12.7872 11.0747 12.6168 10.9921 12.4175C10.9096 12.2181 10.888 11.9988 10.9301 11.7872C10.9721 11.5756 11.076 11.3812 11.2286 11.2286C11.3812 11.076 11.5756 10.9721 11.7872 10.93C11.9988 10.888 12.2181 10.9096 12.4175 10.9921C12.6168 11.0747 12.7872 11.2145 12.9071 11.3939C13.0269 11.5733 13.0909 11.7842 13.0909 12C13.0909 12.2893 12.976 12.5668 12.7714 12.7714C12.5668 12.976 12.2893 13.0909 12 13.0909ZM17.4545 13.0909C17.2388 13.0909 17.0279 13.0269 16.8485 12.9071C16.6691 12.7872 16.5292 12.6168 16.4467 12.4175C16.3641 12.2181 16.3425 11.9988 16.3846 11.7872C16.4267 11.5756 16.5306 11.3812 16.6832 11.2286C16.8357 11.076 17.0301 10.9721 17.2417 10.93C17.4533 10.888 17.6727 10.9096 17.872 10.9921C18.0714 11.0747 18.2417 11.2145 18.3616 11.3939C18.4815 11.5733 18.5455 11.7842 18.5455 12C18.5455 12.2893 18.4305 12.5668 18.2259 12.7714C18.0214 12.976 17.7439 13.0909 17.4545 13.0909Z" fill="#231F20"/>
3 | </svg>
4 | 


--------------------------------------------------------------------------------
1 | <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
2 | <!-- Uploaded to: SVG Repo, www.svgrepo.com, Transformed by: SVG Repo Mixer Tools -->
3 | <svg width="240px" height="240px" viewBox="0 0 76 76" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" baseProfile="full" enable-background="new 0 0 76.00 76.00" xml:space="preserve" fill="#000000">
4 | <g id="SVGRepo_bgCarrier" stroke-width="0"/>
5 | <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
6 | <g id="SVGRepo_iconCarrier"> <path fill="#000000" fill-opacity="1" stroke-width="0.2" stroke-linejoin="round" d="M 15.8332,47.5002L 15.8332,40.1901L 25.3332,31.6669L 30.0832,36.4169L 34.8331,20.5836L 44.3331,31.6669L 50.6664,25.3336L 45.9164,20.5836L 58.583,20.5836L 58.583,33.2502L 53.8331,28.5003L 44.3331,38.0002L 36.4165,28.5003L 31.6665,44.3335L 25.3332,38.0002L 15.8332,47.5002 Z "/> <path fill="#000000" fill-opacity="1" stroke-width="0.2" stroke-linejoin="round" d="M 58.5833,55.4167L 53.8333,55.4167L 53.8333,34.8333L 58.5833,39.5833L 58.5833,55.4167 Z M 49.0833,55.4167L 44.3333,55.4167L 44.3333,44.3333L 49.0833,39.5834L 49.0833,55.4167 Z M 39.5833,55.4167L 34.8333,55.4167L 34.8333,45.9167L 37.2083,36.4167L 39.5833,39.5833L 39.5833,55.4167 Z M 30.0833,55.4167L 25.3333,55.4167L 25.3333,44.3333L 30.0833,49.0833L 30.0833,55.4167 Z M 20.5833,55.4167L 15.8333,55.4167L 15.8333,53.8334L 20.5833,49.0834L 20.5833,55.4167 Z "/> </g>
7 | </svg>


--------------------------------------------------------------------------------
 1 | <?xml version="1.0" encoding="iso-8859-1"?>
 2 | <!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->
 3 | <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
 4 | <svg fill="#000000" height="800px" width="800px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
 5 | 	 viewBox="0 0 386.651 386.651" xml:space="preserve">
 6 | <g>
 7 | 	<path d="M342.367,135.781c-2.674-1.367-5.889-1.122-8.324,0.635l-138.556,99.968l-89.233-83.725
 8 | 		c-3.032-2.844-7.736-2.892-10.826-0.112l-74.395,66.959c-1.685,1.518-2.648,3.679-2.648,5.946v91.451c0,4.418,3.582,8,8,8h312.339
 9 | 		c4.418,0,8-3.582,8-8v-174C346.724,139.899,345.041,137.149,342.367,135.781z M53.507,308.903H34.385v-79.889l19.122-17.211
10 | 		V308.903z M88.045,308.903H69.507v-111.5l18.538-16.685V308.903z M122.582,308.903h-18.538V172.526l18.538,17.393V308.903z
11 | 		 M157.12,308.903h-18.538V204.931l18.538,17.394V308.903z M192.015,308.903H173.12v-71.565l16.227,15.226
12 | 		c0.791,0.741,1.702,1.288,2.667,1.65V308.903z M226.91,308.903h-18.896v-61.828l18.896-13.634V308.903z M261.806,308.903H242.91
13 | 		v-87.006l18.895-13.633V308.903z M296.701,308.903h-18.896V196.72l18.896-13.634V308.903z M330.724,308.903h-18.022v-137.36
14 | 		l18.022-13.003V308.903z"/>
15 | 	<path d="M385.375,65.087c-1.439-2.148-3.904-3.404-6.461-3.337l-50.696,1.368c-3.471,0.094-6.429,2.547-7.161,5.941
16 | 		c-0.732,3.395,0.95,6.85,4.074,8.366l11.846,5.75L196.96,183.012l-95.409-86.504c-4.738-4.296-11.955-4.322-16.723-0.062
17 | 		L4.173,168.491c-5.149,4.599-5.594,12.501-0.995,17.649c4.598,5.148,12.499,5.594,17.649,0.995l72.265-64.55l94.533,85.709
18 | 		c2.369,2.147,5.376,3.239,8.398,3.239c2.532,0,5.074-0.767,7.255-2.322L350.82,104.01l0.701,11.074
19 | 		c0.22,3.464,2.777,6.329,6.193,6.939c0.444,0.079,0.889,0.118,1.328,0.118c2.938,0,5.662-1.724,6.885-4.483l20.077-45.327
20 | 		C387.052,69.968,386.815,67.234,385.375,65.087z"/>
21 | </g>
22 | </svg>


--------------------------------------------------------------------------------
1 | <svg fill="#ffffff" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-whiteidth="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>books</title> <path d="M30.156 26.492l-6.211-23.184c-0.327-1.183-1.393-2.037-2.659-2.037-0.252 0-0.495 0.034-0.727 0.097l0.019-0.004-2.897 0.776c-0.325 0.094-0.609 0.236-0.86 0.42l0.008-0.005c-0.49-0.787-1.349-1.303-2.33-1.306h-2.998c-0.789 0.001-1.5 0.337-1.998 0.873l-0.002 0.002c-0.5-0.537-1.211-0.873-2-0.874h-3c-1.518 0.002-2.748 1.232-2.75 2.75v24c0.002 1.518 1.232 2.748 2.75 2.75h3c0.789-0.002 1.5-0.337 1.998-0.873l0.002-0.002c0.5 0.538 1.211 0.873 2 0.875h2.998c1.518-0.002 2.748-1.232 2.75-2.75v-16.848l4.699 17.54c0.327 1.182 1.392 2.035 2.656 2.037h0c0.001 0 0.003 0 0.005 0 0.251 0 0.494-0.034 0.725-0.098l-0.019 0.005 2.898-0.775c1.182-0.326 2.036-1.392 2.036-2.657 0-0.252-0.034-0.497-0.098-0.729l0.005 0.019zM18.415 9.708l5.31-1.423 3.753 14.007-5.311 1.422zM18.068 3.59l2.896-0.776c0.097-0.027 0.209-0.043 0.325-0.043 0.575 0 1.059 0.389 1.204 0.918l0.002 0.009 0.841 3.139-5.311 1.423-0.778-2.905v-1.055c0.153-0.347 0.449-0.607 0.812-0.708l0.009-0.002zM11.5 2.75h2.998c0.69 0.001 1.249 0.56 1.25 1.25v3.249l-5.498 0.001v-3.25c0.001-0.69 0.56-1.249 1.25-1.25h0zM8.75 23.25h-5.5v-14.5l5.5-0.001zM10.25 8.75l5.498-0.001v14.501h-5.498zM4.5 2.75h3c0.69 0.001 1.249 0.56 1.25 1.25v3.249l-5.5 0.001v-3.25c0.001-0.69 0.56-1.249 1.25-1.25h0zM7.5 29.25h-3c-0.69-0.001-1.249-0.56-1.25-1.25v-3.25h5.5v3.25c-0.001 0.69-0.56 1.249-1.25 1.25h-0zM14.498 29.25h-2.998c-0.69-0.001-1.249-0.56-1.25-1.25v-3.25h5.498v3.25c-0.001 0.69-0.56 1.249-1.25 1.25h-0zM28.58 27.826c-0.164 0.285-0.43 0.495-0.747 0.582l-0.009 0.002-2.898 0.775c-0.096 0.026-0.206 0.041-0.319 0.041-0.575 0-1.060-0.387-1.208-0.915l-0.002-0.009-0.841-3.14 5.311-1.422 0.841 3.14c0.027 0.096 0.042 0.207 0.042 0.321 0 0.23-0.063 0.446-0.173 0.63l0.003-0.006z"></path> </g></svg>


--------------------------------------------------------------------------------
1 | <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <path id="Vector" opacity="0.7" fill-rule="evenodd" clip-rule="evenodd" d="M10.0748 15L6.45272 9.60689L1.91833 15H0L5.60164 8.33938L0 0H4.9252L8.33897 5.08297L12.6163 0H14.5346L9.19291 6.35215L15 15H10.0748ZM12.2111 13.4796H10.9196L2.74677 1.52045H4.03844L7.31172 6.30897L7.87775 7.13991L12.2111 13.4796Z" fill="#242E36"/>
3 | </svg>
4 | 


--------------------------------------------------------------------------------
1 | <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 394 80"><path fill="#000" d="M262 0h68.5v12.7h-27.2v66.6h-13.6V12.7H262V0ZM149 0v12.7H94v20.4h44.3v12.6H94v21h55v12.6H80.5V0h68.7zm34.3 0h-17.8l63.8 79.4h17.9l-32-39.7 32-39.6h-17.9l-23 28.6-23-28.6zm18.3 56.7-9-11-27.1 33.7h17.8l18.3-22.7z"/><path fill="#000" d="M81 79.3 17 0H0v79.3h13.6V17l50.2 62.3H81Zm252.6-.4c-1 0-1.8-.4-2.5-1s-1.1-1.6-1.1-2.6.3-1.8 1-2.5 1.6-1 2.6-1 1.8.3 2.5 1a3.4 3.4 0 0 1 .6 4.3 3.7 3.7 0 0 1-3 1.8zm23.2-33.5h6v23.3c0 2.1-.4 4-1.3 5.5a9.1 9.1 0 0 1-3.8 3.5c-1.6.8-3.5 1.3-5.7 1.3-2 0-3.7-.4-5.3-1s-2.8-1.8-3.7-3.2c-.9-1.3-1.4-3-1.4-5h6c.1.8.3 1.6.7 2.2s1 1.2 1.6 1.5c.7.4 1.5.5 2.4.5 1 0 1.8-.2 2.4-.6a4 4 0 0 0 1.6-1.8c.3-.8.5-1.8.5-3V45.5zm30.9 9.1a4.4 4.4 0 0 0-2-3.3 7.5 7.5 0 0 0-4.3-1.1c-1.3 0-2.4.2-3.3.5-.9.4-1.6 1-2 1.6a3.5 3.5 0 0 0-.3 4c.3.5.7.9 1.3 1.2l1.8 1 2 .5 3.2.8c1.3.3 2.5.7 3.7 1.2a13 13 0 0 1 3.2 1.8 8.1 8.1 0 0 1 3 6.5c0 2-.5 3.7-1.5 5.1a10 10 0 0 1-4.4 3.5c-1.8.8-4.1 1.2-6.8 1.2-2.6 0-4.9-.4-6.8-1.2-2-.8-3.4-2-4.5-3.5a10 10 0 0 1-1.7-5.6h6a5 5 0 0 0 3.5 4.6c1 .4 2.2.6 3.4.6 1.3 0 2.5-.2 3.5-.6 1-.4 1.8-1 2.4-1.7a4 4 0 0 0 .8-2.4c0-.9-.2-1.6-.7-2.2a11 11 0 0 0-2.1-1.4l-3.2-1-3.8-1c-2.8-.7-5-1.7-6.6-3.2a7.2 7.2 0 0 1-2.4-5.7 8 8 0 0 1 1.7-5 10 10 0 0 1 4.3-3.5c2-.8 4-1.2 6.4-1.2 2.3 0 4.4.4 6.2 1.2 1.8.8 3.2 2 4.3 3.4 1 1.4 1.5 3 1.5 5h-5.8z"/></svg>


--------------------------------------------------------------------------------
1 | <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 283 64"><path fill="black" d="M141 16c-11 0-19 7-19 18s9 18 20 18c7 0 13-3 16-7l-7-5c-2 3-6 4-9 4-5 0-9-3-10-7h28v-3c0-11-8-18-19-18zm-9 15c1-4 4-7 9-7s8 3 9 7h-18zm117-15c-11 0-19 7-19 18s9 18 20 18c6 0 12-3 16-7l-8-5c-2 3-5 4-8 4-5 0-9-3-11-7h28l1-3c0-11-8-18-19-18zm-10 15c2-4 5-7 10-7s8 3 9 7h-19zm-39 3c0 6 4 10 10 10 4 0 7-2 9-5l8 5c-3 5-9 8-17 8-11 0-19-7-19-18s8-18 19-18c8 0 14 3 17 8l-8 5c-2-3-5-5-9-5-6 0-10 4-10 10zm83-29v46h-9V5h9zM37 0l37 64H0L37 0zm92 5-27 48L74 5h10l18 30 17-30h10zm59 12v10l-3-1c-6 0-10 4-10 10v15h-9V17h9v9c0-5 6-9 13-9z"/></svg>


--------------------------------------------------------------------------------
/frontend/nextjs/styles/markdown.css:
--------------------------------------------------------------------------------
  1 | .markdown-content {
  2 |   /* Base styles */
  3 |   color: white;
  4 |   font-family: Georgia, 'Times New Roman', Times, serif;
  5 |   font-size: 18px;
  6 |   line-height: 1.6;
  7 | 
  8 |   /* Headings */
  9 |   h1, h2, h3, h4, h5, h6 {
 10 |     line-height: 1.2;
 11 |     font-weight: 500;
 12 |   }
 13 | 
 14 |   h1 { font-size: 2.5em; }
 15 |   h2 { font-size: 2em; }
 16 |   h3 { font-size: 1.5em; }
 17 |   h4 { font-size: 1.2em; }
 18 |   h5 { font-size: 1.1em; }
 19 |   h6 { font-size: 1em; }
 20 | 
 21 |   /* Paragraphs and spacing */
 22 |   p {
 23 |     margin: 0;
 24 |     line-height: 1.6;
 25 |   }
 26 | 
 27 |   /* Lists */
 28 |   ul, ol {
 29 |     margin: 0;
 30 |     padding: 0 0 0 2em; /* Add left padding for the bullet points */
 31 |     list-style-position: outside; /* Keep bullets outside */
 32 |   }
 33 | 
 34 |   li {
 35 |     margin: 0.5em 0; /* Add some vertical spacing between items */
 36 |     display: block; /* Change from grid to block */
 37 |     padding-left: 0.5em; /* Add a little padding after the bullet */
 38 |   }
 39 | 
 40 |   /* Remove the custom bullet styling since we'll use native bullets */
 41 |   ul > li::before {
 42 |     content: none;
 43 |   }
 44 | 
 45 |   /* Ordered lists */
 46 |   ol {
 47 |     margin: 0;
 48 |     padding: 0 0 0 2em; /* Add left padding for numbers */
 49 |     list-style-position: outside;
 50 |   }
 51 | 
 52 |   li {
 53 |     margin: 0.5em 0; /* Add some vertical spacing between items */
 54 |     display: block; /* Change from grid to block */
 55 |   }
 56 | 
 57 |   /* Fix paragraph spacing inside list items */
 58 |   li p {
 59 |     margin: 0; /* Remove default paragraph margins */
 60 |     display: inline; /* Make paragraph inline with the number */
 61 |   }
 62 | 
 63 |   /* If you want to preserve some spacing between paragraphs within a list item */
 64 |   li p + p {
 65 |     margin-top: 0.5em;
 66 |   }
 67 | 
 68 |   /* Links */
 69 |   a {
 70 |     color: rgb(168 85 247);
 71 |     text-decoration: underline;
 72 |     font-weight: 500;
 73 |     
 74 |     &:hover {
 75 |       opacity: 0.8;
 76 |     }
 77 |   }
 78 | 
 79 |   /* Code blocks */
 80 |   pre {
 81 |     background-color: #1e1e1e;
 82 |     padding: 1em;
 83 |     border-radius: 4px;
 84 |     overflow-x: auto;
 85 |     margin: 1em 0;
 86 |   }
 87 | 
 88 |   code {
 89 |     font-family: 'Courier New', Courier, monospace;
 90 |     font-size: 0.9em;
 91 |     padding: 0 0.4em;
 92 |     background-color: #1e1e1e;
 93 |     border-radius: 3px;
 94 |   }
 95 | 
 96 |   /* Blockquotes */
 97 |   blockquote {
 98 |     border-left: 4px solid rgb(168 85 247);
 99 |     margin: 0;
100 |     padding-left: 1em;
101 |     font-style: italic;
102 |   }
103 | 
104 |   /* Tables */
105 |   table {
106 |     border-collapse: collapse;
107 |     width: 100%;
108 |     margin: 1em 0;
109 |   }
110 | 
111 |   th, td {
112 |     border: 1px solid #444;
113 |     padding: 0.5em;
114 |     text-align: left;
115 |   }
116 | 
117 |   th {
118 |     background-color: #333;
119 |   }
120 | 
121 |   /* Horizontal rule */
122 |   hr {
123 |     border: 0;
124 |     border-top: 1px solid #444;
125 |     margin: 2em 0;
126 |   }
127 | } 


--------------------------------------------------------------------------------
/frontend/nextjs/tailwind.config.ts:
--------------------------------------------------------------------------------
 1 | import type { Config } from 'tailwindcss';
 2 | 
 3 | const config: Config = {
 4 |   content: [
 5 |     './pages/**/*.{js,ts,jsx,tsx,mdx}',
 6 |     './components/**/*.{js,ts,jsx,tsx,mdx}',
 7 |     './app/**/*.{js,ts,jsx,tsx,mdx}',
 8 |   ],
 9 |   theme: {
10 |     screens: {
11 |       sm: '640px',
12 |       md: '768px',
13 |       lg: '898px',
14 |       // xl:"1024px"
15 |     },
16 |     container: {
17 |       center: true,
18 |     },
19 |     extend: {
20 |       backgroundImage: {
21 |         'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
22 |         'custom-gradient':
23 |           'linear-gradient(150deg, #1B1B16 1.28%, #565646 90.75%)',
24 |         'gradient-conic':
25 |           'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
26 |       },
27 |     },
28 |   },
29 |   plugins: [],
30 | };
31 | export default config;
32 | 


--------------------------------------------------------------------------------
/frontend/nextjs/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "compilerOptions": {
 3 |     "lib": ["dom", "dom.iterable", "esnext"],
 4 |     "allowJs": true,
 5 |     "skipLibCheck": true,
 6 |     "strict": true,
 7 |     "noEmit": true,
 8 |     "esModuleInterop": true,
 9 |     "module": "esnext",
10 |     "moduleResolution": "bundler",
11 |     "resolveJsonModule": true,
12 |     "isolatedModules": true,
13 |     "jsx": "preserve",
14 |     "incremental": true,
15 |     "plugins": [
16 |       {
17 |         "name": "next"
18 |       }
19 |     ],
20 |     "paths": {
21 |       "@/*": ["./*"]
22 |     }
23 |   },
24 |   "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts", "components/Task/ImagesCarousel.jsx"],
25 |   "exclude": ["node_modules"]
26 | }
27 | 


--------------------------------------------------------------------------------
/frontend/nextjs/types/data.ts:
--------------------------------------------------------------------------------
 1 | export interface BaseData {
 2 |   type: string;
 3 | }
 4 | 
 5 | export interface BasicData extends BaseData {
 6 |   type: 'basic';
 7 |   content: string;
 8 | }
 9 | 
10 | export interface LanggraphButtonData extends BaseData {
11 |   type: 'langgraphButton';
12 |   link: string;
13 | }
14 | 
15 | export interface DifferencesData extends BaseData {
16 |   type: 'differences';
17 |   content: string;
18 |   output: string;
19 | }
20 | 
21 | export interface QuestionData extends BaseData {
22 |   type: 'question';
23 |   content: string;
24 | }
25 | 
26 | export interface ChatData extends BaseData {
27 |   type: 'chat';
28 |   content: string;
29 | }
30 | 
31 | export type Data = BasicData | LanggraphButtonData | DifferencesData | QuestionData | ChatData;
32 | 
33 | export interface ChatBoxSettings {
34 |   report_source: string;
35 |   report_type: string;
36 |   tone: string;
37 | } 


--------------------------------------------------------------------------------
/frontend/nextjs/utils/consolidateBlocks.ts:
--------------------------------------------------------------------------------
 1 | export const consolidateSourceAndImageBlocks = (groupedData: any[]) => {
 2 |   // Consolidate sourceBlocks
 3 |   const consolidatedSourceBlock = {
 4 |     type: 'sourceBlock',
 5 |     items: groupedData
 6 |       .filter(item => item.type === 'sourceBlock')
 7 |       .flatMap(block => block.items || [])
 8 |       .filter((item, index, self) => 
 9 |         index === self.findIndex(t => t.url === item.url)
10 |       )
11 |   };
12 | 
13 |   // Consolidate imageBlocks
14 |   const consolidatedImageBlock = {
15 |     type: 'imagesBlock',
16 |     metadata: groupedData
17 |       .filter(item => item.type === 'imagesBlock')
18 |       .flatMap(block => block.metadata || [])
19 |   };
20 | 
21 |   // Remove all existing sourceBlocks and imageBlocks
22 |   groupedData = groupedData.filter(item => 
23 |     item.type !== 'sourceBlock' && item.type !== 'imagesBlock'
24 |   );
25 | 
26 |   // Add consolidated blocks if they have items
27 |   if (consolidatedSourceBlock.items.length > 0) {
28 |     groupedData.push(consolidatedSourceBlock);
29 |   }
30 |   if (consolidatedImageBlock.metadata.length > 0) {
31 |     groupedData.push(consolidatedImageBlock);
32 |   }
33 | 
34 |   return groupedData;
35 | };


--------------------------------------------------------------------------------
/frontend/pdf_styles.css:
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
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/academicResearchAgentAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/businessAnalystAgentAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/computerSecurityanalystAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/defaultAgentAvatar.JPG


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/favicon.ico


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/financeAgentAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/gptr-logo.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/mathAgentAvatar.png


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/frontend/static/travelAgentAvatar.png


--------------------------------------------------------------------------------
/gpt_researcher/__init__.py:
--------------------------------------------------------------------------------
1 | from .agent import GPTResearcher
2 | 
3 | __all__ = ['GPTResearcher']


--------------------------------------------------------------------------------
/gpt_researcher/actions/__init__.py:
--------------------------------------------------------------------------------
 1 | from .retriever import get_retriever, get_retrievers
 2 | from .query_processing import plan_research_outline
 3 | from .agent_creator import extract_json_with_regex, choose_agent
 4 | from .web_scraping import scrape_urls
 5 | from .report_generation import write_conclusion, summarize_url, generate_draft_section_titles, generate_report, write_report_introduction
 6 | from .markdown_processing import extract_headers, extract_sections, table_of_contents, add_references
 7 | from .utils import stream_output
 8 | 
 9 | __all__ = [
10 |     "get_retriever",
11 |     "get_retrievers",
12 |     "plan_research_outline",
13 |     "extract_json_with_regex",
14 |     "scrape_urls",
15 |     "write_conclusion",
16 |     "summarize_url",
17 |     "generate_draft_section_titles",
18 |     "generate_report",
19 |     "write_report_introduction",
20 |     "extract_headers",
21 |     "extract_sections",
22 |     "table_of_contents",
23 |     "add_references",
24 |     "stream_output",
25 |     "choose_agent"
26 | ]


--------------------------------------------------------------------------------
/gpt_researcher/actions/agent_creator.py:
--------------------------------------------------------------------------------
 1 | import json
 2 | import re
 3 | import json_repair
 4 | from ..utils.llm import create_chat_completion
 5 | from ..prompts import auto_agent_instructions
 6 | 
 7 | async def choose_agent(
 8 |     query, cfg, parent_query=None, cost_callback: callable = None, headers=None
 9 | ):
10 |     """
11 |     Chooses the agent automatically
12 |     Args:
13 |         parent_query: In some cases the research is conducted on a subtopic from the main query.
14 |         The parent query allows the agent to know the main context for better reasoning.
15 |         query: original query
16 |         cfg: Config
17 |         cost_callback: callback for calculating llm costs
18 | 
19 |     Returns:
20 |         agent: Agent name
21 |         agent_role_prompt: Agent role prompt
22 |     """
23 |     query = f"{parent_query} - {query}" if parent_query else f"{query}"
24 |     response = None  # Initialize response to ensure it's defined
25 | 
26 |     try:
27 |         response = await create_chat_completion(
28 |             model=cfg.smart_llm_model,
29 |             messages=[
30 |                 {"role": "system", "content": f"{auto_agent_instructions()}"},
31 |                 {"role": "user", "content": f"task: {query}"},
32 |             ],
33 |             temperature=0.15,
34 |             llm_provider=cfg.smart_llm_provider,
35 |             llm_kwargs=cfg.llm_kwargs,
36 |             cost_callback=cost_callback,
37 |         )
38 | 
39 |         agent_dict = json.loads(response)
40 |         return agent_dict["server"], agent_dict["agent_role_prompt"]
41 | 
42 |     except Exception as e:
43 |         print("⚠️ Error in reading JSON, attempting to repair JSON")
44 |         return await handle_json_error(response)
45 | 
46 | 
47 | async def handle_json_error(response):
48 |     try:
49 |         agent_dict = json_repair.loads(response)
50 |         if agent_dict.get("server") and agent_dict.get("agent_role_prompt"):
51 |             return agent_dict["server"], agent_dict["agent_role_prompt"]
52 |     except Exception as e:
53 |         print(f"Error using json_repair: {e}")
54 | 
55 |     json_string = extract_json_with_regex(response)
56 |     if json_string:
57 |         try:
58 |             json_data = json.loads(json_string)
59 |             return json_data["server"], json_data["agent_role_prompt"]
60 |         except json.JSONDecodeError as e:
61 |             print(f"Error decoding JSON: {e}")
62 | 
63 |     print("No JSON found in the string. Falling back to Default Agent.")
64 |     return "Default Agent", (
65 |         "You are an AI critical thinker research assistant. Your sole purpose is to write well written, "
66 |         "critically acclaimed, objective and structured reports on given text."
67 |     )
68 | 
69 | 
70 | def extract_json_with_regex(response):
71 |     json_match = re.search(r"{.*?}", response, re.DOTALL)
72 |     if json_match:
73 |         return json_match.group(0)
74 |     return None


--------------------------------------------------------------------------------
/gpt_researcher/config/__init__.py:
--------------------------------------------------------------------------------
1 | from .config import Config
2 | from .variables.base import BaseConfig
3 | from .variables.default import DEFAULT_CONFIG as DefaultConfig
4 | 
5 | __all__ = ["Config", "BaseConfig", "DefaultConfig"]
6 | 


--------------------------------------------------------------------------------
/gpt_researcher/config/variables/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/config/variables/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/config/variables/base.py:
--------------------------------------------------------------------------------
 1 | from typing import Union
 2 | from typing_extensions import TypedDict
 3 | 
 4 | 
 5 | class BaseConfig(TypedDict):
 6 |     RETRIEVER: str
 7 |     EMBEDDING: str
 8 |     SIMILARITY_THRESHOLD: float
 9 |     FAST_LLM: str
10 |     SMART_LLM: str
11 |     STRATEGIC_LLM: str
12 |     FAST_TOKEN_LIMIT: int
13 |     SMART_TOKEN_LIMIT: int
14 |     STRATEGIC_TOKEN_LIMIT: int
15 |     BROWSE_CHUNK_MAX_LENGTH: int
16 |     SUMMARY_TOKEN_LIMIT: int
17 |     TEMPERATURE: float
18 |     LLM_TEMPERATURE: float
19 |     USER_AGENT: str
20 |     MAX_SEARCH_RESULTS_PER_QUERY: int
21 |     MEMORY_BACKEND: str
22 |     TOTAL_WORDS: int
23 |     REPORT_FORMAT: str
24 |     CURATE_SOURCES: bool
25 |     MAX_ITERATIONS: int
26 |     LANGUAGE: str
27 |     AGENT_ROLE: Union[str, None]
28 |     SCRAPER: str
29 |     MAX_SUBTOPICS: int
30 |     REPORT_SOURCE: Union[str, None]
31 |     DOC_PATH: str
32 | 


--------------------------------------------------------------------------------
/gpt_researcher/config/variables/default.py:
--------------------------------------------------------------------------------
 1 | from .base import BaseConfig
 2 | 
 3 | DEFAULT_CONFIG: BaseConfig = {
 4 |     "RETRIEVER": "tavily",
 5 |     "EMBEDDING": "openai:text-embedding-3-small",
 6 |     "SIMILARITY_THRESHOLD": 0.42,
 7 |     "FAST_LLM": "openai:gpt-4o-mini",
 8 |     "SMART_LLM": "openai:gpt-4o-2024-11-20",
 9 |     "STRATEGIC_LLM": "openai:gpt-4o", # Can be used with gpt-o1
10 |     "FAST_TOKEN_LIMIT": 2000,
11 |     "SMART_TOKEN_LIMIT": 4000,
12 |     "STRATEGIC_TOKEN_LIMIT": 4000,
13 |     "BROWSE_CHUNK_MAX_LENGTH": 8192,
14 |     "CURATE_SOURCES": False,
15 |     "SUMMARY_TOKEN_LIMIT": 700,
16 |     "TEMPERATURE": 0.4,
17 |     "LLM_TEMPERATURE": 0.55,
18 |     "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
19 |     "MAX_SEARCH_RESULTS_PER_QUERY": 5,
20 |     "MEMORY_BACKEND": "local",
21 |     "TOTAL_WORDS": 1000,
22 |     "REPORT_FORMAT": "APA",
23 |     "MAX_ITERATIONS": 4,
24 |     "AGENT_ROLE": None,
25 |     "SCRAPER": "bs",
26 |     "MAX_SUBTOPICS": 3,
27 |     "LANGUAGE": "english",
28 |     "REPORT_SOURCE": "web",
29 |     "DOC_PATH": "./my-docs"
30 | }
31 | 


--------------------------------------------------------------------------------
/gpt_researcher/config/variables/test_local.json:
--------------------------------------------------------------------------------
1 | {
2 |   "DOC_PATH": "tests/docs"
3 | }
4 | 


--------------------------------------------------------------------------------
/gpt_researcher/context/__init__.py:
--------------------------------------------------------------------------------
1 | from .compression import ContextCompressor
2 | from .retriever import SearchAPIRetriever
3 | 
4 | __all__ = ['ContextCompressor', 'SearchAPIRetriever']
5 | 


--------------------------------------------------------------------------------
/gpt_researcher/context/retriever.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | from enum import Enum
 3 | from typing import Any, Dict, List, Optional
 4 | 
 5 | from langchain.callbacks.manager import CallbackManagerForRetrieverRun
 6 | from langchain.schema import Document
 7 | from langchain.schema.retriever import BaseRetriever
 8 | 
 9 | 
10 | class SearchAPIRetriever(BaseRetriever):
11 |     """Search API retriever."""
12 |     pages: List[Dict] = []
13 | 
14 |     def _get_relevant_documents(
15 |         self, query: str, *, run_manager: CallbackManagerForRetrieverRun
16 |     ) -> List[Document]:
17 | 
18 |         docs = [
19 |             Document(
20 |                 page_content=page.get("raw_content", ""),
21 |                 metadata={
22 |                     "title": page.get("title", ""),
23 |                     "source": page.get("url", ""),
24 |                 },
25 |             )
26 |             for page in self.pages
27 |         ]
28 | 
29 |         return docs
30 | 
31 | class SectionRetriever(BaseRetriever):
32 |     """
33 |     SectionRetriever:
34 |     This class is used to retrieve sections while avoiding redundant subtopics.
35 |     """
36 |     sections: List[Dict] = []
37 |     """
38 |     sections example:
39 |     [
40 |         {
41 |             "section_title": "Example Title",
42 |             "written_content": "Example content"
43 |         },
44 |         ...
45 |     ]
46 |     """
47 |     
48 |     def _get_relevant_documents(
49 |         self, query: str, *, run_manager: CallbackManagerForRetrieverRun
50 |     ) -> List[Document]:
51 | 
52 |         docs = [
53 |             Document(
54 |                 page_content=page.get("written_content", ""),
55 |                 metadata={
56 |                     "section_title": page.get("section_title", ""),
57 |                 },
58 |             )
59 |             for page in self.sections  # Changed 'self.pages' to 'self.sections'
60 |         ]
61 | 
62 |         return docs


--------------------------------------------------------------------------------
/gpt_researcher/document/__init__.py:
--------------------------------------------------------------------------------
1 | from .document import DocumentLoader
2 | from .langchain_document import LangChainDocumentLoader
3 | 
4 | __all__ = ['DocumentLoader', 'LangChainDocumentLoader']
5 | 


--------------------------------------------------------------------------------
/gpt_researcher/document/document.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import os
 3 | 
 4 | from langchain_community.document_loaders import (
 5 |     PyMuPDFLoader, 
 6 |     TextLoader, 
 7 |     UnstructuredCSVLoader, 
 8 |     UnstructuredExcelLoader,
 9 |     UnstructuredMarkdownLoader, 
10 |     UnstructuredPowerPointLoader,
11 |     UnstructuredWordDocumentLoader
12 | )
13 | 
14 | 
15 | class DocumentLoader:
16 | 
17 |     def __init__(self, path):
18 |         self.path = path
19 | 
20 |     async def load(self) -> list:
21 |         tasks = []
22 |         for root, dirs, files in os.walk(self.path):
23 |             for file in files:
24 |                 file_path = os.path.join(root, file)
25 |                 file_name, file_extension_with_dot = os.path.splitext(file_path)
26 |                 file_extension = file_extension_with_dot.strip(".")
27 |                 tasks.append(self._load_document(file_path, file_extension))
28 | 
29 |         docs = []
30 |         for pages in await asyncio.gather(*tasks):
31 |             for page in pages:
32 |                 if page.page_content:
33 |                     docs.append({
34 |                         "raw_content": page.page_content,
35 |                         "url": os.path.basename(page.metadata['source'])
36 |                     })
37 |                     
38 |         if not docs:
39 |             raise ValueError("🤷 Failed to load any documents!")
40 | 
41 |         return docs
42 | 
43 |     async def _load_document(self, file_path: str, file_extension: str) -> list:
44 |         ret_data = []
45 |         try:
46 |             loader_dict = {
47 |                 "pdf": PyMuPDFLoader(file_path),
48 |                 "txt": TextLoader(file_path),
49 |                 "doc": UnstructuredWordDocumentLoader(file_path),
50 |                 "docx": UnstructuredWordDocumentLoader(file_path),
51 |                 "pptx": UnstructuredPowerPointLoader(file_path),
52 |                 "csv": UnstructuredCSVLoader(file_path, mode="elements"),
53 |                 "xls": UnstructuredExcelLoader(file_path, mode="elements"),
54 |                 "xlsx": UnstructuredExcelLoader(file_path, mode="elements"),
55 |                 "md": UnstructuredMarkdownLoader(file_path)
56 |             }
57 | 
58 |             loader = loader_dict.get(file_extension, None)
59 |             if loader:
60 |                 ret_data = loader.load()
61 | 
62 |         except Exception as e:
63 |             print(f"Failed to load document : {file_path}")
64 |             print(e)
65 | 
66 |         return ret_data
67 | 


--------------------------------------------------------------------------------
/gpt_researcher/document/langchain_document.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import os
 3 | 
 4 | from langchain_core.documents import Document
 5 | from typing import List, Dict
 6 | 
 7 | 
 8 | # Supports the base Document class from langchain
 9 | # - https://github.com/langchain-ai/langchain/blob/master/libs/core/langchain_core/documents/base.py
10 | class LangChainDocumentLoader:
11 | 
12 |     def __init__(self, documents: List[Document]):
13 |         self.documents = documents
14 | 
15 |     async def load(self, metadata_source_index="title") -> List[Dict[str, str]]:
16 |         docs = []
17 |         for document in self.documents:
18 |             docs.append(
19 |                 {
20 |                     "raw_content": document.page_content,
21 |                     "url": document.metadata.get(metadata_source_index, ""),
22 |                 }
23 |             )
24 |         return docs
25 | 


--------------------------------------------------------------------------------
/gpt_researcher/llm_provider/__init__.py:
--------------------------------------------------------------------------------
1 | from .generic import GenericLLMProvider
2 | 
3 | __all__ = [
4 |     "GenericLLMProvider",
5 | ]
6 | 


--------------------------------------------------------------------------------
/gpt_researcher/llm_provider/generic/__init__.py:
--------------------------------------------------------------------------------
1 | from .base import GenericLLMProvider
2 | 
3 | __all__ = ["GenericLLMProvider"]


--------------------------------------------------------------------------------
/gpt_researcher/memory/__init__.py:
--------------------------------------------------------------------------------
1 | from .embeddings import Memory
2 | 


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/__init__.py:
--------------------------------------------------------------------------------
 1 | from .arxiv.arxiv import ArxivSearch
 2 | from .bing.bing import BingSearch
 3 | from .custom.custom import CustomRetriever
 4 | from .duckduckgo.duckduckgo import Duckduckgo
 5 | from .google.google import GoogleSearch
 6 | from .pubmed_central.pubmed_central import PubMedCentralSearch
 7 | from .searx.searx import SearxSearch
 8 | from .semantic_scholar.semantic_scholar import SemanticScholarSearch
 9 | from .searchapi.searchapi import SearchApiSearch
10 | from .serpapi.serpapi import SerpApiSearch
11 | from .serper.serper import SerperSearch
12 | from .tavily.tavily_search import TavilySearch
13 | from .exa.exa import ExaSearch
14 | 
15 | __all__ = [
16 |     "TavilySearch",
17 |     "CustomRetriever",
18 |     "Duckduckgo",
19 |     "SearchApiSearch",
20 |     "SerperSearch",
21 |     "SerpApiSearch",
22 |     "GoogleSearch",
23 |     "SearxSearch",
24 |     "BingSearch",
25 |     "ArxivSearch",
26 |     "SemanticScholarSearch",
27 |     "PubMedCentralSearch",
28 |     "ExaSearch"
29 | ]
30 | 


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/arxiv/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/arxiv/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/arxiv/arxiv.py:
--------------------------------------------------------------------------------
 1 | import arxiv
 2 | 
 3 | 
 4 | class ArxivSearch:
 5 |     """
 6 |     Arxiv API Retriever
 7 |     """
 8 |     def __init__(self, query, sort='Relevance'):
 9 |         self.arxiv = arxiv
10 |         self.query = query
11 |         assert sort in ['Relevance', 'SubmittedDate'], "Invalid sort criterion"
12 |         self.sort = arxiv.SortCriterion.SubmittedDate if sort == 'SubmittedDate' else arxiv.SortCriterion.Relevance
13 |         
14 | 
15 |     def search(self, max_results=5):
16 |         """
17 |         Performs the search
18 |         :param query:
19 |         :param max_results:
20 |         :return:
21 |         """
22 | 
23 |         arxiv_gen = list(arxiv.Client().results(
24 |         self.arxiv.Search(
25 |             query= self.query, #+
26 |             max_results=max_results,
27 |             sort_by=self.sort,
28 |         )))
29 | 
30 |         search_result = []
31 | 
32 |         for result in arxiv_gen:
33 | 
34 |             search_result.append({
35 |                 "title": result.title,
36 |                 "href": result.pdf_url,
37 |                 "body": result.summary,
38 |             })
39 |         
40 |         return search_result


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/bing/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/bing/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/bing/bing.py:
--------------------------------------------------------------------------------
 1 | # Bing Search Retriever
 2 | 
 3 | # libraries
 4 | import os
 5 | import requests
 6 | import json
 7 | import logging
 8 | 
 9 | 
10 | class BingSearch():
11 |     """
12 |     Bing Search Retriever
13 |     """
14 | 
15 |     def __init__(self, query):
16 |         """
17 |         Initializes the BingSearch object
18 |         Args:
19 |             query:
20 |         """
21 |         self.query = query
22 |         self.api_key = self.get_api_key()
23 |         self.logger = logging.getLogger(__name__)
24 | 
25 |     def get_api_key(self):
26 |         """
27 |         Gets the Bing API key
28 |         Returns:
29 | 
30 |         """
31 |         try:
32 |             api_key = os.environ["BING_API_KEY"]
33 |         except:
34 |             raise Exception(
35 |                 "Bing API key not found. Please set the BING_API_KEY environment variable.")
36 |         return api_key
37 | 
38 |     def search(self, max_results=7) -> list[dict[str]]:
39 |         """
40 |         Searches the query
41 |         Returns:
42 | 
43 |         """
44 |         print("Searching with query {0}...".format(self.query))
45 |         """Useful for general internet search queries using the Bing API."""
46 | 
47 |         # Search the query
48 |         url = "https://api.bing.microsoft.com/v7.0/search"
49 | 
50 |         headers = {
51 |             'Ocp-Apim-Subscription-Key': self.api_key,
52 |             'Content-Type': 'application/json'
53 |         }
54 |         params = {
55 |             "responseFilter": "Webpages",
56 |             "q": self.query,
57 |             "count": max_results,
58 |             "setLang": "en-GB",
59 |             "textDecorations": False,
60 |             "textFormat": "HTML",
61 |             "safeSearch": "Strict"
62 |         }
63 | 
64 |         resp = requests.get(url, headers=headers, params=params)
65 | 
66 |         # Preprocess the results
67 |         if resp is None:
68 |             return []
69 |         try:
70 |             search_results = json.loads(resp.text)
71 |             results = search_results["webPages"]["value"]
72 |         except Exception as e:
73 |             self.logger.error(
74 |                 f"Error parsing Bing search results: {e}. Resulting in empty response.")
75 |             return []
76 |         if search_results is None:
77 |             self.logger.warning(f"No search results found for query: {self.query}")
78 |             return []
79 |         search_results = []
80 | 
81 |         # Normalize the results to match the format of the other search APIs
82 |         for result in results:
83 |             # skip youtube results
84 |             if "youtube.com" in result["url"]:
85 |                 continue
86 |             search_result = {
87 |                 "title": result["name"],
88 |                 "href": result["url"],
89 |                 "body": result["snippet"],
90 |             }
91 |             search_results.append(search_result)
92 | 
93 |         return search_results
94 | 


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/custom/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/custom/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/custom/custom.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Dict, List, Optional
 2 | import requests
 3 | import os
 4 | 
 5 | 
 6 | class CustomRetriever:
 7 |     """
 8 |     Custom API Retriever
 9 |     """
10 | 
11 |     def __init__(self, query: str):
12 |         self.endpoint = os.getenv('RETRIEVER_ENDPOINT')
13 |         if not self.endpoint:
14 |             raise ValueError("RETRIEVER_ENDPOINT environment variable not set")
15 | 
16 |         self.params = self._populate_params()
17 |         self.query = query
18 | 
19 |     def _populate_params(self) -> Dict[str, Any]:
20 |         """
21 |         Populates parameters from environment variables prefixed with 'RETRIEVER_ARG_'
22 |         """
23 |         return {
24 |             key[len('RETRIEVER_ARG_'):].lower(): value
25 |             for key, value in os.environ.items()
26 |             if key.startswith('RETRIEVER_ARG_')
27 |         }
28 | 
29 |     def search(self, max_results: int = 5) -> Optional[List[Dict[str, Any]]]:
30 |         """
31 |         Performs the search using the custom retriever endpoint.
32 | 
33 |         :param max_results: Maximum number of results to return (not currently used)
34 |         :return: JSON response in the format:
35 |             [
36 |               {
37 |                 "url": "http://example.com/page1",
38 |                 "raw_content": "Content of page 1"
39 |               },
40 |               {
41 |                 "url": "http://example.com/page2",
42 |                 "raw_content": "Content of page 2"
43 |               }
44 |             ]
45 |         """
46 |         try:
47 |             response = requests.get(self.endpoint, params={**self.params, 'query': self.query})
48 |             response.raise_for_status()
49 |             return response.json()
50 |         except requests.RequestException as e:
51 |             print(f"Failed to retrieve search results: {e}")
52 |             return None


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/duckduckgo/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/duckduckgo/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/duckduckgo/duckduckgo.py:
--------------------------------------------------------------------------------
 1 | from itertools import islice
 2 | from ..utils import check_pkg
 3 | 
 4 | 
 5 | class Duckduckgo:
 6 |     """
 7 |     Duckduckgo API Retriever
 8 |     """
 9 |     def __init__(self, query):
10 |         check_pkg('duckduckgo_search')
11 |         from duckduckgo_search import DDGS
12 |         self.ddg = DDGS()
13 |         self.query = query
14 | 
15 |     def search(self, max_results=5):
16 |         """
17 |         Performs the search
18 |         :param query:
19 |         :param max_results:
20 |         :return:
21 |         """
22 |         try:
23 |             search_response = self.ddg.text(self.query, region='wt-wt', max_results=max_results)
24 |         except Exception as e:
25 |             print(f"Error: {e}. Failed fetching sources. Resulting in empty response.")
26 |             search_response = []
27 |         return search_response


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/exa/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/exa/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/google/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/google/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/pubmed_central/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/pubmed_central/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/searchapi/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/searchapi/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/searchapi/searchapi.py:
--------------------------------------------------------------------------------
 1 | # SearchApi Retriever
 2 | 
 3 | # libraries
 4 | import os
 5 | import requests
 6 | import urllib.parse
 7 | 
 8 | 
 9 | class SearchApiSearch():
10 |     """
11 |     SearchApi Retriever
12 |     """
13 |     def __init__(self, query):
14 |         """
15 |         Initializes the SearchApiSearch object
16 |         Args:
17 |             query:
18 |         """
19 |         self.query = query
20 |         self.api_key = self.get_api_key()
21 | 
22 |     def get_api_key(self):
23 |         """
24 |         Gets the SearchApi API key
25 |         Returns:
26 | 
27 |         """
28 |         try:
29 |             api_key = os.environ["SEARCHAPI_API_KEY"]
30 |         except:
31 |             raise Exception("SearchApi key not found. Please set the SEARCHAPI_API_KEY environment variable. "
32 |                             "You can get a key at https://www.searchapi.io/")
33 |         return api_key
34 | 
35 |     def search(self, max_results=7):
36 |         """
37 |         Searches the query
38 |         Returns:
39 | 
40 |         """
41 |         print("SearchApiSearch: Searching with query {0}...".format(self.query))
42 |         """Useful for general internet search queries using SearchApi."""
43 | 
44 | 
45 |         url = "https://www.searchapi.io/api/v1/search"
46 |         params = {
47 |             "q": self.query,
48 |             "engine": "google",
49 |         }
50 | 
51 |         headers = {
52 |             'Content-Type': 'application/json',
53 |             'Authorization': f'Bearer {self.api_key}',
54 |             'X-SearchApi-Source': 'gpt-researcher'
55 |         }
56 | 
57 |         encoded_url = url + "?" + urllib.parse.urlencode(params)
58 |         search_response = []
59 | 
60 |         try:
61 |             response = requests.get(encoded_url, headers=headers, timeout=20)
62 |             if response.status_code == 200:
63 |                 search_results = response.json()
64 |                 if search_results:
65 |                     results = search_results["organic_results"]
66 |                     results_processed = 0
67 |                     for result in results:
68 |                         # skip youtube results
69 |                         if "youtube.com" in result["link"]:
70 |                             continue
71 |                         if results_processed >= max_results:
72 |                             break
73 |                         search_result = {
74 |                             "title": result["title"],
75 |                             "href": result["link"],
76 |                             "body": result["snippet"],
77 |                         }
78 |                         search_response.append(search_result)
79 |                         results_processed += 1
80 |         except Exception as e:
81 |             print(f"Error: {e}. Failed fetching sources. Resulting in empty response.")
82 |             search_response = []
83 | 
84 |         return search_response
85 | 


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/searx/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/searx/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/searx/searx.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | import json
 3 | import requests
 4 | from typing import List, Dict
 5 | from urllib.parse import urljoin
 6 | 
 7 | 
 8 | class SearxSearch():
 9 |     """
10 |     SearxNG API Retriever
11 |     """
12 |     def __init__(self, query: str):
13 |         """
14 |         Initializes the SearxSearch object
15 |         Args:
16 |             query: Search query string
17 |         """
18 |         self.query = query
19 |         self.base_url = self.get_searxng_url()
20 | 
21 |     def get_searxng_url(self) -> str:
22 |         """
23 |         Gets the SearxNG instance URL from environment variables
24 |         Returns:
25 |             str: Base URL of SearxNG instance
26 |         """
27 |         try:
28 |             base_url = os.environ["SEARX_URL"]
29 |             if not base_url.endswith('/'):
30 |                 base_url += '/'
31 |             return base_url
32 |         except KeyError:
33 |             raise Exception(
34 |                 "SearxNG URL not found. Please set the SEARX_URL environment variable. "
35 |                 "You can find public instances at https://searx.space/"
36 |             )
37 | 
38 |     def search(self, max_results: int = 10) -> List[Dict[str, str]]:
39 |         """
40 |         Searches the query using SearxNG API
41 |         Args:
42 |             max_results: Maximum number of results to return
43 |         Returns:
44 |             List of dictionaries containing search results
45 |         """
46 |         search_url = urljoin(self.base_url, "search")
47 |         
48 |         params = {
49 |             # The search query. 
50 |             'q': self.query, 
51 |             # Output format of results. Format needs to be activated in searxng config.
52 |             'format': 'json'
53 |         }
54 | 
55 |         try:
56 |             response = requests.get(
57 |                 search_url,
58 |                 params=params,
59 |                 headers={'Accept': 'application/json'}
60 |             )
61 |             response.raise_for_status()
62 |             results = response.json()
63 | 
64 |             # Normalize results to match the expected format
65 |             search_response = []
66 |             for result in results.get('results', [])[:max_results]:
67 |                 search_response.append({
68 |                     "href": result.get('url', ''),
69 |                     "body": result.get('content', '')
70 |                 })
71 | 
72 |             return search_response
73 | 
74 |         except requests.exceptions.RequestException as e:
75 |             raise Exception(f"Error querying SearxNG: {str(e)}")
76 |         except json.JSONDecodeError:
77 |             raise Exception("Error parsing SearxNG response")
78 | 


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/semantic_scholar/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/semantic_scholar/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/semantic_scholar/semantic_scholar.py:
--------------------------------------------------------------------------------
 1 | from typing import Dict, List
 2 | 
 3 | import requests
 4 | 
 5 | 
 6 | class SemanticScholarSearch:
 7 |     """
 8 |     Semantic Scholar API Retriever
 9 |     """
10 | 
11 |     BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
12 |     VALID_SORT_CRITERIA = ["relevance", "citationCount", "publicationDate"]
13 | 
14 |     def __init__(self, query: str, sort: str = "relevance"):
15 |         """
16 |         Initialize the SemanticScholarSearch class with a query and sort criterion.
17 | 
18 |         :param query: Search query string
19 |         :param sort: Sort criterion ('relevance', 'citationCount', 'publicationDate')
20 |         """
21 |         self.query = query
22 |         assert sort in self.VALID_SORT_CRITERIA, "Invalid sort criterion"
23 |         self.sort = sort.lower()
24 | 
25 |     def search(self, max_results: int = 20) -> List[Dict[str, str]]:
26 |         """
27 |         Perform the search on Semantic Scholar and return results.
28 | 
29 |         :param max_results: Maximum number of results to retrieve
30 |         :return: List of dictionaries containing title, href, and body of each paper
31 |         """
32 |         params = {
33 |             "query": self.query,
34 |             "limit": max_results,
35 |             "fields": "title,abstract,url,venue,year,authors,isOpenAccess,openAccessPdf",
36 |             "sort": self.sort,
37 |         }
38 | 
39 |         try:
40 |             response = requests.get(self.BASE_URL, params=params)
41 |             response.raise_for_status()
42 |         except requests.RequestException as e:
43 |             print(f"An error occurred while accessing Semantic Scholar API: {e}")
44 |             return []
45 | 
46 |         results = response.json().get("data", [])
47 |         search_result = []
48 | 
49 |         for result in results:
50 |             if result.get("isOpenAccess") and result.get("openAccessPdf"):
51 |                 search_result.append(
52 |                     {
53 |                         "title": result.get("title", "No Title"),
54 |                         "href": result["openAccessPdf"].get("url", "No URL"),
55 |                         "body": result.get("abstract", "Abstract not available"),
56 |                     }
57 |                 )
58 | 
59 |         return search_result
60 | 


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/serpapi/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/serpapi/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/serpapi/serpapi.py:
--------------------------------------------------------------------------------
 1 | # SerpApi Retriever
 2 | 
 3 | # libraries
 4 | import os
 5 | import requests
 6 | import urllib.parse
 7 | 
 8 | 
 9 | class SerpApiSearch():
10 |     """
11 |     SerpApi Retriever
12 |     """
13 |     def __init__(self, query):
14 |         """
15 |         Initializes the SerpApiSearch object
16 |         Args:
17 |             query:
18 |         """
19 |         self.query = query
20 |         self.api_key = self.get_api_key()
21 | 
22 |     def get_api_key(self):
23 |         """
24 |         Gets the SerpApi API key
25 |         Returns:
26 | 
27 |         """
28 |         try:
29 |             api_key = os.environ["SERPAPI_API_KEY"]
30 |         except:
31 |             raise Exception("SerpApi API key not found. Please set the SERPAPI_API_KEY environment variable. "
32 |                             "You can get a key at https://serpapi.com/")
33 |         return api_key
34 | 
35 |     def search(self, max_results=7):
36 |         """
37 |         Searches the query
38 |         Returns:
39 | 
40 |         """
41 |         print("SerpApiSearch: Searching with query {0}...".format(self.query))
42 |         """Useful for general internet search queries using SerpApi."""
43 | 
44 | 
45 |         url = "https://serpapi.com/search.json"
46 |         params = {
47 |             "q": self.query,
48 |             "api_key": self.api_key
49 |         }
50 |         encoded_url = url + "?" + urllib.parse.urlencode(params)
51 |         search_response = []
52 |         try:
53 |             response = requests.get(encoded_url, timeout=10)
54 |             if response.status_code == 200:
55 |                 search_results = response.json()
56 |                 if search_results:
57 |                     results = search_results["organic_results"]
58 |                     results_processed = 0
59 |                     for result in results:
60 |                         # skip youtube results
61 |                         if "youtube.com" in result["link"]:
62 |                             continue
63 |                         if results_processed >= max_results:
64 |                             break
65 |                         search_result = {
66 |                             "title": result["title"],
67 |                             "href": result["link"],
68 |                             "body": result["snippet"],
69 |                         }
70 |                         search_response.append(search_result)
71 |                         results_processed += 1
72 |         except Exception as e:
73 |             print(f"Error: {e}. Failed fetching sources. Resulting in empty response.")
74 |             search_response = []
75 | 
76 |         return search_response
77 | 


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/serper/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/serper/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/serper/serper.py:
--------------------------------------------------------------------------------
 1 | # Google Serper Retriever
 2 | 
 3 | # libraries
 4 | import os
 5 | import requests
 6 | import json
 7 | 
 8 | 
 9 | class SerperSearch():
10 |     """
11 |     Google Serper Retriever
12 |     """
13 |     def __init__(self, query):
14 |         """
15 |         Initializes the SerperSearch object
16 |         Args:
17 |             query:
18 |         """
19 |         self.query = query
20 |         self.api_key = self.get_api_key()
21 | 
22 |     def get_api_key(self):
23 |         """
24 |         Gets the Serper API key
25 |         Returns:
26 | 
27 |         """
28 |         try:
29 |             api_key = os.environ["SERPER_API_KEY"]
30 |         except:
31 |             raise Exception("Serper API key not found. Please set the SERPER_API_KEY environment variable. "
32 |                             "You can get a key at https://serper.dev/")
33 |         return api_key
34 | 
35 |     def search(self, max_results=7):
36 |         """
37 |         Searches the query
38 |         Returns:
39 | 
40 |         """
41 |         print("Searching with query {0}...".format(self.query))
42 |         """Useful for general internet search queries using the Serp API."""
43 | 
44 | 
45 |         # Search the query (see https://serper.dev/playground for the format)
46 |         url = "https://google.serper.dev/search"
47 | 
48 |         headers = {
49 |         'X-API-KEY': self.api_key,
50 |         'Content-Type': 'application/json'
51 |         }
52 |         data = json.dumps({"q": self.query, "num": max_results})
53 | 
54 |         resp = requests.request("POST", url, timeout=10, headers=headers, data=data)
55 | 
56 |         # Preprocess the results
57 |         if resp is None:
58 |             return
59 |         try:
60 |             search_results = json.loads(resp.text)
61 |         except Exception:
62 |             return
63 |         if search_results is None:
64 |             return
65 | 
66 |         results = search_results["organic"]
67 |         search_results = []
68 | 
69 |         # Normalize the results to match the format of the other search APIs
70 |         for result in results:
71 |             # skip youtube results
72 |             if "youtube.com" in result["link"]:
73 |                 continue
74 |             search_result = {
75 |                 "title": result["title"],
76 |                 "href": result["link"],
77 |                 "body": result["snippet"],
78 |             }
79 |             search_results.append(search_result)
80 | 
81 |         return search_results
82 | 


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/tavily/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/retrievers/tavily/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/retrievers/utils.py:
--------------------------------------------------------------------------------
 1 | import importlib.util
 2 | import os
 3 | 
 4 | VALID_RETRIEVERS = [
 5 |     "arxiv",
 6 |     "bing",
 7 |     "custom",
 8 |     "duckduckgo",
 9 |     "exa",
10 |     "google",
11 |     "searchapi",
12 |     "searx",
13 |     "semantic_scholar",
14 |     "serpapi",
15 |     "serper",
16 |     "tavily",
17 |     "pubmed_central",
18 | ]
19 | 
20 | 
21 | def check_pkg(pkg: str) -> None:
22 |     if not importlib.util.find_spec(pkg):
23 |         pkg_kebab = pkg.replace("_", "-")
24 |         raise ImportError(
25 |             f"Unable to import {pkg_kebab}. Please install with "
26 |             f"`pip install -U {pkg_kebab}`"
27 |         )
28 | 
29 | # Get a list of all retriever names to be used as validators for supported retrievers
30 | def get_all_retriever_names() -> list:
31 |     try:
32 |         current_dir = os.path.dirname(__file__)
33 | 
34 |         all_items = os.listdir(current_dir)
35 | 
36 |         # Filter out only the directories, excluding __pycache__
37 |         retrievers = [item for item in all_items if os.path.isdir(os.path.join(current_dir, item))]
38 |     except Exception as e:
39 |         print(f"Error in get_all_retriever_names: {e}")
40 |         retrievers = VALID_RETRIEVERS
41 |     
42 |     return retrievers
43 | 


--------------------------------------------------------------------------------
/gpt_researcher/scraper/__init__.py:
--------------------------------------------------------------------------------
 1 | 
 2 | from .beautiful_soup.beautiful_soup import BeautifulSoupScraper
 3 | from .web_base_loader.web_base_loader import WebBaseLoaderScraper
 4 | from .arxiv.arxiv import ArxivScraper
 5 | from .pymupdf.pymupdf import PyMuPDFScraper
 6 | from .browser.browser import BrowserScraper
 7 | from .scraper import Scraper
 8 | 
 9 | __all__ = [
10 |     "BeautifulSoupScraper",
11 |     "WebBaseLoaderScraper",
12 |     "ArxivScraper",
13 |     "PyMuPDFScraper",
14 |     "BrowserScraper",
15 |     "Scraper"
16 | ]


--------------------------------------------------------------------------------
/gpt_researcher/scraper/arxiv/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/scraper/arxiv/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/scraper/arxiv/arxiv.py:
--------------------------------------------------------------------------------
 1 | from langchain_community.retrievers import ArxivRetriever
 2 | 
 3 | 
 4 | class ArxivScraper:
 5 | 
 6 |     def __init__(self, link, session=None):
 7 |         self.link = link
 8 |         self.session = session
 9 | 
10 |     def scrape(self):
11 |         """
12 |         The function scrapes relevant documents from Arxiv based on a given link and returns the content
13 |         of the first document.
14 |         
15 |         Returns:
16 |           The code is returning the page content of the first document retrieved by the ArxivRetriever
17 |         for a given query extracted from the link.
18 |         """
19 |         query = self.link.split("/")[-1]
20 |         retriever = ArxivRetriever(load_max_docs=2, doc_content_chars_max=None)
21 |         docs = retriever.invoke(query=query)
22 |         return docs[0].page_content
23 | 


--------------------------------------------------------------------------------
/gpt_researcher/scraper/beautiful_soup/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/scraper/beautiful_soup/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/scraper/browser/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/scraper/browser/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/scraper/browser/js/overlay.js:
--------------------------------------------------------------------------------
 1 | const overlay = document.createElement('div');
 2 | Object.assign(overlay.style, {
 3 |     position: 'fixed',
 4 |     zIndex: 999999,
 5 |     top: 0,
 6 |     left: 0,
 7 |     width: '100%',
 8 |     height: '100%',
 9 |     background: 'rgba(0, 0, 0, 0.7)',
10 |     color: '#fff',
11 |     fontSize: '24px',
12 |     fontWeight: 'bold',
13 |     display: 'flex',
14 |     justifyContent: 'center',
15 |     alignItems: 'center',
16 | });
17 | const textContent = document.createElement('div');
18 | Object.assign(textContent.style, {
19 |     textAlign: 'center',
20 | });
21 | textContent.textContent = 'GPT Researcher: Analyzing Page';
22 | overlay.appendChild(textContent);
23 | document.body.append(overlay);
24 | document.body.style.overflow = 'hidden';
25 | let dotCount = 0;
26 | setInterval(() => {
27 |     textContent.textContent = 'GPT Researcher: Analyzing Page' + '.'.repeat(dotCount);
28 |     dotCount = (dotCount + 1) % 4;
29 | }, 1000);
30 | 


--------------------------------------------------------------------------------
/gpt_researcher/scraper/browser/processing/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/scraper/browser/processing/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/scraper/browser/processing/html.py:
--------------------------------------------------------------------------------
 1 | """HTML processing functions"""
 2 | from __future__ import annotations
 3 | 
 4 | from bs4 import BeautifulSoup
 5 | from requests.compat import urljoin
 6 | 
 7 | 
 8 | def extract_hyperlinks(soup: BeautifulSoup, base_url: str) -> list[tuple[str, str]]:
 9 |     """Extract hyperlinks from a BeautifulSoup object
10 | 
11 |     Args:
12 |         soup (BeautifulSoup): The BeautifulSoup object
13 |         base_url (str): The base URL
14 | 
15 |     Returns:
16 |         List[Tuple[str, str]]: The extracted hyperlinks
17 |     """
18 |     return [
19 |         (link.text, urljoin(base_url, link["href"]))
20 |         for link in soup.find_all("a", href=True)
21 |     ]
22 | 
23 | 
24 | def format_hyperlinks(hyperlinks: list[tuple[str, str]]) -> list[str]:
25 |     """Format hyperlinks to be displayed to the user
26 | 
27 |     Args:
28 |         hyperlinks (List[Tuple[str, str]]): The hyperlinks to format
29 | 
30 |     Returns:
31 |         List[str]: The formatted hyperlinks
32 |     """
33 |     return [f"{link_text} ({link_url})" for link_text, link_url in hyperlinks]
34 | 


--------------------------------------------------------------------------------
/gpt_researcher/scraper/browser/processing/scrape_skills.py:
--------------------------------------------------------------------------------
 1 | from langchain_community.document_loaders import PyMuPDFLoader
 2 | from langchain_community.retrievers import ArxivRetriever
 3 | 
 4 | 
 5 | def scrape_pdf_with_pymupdf(url) -> str:
 6 |     """Scrape a pdf with pymupdf
 7 | 
 8 |     Args:
 9 |         url (str): The url of the pdf to scrape
10 | 
11 |     Returns:
12 |         str: The text scraped from the pdf
13 |     """
14 |     loader = PyMuPDFLoader(url)
15 |     doc = loader.load()
16 |     return str(doc)
17 | 
18 | 
19 | def scrape_pdf_with_arxiv(query) -> str:
20 |     """Scrape a pdf with arxiv
21 |     default document length of 70000 about ~15 pages or None for no limit
22 | 
23 |     Args:
24 |         query (str): The query to search for
25 | 
26 |     Returns:
27 |         str: The text scraped from the pdf
28 |     """
29 |     retriever = ArxivRetriever(load_max_docs=2, doc_content_chars_max=None)
30 |     docs = retriever.get_relevant_documents(query=query)
31 |     return docs[0].page_content


--------------------------------------------------------------------------------
/gpt_researcher/scraper/pymupdf/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/scraper/pymupdf/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/scraper/pymupdf/pymupdf.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | import requests
 3 | import tempfile
 4 | from urllib.parse import urlparse
 5 | from langchain_community.document_loaders import PyMuPDFLoader
 6 | 
 7 | 
 8 | class PyMuPDFScraper:
 9 | 
10 |     def __init__(self, link, session=None):
11 |         """
12 |         Initialize the scraper with a link and an optional session.
13 | 
14 |         Args:
15 |           link (str): The URL or local file path of the PDF document.
16 |           session (requests.Session, optional): An optional session for making HTTP requests.
17 |         """
18 |         self.link = link
19 |         self.session = session
20 | 
21 |     def is_url(self) -> bool:
22 |         """
23 |         Check if the provided `link` is a valid URL.
24 | 
25 |         Returns:
26 |           bool: True if the link is a valid URL, False otherwise.
27 |         """
28 |         try:
29 |             result = urlparse(self.link)
30 |             return all([result.scheme, result.netloc])  # Check for valid scheme and network location
31 |         except Exception:
32 |             return False
33 | 
34 |     def scrape(self) -> str:
35 |         """
36 |         The `scrape` function uses PyMuPDFLoader to load a document from the provided link (either URL or local file)
37 |         and returns the document as a string.
38 | 
39 |         Returns:
40 |           str: A string representation of the loaded document.
41 |         """
42 |         try:
43 |             if self.is_url():
44 |                 response = requests.get(self.link, timeout=5, stream=True)
45 |                 response.raise_for_status()
46 | 
47 |                 with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
48 |                     temp_filename = temp_file.name  # Get the temporary file name
49 |                     for chunk in response.iter_content(chunk_size=8192):
50 |                         temp_file.write(chunk)  # Write the downloaded content to the temporary file
51 | 
52 |                 loader = PyMuPDFLoader(temp_filename)
53 |                 doc = loader.load()
54 | 
55 |                 os.remove(temp_filename)
56 |             else:
57 |                 loader = PyMuPDFLoader(self.link)
58 |                 doc = loader.load()
59 | 
60 |             return str(doc)
61 | 
62 |         except requests.exceptions.Timeout:
63 |             print(f"Download timed out. Please check the link : {self.link}")
64 |         except Exception as e:
65 |             print(f"Error loading PDF : {self.link} {e}")
66 | 


--------------------------------------------------------------------------------
/gpt_researcher/scraper/web_base_loader/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/scraper/web_base_loader/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/scraper/web_base_loader/web_base_loader.py:
--------------------------------------------------------------------------------
 1 | from bs4 import BeautifulSoup
 2 | from urllib.parse import urljoin
 3 | import requests
 4 | from ..utils import get_relevant_images, extract_title
 5 | 
 6 | class WebBaseLoaderScraper:
 7 | 
 8 |     def __init__(self, link, session=None):
 9 |         self.link = link
10 |         self.session = session or requests.Session()
11 | 
12 |     def scrape(self) -> tuple:
13 |         """
14 |         This Python function scrapes content from a webpage using a WebBaseLoader object and returns the
15 |         concatenated page content.
16 |         
17 |         Returns:
18 |           The `scrape` method is returning a string variable named `content` which contains the
19 |         concatenated page content from the documents loaded by the `WebBaseLoader`. If an exception
20 |         occurs during the process, an error message is printed and an empty string is returned.
21 |         """
22 |         try:
23 |             from langchain_community.document_loaders import WebBaseLoader
24 |             loader = WebBaseLoader(self.link)
25 |             loader.requests_kwargs = {"verify": False}
26 |             docs = loader.load()
27 |             content = ""
28 | 
29 |             for doc in docs:
30 |                 content += doc.page_content
31 | 
32 |             response = self.session.get(self.link)
33 |             soup = BeautifulSoup(response.content, 'html.parser')
34 |             image_urls = get_relevant_images(soup, self.link)
35 |             
36 |             # Extract the title using the utility function
37 |             title = extract_title(soup)
38 | 
39 |             return content, image_urls, title
40 | 
41 |         except Exception as e:
42 |             print("Error! : " + str(e))
43 |             return "", [], ""
44 | 


--------------------------------------------------------------------------------
/gpt_researcher/skills/__init__.py:
--------------------------------------------------------------------------------
 1 | from .context_manager import ContextManager
 2 | from .researcher import ResearchConductor
 3 | from .writer import ReportGenerator
 4 | from .browser import BrowserManager
 5 | from .curator import SourceCurator
 6 | 
 7 | __all__ = [
 8 |     'ResearchConductor',
 9 |     'ReportGenerator',
10 |     'ContextManager',
11 |     'BrowserManager',
12 |     'SourceCurator'
13 | ]
14 | 


--------------------------------------------------------------------------------
/gpt_researcher/utils/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/gpt_researcher/utils/__init__.py


--------------------------------------------------------------------------------
/gpt_researcher/utils/costs.py:
--------------------------------------------------------------------------------
 1 | import tiktoken
 2 | 
 3 | # Per OpenAI Pricing Page: https://openai.com/api/pricing/
 4 | ENCODING_MODEL = "o200k_base"
 5 | INPUT_COST_PER_TOKEN = 0.000005
 6 | OUTPUT_COST_PER_TOKEN = 0.000015
 7 | IMAGE_INFERENCE_COST = 0.003825
 8 | EMBEDDING_COST = 0.02 / 1000000 # Assumes new ada-3-small
 9 | 
10 | 
11 | # Cost estimation is via OpenAI libraries and models. May vary for other models
12 | def estimate_llm_cost(input_content: str, output_content: str) -> float:
13 |     encoding = tiktoken.get_encoding(ENCODING_MODEL)
14 |     input_tokens = encoding.encode(input_content)
15 |     output_tokens = encoding.encode(output_content)
16 |     input_costs = len(input_tokens) * INPUT_COST_PER_TOKEN
17 |     output_costs = len(output_tokens) * OUTPUT_COST_PER_TOKEN
18 |     return input_costs + output_costs
19 | 
20 | 
21 | def estimate_embedding_cost(model, docs):
22 |     encoding = tiktoken.encoding_for_model(model)
23 |     total_tokens = sum(len(encoding.encode(str(doc))) for doc in docs)
24 |     return total_tokens * EMBEDDING_COST
25 | 
26 | 


--------------------------------------------------------------------------------
/gpt_researcher/utils/enum.py:
--------------------------------------------------------------------------------
 1 | from enum import Enum
 2 | 
 3 | 
 4 | class ReportType(Enum):
 5 |     ResearchReport = "research_report"
 6 |     ResourceReport = "resource_report"
 7 |     OutlineReport = "outline_report"
 8 |     CustomReport = "custom_report"
 9 |     DetailedReport = "detailed_report"
10 |     SubtopicReport = "subtopic_report"
11 | 
12 | 
13 | class ReportSource(Enum):
14 |     Web = "web"
15 |     Local = "local"
16 |     LangChainDocuments = "langchain_documents"
17 |     LangChainVectorStore = "langchain_vectorstore"
18 |     Static = "static"
19 |     Hybrid = "hybrid"
20 | 
21 | 
22 | class Tone(Enum):
23 |     Objective = "Objective (impartial and unbiased presentation of facts and findings)"
24 |     Formal = "Formal (adheres to academic standards with sophisticated language and structure)"
25 |     Analytical = (
26 |         "Analytical (critical evaluation and detailed examination of data and theories)"
27 |     )
28 |     Persuasive = (
29 |         "Persuasive (convincing the audience of a particular viewpoint or argument)"
30 |     )
31 |     Informative = (
32 |         "Informative (providing clear and comprehensive information on a topic)"
33 |     )
34 |     Explanatory = "Explanatory (clarifying complex concepts and processes)"
35 |     Descriptive = (
36 |         "Descriptive (detailed depiction of phenomena, experiments, or case studies)"
37 |     )
38 |     Critical = "Critical (judging the validity and relevance of the research and its conclusions)"
39 |     Comparative = "Comparative (juxtaposing different theories, data, or methods to highlight differences and similarities)"
40 |     Speculative = "Speculative (exploring hypotheses and potential implications or future research directions)"
41 |     Reflective = "Reflective (considering the research process and personal insights or experiences)"
42 |     Narrative = (
43 |         "Narrative (telling a story to illustrate research findings or methodologies)"
44 |     )
45 |     Humorous = "Humorous (light-hearted and engaging, usually to make the content more relatable)"
46 |     Optimistic = "Optimistic (highlighting positive findings and potential benefits)"
47 |     Pessimistic = (
48 |         "Pessimistic (focusing on limitations, challenges, or negative outcomes)"
49 |     )
50 | 


--------------------------------------------------------------------------------
/gpt_researcher/utils/logging_config.py:
--------------------------------------------------------------------------------
 1 | import logging
 2 | import json
 3 | import os
 4 | from datetime import datetime
 5 | from pathlib import Path
 6 | 
 7 | class JSONResearchHandler:
 8 |     def __init__(self, json_file):
 9 |         self.json_file = json_file
10 |         self.research_data = {
11 |             "timestamp": datetime.now().isoformat(),
12 |             "events": [],
13 |             "content": {
14 |                 "query": "",
15 |                 "sources": [],
16 |                 "context": [],
17 |                 "report": "",
18 |                 "costs": 0.0
19 |             }
20 |         }
21 | 
22 |     def log_event(self, event_type: str, data: dict):
23 |         self.research_data["events"].append({
24 |             "timestamp": datetime.now().isoformat(),
25 |             "type": event_type,
26 |             "data": data
27 |         })
28 |         self._save_json()
29 | 
30 |     def update_content(self, key: str, value):
31 |         self.research_data["content"][key] = value
32 |         self._save_json()
33 | 
34 |     def _save_json(self):
35 |         with open(self.json_file, 'w') as f:
36 |             json.dump(self.research_data, f, indent=2)
37 | 
38 | def setup_research_logging():
39 |     # Create logs directory if it doesn't exist
40 |     logs_dir = Path("logs")
41 |     logs_dir.mkdir(exist_ok=True)
42 |     
43 |     # Generate timestamp for log files
44 |     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
45 |     
46 |     # Create log file paths
47 |     log_file = logs_dir / f"research_{timestamp}.log"
48 |     json_file = logs_dir / f"research_{timestamp}.json"
49 |     
50 |     # Configure file handler for research logs
51 |     file_handler = logging.FileHandler(log_file)
52 |     file_handler.setLevel(logging.INFO)
53 |     file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
54 |     
55 |     # Get research logger and configure it
56 |     research_logger = logging.getLogger('research')
57 |     research_logger.setLevel(logging.INFO)
58 |     
59 |     # Remove any existing handlers to avoid duplicates
60 |     research_logger.handlers.clear()
61 |     
62 |     # Add file handler
63 |     research_logger.addHandler(file_handler)
64 |     
65 |     # Add stream handler for console output
66 |     console_handler = logging.StreamHandler()
67 |     console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
68 |     research_logger.addHandler(console_handler)
69 |     
70 |     # Prevent propagation to root logger to avoid duplicate logs
71 |     research_logger.propagate = False
72 |     
73 |     # Create JSON handler
74 |     json_handler = JSONResearchHandler(json_file)
75 |     
76 |     return str(log_file), str(json_file), research_logger, json_handler
77 | 
78 | def get_research_logger():
79 |     return logging.getLogger('research')
80 | 
81 | def get_json_handler():
82 |     return getattr(logging.getLogger('research'), 'json_handler', None)
83 | 


--------------------------------------------------------------------------------
/gpt_researcher/utils/validators.py:
--------------------------------------------------------------------------------
 1 | from typing import List
 2 | 
 3 | from pydantic import BaseModel, Field
 4 | 
 5 | class Subtopic(BaseModel):
 6 |     task: str = Field(description="Task name", min_length=1)
 7 | 
 8 | class Subtopics(BaseModel):
 9 |     subtopics: List[Subtopic] = []
10 | 


--------------------------------------------------------------------------------
/gpt_researcher/vector_store/__init__.py:
--------------------------------------------------------------------------------
1 | from .vector_store import VectorStoreWrapper
2 | 
3 | __all__ = ['VectorStoreWrapper']


--------------------------------------------------------------------------------
/gpt_researcher/vector_store/vector_store.py:
--------------------------------------------------------------------------------
 1 | """
 2 | Wrapper for langchain vector store
 3 | """
 4 | from typing import List, Dict
 5 | 
 6 | from langchain.docstore.document import Document
 7 | from langchain.vectorstores import VectorStore
 8 | from langchain.text_splitter import RecursiveCharacterTextSplitter
 9 | 
10 | class VectorStoreWrapper:
11 |     """
12 |     A Wrapper for LangchainVectorStore to handle GPT-Researcher Document Type
13 |     """
14 |     def __init__(self, vector_store : VectorStore):
15 |         self.vector_store = vector_store
16 | 
17 |     def load(self, documents):
18 |         """
19 |         Load the documents into vector_store
20 |         Translate to langchain doc type, split to chunks then load
21 |         """
22 |         langchain_documents = self._create_langchain_documents(documents)
23 |         splitted_documents = self._split_documents(langchain_documents)
24 |         self.vector_store.add_documents(splitted_documents)
25 |     
26 |     def _create_langchain_documents(self, data: List[Dict[str, str]]) -> List[Document]:
27 |         """Convert GPT Researcher Document to Langchain Document"""
28 |         return [Document(page_content=item["raw_content"], metadata={"source": item["url"]}) for item in data]
29 | 
30 |     def _split_documents(self, documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
31 |         """
32 |         Split documents into smaller chunks
33 |         """
34 |         text_splitter = RecursiveCharacterTextSplitter(
35 |             chunk_size=chunk_size,
36 |             chunk_overlap=chunk_overlap,
37 |         )
38 |         return text_splitter.split_documents(documents)
39 | 
40 |     async def asimilarity_search(self, query, k, filter):
41 |         """Return query by vector store"""
42 |         results = await self.vector_store.asimilarity_search(query=query, k=k, filter=filter)
43 |         return results
44 | 


--------------------------------------------------------------------------------
/langgraph.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "python_version": "3.11",
 3 |   "dependencies": [
 4 |     "./multi_agents"
 5 |   ],
 6 |   "graphs": {
 7 |     "agent": "./multi_agents/agent.py:graph"
 8 |   },
 9 |   "env": ".env"
10 | }


--------------------------------------------------------------------------------
/main.py:
--------------------------------------------------------------------------------
 1 | from dotenv import load_dotenv
 2 | import logging
 3 | from pathlib import Path
 4 | 
 5 | # Create logs directory if it doesn't exist
 6 | logs_dir = Path("logs")
 7 | logs_dir.mkdir(exist_ok=True)
 8 | 
 9 | # Configure logging
10 | logging.basicConfig(
11 |     level=logging.INFO,
12 |     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
13 |     handlers=[
14 |         # File handler for general application logs
15 |         logging.FileHandler('logs/app.log'),
16 |         # Stream handler for console output
17 |         logging.StreamHandler()
18 |     ]
19 | )
20 | 
21 | # Create logger instance
22 | logger = logging.getLogger(__name__)
23 | 
24 | load_dotenv()
25 | 
26 | from backend.server.server import app
27 | 
28 | if __name__ == "__main__":
29 |     import uvicorn
30 |     
31 |     logger.info("Starting server...")
32 |     uvicorn.run(app, host="0.0.0.0", port=8000)


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
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/multi_agents/agents/utils/__init__.py


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


--------------------------------------------------------------------------------
/poetry.toml:
--------------------------------------------------------------------------------
1 | [virtualenvs]
2 | in-project = true


--------------------------------------------------------------------------------
/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "gpt-researcher"
 3 | version = "0.8.5"
 4 | description = "GPT Researcher is an autonomous agent designed for comprehensive online research on a variety of tasks."
 5 | authors = ["Assaf Elovic <assaf.elovic@gmail.com>"]
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | 
 9 | [tool.poetry.dependencies]
10 | python = ">=3.10,<3.12"
11 | beautifulsoup4 = ">=4.12.2"
12 | colorama = ">=0.4.6"
13 | duckduckgo_search = ">=4.1.1"
14 | md2pdf = ">=1.0.1"
15 | openai = ">=1.3.3"
16 | python-dotenv = ">=1.0.0"
17 | pyyaml = ">=6.0.1"
18 | uvicorn = ">=0.24.0.post1"
19 | pydantic = ">=2.5.1"
20 | fastapi = ">=0.104.1"
21 | python-multipart = ">=0.0.6"
22 | markdown = ">=3.5.1"
23 | langchain = "^0.2"
24 | langgraph = ">=0.0.29,<0.3"
25 | langchain_community = "^0.2"
26 | langchain-openai = "^0.1"
27 | tavily-python = ">=0.2.8"
28 | permchain = ">=0.0.6"
29 | arxiv = ">=2.0.0"
30 | PyMuPDF = ">=1.23.6"
31 | requests = ">=2.31.0"
32 | jinja2 = ">=3.1.2"
33 | aiofiles = ">=23.2.1"
34 | SQLAlchemy = ">=2.0.28"
35 | mistune = "^3.0.2"
36 | htmldocx = "^0.0.6"
37 | python-docx = "^1.1.0"
38 | lxml = { version = ">=4.9.2", extras = ["html_clean"] }
39 | unstructured = ">=0.13,<0.16"
40 | tiktoken = ">=0.7.0"
41 | json-repair = "^0.29.8"
42 | json5 = "^0.9.25"
43 | loguru = "^0.7.2"
44 | websockets = "^13.1"
45 | 
46 | [build-system]
47 | requires = ["poetry-core"]
48 | build-backend = "poetry.core.masonry.api"
49 | 
50 | [tool.pytest.ini_options]
51 | asyncio_mode = "strict"
52 | addopts = "-v"
53 | testpaths = ["tests"]
54 | python_files = "test_*.py"
55 | asyncio_fixture_loop_scope = "function"


--------------------------------------------------------------------------------
/requirements.txt:
--------------------------------------------------------------------------------
 1 | # dependencies
 2 | beautifulsoup4
 3 | colorama
 4 | md2pdf
 5 | python-dotenv
 6 | pyyaml
 7 | uvicorn
 8 | pydantic
 9 | fastapi
10 | python-multipart
11 | markdown
12 | langchain
13 | langchain_community
14 | langchain-openai
15 | langchain-ollama
16 | langgraph
17 | tiktoken
18 | gpt-researcher
19 | arxiv
20 | PyMuPDF
21 | requests
22 | jinja2
23 | aiofiles
24 | mistune
25 | python-docx
26 | htmldocx
27 | lxml_html_clean
28 | websockets
29 | unstructured
30 | json_repair
31 | json5
32 | loguru
33 | 
34 | # uncomment for testing
35 | # pytest
36 | # pytest-asyncio
37 | 


--------------------------------------------------------------------------------
/setup.py:
--------------------------------------------------------------------------------
 1 | from setuptools import find_packages, setup
 2 | 
 3 | LATEST_VERSION = "0.10.7"
 4 | 
 5 | exclude_packages = [
 6 |     "selenium",
 7 |     "webdriver",
 8 |     "fastapi",
 9 |     "fastapi.*",
10 |     "uvicorn",
11 |     "jinja2",
12 |     "gpt-researcher",
13 |     "langgraph"
14 | ]
15 | 
16 | with open(r"README.md", "r", encoding="utf-8") as f:
17 |     long_description = f.read()
18 | 
19 | with open("requirements.txt", "r") as f:
20 |     reqs = [line.strip() for line in f if not any(pkg in line for pkg in exclude_packages)]
21 | 
22 | setup(
23 |     name="gpt-researcher",
24 |     version=LATEST_VERSION,
25 |     description="GPT Researcher is an autonomous agent designed for comprehensive web research on any task",
26 |     package_dir={'gpt_researcher': 'gpt_researcher'},
27 |     packages=find_packages(exclude=exclude_packages),
28 |     long_description=long_description,
29 |     long_description_content_type="text/markdown",
30 |     url="https://github.com/assafelovic/gpt-researcher",
31 |     author="Assaf Elovic",
32 |     author_email="assaf.elovic@gmail.com",
33 |     license="MIT",
34 |     classifiers=[
35 |         "License :: OSI Approved :: MIT License",
36 |         "Intended Audience :: Developers",
37 |         "Intended Audience :: Education",
38 |         "Intended Audience :: Science/Research",
39 |         "Programming Language :: Python :: 3.11",
40 |         "Programming Language :: Python :: 3.12",
41 |         "Topic :: Scientific/Engineering :: Artificial Intelligence",
42 |     ],
43 |     install_requires=reqs,
44 | 
45 | 
46 | )


--------------------------------------------------------------------------------
/tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/tests/__init__.py


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/assafelovic/gpt-researcher/dd61cdcb7ee1ab42c60d4336a301b8111ae9ad88/tests/docs/doc.pdf


--------------------------------------------------------------------------------
/tests/documents-report-source.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | import asyncio
 3 | import pytest
 4 | # Ensure this path is correct
 5 | from gpt_researcher import GPTResearcher
 6 | from dotenv import load_dotenv
 7 | load_dotenv()
 8 | 
 9 | # Define the report types to test
10 | report_types = [
11 |     "research_report",
12 |     "custom_report",
13 |     "subtopic_report",
14 |     "summary_report",
15 |     "detailed_report",
16 |     "quick_report"
17 | ]
18 | 
19 | # Define a common query and sources for testing
20 | query = "What can you tell me about myself based on my documents?"
21 | 
22 | # Define the output directory
23 | output_dir = "./outputs"
24 | 
25 | 
26 | @pytest.mark.asyncio
27 | @pytest.mark.parametrize("report_type", report_types)
28 | async def test_gpt_researcher(report_type):
29 |     # Ensure the output directory exists
30 |     if not os.path.exists(output_dir):
31 |         os.makedirs(output_dir)
32 | 
33 |     # Create an instance of GPTResearcher with report_source set to "documents"
34 |     researcher = GPTResearcher(
35 |         query=query, report_type=report_type, report_source="documents")
36 | 
37 |     # Conduct research and write the report
38 |     await researcher.conduct_research()
39 |     report = await researcher.write_report()
40 | 
41 |     # Define the expected output filenames
42 |     pdf_filename = os.path.join(output_dir, f"{report_type}.pdf")
43 |     docx_filename = os.path.join(output_dir, f"{report_type}.docx")
44 | 
45 |     # Check if the PDF and DOCX files are created
46 |     # assert os.path.exists(pdf_filename), f"PDF file not found for report type: {report_type}"
47 |     # assert os.path.exists(docx_filename), f"DOCX file not found for report type: {report_type}"
48 | 
49 |     # Clean up the generated files (optional)
50 |     # os.remove(pdf_filename)
51 |     # os.remove(docx_filename)
52 | 
53 | if __name__ == "__main__":
54 |     pytest.main()
55 | 


--------------------------------------------------------------------------------
/tests/gptr-logs-handler.py:
--------------------------------------------------------------------------------
 1 | import logging
 2 | from typing import List, Dict, Any
 3 | import asyncio
 4 | from gpt_researcher import GPTResearcher
 5 | from src.logs_handler import CustomLogsHandler  # Update import
 6 | 
 7 | async def run() -> None:
 8 |     """Run the research process and generate a report."""
 9 |     query = "What happened in the latest burning man floods?"
10 |     report_type = "research_report"
11 |     report_source = "online"
12 |     tone = "informative"
13 |     config_path = None
14 | 
15 |     custom_logs_handler = CustomLogsHandler(query=query)  # Pass query parameter
16 | 
17 |     researcher = GPTResearcher(
18 |         query=query,
19 |         report_type=report_type,
20 |         report_source=report_source,
21 |         tone=tone,
22 |         config_path=config_path,
23 |         websocket=custom_logs_handler
24 |     )
25 | 
26 |     await researcher.conduct_research()  # Conduct the research
27 |     report = await researcher.write_report()  # Write the research report
28 |     logging.info("Report generated successfully.")  # Log report generation
29 | 
30 |     return report
31 | 
32 | # Run the asynchronous function using asyncio
33 | if __name__ == "__main__":
34 |     asyncio.run(run())
35 | 


--------------------------------------------------------------------------------
/tests/report-types.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | import asyncio
 3 | import pytest
 4 | from gpt_researcher.agent import GPTResearcher
 5 | from src.logs_handler import CustomLogsHandler  # Update import
 6 | from typing import List, Dict, Any
 7 | 
 8 | # Define the report types to test
 9 | report_types = [
10 |     "research_report",
11 |     "subtopic_report"
12 | ]
13 | 
14 | # Define a common query and sources for testing
15 | query = "What are the latest advancements in AI?"
16 | # sources = ["https://en.wikipedia.org/wiki/Artificial_intelligence", "https://www.ibm.com/watson/ai"]
17 | 
18 | # Define the output directory
19 | output_dir = "./outputs"
20 | 
21 | @pytest.mark.asyncio
22 | @pytest.mark.parametrize("report_type", report_types)
23 | async def test_gpt_researcher(report_type):
24 |     # Ensure the output directory exists
25 |     if not os.path.exists(output_dir):
26 |         os.makedirs(output_dir)
27 |     
28 |     custom_logs_handler = CustomLogsHandler(query=query)
29 |     # Create an instance of GPTResearcher
30 |     researcher = GPTResearcher(query=query, report_type=report_type, websocket=custom_logs_handler)
31 |     
32 |     # Conduct research and write the report
33 |     await researcher.conduct_research()
34 |     report = await researcher.write_report()
35 |     
36 |     # Define the expected output filenames
37 |     pdf_filename = os.path.join(output_dir, f"{report_type}.pdf")
38 |     docx_filename = os.path.join(output_dir, f"{report_type}.docx")
39 |     
40 |     # Check if the PDF and DOCX files are created
41 |     # assert os.path.exists(pdf_filename), f"PDF file not found for report type: {report_type}"
42 |     # assert os.path.exists(docx_filename), f"DOCX file not found for report type: {report_type}"
43 | 
44 |     # Clean up the generated files (optional)
45 |     # os.remove(pdf_filename)
46 |     # os.remove(docx_filename)
47 | 
48 | if __name__ == "__main__":
49 |     pytest.main()


--------------------------------------------------------------------------------
/tests/test-loaders.py:
--------------------------------------------------------------------------------
 1 | from langchain_community.document_loaders import PyMuPDFLoader, UnstructuredCSVLoader
 2 | 
 3 | # # Test PyMuPDFLoader
 4 | pdf_loader = PyMuPDFLoader("my-docs/Elisha - Coding Career.pdf")
 5 | try:
 6 |     pdf_data = pdf_loader.load()
 7 |     print("PDF Data:", pdf_data)
 8 | except Exception as e:
 9 |     print("Failed to load PDF:", e)
10 | 
11 | # Test UnstructuredCSVLoader
12 | csv_loader = UnstructuredCSVLoader("my-docs/active_braze_protocols_from_bq.csv", mode="elements")
13 | try:
14 |     csv_data = csv_loader.load()
15 |     print("CSV Data:", csv_data)
16 | except Exception as e:
17 |     print("Failed to load CSV:", e)


--------------------------------------------------------------------------------
/tests/test-openai-llm.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | from gpt_researcher.utils.llm import get_llm
 3 | from gpt_researcher import GPTResearcher
 4 | from dotenv import load_dotenv
 5 | load_dotenv()
 6 | 
 7 | async def main():
 8 | 
 9 |     # Example usage of get_llm function
10 |     llm_provider = "openai"
11 |     model = "gpt-3.5-turbo" 
12 |     temperature = 0.7
13 |     max_tokens = 1000
14 | 
15 |     llm = get_llm(llm_provider, model=model, temperature=temperature, max_tokens=max_tokens)
16 |     print(f"LLM Provider: {llm_provider}, Model: {model}, Temperature: {temperature}, Max Tokens: {max_tokens}")
17 |     print('llm: ',llm)
18 |     await test_llm(llm=llm)
19 | 
20 | 
21 | async def test_llm(llm):
22 |     # Test the connection with a simple query
23 |     messages = [{"role": "user", "content": "sup?"}]
24 |     try:
25 |         response = await llm.get_chat_response(messages, stream=False)
26 |         print("LLM response:", response)
27 |     except Exception as e:
28 |         print(f"Error: {e}")
29 | 
30 | # Run the async function
31 | asyncio.run(main())


--------------------------------------------------------------------------------
/tests/test-your-llm.py:
--------------------------------------------------------------------------------
 1 | from gpt_researcher.config.config import Config
 2 | from gpt_researcher.utils.llm import create_chat_completion
 3 | import asyncio
 4 | from dotenv import load_dotenv
 5 | load_dotenv()
 6 | 
 7 | async def main():
 8 |     cfg = Config()
 9 | 
10 |     try:
11 |         report = await create_chat_completion(
12 |             model=cfg.smart_llm_model,
13 |             messages = [{"role": "user", "content": "sup?"}],
14 |             temperature=0.35,
15 |             llm_provider=cfg.smart_llm_provider,
16 |             stream=True,
17 |             max_tokens=cfg.smart_token_limit,
18 |             llm_kwargs=cfg.llm_kwargs
19 |         )
20 |     except Exception as e:
21 |         print(f"Error in calling LLM: {e}")
22 | 
23 | # Run the async function
24 | asyncio.run(main())


--------------------------------------------------------------------------------
/tests/test-your-retriever.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | from dotenv import load_dotenv
 3 | from gpt_researcher.config.config import Config
 4 | from gpt_researcher.actions.retriever import get_retrievers
 5 | from gpt_researcher.skills.researcher import ResearchConductor
 6 | import pprint
 7 | # Load environment variables from .env file
 8 | load_dotenv()
 9 | 
10 | async def test_scrape_data_by_query():
11 |     # Initialize the Config object
12 |     config = Config()
13 | 
14 |     # Retrieve the retrievers based on the current configuration
15 |     retrievers = get_retrievers({}, config)
16 |     print("Retrievers:", retrievers)
17 | 
18 |     # Create a mock researcher object with necessary attributes
19 |     class MockResearcher:
20 |         def init(self):
21 |             self.retrievers = retrievers
22 |             self.cfg = config
23 |             self.verbose = True
24 |             self.websocket = None
25 |             self.scraper_manager = None  # Mock or implement scraper manager
26 |             self.vector_store = None  # Mock or implement vector store
27 | 
28 |     researcher = MockResearcher()
29 |     research_conductor = ResearchConductor(researcher)
30 |     # print('research_conductor',dir(research_conductor))
31 |     # print('MockResearcher',dir(researcher))
32 |     # Define a sub-query to test
33 |     sub_query = "design patterns for autonomous ai agents"
34 | 
35 |     # Iterate through all retrievers
36 |     for retriever_class in retrievers:
37 |         # Instantiate the retriever with the sub-query
38 |         retriever = retriever_class(sub_query)
39 | 
40 |         # Perform the search using the current retriever
41 |         search_results = await asyncio.to_thread(
42 |             retriever.search, max_results=10
43 |         )
44 | 
45 |         print("\033[35mSearch results:\033[0m")
46 |         pprint.pprint(search_results, indent=4, width=80)
47 | 
48 | if __name__ == "__main__":
49 |     asyncio.run(test_scrape_data_by_query())


--------------------------------------------------------------------------------
/tests/test_logging.py:
--------------------------------------------------------------------------------
 1 | import pytest
 2 | from unittest.mock import AsyncMock
 3 | from fastapi import WebSocket
 4 | from src.logs_handler import CustomLogsHandler
 5 | import os
 6 | import json
 7 | 
 8 | @pytest.mark.asyncio
 9 | async def test_custom_logs_handler():
10 |     # Mock websocket
11 |     mock_websocket = AsyncMock()
12 |     mock_websocket.send_json = AsyncMock()
13 |     
14 |     # Test initialization
15 |     handler = CustomLogsHandler(mock_websocket, "test_query")
16 |     
17 |     # Verify log file creation
18 |     assert os.path.exists(handler.log_file)
19 |     
20 |     # Test sending log data
21 |     test_data = {
22 |         "type": "logs",
23 |         "message": "Test log message"
24 |     }
25 |     
26 |     await handler.send_json(test_data)
27 |     
28 |     # Verify websocket was called with correct data
29 |     mock_websocket.send_json.assert_called_once_with(test_data)
30 |     
31 |     # Verify log file contents
32 |     with open(handler.log_file, 'r') as f:
33 |         log_data = json.load(f)
34 |         assert len(log_data['events']) == 1
35 |         assert log_data['events'][0]['data'] == test_data 
36 | 
37 | @pytest.mark.asyncio
38 | async def test_content_update():
39 |     """Test handling of non-log type data that updates content"""
40 |     mock_websocket = AsyncMock()
41 |     mock_websocket.send_json = AsyncMock()
42 |     
43 |     handler = CustomLogsHandler(mock_websocket, "test_query")
44 |     
45 |     # Test content update
46 |     content_data = {
47 |         "query": "test query",
48 |         "sources": ["source1", "source2"],
49 |         "report": "test report"
50 |     }
51 |     
52 |     await handler.send_json(content_data)
53 |     
54 |     mock_websocket.send_json.assert_called_once_with(content_data)
55 |     
56 |     # Verify log file contents
57 |     with open(handler.log_file, 'r') as f:
58 |         log_data = json.load(f)
59 |         assert log_data['content']['query'] == "test query"
60 |         assert log_data['content']['sources'] == ["source1", "source2"]
61 |         assert log_data['content']['report'] == "test report"


--------------------------------------------------------------------------------
/tests/test_logs.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | from pathlib import Path
 3 | import sys
 4 | 
 5 | # Add the project root to Python path
 6 | project_root = Path(__file__).parent.parent
 7 | sys.path.append(str(project_root))
 8 | 
 9 | from src.logs_handler import CustomLogsHandler
10 | 
11 | def test_logs_creation():
12 |     # Print current working directory
13 |     print(f"Current working directory: {os.getcwd()}")
14 |     
15 |     # Print project root
16 |     print(f"Project root: {project_root}")
17 |     
18 |     # Try to create logs directory directly
19 |     logs_dir = project_root / "logs"
20 |     print(f"Attempting to create logs directory at: {logs_dir}")
21 |     
22 |     try:
23 |         # Create directory with full permissions
24 |         os.makedirs(logs_dir, mode=0o777, exist_ok=True)
25 |         print(f"✓ Created directory: {logs_dir}")
26 |         
27 |         # Test file creation
28 |         test_file = logs_dir / "test.txt"
29 |         with open(test_file, 'w') as f:
30 |             f.write("Test log entry")
31 |         print(f"✓ Created test file: {test_file}")
32 |         
33 |         # Initialize the handler
34 |         handler = CustomLogsHandler()
35 |         print("✓ CustomLogsHandler initialized")
36 |         
37 |         # Test JSON logging
38 |         handler.logs.append({"test": "message"})
39 |         print("✓ Added test log entry")
40 |         
41 |     except Exception as e:
42 |         print(f"❌ Error: {str(e)}")
43 |         print(f"Error type: {type(e)}")
44 |         import traceback
45 |         print(f"Traceback: {traceback.format_exc()}")
46 | 
47 | if __name__ == "__main__":
48 |     test_logs_creation() 


--------------------------------------------------------------------------------
/tests/test_researcher_logging.py:
--------------------------------------------------------------------------------
 1 | import pytest
 2 | import asyncio
 3 | from pathlib import Path
 4 | import sys
 5 | import logging
 6 | 
 7 | # Add the project root to Python path
 8 | project_root = Path(__file__).parent.parent
 9 | sys.path.append(str(project_root))
10 | 
11 | # Configure basic logging
12 | logging.basicConfig(level=logging.INFO)
13 | logger = logging.getLogger(__name__)
14 | 
15 | @pytest.mark.asyncio
16 | async def test_researcher_logging():  # Renamed function to be more specific
17 |     """
18 |     Test suite for verifying the researcher's logging infrastructure.
19 |     Ensures proper creation and formatting of log files.
20 |     """
21 |     try:
22 |         # Import here to catch any import errors
23 |         from src.researcher import Researcher
24 |         logger.info("Successfully imported Researcher class")
25 |         
26 |         # Create a researcher instance with a logging-focused query
27 |         researcher = Researcher(
28 |             query="Test query for logging verification",
29 |             report_type="research_report"
30 |         )
31 |         logger.info("Created Researcher instance")
32 |         
33 |         # Run the research
34 |         report = await researcher.research()
35 |         logger.info("Research completed successfully!")
36 |         logger.info(f"Report length: {len(report)}")
37 |         
38 |         # Basic report assertions
39 |         assert report is not None
40 |         assert len(report) > 0
41 |         
42 |         # Detailed log file verification
43 |         logs_dir = Path(project_root) / "logs"
44 |         log_files = list(logs_dir.glob("research_*.log"))
45 |         json_files = list(logs_dir.glob("research_*.json"))
46 |         
47 |         # Verify log files exist
48 |         assert len(log_files) > 0, "No log files were created"
49 |         assert len(json_files) > 0, "No JSON files were created"
50 |         
51 |         # Log the findings
52 |         logger.info(f"\nFound {len(log_files)} log files:")
53 |         for log_file in log_files:
54 |             logger.info(f"- {log_file.name}")
55 |             # Could add additional checks for log file format/content here
56 |             
57 |         logger.info(f"\nFound {len(json_files)} JSON files:")
58 |         for json_file in json_files:
59 |             logger.info(f"- {json_file.name}")
60 |             # Could add additional checks for JSON file structure here
61 |             
62 |     except ImportError as e:
63 |         logger.error(f"Import error: {e}")
64 |         logger.error("Make sure gpt_researcher is installed and in your PYTHONPATH")
65 |         raise
66 |     except Exception as e:
67 |         logger.error(f"Error during research: {e}")
68 |         raise
69 | 
70 | if __name__ == "__main__":
71 |     pytest.main([__file__])