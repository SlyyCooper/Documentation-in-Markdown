
/libs/checkpoint-duckdb/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: test test_watch lint format
 2 | 
 3 | ######################
 4 | # TESTING AND COVERAGE
 5 | ######################
 6 | 
 7 | test:
 8 | 	poetry run pytest tests
 9 | 
10 | test_watch:
11 | 	poetry run ptw .
12 | 
13 | ######################
14 | # LINTING AND FORMATTING
15 | ######################
16 | 
17 | # Define a variable for Python and notebook files.
18 | PYTHON_FILES=.
19 | MYPY_CACHE=.mypy_cache
20 | lint format: PYTHON_FILES=.
21 | lint_diff format_diff: PYTHON_FILES=$(shell git diff --name-only --relative --diff-filter=d main . | grep -E '\.py$$|\.ipynb$$')
22 | lint_package: PYTHON_FILES=langgraph
23 | lint_tests: PYTHON_FILES=tests
24 | lint_tests: MYPY_CACHE=.mypy_cache_test
25 | 
26 | lint lint_diff lint_package lint_tests:
27 | 	poetry run ruff check .
28 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff format $(PYTHON_FILES) --diff
29 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff check --select I $(PYTHON_FILES)
30 | 	[ "$(PYTHON_FILES)" = "" ] || mkdir -p $(MYPY_CACHE)
31 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run mypy $(PYTHON_FILES) --cache-dir $(MYPY_CACHE)
32 | 
33 | format format_diff:
34 | 	poetry run ruff format $(PYTHON_FILES)
35 | 	poetry run ruff check --select I --fix $(PYTHON_FILES)
36 | 


--------------------------------------------------------------------------------
/libs/checkpoint-duckdb/README.md:
--------------------------------------------------------------------------------
 1 | # LangGraph Checkpoint DuckDB
 2 | 
 3 | Implementation of LangGraph CheckpointSaver that uses DuckDB.
 4 | 
 5 | ## Usage
 6 | 
 7 | > [!IMPORTANT]
 8 | > When using DuckDB checkpointers for the first time, make sure to call `.setup()` method on them to create required tables. See example below.
 9 | 
10 | ```python
11 | from langgraph.checkpoint.duckdb import DuckDBSaver
12 | 
13 | write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
14 | read_config = {"configurable": {"thread_id": "1"}}
15 | 
16 | with DuckDBSaver.from_conn_string(":memory:") as checkpointer:
17 |     # call .setup() the first time you're using the checkpointer
18 |     checkpointer.setup()
19 |     checkpoint = {
20 |         "v": 1,
21 |         "ts": "2024-07-31T20:14:19.804150+00:00",
22 |         "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
23 |         "channel_values": {
24 |             "my_key": "meow",
25 |             "node": "node"
26 |         },
27 |         "channel_versions": {
28 |             "__start__": 2,
29 |             "my_key": 3,
30 |             "start:node": 3,
31 |             "node": 3
32 |         },
33 |         "versions_seen": {
34 |             "__input__": {},
35 |             "__start__": {
36 |             "__start__": 1
37 |             },
38 |             "node": {
39 |             "start:node": 2
40 |             }
41 |         },
42 |         "pending_sends": [],
43 |     }
44 | 
45 |     # store checkpoint
46 |     checkpointer.put(write_config, checkpoint, {}, {})
47 | 
48 |     # load checkpoint
49 |     checkpointer.get(read_config)
50 | 
51 |     # list checkpoints
52 |     list(checkpointer.list(read_config))
53 | ```
54 | 
55 | ### Async
56 | 
57 | ```python
58 | from langgraph.checkpoint.duckdb.aio import AsyncDuckDBSaver
59 | 
60 | async with AsyncDuckDBSaver.from_conn_string(":memory:") as checkpointer:
61 |     checkpoint = {
62 |         "v": 1,
63 |         "ts": "2024-07-31T20:14:19.804150+00:00",
64 |         "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
65 |         "channel_values": {
66 |             "my_key": "meow",
67 |             "node": "node"
68 |         },
69 |         "channel_versions": {
70 |             "__start__": 2,
71 |             "my_key": 3,
72 |             "start:node": 3,
73 |             "node": 3
74 |         },
75 |         "versions_seen": {
76 |             "__input__": {},
77 |             "__start__": {
78 |             "__start__": 1
79 |             },
80 |             "node": {
81 |             "start:node": 2
82 |             }
83 |         },
84 |         "pending_sends": [],
85 |     }
86 | 
87 |     # store checkpoint
88 |     await checkpointer.aput(write_config, checkpoint, {}, {})
89 | 
90 |     # load checkpoint
91 |     await checkpointer.aget(read_config)
92 | 
93 |     # list checkpoints
94 |     [c async for c in checkpointer.alist(read_config)]
95 | ```
96 | 


--------------------------------------------------------------------------------
/libs/checkpoint-duckdb/langgraph/checkpoint/duckdb/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint-duckdb/langgraph/checkpoint/duckdb/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint-duckdb/langgraph/store/duckdb/__init__.py:
--------------------------------------------------------------------------------
1 | from langgraph.store.duckdb.aio import AsyncDuckDBStore
2 | from langgraph.store.duckdb.base import DuckDBStore
3 | 
4 | __all__ = ["AsyncDuckDBStore", "DuckDBStore"]
5 | 


--------------------------------------------------------------------------------
/libs/checkpoint-duckdb/langgraph/store/duckdb/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint-duckdb/langgraph/store/duckdb/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint-duckdb/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph-checkpoint-duckdb"
 3 | version = "2.0.1"
 4 | description = "Library with a DuckDB implementation of LangGraph checkpoint saver."
 5 | authors = []
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | repository = "https://www.github.com/langchain-ai/langgraph"
 9 | packages = [{ include = "langgraph" }]
10 | 
11 | [tool.poetry.dependencies]
12 | python = "^3.9.0,<4.0"
13 | langgraph-checkpoint = "^2.0.2"
14 | duckdb = ">=1.1.2"
15 | 
16 | [tool.poetry.group.dev.dependencies]
17 | ruff = "^0.6.2"
18 | codespell = "^2.2.0"
19 | pytest = "^7.2.1"
20 | anyio = "^4.4.0"
21 | pytest-asyncio = "^0.21.1"
22 | pytest-mock = "^3.11.1"
23 | pytest-watch = "^4.2.0"
24 | mypy = "^1.10.0"
25 | langgraph-checkpoint = {path = "../checkpoint", develop = true}
26 | 
27 | [tool.pytest.ini_options]
28 | # --strict-markers will raise errors on unknown marks.
29 | # https://docs.pytest.org/en/7.1.x/how-to/mark.html#raising-errors-on-unknown-marks
30 | #
31 | # https://docs.pytest.org/en/7.1.x/reference/reference.html
32 | # --strict-config       any warnings encountered while parsing the `pytest`
33 | #                       section of the configuration file raise errors.
34 | addopts = "--strict-markers --strict-config --durations=5 -vv"
35 | asyncio_mode = "auto"
36 | 
37 | 
38 | [build-system]
39 | requires = ["poetry-core"]
40 | build-backend = "poetry.core.masonry.api"
41 | 
42 | [tool.ruff]
43 | lint.select = [
44 |   "E",  # pycodestyle
45 |   "F",  # Pyflakes
46 |   "UP", # pyupgrade
47 |   "B",  # flake8-bugbear
48 |   "I",  # isort
49 | ]
50 | lint.ignore = ["E501", "B008", "UP007", "UP006"]
51 | 
52 | [tool.mypy]
53 | # https://mypy.readthedocs.io/en/stable/config_file.html
54 | disallow_untyped_defs = "True"
55 | explicit_package_bases = "True"
56 | warn_no_return = "False"
57 | warn_unused_ignores = "True"
58 | warn_redundant_casts = "True"
59 | allow_redefinition = "True"
60 | disable_error_code = "typeddict-item, return-value"
61 | 


--------------------------------------------------------------------------------
/libs/checkpoint-duckdb/tests/test_async.py:
--------------------------------------------------------------------------------
  1 | from typing import Any
  2 | 
  3 | import pytest
  4 | from langchain_core.runnables import RunnableConfig
  5 | 
  6 | from langgraph.checkpoint.base import (
  7 |     Checkpoint,
  8 |     CheckpointMetadata,
  9 |     create_checkpoint,
 10 |     empty_checkpoint,
 11 | )
 12 | from langgraph.checkpoint.duckdb.aio import AsyncDuckDBSaver
 13 | 
 14 | 
 15 | class TestAsyncDuckDBSaver:
 16 |     @pytest.fixture(autouse=True)
 17 |     async def setup(self) -> None:
 18 |         # objects for test setup
 19 |         self.config_1: RunnableConfig = {
 20 |             "configurable": {
 21 |                 "thread_id": "thread-1",
 22 |                 # for backwards compatibility testing
 23 |                 "thread_ts": "1",
 24 |                 "checkpoint_ns": "",
 25 |             }
 26 |         }
 27 |         self.config_2: RunnableConfig = {
 28 |             "configurable": {
 29 |                 "thread_id": "thread-2",
 30 |                 "checkpoint_id": "2",
 31 |                 "checkpoint_ns": "",
 32 |             }
 33 |         }
 34 |         self.config_3: RunnableConfig = {
 35 |             "configurable": {
 36 |                 "thread_id": "thread-2",
 37 |                 "checkpoint_id": "2-inner",
 38 |                 "checkpoint_ns": "inner",
 39 |             }
 40 |         }
 41 | 
 42 |         self.chkpnt_1: Checkpoint = empty_checkpoint()
 43 |         self.chkpnt_2: Checkpoint = create_checkpoint(self.chkpnt_1, {}, 1)
 44 |         self.chkpnt_3: Checkpoint = empty_checkpoint()
 45 | 
 46 |         self.metadata_1: CheckpointMetadata = {
 47 |             "source": "input",
 48 |             "step": 2,
 49 |             "writes": {},
 50 |             "score": 1,
 51 |         }
 52 |         self.metadata_2: CheckpointMetadata = {
 53 |             "source": "loop",
 54 |             "step": 1,
 55 |             "writes": {"foo": "bar"},
 56 |             "score": None,
 57 |         }
 58 |         self.metadata_3: CheckpointMetadata = {}
 59 | 
 60 |     async def test_asearch(self) -> None:
 61 |         async with AsyncDuckDBSaver.from_conn_string(":memory:") as saver:
 62 |             await saver.setup()
 63 |             await saver.aput(self.config_1, self.chkpnt_1, self.metadata_1, {})
 64 |             await saver.aput(self.config_2, self.chkpnt_2, self.metadata_2, {})
 65 |             await saver.aput(self.config_3, self.chkpnt_3, self.metadata_3, {})
 66 | 
 67 |             # call method / assertions
 68 |             query_1 = {"source": "input"}  # search by 1 key
 69 |             query_2 = {
 70 |                 "step": 1,
 71 |                 "writes": {"foo": "bar"},
 72 |             }  # search by multiple keys
 73 |             query_3: dict[str, Any] = {}  # search by no keys, return all checkpoints
 74 |             query_4 = {"source": "update", "step": 1}  # no match
 75 | 
 76 |             search_results_1 = [c async for c in saver.alist(None, filter=query_1)]
 77 |             assert len(search_results_1) == 1
 78 |             assert search_results_1[0].metadata == self.metadata_1
 79 | 
 80 |             search_results_2 = [c async for c in saver.alist(None, filter=query_2)]
 81 |             assert len(search_results_2) == 1
 82 |             assert search_results_2[0].metadata == self.metadata_2
 83 | 
 84 |             search_results_3 = [c async for c in saver.alist(None, filter=query_3)]
 85 |             assert len(search_results_3) == 3
 86 | 
 87 |             search_results_4 = [c async for c in saver.alist(None, filter=query_4)]
 88 |             assert len(search_results_4) == 0
 89 | 
 90 |             # search by config (defaults to checkpoints across all namespaces)
 91 |             search_results_5 = [
 92 |                 c
 93 |                 async for c in saver.alist({"configurable": {"thread_id": "thread-2"}})
 94 |             ]
 95 |             assert len(search_results_5) == 2
 96 |             assert {
 97 |                 search_results_5[0].config["configurable"]["checkpoint_ns"],
 98 |                 search_results_5[1].config["configurable"]["checkpoint_ns"],
 99 |             } == {"", "inner"}
100 | 
101 |             # TODO: test before and limit params
102 | 
103 |     async def test_null_chars(self) -> None:
104 |         async with AsyncDuckDBSaver.from_conn_string(":memory:") as saver:
105 |             await saver.setup()
106 |             config = await saver.aput(
107 |                 self.config_1, self.chkpnt_1, {"my_key": "\x00abc"}, {}
108 |             )
109 |             assert (await saver.aget_tuple(config)).metadata["my_key"] == "abc"  # type: ignore
110 |             assert [c async for c in saver.alist(None, filter={"my_key": "abc"})][
111 |                 0
112 |             ].metadata["my_key"] == "abc"
113 | 


--------------------------------------------------------------------------------
/libs/checkpoint-duckdb/tests/test_sync.py:
--------------------------------------------------------------------------------
  1 | from typing import Any
  2 | 
  3 | import pytest
  4 | from langchain_core.runnables import RunnableConfig
  5 | 
  6 | from langgraph.checkpoint.base import (
  7 |     Checkpoint,
  8 |     CheckpointMetadata,
  9 |     create_checkpoint,
 10 |     empty_checkpoint,
 11 | )
 12 | from langgraph.checkpoint.duckdb import DuckDBSaver
 13 | 
 14 | 
 15 | class TestDuckDBSaver:
 16 |     @pytest.fixture(autouse=True)
 17 |     def setup(self) -> None:
 18 |         # objects for test setup
 19 |         self.config_1: RunnableConfig = {
 20 |             "configurable": {
 21 |                 "thread_id": "thread-1",
 22 |                 # for backwards compatibility testing
 23 |                 "thread_ts": "1",
 24 |                 "checkpoint_ns": "",
 25 |             }
 26 |         }
 27 |         self.config_2: RunnableConfig = {
 28 |             "configurable": {
 29 |                 "thread_id": "thread-2",
 30 |                 "checkpoint_id": "2",
 31 |                 "checkpoint_ns": "",
 32 |             }
 33 |         }
 34 |         self.config_3: RunnableConfig = {
 35 |             "configurable": {
 36 |                 "thread_id": "thread-2",
 37 |                 "checkpoint_id": "2-inner",
 38 |                 "checkpoint_ns": "inner",
 39 |             }
 40 |         }
 41 | 
 42 |         self.chkpnt_1: Checkpoint = empty_checkpoint()
 43 |         self.chkpnt_2: Checkpoint = create_checkpoint(self.chkpnt_1, {}, 1)
 44 |         self.chkpnt_3: Checkpoint = empty_checkpoint()
 45 | 
 46 |         self.metadata_1: CheckpointMetadata = {
 47 |             "source": "input",
 48 |             "step": 2,
 49 |             "writes": {},
 50 |             "score": 1,
 51 |         }
 52 |         self.metadata_2: CheckpointMetadata = {
 53 |             "source": "loop",
 54 |             "step": 1,
 55 |             "writes": {"foo": "bar"},
 56 |             "score": None,
 57 |         }
 58 |         self.metadata_3: CheckpointMetadata = {}
 59 | 
 60 |     def test_search(self) -> None:
 61 |         with DuckDBSaver.from_conn_string(":memory:") as saver:
 62 |             saver.setup()
 63 |             # save checkpoints
 64 |             saver.put(self.config_1, self.chkpnt_1, self.metadata_1, {})
 65 |             saver.put(self.config_2, self.chkpnt_2, self.metadata_2, {})
 66 |             saver.put(self.config_3, self.chkpnt_3, self.metadata_3, {})
 67 | 
 68 |             # call method / assertions
 69 |             query_1 = {"source": "input"}  # search by 1 key
 70 |             query_2 = {
 71 |                 "step": 1,
 72 |                 "writes": {"foo": "bar"},
 73 |             }  # search by multiple keys
 74 |             query_3: dict[str, Any] = {}  # search by no keys, return all checkpoints
 75 |             query_4 = {"source": "update", "step": 1}  # no match
 76 | 
 77 |             search_results_1 = list(saver.list(None, filter=query_1))
 78 |             assert len(search_results_1) == 1
 79 |             assert search_results_1[0].metadata == self.metadata_1
 80 | 
 81 |             search_results_2 = list(saver.list(None, filter=query_2))
 82 |             assert len(search_results_2) == 1
 83 |             assert search_results_2[0].metadata == self.metadata_2
 84 | 
 85 |             search_results_3 = list(saver.list(None, filter=query_3))
 86 |             assert len(search_results_3) == 3
 87 | 
 88 |             search_results_4 = list(saver.list(None, filter=query_4))
 89 |             assert len(search_results_4) == 0
 90 | 
 91 |             # search by config (defaults to checkpoints across all namespaces)
 92 |             search_results_5 = list(
 93 |                 saver.list({"configurable": {"thread_id": "thread-2"}})
 94 |             )
 95 |             assert len(search_results_5) == 2
 96 |             assert {
 97 |                 search_results_5[0].config["configurable"]["checkpoint_ns"],
 98 |                 search_results_5[1].config["configurable"]["checkpoint_ns"],
 99 |             } == {"", "inner"}
100 | 
101 |             # TODO: test before and limit params
102 | 
103 |     def test_null_chars(self) -> None:
104 |         with DuckDBSaver.from_conn_string(":memory:") as saver:
105 |             saver.setup()
106 |             config = saver.put(self.config_1, self.chkpnt_1, {"my_key": "\x00abc"}, {})
107 |             assert saver.get_tuple(config).metadata["my_key"] == "abc"  # type: ignore
108 |             assert (
109 |                 list(saver.list(None, filter={"my_key": "abc"}))[0].metadata["my_key"]  # type: ignore
110 |                 == "abc"
111 |             )
112 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: test test_watch lint format
 2 | 
 3 | ######################
 4 | # TESTING AND COVERAGE
 5 | ######################
 6 | 
 7 | start-postgres:
 8 | 	POSTGRES_VERSION=${POSTGRES_VERSION:-16} docker compose -f tests/compose-postgres.yml up -V --force-recreate --wait || ( \
 9 | 		echo "Failed to start PostgreSQL, printing logs..."; \
10 | 		docker compose -f tests/compose-postgres.yml logs; \
11 | 		exit 1 \
12 | 	)
13 | 
14 | stop-postgres:
15 | 	docker compose -f tests/compose-postgres.yml down
16 | 
17 | POSTGRES_VERSIONS ?= 15 16
18 | test_pg_version:
19 | 	@echo "Testing PostgreSQL $(POSTGRES_VERSION)"
20 | 	@POSTGRES_VERSION=$(POSTGRES_VERSION) make start-postgres
21 | 	@poetry run pytest $(TEST)
22 | 	@EXIT_CODE=$$?; \
23 | 	make stop-postgres; \
24 | 	echo "Finished testing PostgreSQL $(POSTGRES_VERSION); Exit code: $$EXIT_CODE"; \
25 | 	exit $$EXIT_CODE
26 | 
27 | test:
28 | 	@for version in $(POSTGRES_VERSIONS); do \
29 | 		if ! make test_pg_version POSTGRES_VERSION=$$version; then \
30 | 			echo "Test failed for PostgreSQL $$version"; \
31 | 			exit 1; \
32 | 		fi; \
33 | 	done
34 | 	@echo "All PostgreSQL versions tested successfully"
35 | 
36 | TEST ?= .
37 | test_watch:
38 | 	POSTGRES_VERSION=${POSTGRES_VERSION:-16} make start-postgres; \
39 | 	poetry run ptw $(TEST); \
40 | 	EXIT_CODE=$$?; \
41 | 	make stop-postgres; \
42 | 	exit $$EXIT_CODE
43 | 
44 | ######################
45 | # LINTING AND FORMATTING
46 | ######################
47 | 
48 | # Define a variable for Python and notebook files.
49 | PYTHON_FILES=.
50 | MYPY_CACHE=.mypy_cache
51 | lint format: PYTHON_FILES=.
52 | lint_diff format_diff: PYTHON_FILES=$(shell git diff --name-only --relative --diff-filter=d main . | grep -E '\.py$$|\.ipynb$$')
53 | lint_package: PYTHON_FILES=langgraph
54 | lint_tests: PYTHON_FILES=tests
55 | lint_tests: MYPY_CACHE=.mypy_cache_test
56 | 
57 | lint lint_diff lint_package lint_tests:
58 | 	poetry run ruff check .
59 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff format $(PYTHON_FILES) --diff
60 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff check --select I $(PYTHON_FILES)
61 | 	[ "$(PYTHON_FILES)" = "" ] || mkdir -p $(MYPY_CACHE)
62 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run mypy $(PYTHON_FILES) --cache-dir $(MYPY_CACHE)
63 | 
64 | format format_diff:
65 | 	poetry run ruff format $(PYTHON_FILES)
66 | 	poetry run ruff check --select I --fix $(PYTHON_FILES)
67 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/README.md:
--------------------------------------------------------------------------------
  1 | # LangGraph Checkpoint Postgres
  2 | 
  3 | Implementation of LangGraph CheckpointSaver that uses Postgres.
  4 | 
  5 | ## Dependencies
  6 | 
  7 | By default `langgraph-checkpoint-postgres` installs `psycopg` (Psycopg 3) without any extras. However, you can choose a specific installation that best suits your needs [here](https://www.psycopg.org/psycopg3/docs/basic/install.html) (for example, `psycopg[binary]`).
  8 | 
  9 | ## Usage
 10 | 
 11 | > [!IMPORTANT]
 12 | > When using Postgres checkpointers for the first time, make sure to call `.setup()` method on them to create required tables. See example below.
 13 | 
 14 | > [!IMPORTANT]
 15 | > When manually creating Postgres connections and passing them to `PostgresSaver` or `AsyncPostgresSaver`, make sure to include `autocommit=True` and `row_factory=dict_row` (`from psycopg.rows import dict_row`). See a full example in this [how-to guide](https://langchain-ai.github.io/langgraph/how-tos/persistence_postgres/).
 16 | 
 17 | ```python
 18 | from langgraph.checkpoint.postgres import PostgresSaver
 19 | 
 20 | write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
 21 | read_config = {"configurable": {"thread_id": "1"}}
 22 | 
 23 | DB_URI = "postgres://postgres:postgres@localhost:5432/postgres?sslmode=disable"
 24 | with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
 25 |     # call .setup() the first time you're using the checkpointer
 26 |     checkpointer.setup()
 27 |     checkpoint = {
 28 |         "v": 1,
 29 |         "ts": "2024-07-31T20:14:19.804150+00:00",
 30 |         "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
 31 |         "channel_values": {
 32 |             "my_key": "meow",
 33 |             "node": "node"
 34 |         },
 35 |         "channel_versions": {
 36 |             "__start__": 2,
 37 |             "my_key": 3,
 38 |             "start:node": 3,
 39 |             "node": 3
 40 |         },
 41 |         "versions_seen": {
 42 |             "__input__": {},
 43 |             "__start__": {
 44 |             "__start__": 1
 45 |             },
 46 |             "node": {
 47 |             "start:node": 2
 48 |             }
 49 |         },
 50 |         "pending_sends": [],
 51 |     }
 52 | 
 53 |     # store checkpoint
 54 |     checkpointer.put(write_config, checkpoint, {}, {})
 55 | 
 56 |     # load checkpoint
 57 |     checkpointer.get(read_config)
 58 | 
 59 |     # list checkpoints
 60 |     list(checkpointer.list(read_config))
 61 | ```
 62 | 
 63 | ### Async
 64 | 
 65 | ```python
 66 | from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
 67 | 
 68 | async with AsyncPostgresSaver.from_conn_string(DB_URI) as checkpointer:
 69 |     checkpoint = {
 70 |         "v": 1,
 71 |         "ts": "2024-07-31T20:14:19.804150+00:00",
 72 |         "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
 73 |         "channel_values": {
 74 |             "my_key": "meow",
 75 |             "node": "node"
 76 |         },
 77 |         "channel_versions": {
 78 |             "__start__": 2,
 79 |             "my_key": 3,
 80 |             "start:node": 3,
 81 |             "node": 3
 82 |         },
 83 |         "versions_seen": {
 84 |             "__input__": {},
 85 |             "__start__": {
 86 |             "__start__": 1
 87 |             },
 88 |             "node": {
 89 |             "start:node": 2
 90 |             }
 91 |         },
 92 |         "pending_sends": [],
 93 |     }
 94 | 
 95 |     # store checkpoint
 96 |     await checkpointer.aput(write_config, checkpoint, {}, {})
 97 | 
 98 |     # load checkpoint
 99 |     await checkpointer.aget(read_config)
100 | 
101 |     # list checkpoints
102 |     [c async for c in checkpointer.alist(read_config)]
103 | ```
104 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/langgraph/checkpoint/postgres/_ainternal.py:
--------------------------------------------------------------------------------
 1 | """Shared async utility functions for the Postgres checkpoint & storage classes."""
 2 | 
 3 | from collections.abc import AsyncIterator
 4 | from contextlib import asynccontextmanager
 5 | from typing import Union
 6 | 
 7 | from psycopg import AsyncConnection
 8 | from psycopg.rows import DictRow
 9 | from psycopg_pool import AsyncConnectionPool
10 | 
11 | Conn = Union[AsyncConnection[DictRow], AsyncConnectionPool[AsyncConnection[DictRow]]]
12 | 
13 | 
14 | @asynccontextmanager
15 | async def get_connection(
16 |     conn: Conn,
17 | ) -> AsyncIterator[AsyncConnection[DictRow]]:
18 |     if isinstance(conn, AsyncConnection):
19 |         yield conn
20 |     elif isinstance(conn, AsyncConnectionPool):
21 |         async with conn.connection() as conn:
22 |             yield conn
23 |     else:
24 |         raise TypeError(f"Invalid connection type: {type(conn)}")
25 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/langgraph/checkpoint/postgres/_internal.py:
--------------------------------------------------------------------------------
 1 | """Shared utility functions for the Postgres checkpoint & storage classes."""
 2 | 
 3 | from collections.abc import Iterator
 4 | from contextlib import contextmanager
 5 | from typing import Union
 6 | 
 7 | from psycopg import Connection
 8 | from psycopg.rows import DictRow
 9 | from psycopg_pool import ConnectionPool
10 | 
11 | Conn = Union[Connection[DictRow], ConnectionPool[Connection[DictRow]]]
12 | 
13 | 
14 | @contextmanager
15 | def get_connection(conn: Conn) -> Iterator[Connection[DictRow]]:
16 |     if isinstance(conn, Connection):
17 |         yield conn
18 |     elif isinstance(conn, ConnectionPool):
19 |         with conn.connection() as conn:
20 |             yield conn
21 |     else:
22 |         raise TypeError(f"Invalid connection type: {type(conn)}")
23 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/langgraph/checkpoint/postgres/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint-postgres/langgraph/checkpoint/postgres/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/langgraph/store/postgres/__init__.py:
--------------------------------------------------------------------------------
1 | from langgraph.store.postgres.aio import AsyncPostgresStore
2 | from langgraph.store.postgres.base import PostgresStore
3 | 
4 | __all__ = ["AsyncPostgresStore", "PostgresStore"]
5 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/langgraph/store/postgres/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint-postgres/langgraph/store/postgres/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph-checkpoint-postgres"
 3 | version = "2.0.9"
 4 | description = "Library with a Postgres implementation of LangGraph checkpoint saver."
 5 | authors = []
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | repository = "https://www.github.com/langchain-ai/langgraph"
 9 | packages = [{ include = "langgraph" }]
10 | 
11 | [tool.poetry.dependencies]
12 | python = "^3.9.0,<4.0"
13 | langgraph-checkpoint = "^2.0.7"
14 | orjson = ">=3.10.1"
15 | psycopg = "^3.2.0"
16 | psycopg-pool = "^3.2.0"
17 | 
18 | [tool.poetry.group.dev.dependencies]
19 | ruff = "^0.6.2"
20 | codespell = "^2.2.0"
21 | pytest = "^7.2.1"
22 | anyio = "^4.4.0"
23 | pytest-asyncio = "^0.21.1"
24 | pytest-mock = "^3.11.1"
25 | pytest-watch = "^4.2.0"
26 | mypy = "^1.10.0"
27 | psycopg = {extras = ["binary"], version = ">=3.0.0"}
28 | langgraph-checkpoint = {path = "../checkpoint", develop = true}
29 | 
30 | [tool.pytest.ini_options]
31 | # --strict-markers will raise errors on unknown marks.
32 | # https://docs.pytest.org/en/7.1.x/how-to/mark.html#raising-errors-on-unknown-marks
33 | #
34 | # https://docs.pytest.org/en/7.1.x/reference/reference.html
35 | # --strict-config       any warnings encountered while parsing the `pytest`
36 | #                       section of the configuration file raise errors.
37 | addopts = "--strict-markers --strict-config --durations=5 -vv"
38 | asyncio_mode = "auto"
39 | 
40 | 
41 | [build-system]
42 | requires = ["poetry-core"]
43 | build-backend = "poetry.core.masonry.api"
44 | 
45 | [tool.ruff]
46 | lint.select = [
47 |   "E",  # pycodestyle
48 |   "F",  # Pyflakes
49 |   "UP", # pyupgrade
50 |   "B",  # flake8-bugbear
51 |   "I",  # isort
52 | ]
53 | lint.ignore = ["E501", "B008", "UP007", "UP006"]
54 | 
55 | [tool.mypy]
56 | # https://mypy.readthedocs.io/en/stable/config_file.html
57 | disallow_untyped_defs = "True"
58 | explicit_package_bases = "True"
59 | warn_no_return = "False"
60 | warn_unused_ignores = "True"
61 | warn_redundant_casts = "True"
62 | allow_redefinition = "True"
63 | disable_error_code = "typeddict-item, return-value"
64 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint-postgres/tests/__init__.py


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/tests/compose-postgres.yml:
--------------------------------------------------------------------------------
 1 | services:
 2 |   postgres-test:
 3 |     image: pgvector/pgvector:pg${POSTGRES_VERSION:-16}
 4 |     ports:
 5 |       - "5441:5432"
 6 |     environment:
 7 |       POSTGRES_DB: postgres
 8 |       POSTGRES_USER: postgres
 9 |       POSTGRES_PASSWORD: postgres
10 |     command: ["postgres", "-c", "shared_preload_libraries=vector"]
11 |     healthcheck:
12 |       test: pg_isready -U postgres
13 |       start_period: 10s
14 |       timeout: 1s
15 |       retries: 5
16 |       interval: 60s
17 |       start_interval: 1s
18 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/tests/conftest.py:
--------------------------------------------------------------------------------
 1 | from collections.abc import AsyncIterator
 2 | 
 3 | import pytest
 4 | from psycopg import AsyncConnection
 5 | from psycopg.errors import UndefinedTable
 6 | from psycopg.rows import DictRow, dict_row
 7 | 
 8 | from tests.embed_test_utils import CharacterEmbeddings
 9 | 
10 | DEFAULT_POSTGRES_URI = "postgres://postgres:postgres@localhost:5441/"
11 | DEFAULT_URI = "postgres://postgres:postgres@localhost:5441/postgres?sslmode=disable"
12 | 
13 | 
14 | @pytest.fixture(scope="function")
15 | async def conn() -> AsyncIterator[AsyncConnection[DictRow]]:
16 |     async with await AsyncConnection.connect(
17 |         DEFAULT_URI, autocommit=True, prepare_threshold=0, row_factory=dict_row
18 |     ) as conn:
19 |         yield conn
20 | 
21 | 
22 | @pytest.fixture(scope="function", autouse=True)
23 | async def clear_test_db(conn: AsyncConnection[DictRow]) -> None:
24 |     """Delete all tables before each test."""
25 |     try:
26 |         await conn.execute("DELETE FROM checkpoints")
27 |         await conn.execute("DELETE FROM checkpoint_blobs")
28 |         await conn.execute("DELETE FROM checkpoint_writes")
29 |         await conn.execute("DELETE FROM checkpoint_migrations")
30 |     except UndefinedTable:
31 |         pass
32 |     try:
33 |         await conn.execute("DELETE FROM store_migrations")
34 |         await conn.execute("DELETE FROM store")
35 |     except UndefinedTable:
36 |         pass
37 | 
38 | 
39 | @pytest.fixture
40 | def fake_embeddings() -> CharacterEmbeddings:
41 |     return CharacterEmbeddings(dims=500)
42 | 
43 | 
44 | VECTOR_TYPES = ["vector", "halfvec"]
45 | 


--------------------------------------------------------------------------------
/libs/checkpoint-postgres/tests/embed_test_utils.py:
--------------------------------------------------------------------------------
 1 | """Embedding utilities for testing."""
 2 | 
 3 | import math
 4 | import random
 5 | from collections import Counter, defaultdict
 6 | from typing import Any
 7 | 
 8 | from langchain_core.embeddings import Embeddings
 9 | 
10 | 
11 | class CharacterEmbeddings(Embeddings):
12 |     """Simple character-frequency based embeddings using random projections."""
13 | 
14 |     def __init__(self, dims: int = 50, seed: int = 42):
15 |         """Initialize with embedding dimensions and random seed."""
16 |         self._rng = random.Random(seed)
17 |         self.dims = dims
18 |         # Create projection vector for each character lazily
19 |         self._char_projections: defaultdict[str, list[float]] = defaultdict(
20 |             lambda: [
21 |                 self._rng.gauss(0, 1 / math.sqrt(self.dims)) for _ in range(self.dims)
22 |             ]
23 |         )
24 | 
25 |     def _embed_one(self, text: str) -> list[float]:
26 |         """Embed a single text."""
27 |         counts = Counter(text)
28 |         total = sum(counts.values())
29 | 
30 |         if total == 0:
31 |             return [0.0] * self.dims
32 | 
33 |         embedding = [0.0] * self.dims
34 |         for char, count in counts.items():
35 |             weight = count / total
36 |             char_proj = self._char_projections[char]
37 |             for i, proj in enumerate(char_proj):
38 |                 embedding[i] += weight * proj
39 | 
40 |         norm = math.sqrt(sum(x * x for x in embedding))
41 |         if norm > 0:
42 |             embedding = [x / norm for x in embedding]
43 | 
44 |         return embedding
45 | 
46 |     def embed_documents(self, texts: list[str]) -> list[list[float]]:
47 |         """Embed a list of documents."""
48 |         return [self._embed_one(text) for text in texts]
49 | 
50 |     def embed_query(self, text: str) -> list[float]:
51 |         """Embed a query string."""
52 |         return self._embed_one(text)
53 | 
54 |     def __eq__(self, other: Any) -> bool:
55 |         return isinstance(other, CharacterEmbeddings) and self.dims == other.dims
56 | 


--------------------------------------------------------------------------------
/libs/checkpoint-sqlite/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: test test_watch lint format
 2 | 
 3 | ######################
 4 | # TESTING AND COVERAGE
 5 | ######################
 6 | 
 7 | test:
 8 | 	poetry run pytest tests
 9 | 
10 | test_watch:
11 | 	poetry run ptw .
12 | 
13 | ######################
14 | # LINTING AND FORMATTING
15 | ######################
16 | 
17 | # Define a variable for Python and notebook files.
18 | PYTHON_FILES=.
19 | MYPY_CACHE=.mypy_cache
20 | lint format: PYTHON_FILES=.
21 | lint_diff format_diff: PYTHON_FILES=$(shell git diff --name-only --relative --diff-filter=d main . | grep -E '\.py$$|\.ipynb$$')
22 | lint_package: PYTHON_FILES=langgraph
23 | lint_tests: PYTHON_FILES=tests
24 | lint_tests: MYPY_CACHE=.mypy_cache_test
25 | 
26 | lint lint_diff lint_package lint_tests:
27 | 	poetry run ruff check .
28 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff format $(PYTHON_FILES) --diff
29 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff check --select I $(PYTHON_FILES)
30 | 	[ "$(PYTHON_FILES)" = "" ] || mkdir -p $(MYPY_CACHE)
31 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run mypy $(PYTHON_FILES) --cache-dir $(MYPY_CACHE)
32 | 
33 | format format_diff:
34 | 	poetry run ruff format $(PYTHON_FILES)
35 | 	poetry run ruff check --select I --fix $(PYTHON_FILES)
36 | 


--------------------------------------------------------------------------------
/libs/checkpoint-sqlite/README.md:
--------------------------------------------------------------------------------
 1 | # LangGraph SQLite Checkpoint
 2 | 
 3 | Implementation of LangGraph CheckpointSaver that uses SQLite DB (both sync and async, via `aiosqlite`)
 4 | 
 5 | ## Usage
 6 | 
 7 | ```python
 8 | from langgraph.checkpoint.sqlite import SqliteSaver
 9 | 
10 | write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
11 | read_config = {"configurable": {"thread_id": "1"}}
12 | 
13 | with SqliteSaver.from_conn_string(":memory:") as checkpointer:
14 |     checkpoint = {
15 |         "v": 1,
16 |         "ts": "2024-07-31T20:14:19.804150+00:00",
17 |         "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
18 |         "channel_values": {
19 |             "my_key": "meow",
20 |             "node": "node"
21 |         },
22 |         "channel_versions": {
23 |             "__start__": 2,
24 |             "my_key": 3,
25 |             "start:node": 3,
26 |             "node": 3
27 |         },
28 |         "versions_seen": {
29 |             "__input__": {},
30 |             "__start__": {
31 |                 "__start__": 1
32 |             },
33 |             "node": {
34 |                 "start:node": 2
35 |             }
36 |         },
37 |         "pending_sends": [],
38 |     }
39 | 
40 |     # store checkpoint
41 |     checkpointer.put(write_config, checkpoint, {}, {})
42 | 
43 |     # load checkpoint
44 |     checkpointer.get(read_config)
45 | 
46 |     # list checkpoints
47 |     list(checkpointer.list(read_config))
48 | ```
49 | 
50 | ### Async
51 | 
52 | ```python
53 | from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
54 | 
55 | async with AsyncSqliteSaver.from_conn_string(":memory:") as checkpointer:
56 |     checkpoint = {
57 |         "v": 1,
58 |         "ts": "2024-07-31T20:14:19.804150+00:00",
59 |         "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
60 |         "channel_values": {
61 |             "my_key": "meow",
62 |             "node": "node"
63 |         },
64 |         "channel_versions": {
65 |             "__start__": 2,
66 |             "my_key": 3,
67 |             "start:node": 3,
68 |             "node": 3
69 |         },
70 |         "versions_seen": {
71 |             "__input__": {},
72 |             "__start__": {
73 |                 "__start__": 1
74 |             },
75 |             "node": {
76 |                 "start:node": 2
77 |             }
78 |         },
79 |         "pending_sends": [],
80 |     }
81 | 
82 |     # store checkpoint
83 |     await checkpointer.aput(write_config, checkpoint, {}, {})
84 | 
85 |     # load checkpoint
86 |     await checkpointer.aget(read_config)
87 | 
88 |     # list checkpoints
89 |     [c async for c in checkpointer.alist(read_config)]
90 | ```
91 | 


--------------------------------------------------------------------------------
/libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint-sqlite/langgraph/checkpoint/sqlite/utils.py:
--------------------------------------------------------------------------------
 1 | import json
 2 | from typing import Any, Dict, Optional, Sequence, Tuple
 3 | 
 4 | from langchain_core.runnables import RunnableConfig
 5 | 
 6 | from langgraph.checkpoint.base import get_checkpoint_id
 7 | 
 8 | 
 9 | def _metadata_predicate(
10 |     metadata_filter: Dict[str, Any],
11 | ) -> Tuple[Sequence[str], Sequence[Any]]:
12 |     """Return WHERE clause predicates for (a)search() given metadata filter.
13 | 
14 |     This method returns a tuple of a string and a tuple of values. The string
15 |     is the parametered WHERE clause predicate (excluding the WHERE keyword):
16 |     "column1 = ? AND column2 IS ?". The tuple of values contains the values
17 |     for each of the corresponding parameters.
18 |     """
19 | 
20 |     def _where_value(query_value: Any) -> Tuple[str, Any]:
21 |         """Return tuple of operator and value for WHERE clause predicate."""
22 |         if query_value is None:
23 |             return ("IS ?", None)
24 |         elif (
25 |             isinstance(query_value, str)
26 |             or isinstance(query_value, int)
27 |             or isinstance(query_value, float)
28 |         ):
29 |             return ("= ?", query_value)
30 |         elif isinstance(query_value, bool):
31 |             return ("= ?", 1 if query_value else 0)
32 |         elif isinstance(query_value, dict) or isinstance(query_value, list):
33 |             # query value for JSON object cannot have trailing space after separators (, :)
34 |             # SQLite json_extract() returns JSON string without whitespace
35 |             return ("= ?", json.dumps(query_value, separators=(",", ":")))
36 |         else:
37 |             return ("= ?", str(query_value))
38 | 
39 |     predicates = []
40 |     param_values = []
41 | 
42 |     # process metadata query
43 |     for query_key, query_value in metadata_filter.items():
44 |         operator, param_value = _where_value(query_value)
45 |         predicates.append(
46 |             f"json_extract(CAST(metadata AS TEXT), '$.{query_key}') {operator}"
47 |         )
48 |         param_values.append(param_value)
49 | 
50 |     return (predicates, param_values)
51 | 
52 | 
53 | def search_where(
54 |     config: Optional[RunnableConfig],
55 |     filter: Optional[Dict[str, Any]],
56 |     before: Optional[RunnableConfig] = None,
57 | ) -> Tuple[str, Sequence[Any]]:
58 |     """Return WHERE clause predicates for (a)search() given metadata filter
59 |     and `before` config.
60 | 
61 |     This method returns a tuple of a string and a tuple of values. The string
62 |     is the parametered WHERE clause predicate (including the WHERE keyword):
63 |     "WHERE column1 = ? AND column2 IS ?". The tuple of values contains the
64 |     values for each of the corresponding parameters.
65 |     """
66 |     wheres = []
67 |     param_values = []
68 | 
69 |     # construct predicate for config filter
70 |     if config is not None:
71 |         wheres.append("thread_id = ?")
72 |         param_values.append(config["configurable"]["thread_id"])
73 |         checkpoint_ns = config["configurable"].get("checkpoint_ns")
74 |         if checkpoint_ns is not None:
75 |             wheres.append("checkpoint_ns = ?")
76 |             param_values.append(checkpoint_ns)
77 | 
78 |         if checkpoint_id := get_checkpoint_id(config):
79 |             wheres.append("checkpoint_id = ?")
80 |             param_values.append(checkpoint_id)
81 | 
82 |     # construct predicate for metadata filter
83 |     if filter:
84 |         metadata_predicates, metadata_values = _metadata_predicate(filter)
85 |         wheres.extend(metadata_predicates)
86 |         param_values.extend(metadata_values)
87 | 
88 |     # construct predicate for `before`
89 |     if before is not None:
90 |         wheres.append("checkpoint_id < ?")
91 |         param_values.append(get_checkpoint_id(before))
92 | 
93 |     return ("WHERE " + " AND ".join(wheres) if wheres else "", param_values)
94 | 


--------------------------------------------------------------------------------
/libs/checkpoint-sqlite/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph-checkpoint-sqlite"
 3 | version = "2.0.1"
 4 | description = "Library with a SQLite implementation of LangGraph checkpoint saver."
 5 | authors = []
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | repository = "https://www.github.com/langchain-ai/langgraph"
 9 | packages = [{ include = "langgraph" }]
10 | 
11 | [tool.poetry.dependencies]
12 | python = "^3.9.0"
13 | langgraph-checkpoint = "^2.0.2"
14 | aiosqlite = "^0.20.0"
15 | 
16 | [tool.poetry.group.dev.dependencies]
17 | ruff = "^0.6.2"
18 | codespell = "^2.2.0"
19 | pytest = "^7.2.1"
20 | pytest-asyncio = "^0.21.1"
21 | pytest-mock = "^3.11.1"
22 | pytest-watcher = "^0.4.1"
23 | mypy = "^1.10.0"
24 | langgraph-checkpoint = {path = "../checkpoint", develop = true}
25 | 
26 | [tool.pytest.ini_options]
27 | # --strict-markers will raise errors on unknown marks.
28 | # https://docs.pytest.org/en/7.1.x/how-to/mark.html#raising-errors-on-unknown-marks
29 | #
30 | # https://docs.pytest.org/en/7.1.x/reference/reference.html
31 | # --strict-config       any warnings encountered while parsing the `pytest`
32 | #                       section of the configuration file raise errors.
33 | addopts = "--strict-markers --strict-config --durations=5 -vv"
34 | asyncio_mode = "auto"
35 | 
36 | 
37 | [build-system]
38 | requires = ["poetry-core"]
39 | build-backend = "poetry.core.masonry.api"
40 | 
41 | [tool.ruff]
42 | lint.select = [
43 |   "E",  # pycodestyle
44 |   "F",  # Pyflakes
45 |   "UP", # pyupgrade
46 |   "B",  # flake8-bugbear
47 |   "I",  # isort
48 | ]
49 | lint.ignore = ["E501", "B008", "UP007", "UP006"]
50 | 
51 | [tool.pytest-watcher]
52 | now = true
53 | delay = 0.1
54 | runner_args = ["--ff", "-v", "--tb", "short"]
55 | patterns = ["*.py"]
56 | 
57 | [tool.mypy]
58 | # https://mypy.readthedocs.io/en/stable/config_file.html
59 | disallow_untyped_defs = "True"
60 | explicit_package_bases = "True"
61 | warn_no_return = "False"
62 | warn_unused_ignores = "True"
63 | warn_redundant_casts = "True"
64 | allow_redefinition = "True"
65 | disable_error_code = "typeddict-item, return-value"
66 | 


--------------------------------------------------------------------------------
/libs/checkpoint-sqlite/tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint-sqlite/tests/__init__.py


--------------------------------------------------------------------------------
/libs/checkpoint-sqlite/tests/test_aiosqlite.py:
--------------------------------------------------------------------------------
  1 | from typing import Any
  2 | 
  3 | import pytest
  4 | from langchain_core.runnables import RunnableConfig
  5 | 
  6 | from langgraph.checkpoint.base import (
  7 |     Checkpoint,
  8 |     CheckpointMetadata,
  9 |     create_checkpoint,
 10 |     empty_checkpoint,
 11 | )
 12 | from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
 13 | 
 14 | 
 15 | class TestAsyncSqliteSaver:
 16 |     @pytest.fixture(autouse=True)
 17 |     def setup(self) -> None:
 18 |         # objects for test setup
 19 |         self.config_1: RunnableConfig = {
 20 |             "configurable": {
 21 |                 "thread_id": "thread-1",
 22 |                 # for backwards compatibility testing
 23 |                 "thread_ts": "1",
 24 |                 "checkpoint_ns": "",
 25 |             }
 26 |         }
 27 |         self.config_2: RunnableConfig = {
 28 |             "configurable": {
 29 |                 "thread_id": "thread-2",
 30 |                 "checkpoint_id": "2",
 31 |                 "checkpoint_ns": "",
 32 |             }
 33 |         }
 34 |         self.config_3: RunnableConfig = {
 35 |             "configurable": {
 36 |                 "thread_id": "thread-2",
 37 |                 "checkpoint_id": "2-inner",
 38 |                 "checkpoint_ns": "inner",
 39 |             }
 40 |         }
 41 | 
 42 |         self.chkpnt_1: Checkpoint = empty_checkpoint()
 43 |         self.chkpnt_2: Checkpoint = create_checkpoint(self.chkpnt_1, {}, 1)
 44 |         self.chkpnt_3: Checkpoint = empty_checkpoint()
 45 | 
 46 |         self.metadata_1: CheckpointMetadata = {
 47 |             "source": "input",
 48 |             "step": 2,
 49 |             "writes": {},
 50 |             "score": 1,
 51 |         }
 52 |         self.metadata_2: CheckpointMetadata = {
 53 |             "source": "loop",
 54 |             "step": 1,
 55 |             "writes": {"foo": "bar"},
 56 |             "score": None,
 57 |         }
 58 |         self.metadata_3: CheckpointMetadata = {}
 59 | 
 60 |     async def test_asearch(self) -> None:
 61 |         async with AsyncSqliteSaver.from_conn_string(":memory:") as saver:
 62 |             await saver.aput(self.config_1, self.chkpnt_1, self.metadata_1, {})
 63 |             await saver.aput(self.config_2, self.chkpnt_2, self.metadata_2, {})
 64 |             await saver.aput(self.config_3, self.chkpnt_3, self.metadata_3, {})
 65 | 
 66 |             # call method / assertions
 67 |             query_1 = {"source": "input"}  # search by 1 key
 68 |             query_2 = {
 69 |                 "step": 1,
 70 |                 "writes": {"foo": "bar"},
 71 |             }  # search by multiple keys
 72 |             query_3: dict[str, Any] = {}  # search by no keys, return all checkpoints
 73 |             query_4 = {"source": "update", "step": 1}  # no match
 74 | 
 75 |             search_results_1 = [c async for c in saver.alist(None, filter=query_1)]
 76 |             assert len(search_results_1) == 1
 77 |             assert search_results_1[0].metadata == self.metadata_1
 78 | 
 79 |             search_results_2 = [c async for c in saver.alist(None, filter=query_2)]
 80 |             assert len(search_results_2) == 1
 81 |             assert search_results_2[0].metadata == self.metadata_2
 82 | 
 83 |             search_results_3 = [c async for c in saver.alist(None, filter=query_3)]
 84 |             assert len(search_results_3) == 3
 85 | 
 86 |             search_results_4 = [c async for c in saver.alist(None, filter=query_4)]
 87 |             assert len(search_results_4) == 0
 88 | 
 89 |             # search by config (defaults to checkpoints across all namespaces)
 90 |             search_results_5 = [
 91 |                 c
 92 |                 async for c in saver.alist({"configurable": {"thread_id": "thread-2"}})
 93 |             ]
 94 |             assert len(search_results_5) == 2
 95 |             assert {
 96 |                 search_results_5[0].config["configurable"]["checkpoint_ns"],
 97 |                 search_results_5[1].config["configurable"]["checkpoint_ns"],
 98 |             } == {"", "inner"}
 99 | 
100 |             # TODO: test before and limit params
101 | 


--------------------------------------------------------------------------------
/libs/checkpoint/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2024 LangChain, Inc.
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/libs/checkpoint/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: test test_watch lint format
 2 | 
 3 | ######################
 4 | # TESTING AND COVERAGE
 5 | ######################
 6 | 
 7 | TEST ?= .
 8 | 
 9 | test:
10 | 	poetry run pytest $(TEST)
11 | 
12 | test_watch:
13 | 	poetry run ptw $(TEST)
14 | 
15 | ######################
16 | # LINTING AND FORMATTING
17 | ######################
18 | 
19 | # Define a variable for Python and notebook files.
20 | PYTHON_FILES=.
21 | MYPY_CACHE=.mypy_cache
22 | lint format: PYTHON_FILES=.
23 | lint_diff format_diff: PYTHON_FILES=$(shell git diff --name-only --relative --diff-filter=d main . | grep -E '\.py$$|\.ipynb$$')
24 | lint_package: PYTHON_FILES=langgraph
25 | lint_tests: PYTHON_FILES=tests
26 | lint_tests: MYPY_CACHE=.mypy_cache_test
27 | 
28 | lint lint_diff lint_package lint_tests:
29 | 	poetry run ruff check .
30 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff format $(PYTHON_FILES) --diff
31 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff check --select I $(PYTHON_FILES)
32 | 	[ "$(PYTHON_FILES)" = "" ] || mkdir -p $(MYPY_CACHE)
33 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run mypy $(PYTHON_FILES) --cache-dir $(MYPY_CACHE)
34 | 
35 | format format_diff:
36 | 	poetry run ruff format $(PYTHON_FILES)
37 | 	poetry run ruff check --select I --fix $(PYTHON_FILES)
38 | 


--------------------------------------------------------------------------------
/libs/checkpoint/README.md:
--------------------------------------------------------------------------------
 1 | # LangGraph Checkpoint
 2 | 
 3 | This library defines the base interface for LangGraph checkpointers. Checkpointers provide persistence layer for LangGraph. They allow you to interact with and manage the graph's state. When you use a graph with a checkpointer, the checkpointer saves a _checkpoint_ of the graph state at every superstep, enabling several powerful capabilities like human-in-the-loop, "memory" between interactions and more.
 4 | 
 5 | ## Key concepts
 6 | 
 7 | ### Checkpoint
 8 | 
 9 | Checkpoint is a snapshot of the graph state at a given point in time. Checkpoint tuple refers to an object containing checkpoint and the associated config, metadata and pending writes.
10 | 
11 | ### Thread
12 | 
13 | Threads enable the checkpointing of multiple different runs, making them essential for multi-tenant chat applications and other scenarios where maintaining separate states is necessary. A thread is a unique ID assigned to a series of checkpoints saved by a checkpointer. When using a checkpointer, you must specify a `thread_id` and optionally `checkpoint_id` when running the graph.
14 | 
15 | - `thread_id` is simply the ID of a thread. This is always required
16 | - `checkpoint_id` can optionally be passed. This identifier refers to a specific checkpoint within a thread. This can be used to kick of a run of a graph from some point halfway through a thread.
17 | 
18 | You must pass these when invoking the graph as part of the configurable part of the config, e.g.
19 | 
20 | ```python
21 | {"configurable": {"thread_id": "1"}}  # valid config
22 | {"configurable": {"thread_id": "1", "checkpoint_id": "0c62ca34-ac19-445d-bbb0-5b4984975b2a"}}  # also valid config
23 | ```
24 | 
25 | ### Serde
26 | 
27 | `langgraph_checkpoint` also defines protocol for serialization/deserialization (serde) and provides an default implementation (`langgraph.checkpoint.serde.jsonplus.JsonPlusSerializer`) that handles a wide variety of types, including LangChain and LangGraph primitives, datetimes, enums and more.
28 | 
29 | ### Pending writes
30 | 
31 | When a graph node fails mid-execution at a given superstep, LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that superstep, so that whenever we resume graph execution from that superstep we don't re-run the successful nodes.
32 | 
33 | ## Interface
34 | 
35 | Each checkpointer should conform to `langgraph.checkpoint.base.BaseCheckpointSaver` interface and must implement the following methods:
36 | 
37 | - `.put` - Store a checkpoint with its configuration and metadata.
38 | - `.put_writes` - Store intermediate writes linked to a checkpoint (i.e. pending writes).
39 | - `.get_tuple` - Fetch a checkpoint tuple using for a given configuration (`thread_id` and `thread_ts`).
40 | - `.list` - List checkpoints that match a given configuration and filter criteria.
41 | 
42 | If the checkpointer will be used with asynchronous graph execution (i.e. executing the graph via `.ainvoke`, `.astream`, `.abatch`), checkpointer must implement asynchronous versions of the above methods (`.aput`, `.aput_writes`, `.aget_tuple`, `.alist`).
43 | 
44 | ## Usage
45 | 
46 | ```python
47 | from langgraph.checkpoint.memory import MemorySaver
48 | 
49 | write_config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
50 | read_config = {"configurable": {"thread_id": "1"}}
51 | 
52 | checkpointer = MemorySaver()
53 | checkpoint = {
54 |     "v": 1,
55 |     "ts": "2024-07-31T20:14:19.804150+00:00",
56 |     "id": "1ef4f797-8335-6428-8001-8a1503f9b875",
57 |     "channel_values": {
58 |       "my_key": "meow",
59 |       "node": "node"
60 |     },
61 |     "channel_versions": {
62 |       "__start__": 2,
63 |       "my_key": 3,
64 |       "start:node": 3,
65 |       "node": 3
66 |     },
67 |     "versions_seen": {
68 |       "__input__": {},
69 |       "__start__": {
70 |         "__start__": 1
71 |       },
72 |       "node": {
73 |         "start:node": 2
74 |       }
75 |     },
76 |     "pending_sends": [],
77 | }
78 | 
79 | # store checkpoint
80 | checkpointer.put(write_config, checkpoint, {}, {})
81 | 
82 | # load checkpoint
83 | checkpointer.get(read_config)
84 | 
85 | # list checkpoints
86 | list(checkpointer.list(read_config))
87 | ```
88 | 


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/checkpoint/base/id.py:
--------------------------------------------------------------------------------
  1 | """Adapted from
  2 | https://github.com/oittaa/uuid6-python/blob/main/src/uuid6/__init__.py#L95
  3 | Bundled in to avoid install issues with uuid6 package
  4 | """
  5 | 
  6 | import random
  7 | import time
  8 | import uuid
  9 | from typing import Optional, Tuple
 10 | 
 11 | _last_v6_timestamp = None
 12 | 
 13 | 
 14 | class UUID(uuid.UUID):
 15 |     r"""UUID draft version objects"""
 16 | 
 17 |     __slots__ = ()
 18 | 
 19 |     def __init__(
 20 |         self,
 21 |         hex: Optional[str] = None,
 22 |         bytes: Optional[bytes] = None,
 23 |         bytes_le: Optional[bytes] = None,
 24 |         fields: Optional[Tuple[int, int, int, int, int, int]] = None,
 25 |         int: Optional[int] = None,
 26 |         version: Optional[int] = None,
 27 |         *,
 28 |         is_safe: uuid.SafeUUID = uuid.SafeUUID.unknown,
 29 |     ) -> None:
 30 |         r"""Create a UUID."""
 31 | 
 32 |         if int is None or [hex, bytes, bytes_le, fields].count(None) != 4:
 33 |             return super().__init__(
 34 |                 hex=hex,
 35 |                 bytes=bytes,
 36 |                 bytes_le=bytes_le,
 37 |                 fields=fields,
 38 |                 int=int,
 39 |                 version=version,
 40 |                 is_safe=is_safe,
 41 |             )
 42 |         if not 0 <= int < 1 << 128:
 43 |             raise ValueError("int is out of range (need a 128-bit value)")
 44 |         if version is not None:
 45 |             if not 6 <= version <= 8:
 46 |                 raise ValueError("illegal version number")
 47 |             # Set the variant to RFC 4122.
 48 |             int &= ~(0xC000 << 48)
 49 |             int |= 0x8000 << 48
 50 |             # Set the version number.
 51 |             int &= ~(0xF000 << 64)
 52 |             int |= version << 76
 53 |         super().__init__(int=int, is_safe=is_safe)
 54 | 
 55 |     @property
 56 |     def subsec(self) -> int:
 57 |         return ((self.int >> 64) & 0x0FFF) << 8 | ((self.int >> 54) & 0xFF)
 58 | 
 59 |     @property
 60 |     def time(self) -> int:
 61 |         if self.version == 6:
 62 |             return (
 63 |                 (self.time_low << 28)
 64 |                 | (self.time_mid << 12)
 65 |                 | (self.time_hi_version & 0x0FFF)
 66 |             )
 67 |         if self.version == 7:
 68 |             return self.int >> 80
 69 |         if self.version == 8:
 70 |             return (self.int >> 80) * 10**6 + _subsec_decode(self.subsec)
 71 |         return super().time
 72 | 
 73 | 
 74 | def _subsec_decode(value: int) -> int:
 75 |     return -(-value * 10**6 // 2**20)
 76 | 
 77 | 
 78 | def uuid6(node: Optional[int] = None, clock_seq: Optional[int] = None) -> UUID:
 79 |     r"""UUID version 6 is a field-compatible version of UUIDv1, reordered for
 80 |     improved DB locality. It is expected that UUIDv6 will primarily be
 81 |     used in contexts where there are existing v1 UUIDs. Systems that do
 82 |     not involve legacy UUIDv1 SHOULD consider using UUIDv7 instead.
 83 | 
 84 |     If 'node' is not given, a random 48-bit number is chosen.
 85 | 
 86 |     If 'clock_seq' is given, it is used as the sequence number;
 87 |     otherwise a random 14-bit sequence number is chosen."""
 88 | 
 89 |     global _last_v6_timestamp
 90 | 
 91 |     nanoseconds = time.time_ns()
 92 |     # 0x01b21dd213814000 is the number of 100-ns intervals between the
 93 |     # UUID epoch 1582-10-15 00:00:00 and the Unix epoch 1970-01-01 00:00:00.
 94 |     timestamp = nanoseconds // 100 + 0x01B21DD213814000
 95 |     if _last_v6_timestamp is not None and timestamp <= _last_v6_timestamp:
 96 |         timestamp = _last_v6_timestamp + 1
 97 |     _last_v6_timestamp = timestamp
 98 |     if clock_seq is None:
 99 |         clock_seq = random.getrandbits(14)  # instead of stable storage
100 |     if node is None:
101 |         node = random.getrandbits(48)
102 |     time_high_and_time_mid = (timestamp >> 12) & 0xFFFFFFFFFFFF
103 |     time_low_and_version = timestamp & 0x0FFF
104 |     uuid_int = time_high_and_time_mid << 80
105 |     uuid_int |= time_low_and_version << 64
106 |     uuid_int |= (clock_seq & 0x3FFF) << 48
107 |     uuid_int |= node & 0xFFFFFFFFFFFF
108 |     return UUID(int=uuid_int, version=6)
109 | 


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/checkpoint/base/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint/langgraph/checkpoint/base/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/checkpoint/memory/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint/langgraph/checkpoint/memory/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/checkpoint/serde/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint/langgraph/checkpoint/serde/__init__.py


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/checkpoint/serde/base.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Protocol
 2 | 
 3 | 
 4 | class SerializerProtocol(Protocol):
 5 |     """Protocol for serialization and deserialization of objects.
 6 | 
 7 |     - `dumps`: Serialize an object to bytes.
 8 |     - `dumps_typed`: Serialize an object to a tuple (type, bytes).
 9 |     - `loads`: Deserialize an object from bytes.
10 |     - `loads_typed`: Deserialize an object from a tuple (type, bytes).
11 | 
12 |     Valid implementations include the `pickle`, `json` and `orjson` modules.
13 |     """
14 | 
15 |     def dumps(self, obj: Any) -> bytes: ...
16 | 
17 |     def dumps_typed(self, obj: Any) -> tuple[str, bytes]: ...
18 | 
19 |     def loads(self, data: bytes) -> Any: ...
20 | 
21 |     def loads_typed(self, data: tuple[str, bytes]) -> Any: ...
22 | 
23 | 
24 | class SerializerCompat(SerializerProtocol):
25 |     def __init__(self, serde: SerializerProtocol) -> None:
26 |         self.serde = serde
27 | 
28 |     def dumps(self, obj: Any) -> bytes:
29 |         return self.serde.dumps(obj)
30 | 
31 |     def loads(self, data: bytes) -> Any:
32 |         return self.serde.loads(data)
33 | 
34 |     def dumps_typed(self, obj: Any) -> tuple[str, bytes]:
35 |         return type(obj).__name__, self.serde.dumps(obj)
36 | 
37 |     def loads_typed(self, data: tuple[str, bytes]) -> Any:
38 |         return self.serde.loads(data[1])
39 | 
40 | 
41 | def maybe_add_typed_methods(serde: SerializerProtocol) -> SerializerProtocol:
42 |     """Wrap serde old serde implementations in a class with loads_typed and dumps_typed for backwards compatibility."""
43 | 
44 |     if not hasattr(serde, "loads_typed") or not hasattr(serde, "dumps_typed"):
45 |         return SerializerCompat(serde)
46 | 
47 |     return serde
48 | 


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/checkpoint/serde/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint/langgraph/checkpoint/serde/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/checkpoint/serde/types.py:
--------------------------------------------------------------------------------
 1 | from typing import (
 2 |     Any,
 3 |     Optional,
 4 |     Protocol,
 5 |     Sequence,
 6 |     TypeVar,
 7 |     runtime_checkable,
 8 | )
 9 | 
10 | from typing_extensions import Self
11 | 
12 | ERROR = "__error__"
13 | SCHEDULED = "__scheduled__"
14 | INTERRUPT = "__interrupt__"
15 | RESUME = "__resume__"
16 | TASKS = "__pregel_tasks"
17 | 
18 | Value = TypeVar("Value", covariant=True)
19 | Update = TypeVar("Update", contravariant=True)
20 | C = TypeVar("C")
21 | 
22 | 
23 | class ChannelProtocol(Protocol[Value, Update, C]):
24 |     # Mirrors langgraph.channels.base.BaseChannel
25 |     @property
26 |     def ValueType(self) -> Any: ...
27 | 
28 |     @property
29 |     def UpdateType(self) -> Any: ...
30 | 
31 |     def checkpoint(self) -> Optional[C]: ...
32 | 
33 |     def from_checkpoint(self, checkpoint: Optional[C]) -> Self: ...
34 | 
35 |     def update(self, values: Sequence[Update]) -> bool: ...
36 | 
37 |     def get(self) -> Value: ...
38 | 
39 |     def consume(self) -> bool: ...
40 | 
41 | 
42 | @runtime_checkable
43 | class SendProtocol(Protocol):
44 |     # Mirrors langgraph.constants.Send
45 |     node: str
46 |     arg: Any
47 | 
48 |     def __hash__(self) -> int: ...
49 | 
50 |     def __repr__(self) -> str: ...
51 | 
52 |     def __eq__(self, value: object) -> bool: ...
53 | 


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/store/base/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint/langgraph/store/base/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint/langgraph/store/memory/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint/langgraph/store/memory/py.typed


--------------------------------------------------------------------------------
/libs/checkpoint/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph-checkpoint"
 3 | version = "2.0.9"
 4 | description = "Library with base interfaces for LangGraph checkpoint savers."
 5 | authors = []
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | repository = "https://www.github.com/langchain-ai/langgraph"
 9 | packages = [{ include = "langgraph" }]
10 | 
11 | [tool.poetry.dependencies]
12 | python = "^3.9.0,<4.0"
13 | langchain-core = ">=0.2.38,<0.4"
14 | msgpack = "^1.1.0"
15 | 
16 | [tool.poetry.group.dev.dependencies]
17 | ruff = "^0.6.2"
18 | codespell = "^2.2.0"
19 | pytest = "^7.2.1"
20 | pytest-asyncio = "^0.21.1"
21 | pytest-mock = "^3.11.1"
22 | pytest-watcher = "^0.4.1"
23 | mypy = "^1.10.0"
24 | dataclasses-json = "^0.6.7"
25 | 
26 | [tool.pytest.ini_options]
27 | # --strict-markers will raise errors on unknown marks.
28 | # https://docs.pytest.org/en/7.1.x/how-to/mark.html#raising-errors-on-unknown-marks
29 | #
30 | # https://docs.pytest.org/en/7.1.x/reference/reference.html
31 | # --strict-config       any warnings encountered while parsing the `pytest`
32 | #                       section of the configuration file raise errors.
33 | addopts = "--strict-markers --strict-config --durations=5 -vv"
34 | asyncio_mode = "auto"
35 | 
36 | 
37 | [build-system]
38 | requires = ["poetry-core"]
39 | build-backend = "poetry.core.masonry.api"
40 | 
41 | [tool.ruff]
42 | lint.select = [
43 |   "E",  # pycodestyle
44 |   "F",  # Pyflakes
45 |   "UP", # pyupgrade
46 |   "B",  # flake8-bugbear
47 |   "I",  # isort
48 | ]
49 | lint.ignore = ["E501", "B008", "UP007", "UP006"]
50 | 
51 | [tool.pytest-watcher]
52 | now = true
53 | delay = 0.1
54 | runner_args = ["--ff", "-v", "--tb", "short"]
55 | patterns = ["*.py"]
56 | 
57 | [tool.mypy]
58 | # https://mypy.readthedocs.io/en/stable/config_file.html
59 | disallow_untyped_defs = "True"
60 | explicit_package_bases = "True"
61 | warn_no_return = "False"
62 | warn_unused_ignores = "True"
63 | warn_redundant_casts = "True"
64 | allow_redefinition = "True"
65 | disable_error_code = "typeddict-item, return-value"
66 | 


--------------------------------------------------------------------------------
/libs/checkpoint/tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/checkpoint/tests/__init__.py


--------------------------------------------------------------------------------
/libs/checkpoint/tests/embed_test_utils.py:
--------------------------------------------------------------------------------
 1 | """Embedding utilities for testing."""
 2 | 
 3 | import math
 4 | import random
 5 | from collections import Counter, defaultdict
 6 | from typing import Any
 7 | 
 8 | from langchain_core.embeddings import Embeddings
 9 | 
10 | 
11 | class CharacterEmbeddings(Embeddings):
12 |     """Simple character-frequency based embeddings using random projections."""
13 | 
14 |     def __init__(self, dims: int = 50, seed: int = 42):
15 |         """Initialize with embedding dimensions and random seed."""
16 |         self._rng = random.Random(seed)
17 |         self.dims = dims
18 |         # Create projection vector for each character lazily
19 |         self._char_projections: defaultdict[str, list[float]] = defaultdict(
20 |             lambda: [
21 |                 self._rng.gauss(0, 1 / math.sqrt(self.dims)) for _ in range(self.dims)
22 |             ]
23 |         )
24 | 
25 |     def _embed_one(self, text: str) -> list[float]:
26 |         """Embed a single text."""
27 |         counts = Counter(text)
28 |         total = sum(counts.values())
29 | 
30 |         if total == 0:
31 |             return [0.0] * self.dims
32 | 
33 |         embedding = [0.0] * self.dims
34 |         for char, count in counts.items():
35 |             weight = count / total
36 |             char_proj = self._char_projections[char]
37 |             for i, proj in enumerate(char_proj):
38 |                 embedding[i] += weight * proj
39 | 
40 |         norm = math.sqrt(sum(x * x for x in embedding))
41 |         if norm > 0:
42 |             embedding = [x / norm for x in embedding]
43 | 
44 |         return embedding
45 | 
46 |     def embed_documents(self, texts: list[str]) -> list[list[float]]:
47 |         """Embed a list of documents."""
48 |         return [self._embed_one(text) for text in texts]
49 | 
50 |     def embed_query(self, text: str) -> list[float]:
51 |         """Embed a query string."""
52 |         return self._embed_one(text)
53 | 
54 |     def __eq__(self, other: Any) -> bool:
55 |         return isinstance(other, CharacterEmbeddings) and self.dims == other.dims
56 | 


--------------------------------------------------------------------------------
/libs/cli/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2024 LangChain, Inc.
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/libs/cli/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: test lint format test-integration
 2 | 
 3 | ######################
 4 | # TESTING AND COVERAGE
 5 | ######################
 6 | 
 7 | test:
 8 | 	poetry run pytest tests/unit_tests
 9 | test-integration:
10 | 	poetry run pytest tests/integration_tests
11 | 
12 | ######################
13 | # LINTING AND FORMATTING
14 | ######################
15 | 
16 | # Define a variable for Python and notebook files.
17 | PYTHON_FILES=.
18 | MYPY_CACHE=.mypy_cache
19 | lint format: PYTHON_FILES=.
20 | lint_diff format_diff: PYTHON_FILES=$(shell git diff --name-only --relative --diff-filter=d main . | grep -E '\.py$$|\.ipynb$$')
21 | lint_package: PYTHON_FILES=langgraph_cli
22 | lint_tests: PYTHON_FILES=tests
23 | lint_tests: MYPY_CACHE=.mypy_cache_test
24 | 
25 | lint lint_diff lint_package lint_tests:
26 | 	poetry run ruff check .
27 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff format $(PYTHON_FILES) --diff
28 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff check --select I $(PYTHON_FILES)
29 | 	[ "$(PYTHON_FILES)" = "" ] || mkdir -p $(MYPY_CACHE) || poetry run mypy $(PYTHON_FILES) --cache-dir $(MYPY_CACHE)
30 | 
31 | format format_diff:
32 | 	poetry run ruff format $(PYTHON_FILES)
33 | 	poetry run ruff check --select I --fix $(PYTHON_FILES)
34 | 


--------------------------------------------------------------------------------
/libs/cli/README.md:
--------------------------------------------------------------------------------
  1 | # LangGraph CLI
  2 | 
  3 | The official command-line interface for LangGraph, providing tools to create, develop, and deploy LangGraph applications.
  4 | 
  5 | ## Installation
  6 | 
  7 | Install via pip:
  8 | ```bash
  9 | pip install langgraph-cli
 10 | ```
 11 | 
 12 | For development mode with hot reloading:
 13 | ```bash
 14 | pip install "langgraph-cli[inmem]"
 15 | ```
 16 | 
 17 | ## Commands
 18 | 
 19 | ### `langgraph new` 🌱
 20 | Create a new LangGraph project from a template
 21 | ```bash
 22 | langgraph new [PATH] --template TEMPLATE_NAME
 23 | ```
 24 | 
 25 | ### `langgraph dev` 🏃‍♀️
 26 | Run LangGraph API server in development mode with hot reloading
 27 | ```bash
 28 | langgraph dev [OPTIONS]
 29 |   --host TEXT                 Host to bind to (default: 127.0.0.1)
 30 |   --port INTEGER             Port to bind to (default: 2024)
 31 |   --no-reload               Disable auto-reload
 32 |   --debug-port INTEGER      Enable remote debugging
 33 |   --no-browser             Skip opening browser window
 34 |   -c, --config FILE        Config file path (default: langgraph.json)
 35 | ```
 36 | 
 37 | ### `langgraph up` 🚀
 38 | Launch LangGraph API server in Docker
 39 | ```bash
 40 | langgraph up [OPTIONS]
 41 |   -p, --port INTEGER        Port to expose (default: 8123)
 42 |   --wait                   Wait for services to start
 43 |   --watch                  Restart on file changes
 44 |   --verbose               Show detailed logs
 45 |   -c, --config FILE       Config file path
 46 |   -d, --docker-compose    Additional services file
 47 | ```
 48 | 
 49 | ### `langgraph build`
 50 | Build a Docker image for your LangGraph application
 51 | ```bash
 52 | langgraph build -t IMAGE_TAG [OPTIONS]
 53 |   --platform TEXT          Target platforms (e.g., linux/amd64,linux/arm64)
 54 |   --pull / --no-pull      Use latest/local base image
 55 |   -c, --config FILE       Config file path
 56 | ```
 57 | 
 58 | ### `langgraph dockerfile`
 59 | Generate a Dockerfile for custom deployments
 60 | ```bash
 61 | langgraph dockerfile SAVE_PATH [OPTIONS]
 62 |   -c, --config FILE       Config file path
 63 | ```
 64 | 
 65 | ## Configuration
 66 | 
 67 | The CLI uses a `langgraph.json` configuration file with these key settings:
 68 | 
 69 | ```json
 70 | {
 71 |   "dependencies": ["langchain_openai", "./your_package"],  // Required: Package dependencies
 72 |   "graphs": {
 73 |     "my_graph": "./your_package/file.py:graph"            // Required: Graph definitions
 74 |   },
 75 |   "env": "./.env",                                        // Optional: Environment variables
 76 |   "python_version": "3.11",                               // Optional: Python version (3.11/3.12)
 77 |   "pip_config_file": "./pip.conf",                        // Optional: pip configuration
 78 |   "dockerfile_lines": []                                  // Optional: Additional Dockerfile commands
 79 | }
 80 | ```
 81 | 
 82 | See the [full documentation](https://langchain-ai.github.io/langgraph/docs/cloud/reference/cli.html) for detailed configuration options.
 83 | 
 84 | ## Development
 85 | 
 86 | To develop the CLI itself:
 87 | 
 88 | 1. Clone the repository
 89 | 2. Navigate to the CLI directory: `cd libs/cli`
 90 | 3. Install development dependencies: `poetry install`
 91 | 4. Make your changes to the CLI code
 92 | 5. Test your changes:
 93 |    ```bash
 94 |    # Run CLI commands directly
 95 |    poetry run langgraph --help
 96 |    
 97 |    # Or use the examples
 98 |    cd examples
 99 |    poetry install
100 |    poetry run langgraph dev  # or other commands
101 |    ```
102 | 
103 | ## License
104 | 
105 | This project is licensed under the terms specified in the repository's LICENSE file.
106 | 


--------------------------------------------------------------------------------
/libs/cli/examples/.env.example:
--------------------------------------------------------------------------------
 1 | OPENAI_API_KEY=placeholder
 2 | ANTHROPIC_API_KEY=placeholder
 3 | TAVILY_API_KEY=placeholder
 4 | LANGCHAIN_TRACING_V2=false
 5 | LANGCHAIN_ENDPOINT=placeholder
 6 | LANGCHAIN_API_KEY=placeholder
 7 | LANGCHAIN_PROJECT=placeholder
 8 | LANGGRAPH_AUTH_TYPE=noop
 9 | LANGSMITH_AUTH_ENDPOINT=placeholder
10 | LANGSMITH_TENANT_ID=placeholder


--------------------------------------------------------------------------------
/libs/cli/examples/.gitignore:
--------------------------------------------------------------------------------
1 | .langgraph-data
2 | 


--------------------------------------------------------------------------------
/libs/cli/examples/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: run_w_override
 2 | 
 3 | run:
 4 | 	poetry run langgraph up --watch --no-pull
 5 | 
 6 | run_faux:
 7 | 	cd graphs && poetry run langgraph up --no-pull
 8 | 
 9 | run_graphs_reqs_a:
10 | 	cd graphs_reqs_a && poetry run langgraph up --no-pull
11 | 
12 | run_graphs_reqs_b:
13 | 	cd graphs_reqs_b && poetry run langgraph up --no-pull
14 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs/agent.py:
--------------------------------------------------------------------------------
 1 | from typing import Annotated, Literal, Sequence, TypedDict
 2 | 
 3 | from langchain_anthropic import ChatAnthropic
 4 | from langchain_community.tools.tavily_search import TavilySearchResults
 5 | from langchain_core.messages import BaseMessage
 6 | from langchain_openai import ChatOpenAI
 7 | from langgraph.graph import END, StateGraph, add_messages
 8 | from langgraph.prebuilt import ToolNode
 9 | 
10 | tools = [TavilySearchResults(max_results=1)]
11 | 
12 | model_anth = ChatAnthropic(temperature=0, model_name="claude-3-sonnet-20240229")
13 | model_oai = ChatOpenAI(temperature=0)
14 | 
15 | model_anth = model_anth.bind_tools(tools)
16 | model_oai = model_oai.bind_tools(tools)
17 | 
18 | 
19 | class AgentState(TypedDict):
20 |     messages: Annotated[Sequence[BaseMessage], add_messages]
21 | 
22 | 
23 | # Define the function that determines whether to continue or not
24 | def should_continue(state):
25 |     messages = state["messages"]
26 |     last_message = messages[-1]
27 |     # If there are no tool calls, then we finish
28 |     if not last_message.tool_calls:
29 |         return "end"
30 |     # Otherwise if there is, we continue
31 |     else:
32 |         return "continue"
33 | 
34 | 
35 | # Define the function that calls the model
36 | def call_model(state, config):
37 |     if config["configurable"].get("model", "anthropic") == "anthropic":
38 |         model = model_anth
39 |     else:
40 |         model = model_oai
41 |     messages = state["messages"]
42 |     response = model.invoke(messages)
43 |     # We return a list, because this will get added to the existing list
44 |     return {"messages": [response]}
45 | 
46 | 
47 | # Define the function to execute tools
48 | tool_node = ToolNode(tools)
49 | 
50 | 
51 | class ConfigSchema(TypedDict):
52 |     model: Literal["anthropic", "openai"]
53 | 
54 | 
55 | # Define a new graph
56 | workflow = StateGraph(AgentState, config_schema=ConfigSchema)
57 | 
58 | # Define the two nodes we will cycle between
59 | workflow.add_node("agent", call_model)
60 | workflow.add_node("action", tool_node)
61 | 
62 | # Set the entrypoint as `agent`
63 | # This means that this node is the first one called
64 | workflow.set_entry_point("agent")
65 | 
66 | # We now add a conditional edge
67 | workflow.add_conditional_edges(
68 |     # First, we define the start node. We use `agent`.
69 |     # This means these are the edges taken after the `agent` node is called.
70 |     "agent",
71 |     # Next, we pass in the function that will determine which node is called next.
72 |     should_continue,
73 |     # Finally we pass in a mapping.
74 |     # The keys are strings, and the values are other nodes.
75 |     # END is a special node marking that the graph should finish.
76 |     # What will happen is we will call `should_continue`, and then the output of that
77 |     # will be matched against the keys in this mapping.
78 |     # Based on which one it matches, that node will then be called.
79 |     {
80 |         # If `tools`, then we call the tool node.
81 |         "continue": "action",
82 |         # Otherwise we finish.
83 |         "end": END,
84 |     },
85 | )
86 | 
87 | # We now add a normal edge from `tools` to `agent`.
88 | # This means that after `tools` is called, `agent` node is called next.
89 | workflow.add_edge("action", "agent")
90 | 
91 | # Finally, we compile it!
92 | # This compiles it into a LangChain Runnable,
93 | # meaning you can use it as you would any other runnable
94 | graph = workflow.compile()
95 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs/langgraph.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "python_version": "3.12",
 3 |   "dependencies": [
 4 |     "langchain_community",
 5 |     "langchain_anthropic",
 6 |     "langchain_openai",
 7 |     "wikipedia",
 8 |     "scikit-learn",
 9 |     "."
10 |   ],
11 |   "graphs": {
12 |     "agent": "./agent.py:graph",
13 |     "storm": "./storm.py:graph"
14 |   },
15 |   "env": "../.env"
16 | }
17 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_a/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/examples/graphs_reqs_a/__init__.py


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_a/graphs_submod/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/examples/graphs_reqs_a/graphs_submod/__init__.py


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_a/graphs_submod/agent.py:
--------------------------------------------------------------------------------
 1 | from pathlib import Path
 2 | from typing import Annotated, Sequence, TypedDict
 3 | 
 4 | from langchain_anthropic import ChatAnthropic
 5 | from langchain_community.tools.tavily_search import TavilySearchResults
 6 | from langchain_core.messages import BaseMessage
 7 | from langchain_openai import ChatOpenAI
 8 | from langgraph.graph import END, StateGraph, add_messages
 9 | from langgraph.prebuilt import ToolNode
10 | 
11 | tools = [TavilySearchResults(max_results=1)]
12 | 
13 | model_anth = ChatAnthropic(temperature=0, model_name="claude-3-sonnet-20240229")
14 | model_oai = ChatOpenAI(temperature=0)
15 | 
16 | model_anth = model_anth.bind_tools(tools)
17 | model_oai = model_oai.bind_tools(tools)
18 | 
19 | prompt = open("prompt.txt").read()
20 | subprompt = open(Path(__file__).parent / "subprompt.txt").read()
21 | 
22 | 
23 | class AgentState(TypedDict):
24 |     messages: Annotated[Sequence[BaseMessage], add_messages]
25 | 
26 | 
27 | # Define the function that determines whether to continue or not
28 | def should_continue(state):
29 |     messages = state["messages"]
30 |     last_message = messages[-1]
31 |     # If there are no tool calls, then we finish
32 |     if not last_message.tool_calls:
33 |         return "end"
34 |     # Otherwise if there is, we continue
35 |     else:
36 |         return "continue"
37 | 
38 | 
39 | # Define the function that calls the model
40 | def call_model(state, config):
41 |     if config["configurable"].get("model", "anthropic") == "anthropic":
42 |         model = model_anth
43 |     else:
44 |         model = model_oai
45 |     messages = state["messages"]
46 |     response = model.invoke(messages)
47 |     # We return a list, because this will get added to the existing list
48 |     return {"messages": [response]}
49 | 
50 | 
51 | # Define the function to execute tools
52 | tool_node = ToolNode(tools)
53 | 
54 | 
55 | # Define a new graph
56 | workflow = StateGraph(AgentState)
57 | 
58 | # Define the two nodes we will cycle between
59 | workflow.add_node("agent", call_model)
60 | workflow.add_node("action", tool_node)
61 | 
62 | # Set the entrypoint as `agent`
63 | # This means that this node is the first one called
64 | workflow.set_entry_point("agent")
65 | 
66 | # We now add a conditional edge
67 | workflow.add_conditional_edges(
68 |     # First, we define the start node. We use `agent`.
69 |     # This means these are the edges taken after the `agent` node is called.
70 |     "agent",
71 |     # Next, we pass in the function that will determine which node is called next.
72 |     should_continue,
73 |     # Finally we pass in a mapping.
74 |     # The keys are strings, and the values are other nodes.
75 |     # END is a special node marking that the graph should finish.
76 |     # What will happen is we will call `should_continue`, and then the output of that
77 |     # will be matched against the keys in this mapping.
78 |     # Based on which one it matches, that node will then be called.
79 |     {
80 |         # If `tools`, then we call the tool node.
81 |         "continue": "action",
82 |         # Otherwise we finish.
83 |         "end": END,
84 |     },
85 | )
86 | 
87 | # We now add a normal edge from `tools` to `agent`.
88 | # This means that after `tools` is called, `agent` node is called next.
89 | workflow.add_edge("action", "agent")
90 | 
91 | # Finally, we compile it!
92 | # This compiles it into a LangChain Runnable,
93 | # meaning you can use it as you would any other runnable
94 | graph = workflow.compile()
95 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_a/graphs_submod/subprompt.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/examples/graphs_reqs_a/graphs_submod/subprompt.txt


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_a/hello.py:
--------------------------------------------------------------------------------
1 | from graphs_reqs_a.graphs_submod.agent import graph  # noqa
2 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_a/langgraph.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "dependencies": [
 3 |     "."
 4 |   ],
 5 |   "env": "../.env",
 6 |   "graphs": {
 7 |     "graph": "./hello.py:graph"
 8 |   }
 9 | }
10 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_a/prompt.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/examples/graphs_reqs_a/prompt.txt


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_a/requirements.txt:
--------------------------------------------------------------------------------
1 | requests
2 | langchain_anthropic
3 | langchain_openai
4 | langchain_community
5 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_b/graphs_submod/agent.py:
--------------------------------------------------------------------------------
 1 | from pathlib import Path
 2 | from typing import Annotated, Sequence, TypedDict
 3 | 
 4 | from langchain_anthropic import ChatAnthropic
 5 | from langchain_community.tools.tavily_search import TavilySearchResults
 6 | from langchain_core.messages import BaseMessage
 7 | from langchain_openai import ChatOpenAI
 8 | from langgraph.graph import END, StateGraph, add_messages
 9 | from langgraph.prebuilt import ToolNode
10 | 
11 | tools = [TavilySearchResults(max_results=1)]
12 | 
13 | model_anth = ChatAnthropic(temperature=0, model_name="claude-3-sonnet-20240229")
14 | model_oai = ChatOpenAI(temperature=0)
15 | 
16 | model_anth = model_anth.bind_tools(tools)
17 | model_oai = model_oai.bind_tools(tools)
18 | 
19 | prompt = open("prompt.txt").read()
20 | subprompt = open(Path(__file__).parent / "subprompt.txt").read()
21 | 
22 | 
23 | class AgentState(TypedDict):
24 |     messages: Annotated[Sequence[BaseMessage], add_messages]
25 | 
26 | 
27 | # Define the function that determines whether to continue or not
28 | def should_continue(state):
29 |     messages = state["messages"]
30 |     last_message = messages[-1]
31 |     # If there are no tool calls, then we finish
32 |     if not last_message.tool_calls:
33 |         return "end"
34 |     # Otherwise if there is, we continue
35 |     else:
36 |         return "continue"
37 | 
38 | 
39 | # Define the function that calls the model
40 | def call_model(state, config):
41 |     if config["configurable"].get("model", "anthropic") == "anthropic":
42 |         model = model_anth
43 |     else:
44 |         model = model_oai
45 |     messages = state["messages"]
46 |     response = model.invoke(messages)
47 |     # We return a list, because this will get added to the existing list
48 |     return {"messages": [response]}
49 | 
50 | 
51 | # Define the function to execute tools
52 | tool_node = ToolNode(tools)
53 | 
54 | 
55 | # Define a new graph
56 | workflow = StateGraph(AgentState)
57 | 
58 | # Define the two nodes we will cycle between
59 | workflow.add_node("agent", call_model)
60 | workflow.add_node("action", tool_node)
61 | 
62 | # Set the entrypoint as `agent`
63 | # This means that this node is the first one called
64 | workflow.set_entry_point("agent")
65 | 
66 | # We now add a conditional edge
67 | workflow.add_conditional_edges(
68 |     # First, we define the start node. We use `agent`.
69 |     # This means these are the edges taken after the `agent` node is called.
70 |     "agent",
71 |     # Next, we pass in the function that will determine which node is called next.
72 |     should_continue,
73 |     # Finally we pass in a mapping.
74 |     # The keys are strings, and the values are other nodes.
75 |     # END is a special node marking that the graph should finish.
76 |     # What will happen is we will call `should_continue`, and then the output of that
77 |     # will be matched against the keys in this mapping.
78 |     # Based on which one it matches, that node will then be called.
79 |     {
80 |         # If `tools`, then we call the tool node.
81 |         "continue": "action",
82 |         # Otherwise we finish.
83 |         "end": END,
84 |     },
85 | )
86 | 
87 | # We now add a normal edge from `tools` to `agent`.
88 | # This means that after `tools` is called, `agent` node is called next.
89 | workflow.add_edge("action", "agent")
90 | 
91 | # Finally, we compile it!
92 | # This compiles it into a LangChain Runnable,
93 | # meaning you can use it as you would any other runnable
94 | graph = workflow.compile()
95 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_b/graphs_submod/subprompt.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/examples/graphs_reqs_b/graphs_submod/subprompt.txt


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_b/hello.py:
--------------------------------------------------------------------------------
1 | from graphs_submod.agent import graph  # noqa
2 | from utils.greeter import greet
3 | 
4 | greet()
5 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_b/langgraph.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "dependencies": [
 3 |     "."
 4 |   ],
 5 |   "env": "../.env",
 6 |   "graphs": {
 7 |     "graph": "./hello.py:graph"
 8 |   }
 9 | }
10 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_b/prompt.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/examples/graphs_reqs_b/prompt.txt


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_b/requirements.txt:
--------------------------------------------------------------------------------
1 | requests
2 | langchain_anthropic
3 | langchain_openai
4 | langchain_community
5 | 


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_b/utils/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/examples/graphs_reqs_b/utils/__init__.py


--------------------------------------------------------------------------------
/libs/cli/examples/graphs_reqs_b/utils/greeter.py:
--------------------------------------------------------------------------------
1 | def greet():
2 |     print("Hello, world!")
3 | 


--------------------------------------------------------------------------------
/libs/cli/examples/langgraph.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "pip_config_file": "./pipconf.txt",
 3 |   "dependencies": [
 4 |     "langchain_community",
 5 |     "langchain_anthropic",
 6 |     "langchain_openai",
 7 |     "wikipedia",
 8 |     "scikit-learn",
 9 |     "./graphs"
10 |   ],
11 |   "graphs": {
12 |     "agent": "./graphs/agent.py:graph",
13 |     "storm": "./graphs/storm.py:graph"
14 |   },
15 |   "env": ".env"
16 | }
17 | 


--------------------------------------------------------------------------------
/libs/cli/examples/pipconf.txt:
--------------------------------------------------------------------------------
1 | [global]
2 | timeout = 60
3 | 


--------------------------------------------------------------------------------
/libs/cli/examples/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph-examples"
 3 | version = "0.1.0"
 4 | description = ""
 5 | authors = []
 6 | readme = "README.md"
 7 | packages = []
 8 | package-mode = false
 9 | 
10 | [tool.poetry.dependencies]
11 | python = "^3.9.0,<4.0"
12 | langgraph-cli = {path = "../../cli", develop = true}
13 | langgraph-sdk = {path = "../../sdk-py", develop = true}
14 | 
15 | [build-system]
16 | requires = ["poetry-core"]
17 | build-backend = "poetry.core.masonry.api"
18 | 


--------------------------------------------------------------------------------
1 | node_modules
2 | dist


--------------------------------------------------------------------------------
/libs/cli/js-examples/.editorconfig:
--------------------------------------------------------------------------------
 1 | root = true
 2 | 
 3 | [*]
 4 | end_of_line = lf
 5 | insert_final_newline = true
 6 | 
 7 | [*.{js,json,yml}]
 8 | charset = utf-8
 9 | indent_style = space
10 | indent_size = 2
11 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/.env.example:
--------------------------------------------------------------------------------
1 | # Copy this over:
2 | # cp .env.example .env
3 | # Then modify to suit your needs


--------------------------------------------------------------------------------
/libs/cli/js-examples/.eslintrc.cjs:
--------------------------------------------------------------------------------
 1 | module.exports = {
 2 |   extends: [
 3 |     "eslint:recommended",
 4 |     "prettier",
 5 |     "plugin:@typescript-eslint/recommended",
 6 |   ],
 7 |   parserOptions: {
 8 |     ecmaVersion: 12,
 9 |     parser: "@typescript-eslint/parser",
10 |     project: "./tsconfig.json",
11 |     sourceType: "module",
12 |   },
13 |   plugins: ["import", "@typescript-eslint", "no-instanceof"],
14 |   ignorePatterns: [
15 |     ".eslintrc.cjs",
16 |     "scripts",
17 |     "src/utils/lodash/*",
18 |     "node_modules",
19 |     "dist",
20 |     "dist-cjs",
21 |     "*.js",
22 |     "*.cjs",
23 |     "*.d.ts",
24 |   ],
25 |   rules: {
26 |     "no-process-env": 2,
27 |     "no-instanceof/no-instanceof": 2,
28 |     "@typescript-eslint/explicit-module-boundary-types": 0,
29 |     "@typescript-eslint/no-empty-function": 0,
30 |     "@typescript-eslint/no-shadow": 0,
31 |     "@typescript-eslint/no-empty-interface": 0,
32 |     "@typescript-eslint/no-use-before-define": ["error", "nofunc"],
33 |     "@typescript-eslint/no-unused-vars": ["warn", { args: "none" }],
34 |     "@typescript-eslint/no-floating-promises": "error",
35 |     "@typescript-eslint/no-misused-promises": "error",
36 |     camelcase: 0,
37 |     "class-methods-use-this": 0,
38 |     "import/extensions": [2, "ignorePackages"],
39 |     "import/no-extraneous-dependencies": [
40 |       "error",
41 |       { devDependencies: ["**/*.test.ts"] },
42 |     ],
43 |     "import/no-unresolved": 0,
44 |     "import/prefer-default-export": 0,
45 |     "keyword-spacing": "error",
46 |     "max-classes-per-file": 0,
47 |     "max-len": 0,
48 |     "no-await-in-loop": 0,
49 |     "no-bitwise": 0,
50 |     "no-console": 0,
51 |     "no-restricted-syntax": 0,
52 |     "no-shadow": 0,
53 |     "no-continue": 0,
54 |     "no-underscore-dangle": 0,
55 |     "no-use-before-define": 0,
56 |     "no-useless-constructor": 0,
57 |     "no-return-await": 0,
58 |     "consistent-return": 0,
59 |     "no-else-return": 0,
60 |     "new-cap": ["error", { properties: false, capIsNew: false }],
61 |   },
62 | };
63 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/.gitignore:
--------------------------------------------------------------------------------
 1 | index.cjs
 2 | index.js
 3 | index.d.ts
 4 | node_modules
 5 | dist
 6 | .yarn/*
 7 | !.yarn/patches
 8 | !.yarn/plugins
 9 | !.yarn/releases
10 | !.yarn/sdks
11 | !.yarn/versions
12 | 
13 | .turbo
14 | **/.turbo
15 | **/.eslintcache
16 | 
17 | .env
18 | .ipynb_checkpoints
19 | 
20 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2024 LangChain
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/jest.config.js:
--------------------------------------------------------------------------------
 1 | export default {
 2 |   preset: "ts-jest/presets/default-esm",
 3 |   moduleNameMapper: {
 4 |     "^(\\.{1,2}/.*)\\.js$": "$1",
 5 |   },
 6 |   transform: {
 7 |     "^.+\\.tsx?$": [
 8 |       "ts-jest",
 9 |       {
10 |         useESM: true,
11 |       },
12 |     ],
13 |   },
14 |   extensionsToTreatAsEsm: [".ts"],
15 |   setupFiles: ["dotenv/config"],
16 |   passWithNoTests: true,
17 |   testTimeout: 20_000,
18 | };
19 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/langgraph.json:
--------------------------------------------------------------------------------
1 | {
2 |   "node_version": "20",
3 |   "graphs": {
4 |     "agent": "./src/agent/graph.ts:graph"
5 |   },
6 |   "env": ".env",
7 |   "dependencies": ["."]
8 | }
9 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "example-graph",
 3 |   "version": "0.0.1",
 4 |   "description": "A starter template for creating a LangGraph workflow.",
 5 |   "packageManager": "yarn@1.22.22",
 6 |   "main": "my_app/graph.ts",
 7 |   "author": "Your Name",
 8 |   "license": "MIT",
 9 |   "private": true,
10 |   "type": "module",
11 |   "scripts": {
12 |     "build": "tsc",
13 |     "clean": "rm -rf dist",
14 |     "test": "node --experimental-vm-modules node_modules/jest/bin/jest.js --testPathPattern=\\.test\\.ts$ --testPathIgnorePatterns=\\.int\\.test\\.ts$",
15 |     "test:int": "node --experimental-vm-modules node_modules/jest/bin/jest.js --testPathPattern=\\.int\\.test\\.ts$",
16 |     "format": "prettier --write .",
17 |     "lint": "eslint src",
18 |     "format:check": "prettier --check .",
19 |     "lint:langgraph-json": "node scripts/checkLanggraphPaths.js",
20 |     "lint:all": "yarn lint & yarn lint:langgraph-json & yarn format:check",
21 |     "test:all": "yarn test && yarn test:int && yarn lint:langgraph"
22 |   },
23 |   "dependencies": {
24 |     "@langchain/core": "^0.3.2",
25 |     "@langchain/langgraph": "^0.2.5"
26 |   },
27 |   "devDependencies": {
28 |     "@eslint/eslintrc": "^3.1.0",
29 |     "@eslint/js": "^9.9.1",
30 |     "@tsconfig/recommended": "^1.0.7",
31 |     "@types/jest": "^29.5.0",
32 |     "@typescript-eslint/eslint-plugin": "^5.59.8",
33 |     "@typescript-eslint/parser": "^5.59.8",
34 |     "dotenv": "^16.4.5",
35 |     "eslint": "^8.41.0",
36 |     "eslint-config-prettier": "^8.8.0",
37 |     "eslint-plugin-import": "^2.27.5",
38 |     "eslint-plugin-no-instanceof": "^1.0.1",
39 |     "eslint-plugin-prettier": "^4.2.1",
40 |     "jest": "^29.7.0",
41 |     "prettier": "^3.3.3",
42 |     "ts-jest": "^29.1.0",
43 |     "typescript": "^5.3.3"
44 |   }
45 | }
46 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/src/agent/graph.ts:
--------------------------------------------------------------------------------
  1 | /**
  2 |  * Starter LangGraph.js Template
  3 |  * Make this code your own!
  4 |  */
  5 | import { StateGraph } from "@langchain/langgraph";
  6 | import { RunnableConfig } from "@langchain/core/runnables";
  7 | import { StateAnnotation } from "./state.js";
  8 | 
  9 | /**
 10 |  * Define a node, these do the work of the graph and should have most of the logic.
 11 |  * Must return a subset of the properties set in StateAnnotation.
 12 |  * @param state The current state of the graph.
 13 |  * @param config Extra parameters passed into the state graph.
 14 |  * @returns Some subset of parameters of the graph state, used to update the state
 15 |  * for the edges and nodes executed next.
 16 |  */
 17 | const callModel = async (
 18 |   state: typeof StateAnnotation.State,
 19 |   _config: RunnableConfig,
 20 | ): Promise<typeof StateAnnotation.Update> => {
 21 |   /**
 22 |    * Do some work... (e.g. call an LLM)
 23 |    * For example, with LangChain you could do something like:
 24 |    *
 25 |    * ```bash
 26 |    * $ npm i @langchain/anthropic
 27 |    * ```
 28 |    *
 29 |    * ```ts
 30 |    * import { ChatAnthropic } from "@langchain/anthropic";
 31 |    * const model = new ChatAnthropic({
 32 |    *   model: "claude-3-5-sonnet-20240620",
 33 |    *   apiKey: process.env.ANTHROPIC_API_KEY,
 34 |    * });
 35 |    * const res = await model.invoke(state.messages);
 36 |    * ```
 37 |    *
 38 |    * Or, with an SDK directly:
 39 |    *
 40 |    * ```bash
 41 |    * $ npm i openai
 42 |    * ```
 43 |    *
 44 |    * ```ts
 45 |    * import OpenAI from "openai";
 46 |    * const openai = new OpenAI({
 47 |    *   apiKey: process.env.OPENAI_API_KEY,
 48 |    * });
 49 |    *
 50 |    * const chatCompletion = await openai.chat.completions.create({
 51 |    *   messages: [{
 52 |    *     role: state.messages[0]._getType(),
 53 |    *     content: state.messages[0].content,
 54 |    *   }],
 55 |    *   model: "gpt-4o-mini",
 56 |    * });
 57 |    * ```
 58 |    */
 59 |   console.log("Current state:", state);
 60 |   return {
 61 |     messages: [
 62 |       {
 63 |         role: "assistant",
 64 |         content: `Hi there! How are you?`,
 65 |       },
 66 |     ],
 67 |   };
 68 | };
 69 | 
 70 | /**
 71 |  * Routing function: Determines whether to continue research or end the builder.
 72 |  * This function decides if the gathered information is satisfactory or if more research is needed.
 73 |  *
 74 |  * @param state - The current state of the research builder
 75 |  * @returns Either "callModel" to continue research or END to finish the builder
 76 |  */
 77 | export const route = (
 78 |   state: typeof StateAnnotation.State,
 79 | ): "__end__" | "callModel" => {
 80 |   if (state.messages.length > 0) {
 81 |     return "__end__";
 82 |   }
 83 |   // Loop back
 84 |   return "callModel";
 85 | };
 86 | 
 87 | // Finally, create the graph itself.
 88 | const builder = new StateGraph(StateAnnotation)
 89 |   // Add the nodes to do the work.
 90 |   // Chaining the nodes together in this way
 91 |   // updates the types of the StateGraph instance
 92 |   // so you have static type checking when it comes time
 93 |   // to add the edges.
 94 |   .addNode("callModel", callModel)
 95 |   // Regular edges mean "always transition to node B after node A is done"
 96 |   // The "__start__" and "__end__" nodes are "virtual" nodes that are always present
 97 |   // and represent the beginning and end of the builder.
 98 |   .addEdge("__start__", "callModel")
 99 |   // Conditional edges optionally route to different nodes (or end)
100 |   .addConditionalEdges("callModel", route);
101 | 
102 | export const graph = builder.compile();
103 | 
104 | graph.name = "New Agent";
105 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/src/agent/state.ts:
--------------------------------------------------------------------------------
 1 | import { BaseMessage, BaseMessageLike } from "@langchain/core/messages";
 2 | import { Annotation, messagesStateReducer } from "@langchain/langgraph";
 3 | 
 4 | /**
 5 |  * A graph's StateAnnotation defines three main things:
 6 |  * 1. The structure of the data to be passed between nodes (which "channels" to read from/write to and their types)
 7 |  * 2. Default values for each field
 8 |  * 3. Reducers for the state's. Reducers are functions that determine how to apply updates to the state.
 9 |  * See [Reducers](https://langchain-ai.github.io/langgraphjs/concepts/low_level/#reducers) for more information.
10 |  */
11 | 
12 | // This is the primary state of your agent, where you can store any information
13 | export const StateAnnotation = Annotation.Root({
14 |   /**
15 |    * Messages track the primary execution state of the agent.
16 |    *
17 |    * Typically accumulates a pattern of:
18 |    *
19 |    * 1. HumanMessage - user input
20 |    * 2. AIMessage with .tool_calls - agent picking tool(s) to use to collect
21 |    *     information
22 |    * 3. ToolMessage(s) - the responses (or errors) from the executed tools
23 |    *
24 |    *     (... repeat steps 2 and 3 as needed ...)
25 |    * 4. AIMessage without .tool_calls - agent responding in unstructured
26 |    *     format to the user.
27 |    *
28 |    * 5. HumanMessage - user responds with the next conversational turn.
29 |    *
30 |    *     (... repeat steps 2-5 as needed ... )
31 |    *
32 |    * Merges two lists of messages or message-like objects with role and content,
33 |    * updating existing messages by ID.
34 |    *
35 |    * Message-like objects are automatically coerced by `messagesStateReducer` into
36 |    * LangChain message classes. If a message does not have a given id,
37 |    * LangGraph will automatically assign one.
38 |    *
39 |    * By default, this ensures the state is "append-only", unless the
40 |    * new message has the same ID as an existing message.
41 |    *
42 |    * Returns:
43 |    *     A new list of messages with the messages from \`right\` merged into \`left\`.
44 |    *     If a message in \`right\` has the same ID as a message in \`left\`, the
45 |    *     message from \`right\` will replace the message from \`left\`.`
46 |    */
47 |   messages: Annotation<BaseMessage[], BaseMessageLike[]>({
48 |     reducer: messagesStateReducer,
49 |     default: () => [],
50 |   }),
51 |   /**
52 |    * Feel free to add additional attributes to your state as needed.
53 |    * Common examples include retrieved documents, extracted entities, API connections, etc.
54 |    *
55 |    * For simple fields whose value should be overwritten by the return value of a node,
56 |    * you don't need to define a reducer or default.
57 |    */
58 |   // additionalField: Annotation<string>,
59 | });
60 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/js-examples/static/studio.png


--------------------------------------------------------------------------------
/libs/cli/js-examples/tests/agent.test.ts:
--------------------------------------------------------------------------------
1 | import { describe, it, expect } from "@jest/globals";
2 | import { route } from "../src/agent/graph.js";
3 | describe("Routers", () => {
4 |   it("Test route", async () => {
5 |     const res = route({ messages: [] });
6 |     expect(res).toEqual("callModel");
7 |   }, 100_000);
8 | });
9 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/tests/graph.int.test.ts:
--------------------------------------------------------------------------------
 1 | import { describe, it, expect } from "@jest/globals";
 2 | import { graph } from "../src/agent/graph.js";
 3 | 
 4 | describe("Graph", () => {
 5 |   it("should process input through the graph", async () => {
 6 |     const input = "What is the capital of France?";
 7 |     const result = await graph.invoke({ input });
 8 | 
 9 |     expect(result).toBeDefined();
10 |     expect(typeof result).toBe("object");
11 |     expect(result.messages).toBeDefined();
12 |     expect(Array.isArray(result.messages)).toBe(true);
13 |     expect(result.messages.length).toBeGreaterThan(0);
14 | 
15 |     const lastMessage = result.messages[result.messages.length - 1];
16 |     expect(lastMessage.content.toString().toLowerCase()).toContain("hi");
17 |   }, 30000); // Increased timeout to 30 seconds
18 | });
19 | 


--------------------------------------------------------------------------------
/libs/cli/js-examples/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@tsconfig/recommended",
 3 |   "compilerOptions": {
 4 |     "target": "ES2021",
 5 |     "lib": ["ES2021", "ES2022.Object", "DOM"],
 6 |     "module": "NodeNext",
 7 |     "moduleResolution": "nodenext",
 8 |     "esModuleInterop": true,
 9 |     "noImplicitReturns": true,
10 |     "declaration": true,
11 |     "noFallthroughCasesInSwitch": true,
12 |     "noUnusedLocals": true,
13 |     "noUnusedParameters": true,
14 |     "useDefineForClassFields": true,
15 |     "strictPropertyInitialization": false,
16 |     "allowJs": true,
17 |     "strict": true,
18 |     "strictFunctionTypes": false,
19 |     "outDir": "dist",
20 |     "types": ["jest", "node"],
21 |     "resolveJsonModule": true
22 |   },
23 |   "include": ["**/*.ts", "**/*.js"],
24 |   "exclude": ["node_modules", "dist"]
25 | }
26 | 


--------------------------------------------------------------------------------
/libs/cli/langgraph_cli/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/langgraph_cli/__init__.py


--------------------------------------------------------------------------------
/libs/cli/langgraph_cli/analytics.py:
--------------------------------------------------------------------------------
 1 | import functools
 2 | import json
 3 | import os
 4 | import pathlib
 5 | import platform
 6 | import threading
 7 | import urllib.error
 8 | import urllib.request
 9 | from typing import Any, TypedDict
10 | 
11 | from langgraph_cli.constants import (
12 |     DEFAULT_CONFIG,
13 |     DEFAULT_PORT,
14 |     SUPABASE_PUBLIC_API_KEY,
15 |     SUPABASE_URL,
16 | )
17 | from langgraph_cli.version import __version__
18 | 
19 | 
20 | class LogData(TypedDict):
21 |     os: str
22 |     os_version: str
23 |     python_version: str
24 |     cli_version: str
25 |     cli_command: str
26 |     params: dict[str, Any]
27 | 
28 | 
29 | def get_anonymized_params(kwargs: dict[str, Any]) -> dict[str, bool]:
30 |     params = {}
31 | 
32 |     # anonymize params with values
33 |     if config := kwargs.get("config"):
34 |         if config != pathlib.Path(DEFAULT_CONFIG).resolve():
35 |             params["config"] = True
36 | 
37 |     if port := kwargs.get("port"):
38 |         if port != DEFAULT_PORT:
39 |             params["port"] = True
40 | 
41 |     if kwargs.get("docker_compose"):
42 |         params["docker_compose"] = True
43 | 
44 |     if kwargs.get("debugger_port"):
45 |         params["debugger_port"] = True
46 | 
47 |     if kwargs.get("postgres_uri"):
48 |         params["postgres_uri"] = True
49 | 
50 |     # pick up exact values for boolean flags
51 |     for boolean_param in ["recreate", "pull", "watch", "wait", "verbose"]:
52 |         if kwargs.get(boolean_param):
53 |             params[boolean_param] = kwargs[boolean_param]
54 | 
55 |     return params
56 | 
57 | 
58 | def log_data(data: LogData) -> None:
59 |     headers = {
60 |         "Content-Type": "application/json",
61 |         "apikey": SUPABASE_PUBLIC_API_KEY,
62 |         "User-Agent": "Mozilla/5.0",
63 |     }
64 |     supabase_url = SUPABASE_URL
65 | 
66 |     req = urllib.request.Request(
67 |         f"{supabase_url}/rest/v1/logs",
68 |         data=json.dumps(data).encode("utf-8"),
69 |         headers=headers,
70 |         method="POST",
71 |     )
72 | 
73 |     try:
74 |         urllib.request.urlopen(req)
75 |     except urllib.error.URLError:
76 |         pass
77 | 
78 | 
79 | def log_command(func):
80 |     @functools.wraps(func)
81 |     def decorator(*args, **kwargs):
82 |         if os.getenv("LANGGRAPH_CLI_NO_ANALYTICS") == "1":
83 |             return func(*args, **kwargs)
84 | 
85 |         data = {
86 |             "os": platform.system(),
87 |             "os_version": platform.version(),
88 |             "python_version": platform.python_version(),
89 |             "cli_version": __version__,
90 |             "cli_command": func.__name__,
91 |             "params": get_anonymized_params(kwargs),
92 |         }
93 | 
94 |         background_thread = threading.Thread(target=log_data, args=(data,))
95 |         background_thread.start()
96 |         return func(*args, **kwargs)
97 | 
98 |     return decorator
99 | 


--------------------------------------------------------------------------------
/libs/cli/langgraph_cli/constants.py:
--------------------------------------------------------------------------------
1 | DEFAULT_CONFIG = "langgraph.json"
2 | DEFAULT_PORT = 8123
3 | 
4 | # analytics
5 | SUPABASE_PUBLIC_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt6cmxwcG9qaW5wY3l5YWlweG5iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTkyNTc1NzksImV4cCI6MjAzNDgzMzU3OX0.kkVOlLz3BxemA5nP-vat3K4qRtrDuO4SwZSR_htcX9c"
6 | SUPABASE_URL = "https://kzrlppojinpcyyaipxnb.supabase.co"
7 | 


--------------------------------------------------------------------------------
/libs/cli/langgraph_cli/progress.py:
--------------------------------------------------------------------------------
 1 | import sys
 2 | import threading
 3 | import time
 4 | from typing import Callable
 5 | 
 6 | 
 7 | class Progress:
 8 |     delay: float = 0.1
 9 | 
10 |     @staticmethod
11 |     def spinning_cursor():
12 |         while True:
13 |             yield from "|/-\\"
14 | 
15 |     def __init__(self, *, message=""):
16 |         self.message = message
17 |         self.spinner_generator = self.spinning_cursor()
18 | 
19 |     def spinner_iteration(self):
20 |         message = self.message
21 |         sys.stdout.write(next(self.spinner_generator) + " " + message)
22 |         sys.stdout.flush()
23 |         time.sleep(self.delay)
24 |         # clear the spinner and message
25 |         sys.stdout.write(
26 |             "\b" * (len(message) + 2)
27 |             + " " * (len(message) + 2)
28 |             + "\b" * (len(message) + 2)
29 |         )
30 |         sys.stdout.flush()
31 | 
32 |     def spinner_task(self):
33 |         while self.message:
34 |             message = self.message
35 |             sys.stdout.write(next(self.spinner_generator) + " " + message)
36 |             sys.stdout.flush()
37 |             time.sleep(self.delay)
38 |             # clear the spinner and message
39 |             sys.stdout.write(
40 |                 "\b" * (len(message) + 2)
41 |                 + " " * (len(message) + 2)
42 |                 + "\b" * (len(message) + 2)
43 |             )
44 |             sys.stdout.flush()
45 | 
46 |     def __enter__(self) -> Callable[[str], None]:
47 |         self.thread = threading.Thread(target=self.spinner_task)
48 |         self.thread.start()
49 | 
50 |         def set_message(message):
51 |             self.message = message
52 |             if not message:
53 |                 self.thread.join()
54 | 
55 |         return set_message
56 | 
57 |     def __exit__(self, exception, value, tb):
58 |         self.message = ""
59 |         try:
60 |             self.thread.join()
61 |         finally:
62 |             del self.thread
63 |         if exception is not None:
64 |             return False
65 | 


--------------------------------------------------------------------------------
/libs/cli/langgraph_cli/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/langgraph_cli/py.typed


--------------------------------------------------------------------------------
/libs/cli/langgraph_cli/util.py:
--------------------------------------------------------------------------------
1 | def clean_empty_lines(input_str: str):
2 |     return "\n".join(filter(None, input_str.splitlines()))
3 | 


--------------------------------------------------------------------------------
/libs/cli/langgraph_cli/version.py:
--------------------------------------------------------------------------------
 1 | """Main entrypoint into package."""
 2 | 
 3 | from importlib import metadata
 4 | 
 5 | try:
 6 |     __version__ = metadata.version(__package__)
 7 | except metadata.PackageNotFoundError:
 8 |     # Case where package metadata is not available.
 9 |     __version__ = ""
10 | del metadata  # optional, avoids polluting the results of dir(__package__)
11 | 


--------------------------------------------------------------------------------
/libs/cli/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph-cli"
 3 | version = "0.1.65"
 4 | description = "CLI for interacting with LangGraph API"
 5 | authors = []
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | repository = "https://www.github.com/langchain-ai/langgraph"
 9 | packages = [{ include = "langgraph_cli" }]
10 | 
11 | [tool.poetry.scripts]
12 | langgraph = "langgraph_cli.cli:cli"
13 | 
14 | [tool.poetry.dependencies]
15 | python = "^3.9.0,<4.0"
16 | click = "^8.1.7"
17 | langgraph-api = { version = ">=0.0.12,<0.1.0", optional = true, python = ">=3.11,<4.0" }
18 | python-dotenv = { version = ">=0.8.0", optional = true }
19 | 
20 | [tool.poetry.group.dev.dependencies]
21 | ruff = "^0.6.2"
22 | codespell = "^2.2.0"
23 | pytest = "^7.2.1"
24 | pytest-asyncio = "^0.21.1"
25 | pytest-mock = "^3.11.1"
26 | pytest-watch = "^4.2.0"
27 | mypy = "^1.10.0"
28 | 
29 | [tool.poetry.extras]
30 | inmem = ["langgraph-api", "python-dotenv"]
31 | 
32 | [tool.pytest.ini_options]
33 | # --strict-markers will raise errors on unknown marks.
34 | # https://docs.pytest.org/en/7.1.x/how-to/mark.html#raising-errors-on-unknown-marks
35 | #
36 | # https://docs.pytest.org/en/7.1.x/reference/reference.html
37 | # --strict-config       any warnings encountered while parsing the `pytest`
38 | #                       section of the configuration file raise errors.
39 | addopts = "--strict-markers --strict-config --durations=5 -vv"
40 | asyncio_mode = "auto"
41 | 
42 | 
43 | [build-system]
44 | requires = ["poetry-core"]
45 | build-backend = "poetry.core.masonry.api"
46 | 
47 | [tool.ruff]
48 | lint.select = [
49 |   # pycodestyle
50 |   "E",
51 |   # Pyflakes
52 |   "F",
53 |   # pyupgrade
54 |   "UP",
55 |   # flake8-bugbear
56 |   "B",
57 |   # isort
58 |   "I",
59 | ]
60 | lint.ignore = ["E501", "B008"]
61 | 


--------------------------------------------------------------------------------
/libs/cli/tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/tests/__init__.py


--------------------------------------------------------------------------------
/libs/cli/tests/integration_tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/tests/integration_tests/__init__.py


--------------------------------------------------------------------------------
/libs/cli/tests/integration_tests/test_cli.py:
--------------------------------------------------------------------------------
 1 | import pytest
 2 | import requests
 3 | 
 4 | from langgraph_cli.templates import TEMPLATE_ID_TO_CONFIG
 5 | 
 6 | 
 7 | @pytest.mark.parametrize("template_key", TEMPLATE_ID_TO_CONFIG.keys())
 8 | def test_template_urls_work(template_key: str) -> None:
 9 |     """Integration test to verify that all template URLs are reachable."""
10 |     _, _, template_url = TEMPLATE_ID_TO_CONFIG[template_key]
11 |     response = requests.head(template_url)
12 |     # Returns 302 on a successful HEAD request
13 |     assert response.status_code == 302, f"URL {template_url} is not reachable."
14 | 


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/tests/unit_tests/__init__.py


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/agent.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import os
 3 | from typing import Annotated, Sequence, TypedDict
 4 | 
 5 | from langchain_core.language_models.fake_chat_models import FakeListChatModel
 6 | from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage
 7 | from langgraph.graph import END, StateGraph, add_messages
 8 | 
 9 | # check that env var is present
10 | os.environ["SOME_ENV_VAR"]
11 | 
12 | 
13 | class AgentState(TypedDict):
14 |     some_bytes: bytes
15 |     some_byte_array: bytearray
16 |     dict_with_bytes: dict[str, bytes]
17 |     messages: Annotated[Sequence[BaseMessage], add_messages]
18 |     sleep: int
19 | 
20 | 
21 | async def call_model(state, config):
22 |     if sleep := state.get("sleep"):
23 |         await asyncio.sleep(sleep)
24 | 
25 |     messages = state["messages"]
26 | 
27 |     if len(messages) > 1:
28 |         assert state["some_bytes"] == b"some_bytes"
29 |         assert state["some_byte_array"] == bytearray(b"some_byte_array")
30 |         assert state["dict_with_bytes"] == {"more_bytes": b"more_bytes"}
31 | 
32 |     # hacky way to reset model to the "first" response
33 |     if isinstance(messages[-1], HumanMessage):
34 |         model.i = 0
35 | 
36 |     response = await model.ainvoke(messages)
37 |     return {
38 |         "messages": [response],
39 |         "some_bytes": b"some_bytes",
40 |         "some_byte_array": bytearray(b"some_byte_array"),
41 |         "dict_with_bytes": {"more_bytes": b"more_bytes"},
42 |     }
43 | 
44 | 
45 | def call_tool(state):
46 |     last_message_content = state["messages"][-1].content
47 |     return {
48 |         "messages": [
49 |             ToolMessage(
50 |                 f"tool_call__{last_message_content}", tool_call_id="tool_call_id"
51 |             )
52 |         ]
53 |     }
54 | 
55 | 
56 | def should_continue(state):
57 |     messages = state["messages"]
58 |     last_message = messages[-1]
59 |     if last_message.content == "end":
60 |         return END
61 |     else:
62 |         return "tool"
63 | 
64 | 
65 | # NOTE: the model cycles through responses infinitely here
66 | model = FakeListChatModel(responses=["begin", "end"])
67 | workflow = StateGraph(AgentState)
68 | 
69 | workflow.add_node("agent", call_model)
70 | workflow.add_node("tool", call_tool)
71 | 
72 | workflow.set_entry_point("agent")
73 | 
74 | workflow.add_conditional_edges(
75 |     "agent",
76 |     should_continue,
77 | )
78 | 
79 | workflow.add_edge("tool", "agent")
80 | 
81 | graph = workflow.compile()
82 | 


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/cli/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/tests/unit_tests/cli/__init__.py


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/cli/test_templates.py:
--------------------------------------------------------------------------------
 1 | """Unit tests for the 'new' CLI command.
 2 | 
 3 | This command creates a new LangGraph project using a specified template.
 4 | """
 5 | 
 6 | import os
 7 | from io import BytesIO
 8 | from pathlib import Path
 9 | from tempfile import TemporaryDirectory
10 | from unittest.mock import MagicMock, patch
11 | from urllib import request
12 | from zipfile import ZipFile
13 | 
14 | from click.testing import CliRunner
15 | 
16 | from langgraph_cli.cli import cli
17 | from langgraph_cli.templates import TEMPLATE_ID_TO_CONFIG
18 | 
19 | 
20 | @patch.object(request, "urlopen")
21 | def test_create_new_with_mocked_download(mock_urlopen: MagicMock) -> None:
22 |     """Test the 'new' CLI command with a mocked download response using urllib."""
23 |     # Mock the response content to simulate a ZIP file
24 |     mock_zip_content = BytesIO()
25 |     with ZipFile(mock_zip_content, "w") as mock_zip:
26 |         mock_zip.writestr("test-file.txt", "Test content.")
27 | 
28 |     # Create a mock response that behaves like a context manager
29 |     mock_response = MagicMock()
30 |     mock_response.read.return_value = mock_zip_content.getvalue()
31 |     mock_response.__enter__.return_value = mock_response  # Setup enter context
32 |     mock_response.status = 200
33 | 
34 |     mock_urlopen.return_value = mock_response
35 | 
36 |     with TemporaryDirectory() as temp_dir:
37 |         runner = CliRunner()
38 |         template = next(
39 |             iter(TEMPLATE_ID_TO_CONFIG)
40 |         )  # Select the first template for the test
41 |         result = runner.invoke(cli, ["new", temp_dir, "--template", template])
42 | 
43 |         # Verify CLI command execution and success
44 |         assert result.exit_code == 0, result.output
45 |         assert (
46 |             "New project created" in result.output
47 |         ), "Expected success message in output."
48 | 
49 |         # Verify that the directory is not empty
50 |         assert os.listdir(temp_dir), "Expected files to be created in temp directory."
51 | 
52 |         # Check for a known file in the extracted content
53 |         extracted_files = [f.name for f in Path(temp_dir).glob("*")]
54 |         assert (
55 |             "test-file.txt" in extracted_files
56 |         ), "Expected 'test-file.txt' in the extracted content."
57 | 
58 | 
59 | def test_invalid_template_id() -> None:
60 |     """Test that an invalid template ID passed via CLI results in a graceful error."""
61 |     runner = CliRunner()
62 |     result = runner.invoke(
63 |         cli, ["new", "dummy_path", "--template", "invalid-template-id"]
64 |     )
65 | 
66 |     # Verify the command failed and proper message is displayed
67 |     assert result.exit_code != 0, "Expected non-zero exit code for invalid template."
68 |     assert (
69 |         "Template 'invalid-template-id' not found" in result.output
70 |     ), "Expected error message in output."
71 | 


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/conftest.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | from unittest.mock import patch
 3 | 
 4 | import pytest
 5 | 
 6 | 
 7 | @pytest.fixture(autouse=True)
 8 | def disable_analytics_env() -> None:
 9 |     """Disable analytics for unit tests LANGGRAPH_CLI_NO_ANALYTICS."""
10 |     # First check if the environment variable is already set, if so, log a warning prior
11 |     # to overriding it.
12 |     if "LANGGRAPH_CLI_NO_ANALYTICS" in os.environ:
13 |         print("⚠️ LANGGRAPH_CLI_NO_ANALYTICS is set. Overriding it for the test.")
14 | 
15 |     with patch.dict(os.environ, {"LANGGRAPH_CLI_NO_ANALYTICS": "0"}):
16 |         yield
17 | 


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/graphs/agent.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/tests/unit_tests/graphs/agent.py


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/helpers.py:
--------------------------------------------------------------------------------
1 | def clean_empty_lines(input_str: str):
2 |     return "\n".join(filter(None, input_str.splitlines()))
3 | 


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/pipconfig.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/cli/tests/unit_tests/pipconfig.txt


--------------------------------------------------------------------------------
/libs/cli/tests/unit_tests/test_config.json:
--------------------------------------------------------------------------------
 1 | {
 2 |     "python_version": "3.12",
 3 |     "pip_config_file": "pipconfig.txt",
 4 |     "dockerfile_lines": [
 5 |         "ARG meow=woof"
 6 |     ],
 7 |     "dependencies": [
 8 |         "langchain_openai",
 9 |         "."
10 |     ],
11 |     "graphs": {
12 |         "agent": "graphs/agent.py:graph"
13 |     },
14 |     "env": ".env"
15 | }
16 | 


--------------------------------------------------------------------------------
/libs/langgraph/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2024 LangChain, Inc.
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/libs/langgraph/Makefile:
--------------------------------------------------------------------------------
  1 | .PHONY: all format lint test test_watch integration_tests spell_check spell_fix benchmark profile
  2 | 
  3 | # Default target executed when no arguments are given to make.
  4 | all: help
  5 | 
  6 | ######################
  7 | # TESTING AND COVERAGE
  8 | ######################
  9 | 
 10 | # Benchmarks
 11 | 
 12 | OUTPUT ?= out/benchmark.json
 13 | 
 14 | benchmark:
 15 | 	mkdir -p out
 16 | 	rm -f $(OUTPUT)
 17 | 	poetry run python -m bench -o $(OUTPUT) --rigorous
 18 | 
 19 | benchmark-fast:
 20 | 	mkdir -p out
 21 | 	rm -f $(OUTPUT)
 22 | 	poetry run python -m bench -o $(OUTPUT) --fast
 23 | 
 24 | GRAPH ?= bench/fanout_to_subgraph.py
 25 | 
 26 | profile:
 27 | 	mkdir -p out
 28 | 	sudo poetry run py-spy record -g -o out/profile.svg -- python $(GRAPH)
 29 | 
 30 | # Run unit tests and generate a coverage report.
 31 | coverage:
 32 | 	poetry run pytest --cov \
 33 | 		--cov-config=.coveragerc \
 34 | 		--cov-report xml \
 35 | 		--cov-report term-missing:skip-covered
 36 | 
 37 | start-postgres:
 38 | 	docker compose -f tests/compose-postgres.yml up -V --force-recreate --wait --remove-orphans
 39 | 
 40 | stop-postgres:
 41 | 	docker compose -f tests/compose-postgres.yml down -v
 42 | 
 43 | TEST ?= .
 44 | 
 45 | test:
 46 | 	make start-postgres && poetry run pytest $(TEST); \
 47 | 	EXIT_CODE=$$?; \
 48 | 	make stop-postgres; \
 49 | 	exit $$EXIT_CODE
 50 | 
 51 | test_parallel:
 52 | 	make start-postgres && poetry run pytest -n auto --dist worksteal $(TEST); \
 53 | 	EXIT_CODE=$$?; \
 54 | 	make stop-postgres; \
 55 | 	exit $$EXIT_CODE
 56 | 
 57 | WORKERS ?= auto
 58 | XDIST_ARGS := $(if $(WORKERS),-n $(WORKERS) --dist worksteal,)
 59 | MAXFAIL ?=
 60 | MAXFAIL_ARGS := $(if $(MAXFAIL),--maxfail $(MAXFAIL),)
 61 | 
 62 | test_watch:
 63 | 	make start-postgres && poetry run ptw . -- --ff -vv -x $(XDIST_ARGS) $(MAXFAIL_ARGS) --snapshot-update --tb short $(TEST); \
 64 | 	EXIT_CODE=$$?; \
 65 | 	make stop-postgres; \
 66 | 	exit $$EXIT_CODE
 67 | 
 68 | test_watch_all:
 69 | 	npx concurrently -n langgraph,checkpoint,checkpoint-sqlite,postgres "make test_watch" "make -C ../checkpoint test_watch" "make -C ../checkpoint-sqlite test_watch" "make -C ../checkpoint-postgres test_watch"
 70 | 
 71 | ######################
 72 | # LINTING AND FORMATTING
 73 | ######################
 74 | 
 75 | # Define a variable for Python and notebook files.
 76 | PYTHON_FILES=.
 77 | MYPY_CACHE=.mypy_cache
 78 | lint format: PYTHON_FILES=.
 79 | lint_diff format_diff: PYTHON_FILES=$(shell git diff --name-only --relative --diff-filter=d main . | grep -E '\.py$$|\.ipynb$$')
 80 | lint_package: PYTHON_FILES=langgraph
 81 | lint_tests: PYTHON_FILES=tests
 82 | lint_tests: MYPY_CACHE=.mypy_cache_test
 83 | 
 84 | lint lint_diff lint_package lint_tests:
 85 | 	poetry run ruff check .
 86 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff format $(PYTHON_FILES) --diff
 87 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff check --select I $(PYTHON_FILES)
 88 | 	[ "$(PYTHON_FILES)" = "" ] || mkdir -p $(MYPY_CACHE)
 89 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run mypy langgraph --cache-dir $(MYPY_CACHE)
 90 | 
 91 | format format_diff:
 92 | 	poetry run ruff format $(PYTHON_FILES)
 93 | 	poetry run ruff check --select I --fix $(PYTHON_FILES)
 94 | 
 95 | spell_check:
 96 | 	poetry run codespell --toml pyproject.toml
 97 | 
 98 | spell_fix:
 99 | 	poetry run codespell --toml pyproject.toml -w
100 | 
101 | 
102 | ######################
103 | # HELP
104 | ######################
105 | 
106 | help:
107 | 	@echo '===================='
108 | 	@echo '-- DOCUMENTATION --'
109 | 	
110 | 	@echo '-- LINTING --'
111 | 	@echo 'format                       - run code formatters'
112 | 	@echo 'lint                         - run linters'
113 | 	@echo 'spell_check               	- run codespell on the project'
114 | 	@echo 'spell_fix               		- run codespell on the project and fix the errors'
115 | 	@echo '-- TESTS --'
116 | 	@echo 'coverage                     - run unit tests and generate coverage report'
117 | 	@echo 'test                         - run unit tests'
118 | 	@echo 'test TEST_FILE=<test_file>   - run all tests in file'
119 | 	@echo 'test_watch                   - run unit tests in watch mode'
120 | 


--------------------------------------------------------------------------------
/libs/langgraph/bench/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/langgraph/bench/__init__.py


--------------------------------------------------------------------------------
/libs/langgraph/bench/fanout_to_subgraph.py:
--------------------------------------------------------------------------------
  1 | import operator
  2 | from typing import Annotated, TypedDict
  3 | 
  4 | from langgraph.constants import END, START, Send
  5 | from langgraph.graph.state import StateGraph
  6 | 
  7 | 
  8 | def fanout_to_subgraph() -> StateGraph:
  9 |     class OverallState(TypedDict):
 10 |         subjects: list[str]
 11 |         jokes: Annotated[list[str], operator.add]
 12 | 
 13 |     async def continue_to_jokes(state: OverallState):
 14 |         return [Send("generate_joke", {"subject": s}) for s in state["subjects"]]
 15 | 
 16 |     class JokeInput(TypedDict):
 17 |         subject: str
 18 | 
 19 |     class JokeOutput(TypedDict):
 20 |         jokes: list[str]
 21 | 
 22 |     async def bump(state: JokeOutput):
 23 |         return {"jokes": [state["jokes"][0] + " a"]}
 24 | 
 25 |     async def generate(state: JokeInput):
 26 |         return {"jokes": [f"Joke about {state['subject']}"]}
 27 | 
 28 |     async def edit(state: JokeInput):
 29 |         subject = state["subject"]
 30 |         return {"subject": f"{subject} - hohoho"}
 31 | 
 32 |     async def bump_loop(state: JokeOutput):
 33 |         return END if state["jokes"][0].endswith(" a" * 10) else "bump"
 34 | 
 35 |     # subgraph
 36 |     subgraph = StateGraph(input=JokeInput, output=JokeOutput)
 37 |     subgraph.add_node("edit", edit)
 38 |     subgraph.add_node("generate", generate)
 39 |     subgraph.add_node("bump", bump)
 40 |     subgraph.set_entry_point("edit")
 41 |     subgraph.add_edge("edit", "generate")
 42 |     subgraph.add_edge("generate", "bump")
 43 |     subgraph.add_conditional_edges("bump", bump_loop)
 44 |     subgraph.set_finish_point("generate")
 45 |     subgraphc = subgraph.compile()
 46 | 
 47 |     # parent graph
 48 |     builder = StateGraph(OverallState)
 49 |     builder.add_node("generate_joke", subgraphc)
 50 |     builder.add_conditional_edges(START, continue_to_jokes)
 51 |     builder.add_edge("generate_joke", END)
 52 | 
 53 |     return builder
 54 | 
 55 | 
 56 | def fanout_to_subgraph_sync() -> StateGraph:
 57 |     class OverallState(TypedDict):
 58 |         subjects: list[str]
 59 |         jokes: Annotated[list[str], operator.add]
 60 | 
 61 |     def continue_to_jokes(state: OverallState):
 62 |         return [Send("generate_joke", {"subject": s}) for s in state["subjects"]]
 63 | 
 64 |     class JokeInput(TypedDict):
 65 |         subject: str
 66 | 
 67 |     class JokeOutput(TypedDict):
 68 |         jokes: list[str]
 69 | 
 70 |     def bump(state: JokeOutput):
 71 |         return {"jokes": [state["jokes"][0] + " a"]}
 72 | 
 73 |     def generate(state: JokeInput):
 74 |         return {"jokes": [f"Joke about {state['subject']}"]}
 75 | 
 76 |     def edit(state: JokeInput):
 77 |         subject = state["subject"]
 78 |         return {"subject": f"{subject} - hohoho"}
 79 | 
 80 |     def bump_loop(state: JokeOutput):
 81 |         return END if state["jokes"][0].endswith(" a" * 10) else "bump"
 82 | 
 83 |     # subgraph
 84 |     subgraph = StateGraph(input=JokeInput, output=JokeOutput)
 85 |     subgraph.add_node("edit", edit)
 86 |     subgraph.add_node("generate", generate)
 87 |     subgraph.add_node("bump", bump)
 88 |     subgraph.set_entry_point("edit")
 89 |     subgraph.add_edge("edit", "generate")
 90 |     subgraph.add_edge("generate", "bump")
 91 |     subgraph.add_conditional_edges("bump", bump_loop)
 92 |     subgraph.set_finish_point("generate")
 93 |     subgraphc = subgraph.compile()
 94 | 
 95 |     # parent graph
 96 |     builder = StateGraph(OverallState)
 97 |     builder.add_node("generate_joke", subgraphc)
 98 |     builder.add_conditional_edges(START, continue_to_jokes)
 99 |     builder.add_edge("generate_joke", END)
100 | 
101 |     return builder
102 | 
103 | 
104 | if __name__ == "__main__":
105 |     import asyncio
106 |     import random
107 | 
108 |     import uvloop
109 | 
110 |     from langgraph.checkpoint.memory import MemorySaver
111 | 
112 |     graph = fanout_to_subgraph().compile(checkpointer=MemorySaver())
113 |     input = {
114 |         "subjects": [
115 |             random.choices("abcdefghijklmnopqrstuvwxyz", k=1000) for _ in range(1000)
116 |         ]
117 |     }
118 |     config = {"configurable": {"thread_id": "1"}}
119 | 
120 |     async def run():
121 |         len([c async for c in graph.astream(input, config=config)])
122 | 
123 |     uvloop.install()
124 |     asyncio.run(run())
125 | 


--------------------------------------------------------------------------------
/libs/langgraph/bench/react_agent.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Optional
 2 | from uuid import uuid4
 3 | 
 4 | from langchain_core.callbacks import CallbackManagerForLLMRun
 5 | from langchain_core.language_models.fake_chat_models import (
 6 |     FakeMessagesListChatModel,
 7 | )
 8 | from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
 9 | from langchain_core.outputs import ChatGeneration, ChatResult
10 | from langchain_core.tools import StructuredTool
11 | 
12 | from langgraph.checkpoint.base import BaseCheckpointSaver
13 | from langgraph.prebuilt.chat_agent_executor import create_react_agent
14 | from langgraph.pregel import Pregel
15 | 
16 | 
17 | def react_agent(n_tools: int, checkpointer: Optional[BaseCheckpointSaver]) -> Pregel:
18 |     class FakeFuntionChatModel(FakeMessagesListChatModel):
19 |         def bind_tools(self, functions: list):
20 |             return self
21 | 
22 |         def _generate(
23 |             self,
24 |             messages: list[BaseMessage],
25 |             stop: Optional[list[str]] = None,
26 |             run_manager: Optional[CallbackManagerForLLMRun] = None,
27 |             **kwargs: Any,
28 |         ) -> ChatResult:
29 |             response = self.responses[self.i].copy()
30 |             if self.i < len(self.responses) - 1:
31 |                 self.i += 1
32 |             else:
33 |                 self.i = 0
34 |             generation = ChatGeneration(message=response)
35 |             return ChatResult(generations=[generation])
36 | 
37 |     tool = StructuredTool.from_function(
38 |         lambda query: f"result for query: {query}" * 10,
39 |         name=str(uuid4()),
40 |         description="",
41 |     )
42 | 
43 |     model = FakeFuntionChatModel(
44 |         responses=[
45 |             AIMessage(
46 |                 content="",
47 |                 tool_calls=[
48 |                     {
49 |                         "id": str(uuid4()),
50 |                         "name": tool.name,
51 |                         "args": {"query": str(uuid4()) * 100},
52 |                     }
53 |                 ],
54 |                 id=str(uuid4()),
55 |             )
56 |             for _ in range(n_tools)
57 |         ]
58 |         + [
59 |             AIMessage(content="answer" * 100, id=str(uuid4())),
60 |         ]
61 |     )
62 | 
63 |     return create_react_agent(model, [tool], checkpointer=checkpointer)
64 | 
65 | 
66 | if __name__ == "__main__":
67 |     import asyncio
68 | 
69 |     import uvloop
70 | 
71 |     from langgraph.checkpoint.memory import MemorySaver
72 | 
73 |     graph = react_agent(100, checkpointer=MemorySaver())
74 |     input = {"messages": [HumanMessage("hi?")]}
75 |     config = {"configurable": {"thread_id": "1"}, "recursion_limit": 20000000000}
76 | 
77 |     async def run():
78 |         len([c async for c in graph.astream(input, config=config)])
79 | 
80 |     uvloop.install()
81 |     asyncio.run(run())
82 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/_api/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/langgraph/langgraph/_api/__init__.py


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/_api/deprecation.py:
--------------------------------------------------------------------------------
 1 | import functools
 2 | import warnings
 3 | from typing import Any, Callable, Type, TypeVar, Union, cast
 4 | 
 5 | 
 6 | class LangGraphDeprecationWarning(DeprecationWarning):
 7 |     pass
 8 | 
 9 | 
10 | F = TypeVar("F", bound=Callable[..., Any])
11 | C = TypeVar("C", bound=Type[Any])
12 | 
13 | 
14 | def deprecated(
15 |     since: str, alternative: str, *, removal: str = "", example: str = ""
16 | ) -> Callable[[F], F]:
17 |     def decorator(obj: Union[F, C]) -> Union[F, C]:
18 |         removal_str = removal if removal else "a future version"
19 |         message = (
20 |             f"{obj.__name__} is deprecated as of version {since} and will be"
21 |             f" removed in {removal_str}. Use {alternative} instead.{example}"
22 |         )
23 |         if isinstance(obj, type):
24 |             original_init = obj.__init__  # type: ignore[misc]
25 | 
26 |             @functools.wraps(original_init)
27 |             def new_init(self, *args: Any, **kwargs: Any) -> None:  # type: ignore[no-untyped-def]
28 |                 warnings.warn(message, LangGraphDeprecationWarning, stacklevel=2)
29 |                 original_init(self, *args, **kwargs)
30 | 
31 |             obj.__init__ = new_init  # type: ignore[misc]
32 | 
33 |             docstring = (
34 |                 f"**Deprecated**: This class is deprecated as of version {since}. "
35 |                 f"Use `{alternative}` instead."
36 |             )
37 |             if obj.__doc__:
38 |                 docstring = docstring + f"\n\n{obj.__doc__}"
39 |             obj.__doc__ = docstring
40 | 
41 |             return cast(C, obj)
42 |         elif callable(obj):
43 | 
44 |             @functools.wraps(obj)
45 |             def wrapper(*args: Any, **kwargs: Any) -> Any:
46 |                 warnings.warn(message, LangGraphDeprecationWarning, stacklevel=2)
47 |                 return obj(*args, **kwargs)
48 | 
49 |             docstring = (
50 |                 f"**Deprecated**: This function is deprecated as of version {since}. "
51 |                 f"Use `{alternative}` instead."
52 |             )
53 |             if obj.__doc__:
54 |                 docstring = docstring + f"\n\n{obj.__doc__}"
55 |             wrapper.__doc__ = docstring
56 | 
57 |             return cast(F, wrapper)
58 |         else:
59 |             raise TypeError(
60 |                 f"Can only add deprecation decorator to classes or callables, got '{type(obj)}' instead."
61 |             )
62 | 
63 |     return decorator
64 | 
65 | 
66 | def deprecated_parameter(
67 |     arg_name: str, since: str, alternative: str, *, removal: str
68 | ) -> Callable[[F], F]:
69 |     def decorator(func: F) -> F:
70 |         @functools.wraps(func)
71 |         def wrapper(*args, **kwargs):  # type: ignore[no-untyped-def]
72 |             if arg_name in kwargs:
73 |                 warnings.warn(
74 |                     f"Parameter '{arg_name}' in function '{func.__name__}' is "
75 |                     f"deprecated as of version {since} and will be removed in version {removal}. "
76 |                     f"Use '{alternative}' parameter instead.",
77 |                     category=LangGraphDeprecationWarning,
78 |                     stacklevel=2,
79 |                 )
80 |             return func(*args, **kwargs)
81 | 
82 |         return cast(F, wrapper)
83 | 
84 |     return decorator
85 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/__init__.py:
--------------------------------------------------------------------------------
 1 | from langgraph.channels.any_value import AnyValue
 2 | from langgraph.channels.binop import BinaryOperatorAggregate
 3 | from langgraph.channels.context import Context
 4 | from langgraph.channels.ephemeral_value import EphemeralValue
 5 | from langgraph.channels.last_value import LastValue
 6 | from langgraph.channels.topic import Topic
 7 | from langgraph.channels.untracked_value import UntrackedValue
 8 | 
 9 | __all__ = [
10 |     "LastValue",
11 |     "Topic",
12 |     "Context",
13 |     "BinaryOperatorAggregate",
14 |     "UntrackedValue",
15 |     "EphemeralValue",
16 |     "AnyValue",
17 | ]
18 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/any_value.py:
--------------------------------------------------------------------------------
 1 | from typing import Generic, Optional, Sequence, Type
 2 | 
 3 | from typing_extensions import Self
 4 | 
 5 | from langgraph.channels.base import BaseChannel, Value
 6 | from langgraph.errors import EmptyChannelError
 7 | 
 8 | 
 9 | class AnyValue(Generic[Value], BaseChannel[Value, Value, Value]):
10 |     """Stores the last value received, assumes that if multiple values are
11 |     received, they are all equal."""
12 | 
13 |     __slots__ = ("typ", "value")
14 | 
15 |     def __eq__(self, value: object) -> bool:
16 |         return isinstance(value, AnyValue)
17 | 
18 |     @property
19 |     def ValueType(self) -> Type[Value]:
20 |         """The type of the value stored in the channel."""
21 |         return self.typ
22 | 
23 |     @property
24 |     def UpdateType(self) -> Type[Value]:
25 |         """The type of the update received by the channel."""
26 |         return self.typ
27 | 
28 |     def from_checkpoint(self, checkpoint: Optional[Value]) -> Self:
29 |         empty = self.__class__(self.typ)
30 |         empty.key = self.key
31 |         if checkpoint is not None:
32 |             empty.value = checkpoint
33 |         return empty
34 | 
35 |     def update(self, values: Sequence[Value]) -> bool:
36 |         if len(values) == 0:
37 |             try:
38 |                 del self.value
39 |                 return True
40 |             except AttributeError:
41 |                 return False
42 | 
43 |         self.value = values[-1]
44 |         return True
45 | 
46 |     def get(self) -> Value:
47 |         try:
48 |             return self.value
49 |         except AttributeError:
50 |             raise EmptyChannelError()
51 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/base.py:
--------------------------------------------------------------------------------
 1 | from abc import ABC, abstractmethod
 2 | from typing import Any, Generic, Optional, Sequence, TypeVar
 3 | 
 4 | from typing_extensions import Self
 5 | 
 6 | from langgraph.errors import EmptyChannelError, InvalidUpdateError
 7 | 
 8 | Value = TypeVar("Value")
 9 | Update = TypeVar("Update")
10 | C = TypeVar("C")
11 | 
12 | 
13 | class BaseChannel(Generic[Value, Update, C], ABC):
14 |     __slots__ = ("key", "typ")
15 | 
16 |     def __init__(self, typ: Any, key: str = "") -> None:
17 |         self.typ = typ
18 |         self.key = key
19 | 
20 |     @property
21 |     @abstractmethod
22 |     def ValueType(self) -> Any:
23 |         """The type of the value stored in the channel."""
24 | 
25 |     @property
26 |     @abstractmethod
27 |     def UpdateType(self) -> Any:
28 |         """The type of the update received by the channel."""
29 | 
30 |     # serialize/deserialize methods
31 | 
32 |     def checkpoint(self) -> Optional[C]:
33 |         """Return a serializable representation of the channel's current state.
34 |         Raises EmptyChannelError if the channel is empty (never updated yet),
35 |         or doesn't support checkpoints."""
36 |         return self.get()
37 | 
38 |     @abstractmethod
39 |     def from_checkpoint(self, checkpoint: Optional[C]) -> Self:
40 |         """Return a new identical channel, optionally initialized from a checkpoint.
41 |         If the checkpoint contains complex data structures, they should be copied."""
42 | 
43 |     # state methods
44 | 
45 |     @abstractmethod
46 |     def update(self, values: Sequence[Update]) -> bool:
47 |         """Update the channel's value with the given sequence of updates.
48 |         The order of the updates in the sequence is arbitrary.
49 |         This method is called by Pregel for all channels at the end of each step.
50 |         If there are no updates, it is called with an empty sequence.
51 |         Raises InvalidUpdateError if the sequence of updates is invalid.
52 |         Returns True if the channel was updated, False otherwise."""
53 | 
54 |     @abstractmethod
55 |     def get(self) -> Value:
56 |         """Return the current value of the channel.
57 | 
58 |         Raises EmptyChannelError if the channel is empty (never updated yet)."""
59 | 
60 |     def consume(self) -> bool:
61 |         """Mark the current value of the channel as consumed. By default, no-op.
62 |         This is called by Pregel before the start of the next step, for all
63 |         channels that triggered a node. If the channel was updated, return True.
64 |         """
65 |         return False
66 | 
67 | 
68 | __all__ = [
69 |     "BaseChannel",
70 |     "EmptyChannelError",
71 |     "InvalidUpdateError",
72 | ]
73 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/binop.py:
--------------------------------------------------------------------------------
 1 | import collections.abc
 2 | from typing import (
 3 |     Callable,
 4 |     Generic,
 5 |     Optional,
 6 |     Sequence,
 7 |     Type,
 8 | )
 9 | 
10 | from typing_extensions import NotRequired, Required, Self
11 | 
12 | from langgraph.channels.base import BaseChannel, Value
13 | from langgraph.errors import EmptyChannelError
14 | 
15 | 
16 | # Adapted from typing_extensions
17 | def _strip_extras(t):  # type: ignore[no-untyped-def]
18 |     """Strips Annotated, Required and NotRequired from a given type."""
19 |     if hasattr(t, "__origin__"):
20 |         return _strip_extras(t.__origin__)
21 |     if hasattr(t, "__origin__") and t.__origin__ in (Required, NotRequired):
22 |         return _strip_extras(t.__args__[0])
23 | 
24 |     return t
25 | 
26 | 
27 | class BinaryOperatorAggregate(Generic[Value], BaseChannel[Value, Value, Value]):
28 |     """Stores the result of applying a binary operator to the current value and each new value.
29 | 
30 |     ```python
31 |     import operator
32 | 
33 |     total = Channels.BinaryOperatorAggregate(int, operator.add)
34 |     ```
35 |     """
36 | 
37 |     __slots__ = ("value", "operator")
38 | 
39 |     def __init__(self, typ: Type[Value], operator: Callable[[Value, Value], Value]):
40 |         super().__init__(typ)
41 |         self.operator = operator
42 |         # special forms from typing or collections.abc are not instantiable
43 |         # so we need to replace them with their concrete counterparts
44 |         typ = _strip_extras(typ)
45 |         if typ in (collections.abc.Sequence, collections.abc.MutableSequence):
46 |             typ = list
47 |         if typ in (collections.abc.Set, collections.abc.MutableSet):
48 |             typ = set
49 |         if typ in (collections.abc.Mapping, collections.abc.MutableMapping):
50 |             typ = dict
51 |         try:
52 |             self.value = typ()
53 |         except Exception:
54 |             pass
55 | 
56 |     def __eq__(self, value: object) -> bool:
57 |         return isinstance(value, BinaryOperatorAggregate) and (
58 |             value.operator is self.operator
59 |             if value.operator.__name__ != "<lambda>"
60 |             and self.operator.__name__ != "<lambda>"
61 |             else True
62 |         )
63 | 
64 |     @property
65 |     def ValueType(self) -> Type[Value]:
66 |         """The type of the value stored in the channel."""
67 |         return self.typ
68 | 
69 |     @property
70 |     def UpdateType(self) -> Type[Value]:
71 |         """The type of the update received by the channel."""
72 |         return self.typ
73 | 
74 |     def from_checkpoint(self, checkpoint: Optional[Value]) -> Self:
75 |         empty = self.__class__(self.typ, self.operator)
76 |         empty.key = self.key
77 |         if checkpoint is not None:
78 |             empty.value = checkpoint
79 |         return empty
80 | 
81 |     def update(self, values: Sequence[Value]) -> bool:
82 |         if not values:
83 |             return False
84 |         if not hasattr(self, "value"):
85 |             self.value = values[0]
86 |             values = values[1:]
87 |         for value in values:
88 |             self.value = self.operator(self.value, value)
89 |         return True
90 | 
91 |     def get(self) -> Value:
92 |         try:
93 |             return self.value
94 |         except AttributeError:
95 |             raise EmptyChannelError()
96 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/context.py:
--------------------------------------------------------------------------------
1 | from langgraph.managed.context import Context as ContextManagedValue
2 | 
3 | Context = ContextManagedValue.of
4 | 
5 | __all__ = ["Context"]
6 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/dynamic_barrier_value.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Generic, NamedTuple, Optional, Sequence, Type, Union
 2 | 
 3 | from typing_extensions import Self
 4 | 
 5 | from langgraph.channels.base import BaseChannel, Value
 6 | from langgraph.errors import EmptyChannelError, InvalidUpdateError
 7 | 
 8 | 
 9 | class WaitForNames(NamedTuple):
10 |     names: set[Any]
11 | 
12 | 
13 | class DynamicBarrierValue(
14 |     Generic[Value], BaseChannel[Value, Union[Value, WaitForNames], set[Value]]
15 | ):
16 |     """A channel that switches between two states
17 | 
18 |     - in the "priming" state it can't be read from.
19 |         - if it receives a WaitForNames update, it switches to the "waiting" state.
20 |     - in the "waiting" state it collects named values until all are received.
21 |         - once all named values are received, it can be read once, and it switches
22 |           back to the "priming" state.
23 |     """
24 | 
25 |     __slots__ = ("names", "seen")
26 | 
27 |     names: Optional[set[Value]]
28 |     seen: set[Value]
29 | 
30 |     def __init__(self, typ: Type[Value]) -> None:
31 |         super().__init__(typ)
32 |         self.names = None
33 |         self.seen = set()
34 | 
35 |     def __eq__(self, value: object) -> bool:
36 |         return isinstance(value, DynamicBarrierValue) and value.names == self.names
37 | 
38 |     @property
39 |     def ValueType(self) -> Type[Value]:
40 |         """The type of the value stored in the channel."""
41 |         return self.typ
42 | 
43 |     @property
44 |     def UpdateType(self) -> Type[Value]:
45 |         """The type of the update received by the channel."""
46 |         return self.typ
47 | 
48 |     def checkpoint(self) -> tuple[Optional[set[Value]], set[Value]]:
49 |         return (self.names, self.seen)
50 | 
51 |     def from_checkpoint(
52 |         self,
53 |         checkpoint: Optional[tuple[Optional[set[Value]], set[Value]]],
54 |     ) -> Self:
55 |         empty = self.__class__(self.typ)
56 |         empty.key = self.key
57 |         if checkpoint is not None:
58 |             names, seen = checkpoint
59 |             empty.names = names if names is not None else None
60 |             empty.seen = seen
61 |         return empty
62 | 
63 |     def update(self, values: Sequence[Union[Value, WaitForNames]]) -> bool:
64 |         if wait_for_names := [v for v in values if isinstance(v, WaitForNames)]:
65 |             if len(wait_for_names) > 1:
66 |                 raise InvalidUpdateError(
67 |                     f"At key '{self.key}': Received multiple WaitForNames updates in the same step."
68 |                 )
69 |             self.names = wait_for_names[0].names
70 |             return True
71 |         elif self.names is not None:
72 |             updated = False
73 |             for value in values:
74 |                 assert not isinstance(value, WaitForNames)
75 |                 if value in self.names:
76 |                     if value not in self.seen:
77 |                         self.seen.add(value)
78 |                         updated = True
79 |                 else:
80 |                     raise InvalidUpdateError(f"Value {value} not in {self.names}")
81 |             return updated
82 | 
83 |     def get(self) -> Value:
84 |         if self.seen != self.names:
85 |             raise EmptyChannelError()
86 |         return None
87 | 
88 |     def consume(self) -> bool:
89 |         if self.seen == self.names:
90 |             self.seen = set()
91 |             self.names = None
92 |             return True
93 |         return False
94 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/ephemeral_value.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Generic, Optional, Sequence, Type
 2 | 
 3 | from typing_extensions import Self
 4 | 
 5 | from langgraph.channels.base import BaseChannel, Value
 6 | from langgraph.errors import EmptyChannelError, InvalidUpdateError
 7 | 
 8 | 
 9 | class EphemeralValue(Generic[Value], BaseChannel[Value, Value, Value]):
10 |     """Stores the value received in the step immediately preceding, clears after."""
11 | 
12 |     __slots__ = ("value", "guard")
13 | 
14 |     def __init__(self, typ: Any, guard: bool = True) -> None:
15 |         super().__init__(typ)
16 |         self.guard = guard
17 | 
18 |     def __eq__(self, value: object) -> bool:
19 |         return isinstance(value, EphemeralValue) and value.guard == self.guard
20 | 
21 |     @property
22 |     def ValueType(self) -> Type[Value]:
23 |         """The type of the value stored in the channel."""
24 |         return self.typ
25 | 
26 |     @property
27 |     def UpdateType(self) -> Type[Value]:
28 |         """The type of the update received by the channel."""
29 |         return self.typ
30 | 
31 |     def from_checkpoint(self, checkpoint: Optional[Value]) -> Self:
32 |         empty = self.__class__(self.typ, self.guard)
33 |         empty.key = self.key
34 |         if checkpoint is not None:
35 |             empty.value = checkpoint
36 |         return empty
37 | 
38 |     def update(self, values: Sequence[Value]) -> bool:
39 |         if len(values) == 0:
40 |             try:
41 |                 del self.value
42 |                 return True
43 |             except AttributeError:
44 |                 return False
45 |         if len(values) != 1 and self.guard:
46 |             raise InvalidUpdateError(
47 |                 f"At key '{self.key}': EphemeralValue(guard=True) can receive only one value per step. Use guard=False if you want to store any one of multiple values."
48 |             )
49 | 
50 |         self.value = values[-1]
51 |         return True
52 | 
53 |     def get(self) -> Value:
54 |         try:
55 |             return self.value
56 |         except AttributeError:
57 |             raise EmptyChannelError()
58 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/last_value.py:
--------------------------------------------------------------------------------
 1 | from typing import Generic, Optional, Sequence, Type
 2 | 
 3 | from typing_extensions import Self
 4 | 
 5 | from langgraph.channels.base import BaseChannel, Value
 6 | from langgraph.errors import (
 7 |     EmptyChannelError,
 8 |     ErrorCode,
 9 |     InvalidUpdateError,
10 |     create_error_message,
11 | )
12 | 
13 | 
14 | class LastValue(Generic[Value], BaseChannel[Value, Value, Value]):
15 |     """Stores the last value received, can receive at most one value per step."""
16 | 
17 |     __slots__ = ("value",)
18 | 
19 |     def __eq__(self, value: object) -> bool:
20 |         return isinstance(value, LastValue)
21 | 
22 |     @property
23 |     def ValueType(self) -> Type[Value]:
24 |         """The type of the value stored in the channel."""
25 |         return self.typ
26 | 
27 |     @property
28 |     def UpdateType(self) -> Type[Value]:
29 |         """The type of the update received by the channel."""
30 |         return self.typ
31 | 
32 |     def from_checkpoint(self, checkpoint: Optional[Value]) -> Self:
33 |         empty = self.__class__(self.typ)
34 |         empty.key = self.key
35 |         if checkpoint is not None:
36 |             empty.value = checkpoint
37 |         return empty
38 | 
39 |     def update(self, values: Sequence[Value]) -> bool:
40 |         if len(values) == 0:
41 |             return False
42 |         if len(values) != 1:
43 |             msg = create_error_message(
44 |                 message=f"At key '{self.key}': Can receive only one value per step. Use an Annotated key to handle multiple values.",
45 |                 error_code=ErrorCode.INVALID_CONCURRENT_GRAPH_UPDATE,
46 |             )
47 |             raise InvalidUpdateError(msg)
48 | 
49 |         self.value = values[-1]
50 |         return True
51 | 
52 |     def get(self) -> Value:
53 |         try:
54 |             return self.value
55 |         except AttributeError:
56 |             raise EmptyChannelError()
57 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/named_barrier_value.py:
--------------------------------------------------------------------------------
 1 | from typing import Generic, Optional, Sequence, Type
 2 | 
 3 | from typing_extensions import Self
 4 | 
 5 | from langgraph.channels.base import BaseChannel, Value
 6 | from langgraph.errors import EmptyChannelError, InvalidUpdateError
 7 | 
 8 | 
 9 | class NamedBarrierValue(Generic[Value], BaseChannel[Value, Value, set[Value]]):
10 |     """A channel that waits until all named values are received before making the value available."""
11 | 
12 |     __slots__ = ("names", "seen")
13 | 
14 |     names: set[Value]
15 |     seen: set[Value]
16 | 
17 |     def __init__(self, typ: Type[Value], names: set[Value]) -> None:
18 |         super().__init__(typ)
19 |         self.names = names
20 |         self.seen: set[str] = set()
21 | 
22 |     def __eq__(self, value: object) -> bool:
23 |         return isinstance(value, NamedBarrierValue) and value.names == self.names
24 | 
25 |     @property
26 |     def ValueType(self) -> Type[Value]:
27 |         """The type of the value stored in the channel."""
28 |         return self.typ
29 | 
30 |     @property
31 |     def UpdateType(self) -> Type[Value]:
32 |         """The type of the update received by the channel."""
33 |         return self.typ
34 | 
35 |     def checkpoint(self) -> set[Value]:
36 |         return self.seen
37 | 
38 |     def from_checkpoint(self, checkpoint: Optional[set[Value]]) -> Self:
39 |         empty = self.__class__(self.typ, self.names)
40 |         empty.key = self.key
41 |         if checkpoint is not None:
42 |             empty.seen = checkpoint
43 |         return empty
44 | 
45 |     def update(self, values: Sequence[Value]) -> bool:
46 |         updated = False
47 |         for value in values:
48 |             if value in self.names:
49 |                 if value not in self.seen:
50 |                     self.seen.add(value)
51 |                     updated = True
52 |             else:
53 |                 raise InvalidUpdateError(
54 |                     f"At key '{self.key}': Value {value} not in {self.names}"
55 |                 )
56 |         return updated
57 | 
58 |     def get(self) -> Value:
59 |         if self.seen != self.names:
60 |             raise EmptyChannelError()
61 |         return None
62 | 
63 |     def consume(self) -> bool:
64 |         if self.seen == self.names:
65 |             self.seen = set()
66 |             return True
67 |         return False
68 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/topic.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Generic, Iterator, Optional, Sequence, Type, Union
 2 | 
 3 | from typing_extensions import Self
 4 | 
 5 | from langgraph.channels.base import BaseChannel, Value
 6 | from langgraph.errors import EmptyChannelError
 7 | 
 8 | 
 9 | def flatten(values: Sequence[Union[Value, list[Value]]]) -> Iterator[Value]:
10 |     for value in values:
11 |         if isinstance(value, list):
12 |             yield from value
13 |         else:
14 |             yield value
15 | 
16 | 
17 | class Topic(
18 |     Generic[Value],
19 |     BaseChannel[
20 |         Sequence[Value], Union[Value, list[Value]], tuple[set[Value], list[Value]]
21 |     ],
22 | ):
23 |     """A configurable PubSub Topic.
24 | 
25 |     Args:
26 |         typ: The type of the value stored in the channel.
27 |         accumulate: Whether to accumulate values across steps. If False, the channel will be emptied after each step.
28 |     """
29 | 
30 |     __slots__ = ("values", "accumulate")
31 | 
32 |     def __init__(self, typ: Type[Value], accumulate: bool = False) -> None:
33 |         super().__init__(typ)
34 |         # attrs
35 |         self.accumulate = accumulate
36 |         # state
37 |         self.values = list[Value]()
38 | 
39 |     def __eq__(self, value: object) -> bool:
40 |         return isinstance(value, Topic) and value.accumulate == self.accumulate
41 | 
42 |     @property
43 |     def ValueType(self) -> Any:
44 |         """The type of the value stored in the channel."""
45 |         return Sequence[self.typ]  # type: ignore[name-defined]
46 | 
47 |     @property
48 |     def UpdateType(self) -> Any:
49 |         """The type of the update received by the channel."""
50 |         return Union[self.typ, list[self.typ]]  # type: ignore[name-defined]
51 | 
52 |     def checkpoint(self) -> tuple[set[Value], list[Value]]:
53 |         return self.values
54 | 
55 |     def from_checkpoint(self, checkpoint: Optional[list[Value]]) -> Self:
56 |         empty = self.__class__(self.typ, self.accumulate)
57 |         empty.key = self.key
58 |         if checkpoint is not None:
59 |             if isinstance(checkpoint, tuple):
60 |                 empty.values = checkpoint[1]
61 |             else:
62 |                 empty.values = checkpoint
63 |         return empty
64 | 
65 |     def update(self, values: Sequence[Union[Value, list[Value]]]) -> None:
66 |         current = list(self.values)
67 |         if not self.accumulate:
68 |             self.values = list[Value]()
69 |         if flat_values := flatten(values):
70 |             self.values.extend(flat_values)
71 |         return self.values != current
72 | 
73 |     def get(self) -> Sequence[Value]:
74 |         if self.values:
75 |             return list(self.values)
76 |         else:
77 |             raise EmptyChannelError
78 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/channels/untracked_value.py:
--------------------------------------------------------------------------------
 1 | from typing import Generic, Optional, Sequence, Type
 2 | 
 3 | from typing_extensions import Self
 4 | 
 5 | from langgraph.channels.base import BaseChannel, Value
 6 | from langgraph.errors import EmptyChannelError, InvalidUpdateError
 7 | 
 8 | 
 9 | class UntrackedValue(Generic[Value], BaseChannel[Value, Value, Value]):
10 |     """Stores the last value received, never checkpointed."""
11 | 
12 |     __slots__ = ("value", "guard")
13 | 
14 |     def __init__(self, typ: Type[Value], guard: bool = True) -> None:
15 |         super().__init__(typ)
16 |         self.guard = guard
17 | 
18 |     def __eq__(self, value: object) -> bool:
19 |         return isinstance(value, UntrackedValue) and value.guard == self.guard
20 | 
21 |     @property
22 |     def ValueType(self) -> Type[Value]:
23 |         """The type of the value stored in the channel."""
24 |         return self.typ
25 | 
26 |     @property
27 |     def UpdateType(self) -> Type[Value]:
28 |         """The type of the update received by the channel."""
29 |         return self.typ
30 | 
31 |     def checkpoint(self) -> Value:
32 |         raise EmptyChannelError()
33 | 
34 |     def from_checkpoint(self, checkpoint: Optional[Value]) -> Self:
35 |         empty = self.__class__(self.typ, self.guard)
36 |         empty.key = self.key
37 |         return empty
38 | 
39 |     def update(self, values: Sequence[Value]) -> bool:
40 |         if len(values) == 0:
41 |             return False
42 |         if len(values) != 1 and self.guard:
43 |             raise InvalidUpdateError(
44 |                 f"At key '{self.key}': UntrackedValue(guard=True) can receive only one value per step. Use guard=False if you want to store any one of multiple values."
45 |             )
46 | 
47 |         self.value = values[-1]
48 |         return True
49 | 
50 |     def get(self) -> Value:
51 |         try:
52 |             return self.value
53 |         except AttributeError:
54 |             raise EmptyChannelError()
55 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/errors.py:
--------------------------------------------------------------------------------
  1 | from enum import Enum
  2 | from typing import Any, Sequence
  3 | 
  4 | from langgraph.checkpoint.base import EmptyChannelError  # noqa: F401
  5 | from langgraph.types import Command, Interrupt
  6 | 
  7 | # EmptyChannelError re-exported for backwards compatibility
  8 | 
  9 | 
 10 | class ErrorCode(Enum):
 11 |     GRAPH_RECURSION_LIMIT = "GRAPH_RECURSION_LIMIT"
 12 |     INVALID_CONCURRENT_GRAPH_UPDATE = "INVALID_CONCURRENT_GRAPH_UPDATE"
 13 |     INVALID_GRAPH_NODE_RETURN_VALUE = "INVALID_GRAPH_NODE_RETURN_VALUE"
 14 |     MULTIPLE_SUBGRAPHS = "MULTIPLE_SUBGRAPHS"
 15 |     INVALID_CHAT_HISTORY = "INVALID_CHAT_HISTORY"
 16 | 
 17 | 
 18 | def create_error_message(*, message: str, error_code: ErrorCode) -> str:
 19 |     return (
 20 |         f"{message}\n"
 21 |         "For troubleshooting, visit: https://python.langchain.com/docs/"
 22 |         f"troubleshooting/errors/{error_code.value}"
 23 |     )
 24 | 
 25 | 
 26 | class GraphRecursionError(RecursionError):
 27 |     """Raised when the graph has exhausted the maximum number of steps.
 28 | 
 29 |     This prevents infinite loops. To increase the maximum number of steps,
 30 |     run your graph with a config specifying a higher `recursion_limit`.
 31 | 
 32 |     Troubleshooting Guides:
 33 | 
 34 |     - [GRAPH_RECURSION_LIMIT](https://python.langchain.com/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT)
 35 | 
 36 |     Examples:
 37 | 
 38 |         graph = builder.compile()
 39 |         graph.invoke(
 40 |             {"messages": [("user", "Hello, world!")]},
 41 |             # The config is the second positional argument
 42 |             {"recursion_limit": 1000},
 43 |         )
 44 |     """
 45 | 
 46 |     pass
 47 | 
 48 | 
 49 | class InvalidUpdateError(Exception):
 50 |     """Raised when attempting to update a channel with an invalid set of updates.
 51 | 
 52 |     Troubleshooting Guides:
 53 | 
 54 |     - [INVALID_CONCURRENT_GRAPH_UPDATE](https://python.langchain.com/docs/troubleshooting/errors/INVALID_CONCURRENT_GRAPH_UPDATE)
 55 |     - [INVALID_GRAPH_NODE_RETURN_VALUE](https://python.langchain.com/docs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE)
 56 |     """
 57 | 
 58 |     pass
 59 | 
 60 | 
 61 | class GraphBubbleUp(Exception):
 62 |     pass
 63 | 
 64 | 
 65 | class GraphInterrupt(GraphBubbleUp):
 66 |     """Raised when a subgraph is interrupted, suppressed by the root graph.
 67 |     Never raised directly, or surfaced to the user."""
 68 | 
 69 |     def __init__(self, interrupts: Sequence[Interrupt] = ()) -> None:
 70 |         super().__init__(interrupts)
 71 | 
 72 | 
 73 | class NodeInterrupt(GraphInterrupt):
 74 |     """Raised by a node to interrupt execution."""
 75 | 
 76 |     def __init__(self, value: Any) -> None:
 77 |         super().__init__([Interrupt(value=value)])
 78 | 
 79 | 
 80 | class GraphDelegate(GraphBubbleUp):
 81 |     """Raised when a graph is delegated (for distributed mode)."""
 82 | 
 83 |     def __init__(self, *args: dict[str, Any]) -> None:
 84 |         super().__init__(*args)
 85 | 
 86 | 
 87 | class ParentCommand(GraphBubbleUp):
 88 |     args: tuple[Command]
 89 | 
 90 |     def __init__(self, command: Command) -> None:
 91 |         super().__init__(command)
 92 | 
 93 | 
 94 | class EmptyInputError(Exception):
 95 |     """Raised when graph receives an empty input."""
 96 | 
 97 |     pass
 98 | 
 99 | 
100 | class TaskNotFound(Exception):
101 |     """Raised when the executor is unable to find a task (for distributed mode)."""
102 | 
103 |     pass
104 | 
105 | 
106 | class CheckpointNotLatest(Exception):
107 |     """Raised when the checkpoint is not the latest version (for distributed mode)."""
108 | 
109 |     pass
110 | 
111 | 
112 | class MultipleSubgraphsError(Exception):
113 |     """Raised when multiple subgraphs are called inside the same node.
114 | 
115 |     Troubleshooting guides:
116 | 
117 |     - [MULTIPLE_SUBGRAPHS](https://python.langchain.com/docs/troubleshooting/errors/MULTIPLE_SUBGRAPHS)
118 |     """
119 | 
120 |     pass
121 | 
122 | 
123 | _SEEN_CHECKPOINT_NS: set[str] = set()
124 | """Used for subgraph detection."""
125 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/func/__init__.py:
--------------------------------------------------------------------------------
  1 | import asyncio
  2 | import concurrent
  3 | import concurrent.futures
  4 | import inspect
  5 | import types
  6 | from functools import partial, update_wrapper
  7 | from typing import (
  8 |     Any,
  9 |     Awaitable,
 10 |     Callable,
 11 |     Optional,
 12 |     TypeVar,
 13 |     Union,
 14 |     overload,
 15 | )
 16 | 
 17 | from typing_extensions import ParamSpec
 18 | 
 19 | from langgraph.channels.ephemeral_value import EphemeralValue
 20 | from langgraph.channels.last_value import LastValue
 21 | from langgraph.checkpoint.base import BaseCheckpointSaver
 22 | from langgraph.constants import END, START, TAG_HIDDEN
 23 | from langgraph.pregel import Pregel
 24 | from langgraph.pregel.call import get_runnable_for_func
 25 | from langgraph.pregel.read import PregelNode
 26 | from langgraph.pregel.write import ChannelWrite, ChannelWriteEntry
 27 | from langgraph.store.base import BaseStore
 28 | from langgraph.types import RetryPolicy, StreamMode, StreamWriter
 29 | 
 30 | P = ParamSpec("P")
 31 | P1 = TypeVar("P1")
 32 | T = TypeVar("T")
 33 | 
 34 | 
 35 | def call(
 36 |     func: Callable[[P1], T],
 37 |     input: P1,
 38 |     *,
 39 |     retry: Optional[RetryPolicy] = None,
 40 | ) -> concurrent.futures.Future[T]:
 41 |     from langgraph.constants import CONFIG_KEY_CALL
 42 |     from langgraph.utils.config import get_configurable
 43 | 
 44 |     conf = get_configurable()
 45 |     impl = conf[CONFIG_KEY_CALL]
 46 |     fut = impl(func, input, retry=retry)
 47 |     return fut
 48 | 
 49 | 
 50 | @overload
 51 | def task(
 52 |     *, retry: Optional[RetryPolicy] = None
 53 | ) -> Callable[[Callable[P, Awaitable[T]]], Callable[P, asyncio.Future[T]]]: ...
 54 | 
 55 | 
 56 | @overload
 57 | def task(  # type: ignore[overload-cannot-match]
 58 |     *, retry: Optional[RetryPolicy] = None
 59 | ) -> Callable[[Callable[P, T]], Callable[P, concurrent.futures.Future[T]]]: ...
 60 | 
 61 | 
 62 | def task(
 63 |     *, retry: Optional[RetryPolicy] = None
 64 | ) -> Union[
 65 |     Callable[[Callable[P, Awaitable[T]]], Callable[P, asyncio.Future[T]]],
 66 |     Callable[[Callable[P, T]], Callable[P, concurrent.futures.Future[T]]],
 67 | ]:
 68 |     def _task(func: Callable[P, T]) -> Callable[P, concurrent.futures.Future[T]]:
 69 |         return update_wrapper(partial(call, func, retry=retry), func)
 70 | 
 71 |     return _task
 72 | 
 73 | 
 74 | def entrypoint(
 75 |     *,
 76 |     checkpointer: Optional[BaseCheckpointSaver] = None,
 77 |     store: Optional[BaseStore] = None,
 78 | ) -> Callable[[types.FunctionType], Pregel]:
 79 |     def _imp(func: types.FunctionType) -> Pregel:
 80 |         if inspect.isgeneratorfunction(func):
 81 | 
 82 |             def gen_wrapper(*args: Any, writer: StreamWriter, **kwargs: Any) -> Any:
 83 |                 for chunk in func(*args, **kwargs):
 84 |                     writer(chunk)
 85 | 
 86 |             bound = get_runnable_for_func(gen_wrapper)
 87 |             stream_mode: StreamMode = "custom"
 88 |         elif inspect.isasyncgenfunction(func):
 89 | 
 90 |             async def agen_wrapper(
 91 |                 *args: Any, writer: StreamWriter, **kwargs: Any
 92 |             ) -> Any:
 93 |                 async for chunk in func(*args, **kwargs):
 94 |                     writer(chunk)
 95 | 
 96 |             bound = get_runnable_for_func(agen_wrapper)
 97 |             stream_mode = "custom"
 98 |         else:
 99 |             bound = get_runnable_for_func(func)
100 |             stream_mode = "updates"
101 | 
102 |         return Pregel(
103 |             nodes={
104 |                 func.__name__: PregelNode(
105 |                     bound=bound,
106 |                     triggers=[START],
107 |                     channels=[START],
108 |                     writers=[ChannelWrite([ChannelWriteEntry(END)], tags=[TAG_HIDDEN])],
109 |                 )
110 |             },
111 |             channels={START: EphemeralValue(Any), END: LastValue(Any, END)},
112 |             input_channels=START,
113 |             output_channels=END,
114 |             stream_channels=END,
115 |             stream_mode=stream_mode,
116 |             checkpointer=checkpointer,
117 |             store=store,
118 |         )
119 | 
120 |     return _imp
121 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/graph/__init__.py:
--------------------------------------------------------------------------------
 1 | from langgraph.graph.graph import END, START, Graph
 2 | from langgraph.graph.message import MessageGraph, MessagesState, add_messages
 3 | from langgraph.graph.state import StateGraph
 4 | 
 5 | __all__ = [
 6 |     "END",
 7 |     "START",
 8 |     "Graph",
 9 |     "StateGraph",
10 |     "MessageGraph",
11 |     "add_messages",
12 |     "MessagesState",
13 | ]
14 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/managed/__init__.py:
--------------------------------------------------------------------------------
1 | from langgraph.managed.is_last_step import IsLastStep, RemainingSteps
2 | 
3 | __all__ = ["IsLastStep", "RemainingSteps"]
4 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/managed/base.py:
--------------------------------------------------------------------------------
  1 | from abc import ABC, abstractmethod
  2 | from contextlib import asynccontextmanager, contextmanager
  3 | from inspect import isclass
  4 | from typing import (
  5 |     Any,
  6 |     AsyncIterator,
  7 |     Generic,
  8 |     Iterator,
  9 |     NamedTuple,
 10 |     Sequence,
 11 |     Type,
 12 |     TypeVar,
 13 |     Union,
 14 | )
 15 | 
 16 | from typing_extensions import Self, TypeGuard
 17 | 
 18 | from langgraph.types import LoopProtocol
 19 | 
 20 | V = TypeVar("V")
 21 | U = TypeVar("U")
 22 | 
 23 | 
 24 | class ManagedValue(ABC, Generic[V]):
 25 |     def __init__(self, loop: LoopProtocol) -> None:
 26 |         self.loop = loop
 27 | 
 28 |     @classmethod
 29 |     @contextmanager
 30 |     def enter(cls, loop: LoopProtocol, **kwargs: Any) -> Iterator[Self]:
 31 |         try:
 32 |             value = cls(loop, **kwargs)
 33 |             yield value
 34 |         finally:
 35 |             # because managed value and Pregel have reference to each other
 36 |             # let's make sure to break the reference on exit
 37 |             try:
 38 |                 del value
 39 |             except UnboundLocalError:
 40 |                 pass
 41 | 
 42 |     @classmethod
 43 |     @asynccontextmanager
 44 |     async def aenter(cls, loop: LoopProtocol, **kwargs: Any) -> AsyncIterator[Self]:
 45 |         try:
 46 |             value = cls(loop, **kwargs)
 47 |             yield value
 48 |         finally:
 49 |             # because managed value and Pregel have reference to each other
 50 |             # let's make sure to break the reference on exit
 51 |             try:
 52 |                 del value
 53 |             except UnboundLocalError:
 54 |                 pass
 55 | 
 56 |     @abstractmethod
 57 |     def __call__(self) -> V: ...
 58 | 
 59 | 
 60 | class WritableManagedValue(Generic[V, U], ManagedValue[V], ABC):
 61 |     @abstractmethod
 62 |     def update(self, writes: Sequence[U]) -> None: ...
 63 | 
 64 |     @abstractmethod
 65 |     async def aupdate(self, writes: Sequence[U]) -> None: ...
 66 | 
 67 | 
 68 | class ConfiguredManagedValue(NamedTuple):
 69 |     cls: Type[ManagedValue]
 70 |     kwargs: dict[str, Any]
 71 | 
 72 | 
 73 | ManagedValueSpec = Union[Type[ManagedValue], ConfiguredManagedValue]
 74 | 
 75 | 
 76 | def is_managed_value(value: Any) -> TypeGuard[ManagedValueSpec]:
 77 |     return (isclass(value) and issubclass(value, ManagedValue)) or isinstance(
 78 |         value, ConfiguredManagedValue
 79 |     )
 80 | 
 81 | 
 82 | def is_readonly_managed_value(value: Any) -> TypeGuard[Type[ManagedValue]]:
 83 |     return (
 84 |         isclass(value)
 85 |         and issubclass(value, ManagedValue)
 86 |         and not issubclass(value, WritableManagedValue)
 87 |     ) or (
 88 |         isinstance(value, ConfiguredManagedValue)
 89 |         and not issubclass(value.cls, WritableManagedValue)
 90 |     )
 91 | 
 92 | 
 93 | def is_writable_managed_value(value: Any) -> TypeGuard[Type[WritableManagedValue]]:
 94 |     return (isclass(value) and issubclass(value, WritableManagedValue)) or (
 95 |         isinstance(value, ConfiguredManagedValue)
 96 |         and issubclass(value.cls, WritableManagedValue)
 97 |     )
 98 | 
 99 | 
100 | ChannelKeyPlaceholder = object()
101 | ChannelTypePlaceholder = object()
102 | 
103 | 
104 | ManagedValueMapping = dict[str, ManagedValue]
105 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/managed/context.py:
--------------------------------------------------------------------------------
  1 | from contextlib import asynccontextmanager, contextmanager
  2 | from inspect import signature
  3 | from typing import (
  4 |     Any,
  5 |     AsyncContextManager,
  6 |     AsyncIterator,
  7 |     Callable,
  8 |     ContextManager,
  9 |     Generic,
 10 |     Iterator,
 11 |     Optional,
 12 |     Type,
 13 |     Union,
 14 | )
 15 | 
 16 | from typing_extensions import Self
 17 | 
 18 | from langgraph.managed.base import ConfiguredManagedValue, ManagedValue, V
 19 | from langgraph.types import LoopProtocol
 20 | 
 21 | 
 22 | class Context(ManagedValue[V], Generic[V]):
 23 |     runtime = True
 24 | 
 25 |     value: V
 26 | 
 27 |     @staticmethod
 28 |     def of(
 29 |         ctx: Union[
 30 |             None,
 31 |             Callable[..., ContextManager[V]],
 32 |             Type[ContextManager[V]],
 33 |             Callable[..., AsyncContextManager[V]],
 34 |             Type[AsyncContextManager[V]],
 35 |         ] = None,
 36 |         actx: Optional[
 37 |             Union[
 38 |                 Callable[..., AsyncContextManager[V]],
 39 |                 Type[AsyncContextManager[V]],
 40 |             ]
 41 |         ] = None,
 42 |     ) -> ConfiguredManagedValue:
 43 |         if ctx is None and actx is None:
 44 |             raise ValueError("Must provide either sync or async context manager.")
 45 |         return ConfiguredManagedValue(Context, {"ctx": ctx, "actx": actx})
 46 | 
 47 |     @classmethod
 48 |     @contextmanager
 49 |     def enter(cls, loop: LoopProtocol, **kwargs: Any) -> Iterator[Self]:
 50 |         with super().enter(loop, **kwargs) as self:
 51 |             if self.ctx is None:
 52 |                 raise ValueError(
 53 |                     "Synchronous context manager not found. Please initialize Context value with a sync context manager, or invoke your graph asynchronously."
 54 |                 )
 55 |             ctx = (
 56 |                 self.ctx(loop.config)  # type: ignore[call-arg]
 57 |                 if signature(self.ctx).parameters.get("config")
 58 |                 else self.ctx()
 59 |             )
 60 |             with ctx as v:  # type: ignore[union-attr]
 61 |                 self.value = v
 62 |                 yield self
 63 | 
 64 |     @classmethod
 65 |     @asynccontextmanager
 66 |     async def aenter(cls, loop: LoopProtocol, **kwargs: Any) -> AsyncIterator[Self]:
 67 |         async with super().aenter(loop, **kwargs) as self:
 68 |             if self.actx is not None:
 69 |                 ctx = (
 70 |                     self.actx(loop.config)  # type: ignore[call-arg]
 71 |                     if signature(self.actx).parameters.get("config")
 72 |                     else self.actx()
 73 |                 )
 74 |             elif self.ctx is not None:
 75 |                 ctx = (
 76 |                     self.ctx(loop.config)  # type: ignore
 77 |                     if signature(self.ctx).parameters.get("config")
 78 |                     else self.ctx()
 79 |                 )
 80 |             else:
 81 |                 raise ValueError(
 82 |                     "Asynchronous context manager not found. Please initialize Context value with an async context manager, or invoke your graph synchronously."
 83 |                 )
 84 |             if hasattr(ctx, "__aenter__"):
 85 |                 async with ctx as v:
 86 |                     self.value = v
 87 |                     yield self
 88 |             elif hasattr(ctx, "__enter__") and hasattr(ctx, "__exit__"):
 89 |                 with ctx as v:
 90 |                     self.value = v
 91 |                     yield self
 92 |             else:
 93 |                 raise ValueError(
 94 |                     "Context manager must have either __enter__ or __aenter__ method."
 95 |                 )
 96 | 
 97 |     def __init__(
 98 |         self,
 99 |         loop: LoopProtocol,
100 |         *,
101 |         ctx: Union[None, Type[ContextManager[V]], Type[AsyncContextManager[V]]] = None,
102 |         actx: Optional[Type[AsyncContextManager[V]]] = None,
103 |     ) -> None:
104 |         self.ctx = ctx
105 |         self.actx = actx
106 | 
107 |     def __call__(self) -> V:
108 |         return self.value
109 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/managed/is_last_step.py:
--------------------------------------------------------------------------------
 1 | from typing import Annotated
 2 | 
 3 | from langgraph.managed.base import ManagedValue
 4 | 
 5 | 
 6 | class IsLastStepManager(ManagedValue[bool]):
 7 |     def __call__(self) -> bool:
 8 |         return self.loop.step == self.loop.stop - 1
 9 | 
10 | 
11 | IsLastStep = Annotated[bool, IsLastStepManager]
12 | 
13 | 
14 | class RemainingStepsManager(ManagedValue[int]):
15 |     def __call__(self) -> int:
16 |         return self.loop.stop - self.loop.step
17 | 
18 | 
19 | RemainingSteps = Annotated[int, RemainingStepsManager]
20 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/managed/shared_value.py:
--------------------------------------------------------------------------------
  1 | import collections.abc
  2 | from contextlib import asynccontextmanager, contextmanager
  3 | from typing import (
  4 |     Any,
  5 |     AsyncIterator,
  6 |     Iterator,
  7 |     Optional,
  8 |     Sequence,
  9 |     Type,
 10 | )
 11 | 
 12 | from typing_extensions import NotRequired, Required, Self
 13 | 
 14 | from langgraph.constants import CONF
 15 | from langgraph.errors import InvalidUpdateError
 16 | from langgraph.managed.base import (
 17 |     ChannelKeyPlaceholder,
 18 |     ChannelTypePlaceholder,
 19 |     ConfiguredManagedValue,
 20 |     WritableManagedValue,
 21 | )
 22 | from langgraph.store.base import PutOp
 23 | from langgraph.types import LoopProtocol
 24 | 
 25 | V = dict[str, Any]
 26 | 
 27 | 
 28 | Value = dict[str, V]
 29 | Update = dict[str, Optional[V]]
 30 | 
 31 | 
 32 | # Adapted from typing_extensions
 33 | def _strip_extras(t):  # type: ignore[no-untyped-def]
 34 |     """Strips Annotated, Required and NotRequired from a given type."""
 35 |     if hasattr(t, "__origin__"):
 36 |         return _strip_extras(t.__origin__)
 37 |     if hasattr(t, "__origin__") and t.__origin__ in (Required, NotRequired):
 38 |         return _strip_extras(t.__args__[0])
 39 | 
 40 |     return t
 41 | 
 42 | 
 43 | class SharedValue(WritableManagedValue[Value, Update]):
 44 |     @staticmethod
 45 |     def on(scope: str) -> ConfiguredManagedValue:
 46 |         return ConfiguredManagedValue(
 47 |             SharedValue,
 48 |             {
 49 |                 "scope": scope,
 50 |                 "key": ChannelKeyPlaceholder,
 51 |                 "typ": ChannelTypePlaceholder,
 52 |             },
 53 |         )
 54 | 
 55 |     @classmethod
 56 |     @contextmanager
 57 |     def enter(cls, loop: LoopProtocol, **kwargs: Any) -> Iterator[Self]:
 58 |         with super().enter(loop, **kwargs) as value:
 59 |             if loop.store is not None:
 60 |                 saved = loop.store.search(value.ns)
 61 |                 value.value = {it.key: it.value for it in saved}
 62 |             yield value
 63 | 
 64 |     @classmethod
 65 |     @asynccontextmanager
 66 |     async def aenter(cls, loop: LoopProtocol, **kwargs: Any) -> AsyncIterator[Self]:
 67 |         async with super().aenter(loop, **kwargs) as value:
 68 |             if loop.store is not None:
 69 |                 saved = await loop.store.asearch(value.ns)
 70 |                 value.value = {it.key: it.value for it in saved}
 71 |             yield value
 72 | 
 73 |     def __init__(
 74 |         self, loop: LoopProtocol, *, typ: Type[Any], scope: str, key: str
 75 |     ) -> None:
 76 |         super().__init__(loop)
 77 |         if typ := _strip_extras(typ):
 78 |             if typ not in (
 79 |                 dict,
 80 |                 collections.abc.Mapping,
 81 |                 collections.abc.MutableMapping,
 82 |             ):
 83 |                 raise ValueError("SharedValue must be a dict")
 84 |         self.scope = scope
 85 |         self.value: Value = {}
 86 |         if self.loop.store is None:
 87 |             pass
 88 |         elif scope_value := self.loop.config[CONF].get(self.scope):
 89 |             self.ns = ("scoped", scope, key, scope_value)
 90 |         else:
 91 |             raise ValueError(
 92 |                 f"Scope {scope} for shared state key not in config.configurable"
 93 |             )
 94 | 
 95 |     def __call__(self) -> Value:
 96 |         return self.value
 97 | 
 98 |     def _process_update(self, values: Sequence[Update]) -> list[PutOp]:
 99 |         writes: list[PutOp] = []
100 |         for vv in values:
101 |             for k, v in vv.items():
102 |                 if v is None:
103 |                     if k in self.value:
104 |                         del self.value[k]
105 |                         writes.append(PutOp(self.ns, k, None))
106 |                 elif not isinstance(v, dict):
107 |                     raise InvalidUpdateError("Received a non-dict value")
108 |                 else:
109 |                     self.value[k] = v
110 |                     writes.append(PutOp(self.ns, k, v))
111 |         return writes
112 | 
113 |     def update(self, values: Sequence[Update]) -> None:
114 |         if self.loop.store is None:
115 |             self._process_update(values)
116 |         else:
117 |             return self.loop.store.batch(self._process_update(values))
118 | 
119 |     async def aupdate(self, writes: Sequence[Update]) -> None:
120 |         if self.loop.store is None:
121 |             self._process_update(writes)
122 |         else:
123 |             return await self.loop.store.abatch(self._process_update(writes))
124 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/prebuilt/__init__.py:
--------------------------------------------------------------------------------
 1 | """langgraph.prebuilt exposes a higher-level API for creating and executing agents and tools."""
 2 | 
 3 | from langgraph.prebuilt.chat_agent_executor import create_react_agent
 4 | from langgraph.prebuilt.tool_executor import ToolExecutor, ToolInvocation
 5 | from langgraph.prebuilt.tool_node import (
 6 |     InjectedState,
 7 |     InjectedStore,
 8 |     ToolNode,
 9 |     tools_condition,
10 | )
11 | from langgraph.prebuilt.tool_validator import ValidationNode
12 | 
13 | __all__ = [
14 |     "create_react_agent",
15 |     "ToolExecutor",
16 |     "ToolInvocation",
17 |     "ToolNode",
18 |     "tools_condition",
19 |     "ValidationNode",
20 |     "InjectedState",
21 |     "InjectedStore",
22 | ]
23 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/pregel/log.py:
--------------------------------------------------------------------------------
1 | import logging
2 | 
3 | logger = logging.getLogger("langgraph")
4 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/pregel/manager.py:
--------------------------------------------------------------------------------
  1 | import asyncio
  2 | from contextlib import AsyncExitStack, ExitStack, asynccontextmanager, contextmanager
  3 | from typing import AsyncIterator, Iterator, Mapping, Union
  4 | 
  5 | from langgraph.channels.base import BaseChannel
  6 | from langgraph.checkpoint.base import Checkpoint
  7 | from langgraph.managed.base import (
  8 |     ConfiguredManagedValue,
  9 |     ManagedValueMapping,
 10 |     ManagedValueSpec,
 11 | )
 12 | from langgraph.managed.context import Context
 13 | from langgraph.types import LoopProtocol
 14 | 
 15 | 
 16 | @contextmanager
 17 | def ChannelsManager(
 18 |     specs: Mapping[str, Union[BaseChannel, ManagedValueSpec]],
 19 |     checkpoint: Checkpoint,
 20 |     loop: LoopProtocol,
 21 |     *,
 22 |     skip_context: bool = False,
 23 | ) -> Iterator[tuple[Mapping[str, BaseChannel], ManagedValueMapping]]:
 24 |     """Manage channels for the lifetime of a Pregel invocation (multiple steps)."""
 25 |     channel_specs: dict[str, BaseChannel] = {}
 26 |     managed_specs: dict[str, ManagedValueSpec] = {}
 27 |     for k, v in specs.items():
 28 |         if isinstance(v, BaseChannel):
 29 |             channel_specs[k] = v
 30 |         elif (
 31 |             skip_context and isinstance(v, ConfiguredManagedValue) and v.cls is Context
 32 |         ):
 33 |             managed_specs[k] = Context.of(noop_context)
 34 |         else:
 35 |             managed_specs[k] = v
 36 |     with ExitStack() as stack:
 37 |         yield (
 38 |             {
 39 |                 k: v.from_checkpoint(checkpoint["channel_values"].get(k))
 40 |                 for k, v in channel_specs.items()
 41 |             },
 42 |             ManagedValueMapping(
 43 |                 {
 44 |                     key: stack.enter_context(
 45 |                         value.cls.enter(loop, **value.kwargs)
 46 |                         if isinstance(value, ConfiguredManagedValue)
 47 |                         else value.enter(loop)
 48 |                     )
 49 |                     for key, value in managed_specs.items()
 50 |                 }
 51 |             ),
 52 |         )
 53 | 
 54 | 
 55 | @asynccontextmanager
 56 | async def AsyncChannelsManager(
 57 |     specs: Mapping[str, Union[BaseChannel, ManagedValueSpec]],
 58 |     checkpoint: Checkpoint,
 59 |     loop: LoopProtocol,
 60 |     *,
 61 |     skip_context: bool = False,
 62 | ) -> AsyncIterator[tuple[Mapping[str, BaseChannel], ManagedValueMapping]]:
 63 |     """Manage channels for the lifetime of a Pregel invocation (multiple steps)."""
 64 |     channel_specs: dict[str, BaseChannel] = {}
 65 |     managed_specs: dict[str, ManagedValueSpec] = {}
 66 |     for k, v in specs.items():
 67 |         if isinstance(v, BaseChannel):
 68 |             channel_specs[k] = v
 69 |         elif (
 70 |             skip_context and isinstance(v, ConfiguredManagedValue) and v.cls is Context
 71 |         ):
 72 |             managed_specs[k] = Context.of(noop_context)
 73 |         else:
 74 |             managed_specs[k] = v
 75 |     async with AsyncExitStack() as stack:
 76 |         # managed: create enter tasks with reference to spec, await them
 77 |         if tasks := {
 78 |             asyncio.create_task(
 79 |                 stack.enter_async_context(
 80 |                     value.cls.aenter(loop, **value.kwargs)
 81 |                     if isinstance(value, ConfiguredManagedValue)
 82 |                     else value.aenter(loop)
 83 |                 )
 84 |             ): key
 85 |             for key, value in managed_specs.items()
 86 |         }:
 87 |             done, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
 88 |         else:
 89 |             done = set()
 90 |         yield (
 91 |             # channels: enter each channel with checkpoint
 92 |             {
 93 |                 k: v.from_checkpoint(checkpoint["channel_values"].get(k))
 94 |                 for k, v in channel_specs.items()
 95 |             },
 96 |             # managed: build mapping from spec to result
 97 |             ManagedValueMapping({tasks[task]: task.result() for task in done}),
 98 |         )
 99 | 
100 | 
101 | @contextmanager
102 | def noop_context() -> Iterator[None]:
103 |     yield None
104 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/pregel/protocol.py:
--------------------------------------------------------------------------------
  1 | from abc import ABC, abstractmethod
  2 | from typing import (
  3 |     Any,
  4 |     AsyncIterator,
  5 |     Iterator,
  6 |     Optional,
  7 |     Sequence,
  8 |     Union,
  9 | )
 10 | 
 11 | from langchain_core.runnables import Runnable, RunnableConfig
 12 | from langchain_core.runnables.graph import Graph as DrawableGraph
 13 | from typing_extensions import Self
 14 | 
 15 | from langgraph.pregel.types import All, StateSnapshot, StreamMode
 16 | 
 17 | 
 18 | class PregelProtocol(
 19 |     Runnable[Union[dict[str, Any], Any], Union[dict[str, Any], Any]], ABC
 20 | ):
 21 |     @abstractmethod
 22 |     def with_config(
 23 |         self, config: Optional[RunnableConfig] = None, **kwargs: Any
 24 |     ) -> Self: ...
 25 | 
 26 |     @abstractmethod
 27 |     def get_graph(
 28 |         self,
 29 |         config: Optional[RunnableConfig] = None,
 30 |         *,
 31 |         xray: Union[int, bool] = False,
 32 |     ) -> DrawableGraph: ...
 33 | 
 34 |     @abstractmethod
 35 |     async def aget_graph(
 36 |         self,
 37 |         config: Optional[RunnableConfig] = None,
 38 |         *,
 39 |         xray: Union[int, bool] = False,
 40 |     ) -> DrawableGraph: ...
 41 | 
 42 |     @abstractmethod
 43 |     def get_state(
 44 |         self, config: RunnableConfig, *, subgraphs: bool = False
 45 |     ) -> StateSnapshot: ...
 46 | 
 47 |     @abstractmethod
 48 |     async def aget_state(
 49 |         self, config: RunnableConfig, *, subgraphs: bool = False
 50 |     ) -> StateSnapshot: ...
 51 | 
 52 |     @abstractmethod
 53 |     def get_state_history(
 54 |         self,
 55 |         config: RunnableConfig,
 56 |         *,
 57 |         filter: Optional[dict[str, Any]] = None,
 58 |         before: Optional[RunnableConfig] = None,
 59 |         limit: Optional[int] = None,
 60 |     ) -> Iterator[StateSnapshot]: ...
 61 | 
 62 |     @abstractmethod
 63 |     def aget_state_history(
 64 |         self,
 65 |         config: RunnableConfig,
 66 |         *,
 67 |         filter: Optional[dict[str, Any]] = None,
 68 |         before: Optional[RunnableConfig] = None,
 69 |         limit: Optional[int] = None,
 70 |     ) -> AsyncIterator[StateSnapshot]: ...
 71 | 
 72 |     @abstractmethod
 73 |     def update_state(
 74 |         self,
 75 |         config: RunnableConfig,
 76 |         values: Optional[Union[dict[str, Any], Any]],
 77 |         as_node: Optional[str] = None,
 78 |     ) -> RunnableConfig: ...
 79 | 
 80 |     @abstractmethod
 81 |     async def aupdate_state(
 82 |         self,
 83 |         config: RunnableConfig,
 84 |         values: Optional[Union[dict[str, Any], Any]],
 85 |         as_node: Optional[str] = None,
 86 |     ) -> RunnableConfig: ...
 87 | 
 88 |     @abstractmethod
 89 |     def stream(
 90 |         self,
 91 |         input: Union[dict[str, Any], Any],
 92 |         config: Optional[RunnableConfig] = None,
 93 |         *,
 94 |         stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None,
 95 |         interrupt_before: Optional[Union[All, Sequence[str]]] = None,
 96 |         interrupt_after: Optional[Union[All, Sequence[str]]] = None,
 97 |         subgraphs: bool = False,
 98 |     ) -> Iterator[Union[dict[str, Any], Any]]: ...
 99 | 
100 |     @abstractmethod
101 |     def astream(
102 |         self,
103 |         input: Union[dict[str, Any], Any],
104 |         config: Optional[RunnableConfig] = None,
105 |         *,
106 |         stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None,
107 |         interrupt_before: Optional[Union[All, Sequence[str]]] = None,
108 |         interrupt_after: Optional[Union[All, Sequence[str]]] = None,
109 |         subgraphs: bool = False,
110 |     ) -> AsyncIterator[Union[dict[str, Any], Any]]: ...
111 | 
112 |     @abstractmethod
113 |     def invoke(
114 |         self,
115 |         input: Union[dict[str, Any], Any],
116 |         config: Optional[RunnableConfig] = None,
117 |         *,
118 |         interrupt_before: Optional[Union[All, Sequence[str]]] = None,
119 |         interrupt_after: Optional[Union[All, Sequence[str]]] = None,
120 |     ) -> Union[dict[str, Any], Any]: ...
121 | 
122 |     @abstractmethod
123 |     async def ainvoke(
124 |         self,
125 |         input: Union[dict[str, Any], Any],
126 |         config: Optional[RunnableConfig] = None,
127 |         *,
128 |         interrupt_before: Optional[Union[All, Sequence[str]]] = None,
129 |         interrupt_after: Optional[Union[All, Sequence[str]]] = None,
130 |     ) -> Union[dict[str, Any], Any]: ...
131 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/pregel/types.py:
--------------------------------------------------------------------------------
 1 | """Re-export types moved to langgraph.types"""
 2 | 
 3 | from langgraph.types import (
 4 |     All,
 5 |     CachePolicy,
 6 |     PregelExecutableTask,
 7 |     PregelTask,
 8 |     RetryPolicy,
 9 |     StateSnapshot,
10 |     StreamMode,
11 |     StreamWriter,
12 |     default_retry_on,
13 | )
14 | 
15 | __all__ = [
16 |     "All",
17 |     "CachePolicy",
18 |     "PregelExecutableTask",
19 |     "PregelTask",
20 |     "RetryPolicy",
21 |     "StateSnapshot",
22 |     "StreamMode",
23 |     "StreamWriter",
24 |     "default_retry_on",
25 | ]
26 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/pregel/utils.py:
--------------------------------------------------------------------------------
 1 | from typing import Optional
 2 | 
 3 | from langchain_core.runnables import RunnableLambda, RunnableSequence
 4 | from langchain_core.runnables.utils import get_function_nonlocals
 5 | 
 6 | from langgraph.checkpoint.base import ChannelVersions
 7 | from langgraph.pregel.protocol import PregelProtocol
 8 | from langgraph.utils.runnable import Runnable, RunnableCallable, RunnableSeq
 9 | 
10 | 
11 | def get_new_channel_versions(
12 |     previous_versions: ChannelVersions, current_versions: ChannelVersions
13 | ) -> ChannelVersions:
14 |     """Get subset of current_versions that are newer than previous_versions."""
15 |     if previous_versions:
16 |         version_type = type(next(iter(current_versions.values()), None))
17 |         null_version = version_type()  # type: ignore[misc]
18 |         new_versions = {
19 |             k: v
20 |             for k, v in current_versions.items()
21 |             if v > previous_versions.get(k, null_version)  # type: ignore[operator]
22 |         }
23 |     else:
24 |         new_versions = current_versions
25 | 
26 |     return new_versions
27 | 
28 | 
29 | def find_subgraph_pregel(candidate: Runnable) -> Optional[Runnable]:
30 |     from langgraph.pregel import Pregel
31 | 
32 |     candidates: list[Runnable] = [candidate]
33 | 
34 |     for c in candidates:
35 |         if (
36 |             isinstance(c, PregelProtocol)
37 |             # subgraphs that disabled checkpointing are not considered
38 |             and (not isinstance(c, Pregel) or c.checkpointer is not False)
39 |         ):
40 |             return c
41 |         elif isinstance(c, RunnableSequence) or isinstance(c, RunnableSeq):
42 |             candidates.extend(c.steps)
43 |         elif isinstance(c, RunnableLambda):
44 |             candidates.extend(c.deps)
45 |         elif isinstance(c, RunnableCallable):
46 |             if c.func is not None:
47 |                 candidates.extend(
48 |                     nl.__self__ if hasattr(nl, "__self__") else nl
49 |                     for nl in get_function_nonlocals(c.func)
50 |                 )
51 |             elif c.afunc is not None:
52 |                 candidates.extend(
53 |                     nl.__self__ if hasattr(nl, "__self__") else nl
54 |                     for nl in get_function_nonlocals(c.afunc)
55 |                 )
56 | 
57 |     return None
58 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/pregel/validate.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Mapping, Optional, Sequence, Union
 2 | 
 3 | from langgraph.channels.base import BaseChannel
 4 | from langgraph.constants import RESERVED
 5 | from langgraph.pregel.read import PregelNode
 6 | from langgraph.types import All
 7 | 
 8 | 
 9 | def validate_graph(
10 |     nodes: Mapping[str, PregelNode],
11 |     channels: dict[str, BaseChannel],
12 |     input_channels: Union[str, Sequence[str]],
13 |     output_channels: Union[str, Sequence[str]],
14 |     stream_channels: Optional[Union[str, Sequence[str]]],
15 |     interrupt_after_nodes: Union[All, Sequence[str]],
16 |     interrupt_before_nodes: Union[All, Sequence[str]],
17 | ) -> None:
18 |     for chan in channels:
19 |         if chan in RESERVED:
20 |             raise ValueError(f"Channel names {chan} are reserved")
21 | 
22 |     subscribed_channels = set[str]()
23 |     for name, node in nodes.items():
24 |         if name in RESERVED:
25 |             raise ValueError(f"Node names {RESERVED} are reserved")
26 |         if isinstance(node, PregelNode):
27 |             subscribed_channels.update(node.triggers)
28 |         else:
29 |             raise TypeError(
30 |                 f"Invalid node type {type(node)}, expected Channel.subscribe_to()"
31 |             )
32 | 
33 |     for chan in subscribed_channels:
34 |         if chan not in channels:
35 |             raise ValueError(f"Subscribed channel '{chan}' not in 'channels'")
36 | 
37 |     if isinstance(input_channels, str):
38 |         if input_channels not in channels:
39 |             raise ValueError(f"Input channel '{input_channels}' not in 'channels'")
40 |         if input_channels not in subscribed_channels:
41 |             raise ValueError(
42 |                 f"Input channel {input_channels} is not subscribed to by any node"
43 |             )
44 |     else:
45 |         for chan in input_channels:
46 |             if chan not in channels:
47 |                 raise ValueError(f"Input channel '{chan}' not in 'channels'")
48 |         if all(chan not in subscribed_channels for chan in input_channels):
49 |             raise ValueError(
50 |                 f"None of the input channels {input_channels} are subscribed to by any node"
51 |             )
52 | 
53 |     all_output_channels = set[str]()
54 |     if isinstance(output_channels, str):
55 |         all_output_channels.add(output_channels)
56 |     else:
57 |         all_output_channels.update(output_channels)
58 |     if isinstance(stream_channels, str):
59 |         all_output_channels.add(stream_channels)
60 |     elif stream_channels is not None:
61 |         all_output_channels.update(stream_channels)
62 | 
63 |     for chan in all_output_channels:
64 |         if chan not in channels:
65 |             raise ValueError(f"Output channel '{chan}' not in 'channels'")
66 | 
67 |     if interrupt_after_nodes != "*":
68 |         for n in interrupt_after_nodes:
69 |             if n not in nodes:
70 |                 raise ValueError(f"Node {n} not in nodes")
71 |     if interrupt_before_nodes != "*":
72 |         for n in interrupt_before_nodes:
73 |             if n not in nodes:
74 |                 raise ValueError(f"Node {n} not in nodes")
75 | 
76 | 
77 | def validate_keys(
78 |     keys: Optional[Union[str, Sequence[str]]],
79 |     channels: Mapping[str, Any],
80 | ) -> None:
81 |     if isinstance(keys, str):
82 |         if keys not in channels:
83 |             raise ValueError(f"Key {keys} not in channels")
84 |     elif keys is not None:
85 |         for chan in keys:
86 |             if chan not in channels:
87 |                 raise ValueError(f"Key {chan} not in channels")
88 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/langgraph/langgraph/py.typed


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/utils/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/langgraph/langgraph/utils/__init__.py


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/utils/pydantic.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Dict, Optional, Union
 2 | 
 3 | from pydantic import BaseModel
 4 | from pydantic.v1 import BaseModel as BaseModelV1
 5 | 
 6 | 
 7 | def create_model(
 8 |     model_name: str,
 9 |     *,
10 |     field_definitions: Optional[Dict[str, Any]] = None,
11 |     root: Optional[Any] = None,
12 | ) -> Union[BaseModel, BaseModelV1]:
13 |     """Create a pydantic model with the given field definitions.
14 | 
15 |     Args:
16 |         model_name: The name of the model.
17 |         field_definitions: The field definitions for the model.
18 |         root: Type for a root model (RootModel)
19 |     """
20 |     try:
21 |         # for langchain-core >= 0.3.0
22 |         from langchain_core.utils.pydantic import create_model_v2
23 | 
24 |         return create_model_v2(
25 |             model_name,
26 |             field_definitions=field_definitions,
27 |             root=root,
28 |         )
29 |     except ImportError:
30 |         # for langchain-core < 0.3.0
31 |         from langchain_core.runnables.utils import create_model
32 | 
33 |         v1_kwargs = {}
34 |         if root is not None:
35 |             v1_kwargs["__root__"] = root
36 | 
37 |         return create_model(model_name, **v1_kwargs, **(field_definitions or {}))
38 | 


--------------------------------------------------------------------------------
/libs/langgraph/langgraph/version.py:
--------------------------------------------------------------------------------
 1 | """Exports package version."""
 2 | 
 3 | from importlib import metadata
 4 | 
 5 | try:
 6 |     __version__ = metadata.version(__package__)
 7 | except metadata.PackageNotFoundError:
 8 |     # Case where package metadata is not available.
 9 |     __version__ = ""
10 | del metadata  # optional, avoids polluting the results of dir(__package__)
11 | 


--------------------------------------------------------------------------------
/libs/langgraph/poetry.toml:
--------------------------------------------------------------------------------
1 | [virtualenvs]
2 | in-project = true
3 | 
4 | [installer]
5 | modern-installation = false
6 | 


--------------------------------------------------------------------------------
/libs/langgraph/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph"
 3 | version = "0.2.60"
 4 | description = "Building stateful, multi-actor applications with LLMs"
 5 | authors = []
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | repository = "https://www.github.com/langchain-ai/langgraph"
 9 | 
10 | [tool.poetry.dependencies]
11 | python = ">=3.9.0,<4.0"
12 | langchain-core = ">=0.2.43,<0.4.0,!=0.3.0,!=0.3.1,!=0.3.2,!=0.3.3,!=0.3.4,!=0.3.5,!=0.3.6,!=0.3.7,!=0.3.8,!=0.3.9,!=0.3.10,!=0.3.11,!=0.3.12,!=0.3.13,!=0.3.14,!=0.3.15,!=0.3.16,!=0.3.17,!=0.3.18,!=0.3.19,!=0.3.20,!=0.3.21,!=0.3.22"
13 | langgraph-checkpoint = "^2.0.4"
14 | langgraph-sdk = "^0.1.42"
15 | 
16 | [tool.poetry.group.dev.dependencies]
17 | pytest = "^8.3.2"
18 | pytest-cov = "^4.0.0"
19 | pytest-dotenv = "^0.5.2"
20 | pytest-mock  = "^3.10.0"
21 | syrupy = "^4.0.2"
22 | httpx = "^0.26.0"
23 | pytest-watcher = "^0.4.1"
24 | mypy = "^1.6.0"
25 | ruff = "^0.6.2"
26 | jupyter = "^1.0.0"
27 | pytest-xdist = {extras = ["psutil"], version = "^3.6.1"}
28 | pytest-repeat = "^0.9.3"
29 | langgraph-checkpoint = {path = "../checkpoint", develop = true}
30 | langgraph-checkpoint-duckdb = {path = "../checkpoint-duckdb", develop = true}
31 | langgraph-checkpoint-sqlite = {path = "../checkpoint-sqlite", develop = true}
32 | langgraph-checkpoint-postgres = {path = "../checkpoint-postgres", develop = true}
33 | langgraph-sdk = {path = "../sdk-py", develop = true}
34 | psycopg = {extras = ["binary"], version = ">=3.0.0", python = ">=3.10"}
35 | uvloop = "0.21.0beta1"
36 | pyperf = "^2.7.0"
37 | py-spy = "^0.3.14"
38 | types-requests = "^2.32.0.20240914"
39 | 
40 | [tool.ruff]
41 | lint.select = [ "E", "F", "I" ]
42 | lint.ignore = [ "E501" ]
43 | line-length = 88
44 | indent-width = 4
45 | extend-include = ["*.ipynb"]
46 | 
47 | [tool.ruff.format]
48 | quote-style = "double"
49 | indent-style = "space"
50 | skip-magic-trailing-comma = false
51 | line-ending = "auto"
52 | docstring-code-format = false
53 | docstring-code-line-length = "dynamic"
54 | 
55 | [tool.mypy]
56 | # https://mypy.readthedocs.io/en/stable/config_file.html
57 | disallow_untyped_defs = "True"
58 | explicit_package_bases = "True"
59 | warn_no_return = "False"
60 | warn_unused_ignores = "True"
61 | warn_redundant_casts = "True"
62 | allow_redefinition = "True"
63 | disable_error_code = "typeddict-item, return-value, override, has-type"
64 | 
65 | [tool.coverage.run]
66 | omit = ["tests/*"]
67 | 
68 | [tool.pytest-watcher]
69 | now = true
70 | delay = 0.1
71 | patterns = ["*.py"]
72 | 
73 | [build-system]
74 | requires = ["poetry-core>=1.0.0"]
75 | build-backend = "poetry.core.masonry.api"
76 | 
77 | [tool.pytest.ini_options]
78 | # --strict-markers will raise errors on unknown marks.
79 | # https://docs.pytest.org/en/7.1.x/how-to/mark.html#raising-errors-on-unknown-marks
80 | #
81 | # https://docs.pytest.org/en/7.1.x/reference/reference.html
82 | # --strict-config       any warnings encountered while parsing the `pytest`
83 | #                       section of the configuration file raise errors.
84 | #
85 | # https://github.com/tophat/syrupy
86 | # --snapshot-warn-unused    Prints a warning on unused snapshots rather than fail the test suite.
87 | addopts = "--full-trace --strict-markers --strict-config --durations=5 --snapshot-warn-unused"
88 | # Registering custom markers.
89 | # https://docs.pytest.org/en/7.1.x/example/markers.html#registering-markers
90 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/langgraph/tests/__init__.py


--------------------------------------------------------------------------------
/libs/langgraph/tests/agents.py:
--------------------------------------------------------------------------------
 1 | from typing import Literal, Union
 2 | 
 3 | from pydantic import BaseModel
 4 | 
 5 | 
 6 | # define these objects to avoid importing langchain_core.agents
 7 | # and therefore avoid relying on core Pydantic version
 8 | class AgentAction(BaseModel):
 9 |     tool: str
10 |     tool_input: Union[str, dict]
11 |     log: str
12 |     type: Literal["AgentAction"] = "AgentAction"
13 | 
14 |     model_config = {
15 |         "json_schema_extra": {
16 |             "description": (
17 |                 """Represents a request to execute an action by an agent.
18 | 
19 | The action consists of the name of the tool to execute and the input to pass
20 | to the tool. The log is used to pass along extra information about the action."""
21 |             )
22 |         }
23 |     }
24 | 
25 | 
26 | class AgentFinish(BaseModel):
27 |     """Final return value of an ActionAgent.
28 | 
29 |     Agents return an AgentFinish when they have reached a stopping condition.
30 |     """
31 | 
32 |     return_values: dict
33 |     log: str
34 |     type: Literal["AgentFinish"] = "AgentFinish"
35 |     model_config = {
36 |         "json_schema_extra": {
37 |             "description": (
38 |                 """Final return value of an ActionAgent.
39 | 
40 | Agents return an AgentFinish when they have reached a stopping condition."""
41 |             )
42 |         }
43 |     }
44 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/any_int.py:
--------------------------------------------------------------------------------
1 | class AnyInt(int):
2 |     def __init__(self) -> None:
3 |         super().__init__()
4 | 
5 |     def __eq__(self, other: object) -> bool:
6 |         return isinstance(other, int)
7 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/any_str.py:
--------------------------------------------------------------------------------
 1 | import re
 2 | from typing import Any, Sequence, Union
 3 | 
 4 | from typing_extensions import Self
 5 | 
 6 | 
 7 | class FloatBetween(float):
 8 |     def __new__(cls, min_value: float, max_value: float) -> Self:
 9 |         return super().__new__(cls, min_value)
10 | 
11 |     def __init__(self, min_value: float, max_value: float) -> None:
12 |         super().__init__()
13 |         self.min_value = min_value
14 |         self.max_value = max_value
15 | 
16 |     def __eq__(self, other: object) -> bool:
17 |         return (
18 |             isinstance(other, float)
19 |             and other >= self.min_value
20 |             and other <= self.max_value
21 |         )
22 | 
23 |     def __hash__(self) -> int:
24 |         return hash((float(self), self.min_value, self.max_value))
25 | 
26 | 
27 | class AnyStr(str):
28 |     def __init__(self, prefix: Union[str, re.Pattern] = "") -> None:
29 |         super().__init__()
30 |         self.prefix = prefix
31 | 
32 |     def __eq__(self, other: object) -> bool:
33 |         return isinstance(other, str) and (
34 |             other.startswith(self.prefix)
35 |             if isinstance(self.prefix, str)
36 |             else self.prefix.match(other)
37 |         )
38 | 
39 |     def __hash__(self) -> int:
40 |         return hash((str(self), self.prefix))
41 | 
42 | 
43 | class AnyDict(dict):
44 |     def __init__(self, *args, **kwargs) -> None:
45 |         super().__init__(*args, **kwargs)
46 | 
47 |     def __eq__(self, other: object) -> bool:
48 |         if not isinstance(other, dict) or len(self) != len(other):
49 |             return False
50 |         for k, v in self.items():
51 |             if kk := next((kk for kk in other if kk == k), None):
52 |                 if v == other[kk]:
53 |                     continue
54 |                 else:
55 |                     return False
56 |         else:
57 |             return True
58 | 
59 | 
60 | class AnyVersion:
61 |     def __init__(self) -> None:
62 |         super().__init__()
63 | 
64 |     def __eq__(self, other: object) -> bool:
65 |         return isinstance(other, (str, int, float))
66 | 
67 |     def __hash__(self) -> int:
68 |         return hash(str(self))
69 | 
70 | 
71 | class UnsortedSequence:
72 |     def __init__(self, *values: Any) -> None:
73 |         self.seq = values
74 | 
75 |     def __eq__(self, value: object) -> bool:
76 |         return (
77 |             isinstance(value, Sequence)
78 |             and len(self.seq) == len(value)
79 |             and all(a in value for a in self.seq)
80 |         )
81 | 
82 |     def __hash__(self) -> int:
83 |         return hash(frozenset(self.seq))
84 | 
85 |     def __repr__(self) -> str:
86 |         return repr(self.seq)
87 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/compose-postgres.yml:
--------------------------------------------------------------------------------
 1 | name: langgraph-tests
 2 | services:
 3 |   postgres-test:
 4 |     image: postgres:16
 5 |     ports:
 6 |       - "5442:5432"
 7 |     environment:
 8 |       POSTGRES_DB: postgres
 9 |       POSTGRES_USER: postgres
10 |       POSTGRES_PASSWORD: postgres
11 |     healthcheck:
12 |       test: pg_isready -U postgres
13 |       start_period: 10s
14 |       timeout: 1s
15 |       retries: 5
16 |       interval: 60s
17 |       start_interval: 1s
18 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/fake_tracer.py:
--------------------------------------------------------------------------------
 1 | from typing import Any, Optional
 2 | from uuid import UUID
 3 | 
 4 | from langchain_core.messages.base import BaseMessage
 5 | from langchain_core.outputs.chat_generation import ChatGeneration
 6 | from langchain_core.outputs.llm_result import LLMResult
 7 | from langchain_core.tracers import BaseTracer, Run
 8 | 
 9 | 
10 | class FakeTracer(BaseTracer):
11 |     """Fake tracer that records LangChain execution.
12 |     It replaces run ids with deterministic UUIDs for snapshotting."""
13 | 
14 |     def __init__(self) -> None:
15 |         """Initialize the tracer."""
16 |         super().__init__()
17 |         self.runs: list[Run] = []
18 |         self.uuids_map: dict[UUID, UUID] = {}
19 |         self.uuids_generator = (
20 |             UUID(f"00000000-0000-4000-8000-{i:012}", version=4) for i in range(10000)
21 |         )
22 | 
23 |     def _replace_uuid(self, uuid: UUID) -> UUID:
24 |         if uuid not in self.uuids_map:
25 |             self.uuids_map[uuid] = next(self.uuids_generator)
26 |         return self.uuids_map[uuid]
27 | 
28 |     def _replace_message_id(self, maybe_message: Any) -> Any:
29 |         if isinstance(maybe_message, BaseMessage):
30 |             maybe_message.id = str(next(self.uuids_generator))
31 |         if isinstance(maybe_message, ChatGeneration):
32 |             maybe_message.message.id = str(next(self.uuids_generator))
33 |         if isinstance(maybe_message, LLMResult):
34 |             for i, gen_list in enumerate(maybe_message.generations):
35 |                 for j, gen in enumerate(gen_list):
36 |                     maybe_message.generations[i][j] = self._replace_message_id(gen)
37 |         if isinstance(maybe_message, dict):
38 |             for k, v in maybe_message.items():
39 |                 maybe_message[k] = self._replace_message_id(v)
40 |         if isinstance(maybe_message, list):
41 |             for i, v in enumerate(maybe_message):
42 |                 maybe_message[i] = self._replace_message_id(v)
43 | 
44 |         return maybe_message
45 | 
46 |     def _copy_run(self, run: Run) -> Run:
47 |         if run.dotted_order:
48 |             levels = run.dotted_order.split(".")
49 |             processed_levels = []
50 |             for level in levels:
51 |                 timestamp, run_id = level.split("Z")
52 |                 new_run_id = self._replace_uuid(UUID(run_id))
53 |                 processed_level = f"{timestamp}Z{new_run_id}"
54 |                 processed_levels.append(processed_level)
55 |             new_dotted_order = ".".join(processed_levels)
56 |         else:
57 |             new_dotted_order = None
58 |         return run.copy(
59 |             update={
60 |                 "id": self._replace_uuid(run.id),
61 |                 "parent_run_id": (
62 |                     self.uuids_map[run.parent_run_id] if run.parent_run_id else None
63 |                 ),
64 |                 "child_runs": [self._copy_run(child) for child in run.child_runs],
65 |                 "trace_id": self._replace_uuid(run.trace_id) if run.trace_id else None,
66 |                 "dotted_order": new_dotted_order,
67 |                 "inputs": self._replace_message_id(run.inputs),
68 |                 "outputs": self._replace_message_id(run.outputs),
69 |             }
70 |         )
71 | 
72 |     def _persist_run(self, run: Run) -> None:
73 |         """Persist a run."""
74 | 
75 |         self.runs.append(self._copy_run(run))
76 | 
77 |     def flattened_runs(self) -> list[Run]:
78 |         q = [] + self.runs
79 |         result = []
80 |         while q:
81 |             parent = q.pop()
82 |             result.append(parent)
83 |             if parent.child_runs:
84 |                 q.extend(parent.child_runs)
85 |         return result
86 | 
87 |     @property
88 |     def run_ids(self) -> list[Optional[UUID]]:
89 |         runs = self.flattened_runs()
90 |         uuids_map = {v: k for k, v in self.uuids_map.items()}
91 |         return [uuids_map.get(r.id) for r in runs]
92 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/messages.py:
--------------------------------------------------------------------------------
 1 | """Redefined messages as a work-around for pydantic issue with AnyStr.
 2 | 
 3 | The code below creates version of pydantic models
 4 | that will work in unit tests with AnyStr as id field
 5 | Please note that the `id` field is assigned AFTER the model is created
 6 | to workaround an issue with pydantic ignoring the __eq__ method on
 7 | subclassed strings.
 8 | """
 9 | 
10 | from typing import Any
11 | 
12 | from langchain_core.documents import Document
13 | from langchain_core.messages import AIMessage, AIMessageChunk, HumanMessage, ToolMessage
14 | 
15 | from tests.any_str import AnyStr
16 | 
17 | 
18 | def _AnyIdDocument(**kwargs: Any) -> Document:
19 |     """Create a document with an id field."""
20 |     message = Document(**kwargs)
21 |     message.id = AnyStr()
22 |     return message
23 | 
24 | 
25 | def _AnyIdAIMessage(**kwargs: Any) -> AIMessage:
26 |     """Create ai message with an any id field."""
27 |     message = AIMessage(**kwargs)
28 |     message.id = AnyStr()
29 |     return message
30 | 
31 | 
32 | def _AnyIdAIMessageChunk(**kwargs: Any) -> AIMessageChunk:
33 |     """Create ai message with an any id field."""
34 |     message = AIMessageChunk(**kwargs)
35 |     message.id = AnyStr()
36 |     return message
37 | 
38 | 
39 | def _AnyIdHumanMessage(**kwargs: Any) -> HumanMessage:
40 |     """Create a human message with an any id field."""
41 |     message = HumanMessage(**kwargs)
42 |     message.id = AnyStr()
43 |     return message
44 | 
45 | 
46 | def _AnyIdToolMessage(**kwargs: Any) -> ToolMessage:
47 |     """Create a tool message with an any id field."""
48 |     message = ToolMessage(**kwargs)
49 |     message.id = AnyStr()
50 |     return message
51 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/test_algo.py:
--------------------------------------------------------------------------------
 1 | from langgraph.checkpoint.base import empty_checkpoint
 2 | from langgraph.pregel.algo import prepare_next_tasks
 3 | from langgraph.pregel.manager import ChannelsManager
 4 | 
 5 | 
 6 | def test_prepare_next_tasks() -> None:
 7 |     config = {}
 8 |     processes = {}
 9 |     checkpoint = empty_checkpoint()
10 | 
11 |     with ChannelsManager({}, checkpoint, config) as (channels, managed):
12 |         assert (
13 |             prepare_next_tasks(
14 |                 checkpoint,
15 |                 {},
16 |                 processes,
17 |                 channels,
18 |                 managed,
19 |                 config,
20 |                 0,
21 |                 for_execution=False,
22 |             )
23 |             == {}
24 |         )
25 |         assert (
26 |             prepare_next_tasks(
27 |                 checkpoint,
28 |                 {},
29 |                 processes,
30 |                 channels,
31 |                 managed,
32 |                 config,
33 |                 0,
34 |                 for_execution=True,
35 |                 checkpointer=None,
36 |                 store=None,
37 |                 manager=None,
38 |             )
39 |             == {}
40 |         )
41 | 
42 |         # TODO: add more tests
43 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/test_channels.py:
--------------------------------------------------------------------------------
 1 | import operator
 2 | from typing import Sequence, Union
 3 | 
 4 | import pytest
 5 | 
 6 | from langgraph.channels.binop import BinaryOperatorAggregate
 7 | from langgraph.channels.last_value import LastValue
 8 | from langgraph.channels.topic import Topic
 9 | from langgraph.errors import EmptyChannelError, InvalidUpdateError
10 | 
11 | pytestmark = pytest.mark.anyio
12 | 
13 | 
14 | def test_last_value() -> None:
15 |     channel = LastValue(int).from_checkpoint(None)
16 |     assert channel.ValueType is int
17 |     assert channel.UpdateType is int
18 | 
19 |     with pytest.raises(EmptyChannelError):
20 |         channel.get()
21 |     with pytest.raises(InvalidUpdateError):
22 |         channel.update([5, 6])
23 | 
24 |     channel.update([3])
25 |     assert channel.get() == 3
26 |     channel.update([4])
27 |     assert channel.get() == 4
28 |     checkpoint = channel.checkpoint()
29 |     channel = LastValue(int).from_checkpoint(checkpoint)
30 |     assert channel.get() == 4
31 | 
32 | 
33 | def test_topic() -> None:
34 |     channel = Topic(str).from_checkpoint(None)
35 |     assert channel.ValueType is Sequence[str]
36 |     assert channel.UpdateType is Union[str, list[str]]
37 | 
38 |     assert channel.update(["a", "b"])
39 |     assert channel.get() == ["a", "b"]
40 |     assert channel.update([["c", "d"], "d"])
41 |     assert channel.get() == ["c", "d", "d"]
42 |     assert channel.update([])
43 |     with pytest.raises(EmptyChannelError):
44 |         channel.get()
45 |     assert not channel.update([]), "channel already empty"
46 |     assert channel.update(["e"])
47 |     assert channel.get() == ["e"]
48 |     checkpoint = channel.checkpoint()
49 |     channel = Topic(str).from_checkpoint(checkpoint)
50 |     assert channel.get() == ["e"]
51 |     channel_copy = Topic(str).from_checkpoint(checkpoint)
52 |     channel_copy.update(["f"])
53 |     assert channel_copy.get() == ["f"]
54 |     assert channel.get() == ["e"]
55 | 
56 | 
57 | def test_topic_accumulate() -> None:
58 |     channel = Topic(str, accumulate=True).from_checkpoint(None)
59 |     assert channel.ValueType is Sequence[str]
60 |     assert channel.UpdateType is Union[str, list[str]]
61 | 
62 |     assert channel.update(["a", "b"])
63 |     assert channel.get() == ["a", "b"]
64 |     assert channel.update(["b", ["c", "d"], "d"])
65 |     assert channel.get() == ["a", "b", "b", "c", "d", "d"]
66 |     assert not channel.update([])
67 |     assert channel.get() == ["a", "b", "b", "c", "d", "d"]
68 |     checkpoint = channel.checkpoint()
69 |     channel = Topic(str, accumulate=True).from_checkpoint(checkpoint)
70 |     assert channel.get() == ["a", "b", "b", "c", "d", "d"]
71 |     assert channel.update(["e"])
72 |     assert channel.get() == ["a", "b", "b", "c", "d", "d", "e"]
73 | 
74 | 
75 | def test_binop() -> None:
76 |     channel = BinaryOperatorAggregate(int, operator.add).from_checkpoint(None)
77 |     assert channel.ValueType is int
78 |     assert channel.UpdateType is int
79 | 
80 |     assert channel.get() == 0
81 | 
82 |     channel.update([1, 2, 3])
83 |     assert channel.get() == 6
84 |     channel.update([4])
85 |     assert channel.get() == 10
86 |     checkpoint = channel.checkpoint()
87 |     channel = BinaryOperatorAggregate(int, operator.add).from_checkpoint(checkpoint)
88 |     assert channel.get() == 10
89 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/test_interruption.py:
--------------------------------------------------------------------------------
 1 | from typing import TypedDict
 2 | 
 3 | import pytest
 4 | from pytest_mock import MockerFixture
 5 | 
 6 | from langgraph.graph import END, START, StateGraph
 7 | from tests.conftest import (
 8 |     ALL_CHECKPOINTERS_ASYNC,
 9 |     ALL_CHECKPOINTERS_SYNC,
10 |     awith_checkpointer,
11 | )
12 | 
13 | pytestmark = pytest.mark.anyio
14 | 
15 | 
16 | @pytest.mark.parametrize("checkpointer_name", ALL_CHECKPOINTERS_SYNC)
17 | def test_interruption_without_state_updates(
18 |     request: pytest.FixtureRequest, checkpointer_name: str, mocker: MockerFixture
19 | ) -> None:
20 |     """Test interruption without state updates. This test confirms that
21 |     interrupting doesn't require a state key having been updated in the prev step"""
22 | 
23 |     class State(TypedDict):
24 |         input: str
25 | 
26 |     def noop(_state):
27 |         pass
28 | 
29 |     builder = StateGraph(State)
30 |     builder.add_node("step_1", noop)
31 |     builder.add_node("step_2", noop)
32 |     builder.add_node("step_3", noop)
33 |     builder.add_edge(START, "step_1")
34 |     builder.add_edge("step_1", "step_2")
35 |     builder.add_edge("step_2", "step_3")
36 |     builder.add_edge("step_3", END)
37 | 
38 |     checkpointer = request.getfixturevalue(f"checkpointer_{checkpointer_name}")
39 |     graph = builder.compile(checkpointer=checkpointer, interrupt_after="*")
40 | 
41 |     initial_input = {"input": "hello world"}
42 |     thread = {"configurable": {"thread_id": "1"}}
43 | 
44 |     graph.invoke(initial_input, thread, debug=True)
45 |     assert graph.get_state(thread).next == ("step_2",)
46 | 
47 |     graph.invoke(None, thread, debug=True)
48 |     assert graph.get_state(thread).next == ("step_3",)
49 | 
50 |     graph.invoke(None, thread, debug=True)
51 |     assert graph.get_state(thread).next == ()
52 | 
53 | 
54 | @pytest.mark.parametrize("checkpointer_name", ALL_CHECKPOINTERS_ASYNC)
55 | async def test_interruption_without_state_updates_async(
56 |     checkpointer_name: str, mocker: MockerFixture
57 | ):
58 |     """Test interruption without state updates. This test confirms that
59 |     interrupting doesn't require a state key having been updated in the prev step"""
60 | 
61 |     class State(TypedDict):
62 |         input: str
63 | 
64 |     async def noop(_state):
65 |         pass
66 | 
67 |     builder = StateGraph(State)
68 |     builder.add_node("step_1", noop)
69 |     builder.add_node("step_2", noop)
70 |     builder.add_node("step_3", noop)
71 |     builder.add_edge(START, "step_1")
72 |     builder.add_edge("step_1", "step_2")
73 |     builder.add_edge("step_2", "step_3")
74 |     builder.add_edge("step_3", END)
75 | 
76 |     async with awith_checkpointer(checkpointer_name) as checkpointer:
77 |         graph = builder.compile(checkpointer=checkpointer, interrupt_after="*")
78 | 
79 |         initial_input = {"input": "hello world"}
80 |         thread = {"configurable": {"thread_id": "1"}}
81 | 
82 |         await graph.ainvoke(initial_input, thread, debug=True)
83 |         assert (await graph.aget_state(thread)).next == ("step_2",)
84 | 
85 |         await graph.ainvoke(None, thread, debug=True)
86 |         assert (await graph.aget_state(thread)).next == ("step_3",)
87 | 
88 |         await graph.ainvoke(None, thread, debug=True)
89 |         assert (await graph.aget_state(thread)).next == ()
90 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/test_io.py:
--------------------------------------------------------------------------------
 1 | from typing import Iterator
 2 | 
 3 | from langgraph.pregel.io import single
 4 | 
 5 | 
 6 | def test_single() -> None:
 7 |     closed = False
 8 | 
 9 |     def myiter() -> Iterator[int]:
10 |         try:
11 |             yield 1
12 |             yield 2
13 |         finally:
14 |             nonlocal closed
15 |             closed = True
16 | 
17 |     assert single(myiter()) == 1
18 |     assert closed
19 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/test_runnable.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from typing import Any
 4 | 
 5 | import pytest
 6 | 
 7 | from langgraph.store.base import BaseStore
 8 | from langgraph.types import StreamWriter
 9 | from langgraph.utils.runnable import RunnableCallable
10 | 
11 | pytestmark = pytest.mark.anyio
12 | 
13 | 
14 | def test_runnable_callable_func_accepts():
15 |     def sync_func(x: Any) -> str:
16 |         return f"{x}"
17 | 
18 |     async def async_func(x: Any) -> str:
19 |         return f"{x}"
20 | 
21 |     def func_with_store(x: Any, store: BaseStore) -> str:
22 |         return f"{x}"
23 | 
24 |     def func_with_writer(x: Any, writer: StreamWriter) -> str:
25 |         return f"{x}"
26 | 
27 |     async def afunc_with_store(x: Any, store: BaseStore) -> str:
28 |         return f"{x}"
29 | 
30 |     async def afunc_with_writer(x: Any, writer: StreamWriter) -> str:
31 |         return f"{x}"
32 | 
33 |     runnables = {
34 |         "sync": RunnableCallable(sync_func),
35 |         "async": RunnableCallable(func=None, afunc=async_func),
36 |         "with_store": RunnableCallable(func_with_store),
37 |         "with_writer": RunnableCallable(func_with_writer),
38 |         "awith_store": RunnableCallable(afunc_with_store),
39 |         "awith_writer": RunnableCallable(afunc_with_writer),
40 |     }
41 | 
42 |     expected_store = {"with_store": True, "awith_store": True}
43 |     expected_writer = {"with_writer": True, "awith_writer": True}
44 | 
45 |     for name, runnable in runnables.items():
46 |         assert runnable.func_accepts["writer"] == expected_writer.get(name, False)
47 |         assert runnable.func_accepts["store"] == expected_store.get(name, False)
48 | 
49 | 
50 | async def test_runnable_callable_basic():
51 |     def sync_func(x: Any) -> str:
52 |         return f"{x}"
53 | 
54 |     async def async_func(x: Any) -> str:
55 |         return f"{x}"
56 | 
57 |     runnable_sync = RunnableCallable(sync_func)
58 |     runnable_async = RunnableCallable(func=None, afunc=async_func)
59 | 
60 |     result_sync = runnable_sync.invoke("test")
61 |     assert result_sync == "test"
62 | 
63 |     # Test asynchronous ainvoke
64 |     result_async = await runnable_async.ainvoke("test")
65 |     assert result_async == "test"
66 | 


--------------------------------------------------------------------------------
/libs/langgraph/tests/test_tracing_interops.py:
--------------------------------------------------------------------------------
  1 | import json
  2 | import sys
  3 | import time
  4 | from typing import Any, Callable, Tuple, TypedDict, TypeVar
  5 | from unittest.mock import MagicMock
  6 | 
  7 | import langsmith as ls
  8 | import pytest
  9 | from langchain_core.runnables import RunnableConfig
 10 | from langchain_core.tracers import LangChainTracer
 11 | 
 12 | from langgraph.graph import StateGraph
 13 | 
 14 | pytestmark = pytest.mark.anyio
 15 | 
 16 | 
 17 | def _get_mock_client(**kwargs: Any) -> ls.Client:
 18 |     mock_session = MagicMock()
 19 |     return ls.Client(session=mock_session, api_key="test", **kwargs)
 20 | 
 21 | 
 22 | def _get_calls(
 23 |     mock_client: Any,
 24 |     verbs: set[str] = {"POST"},
 25 | ) -> list:
 26 |     return [
 27 |         c
 28 |         for c in mock_client.session.request.mock_calls
 29 |         if c.args and c.args[0] in verbs
 30 |     ]
 31 | 
 32 | 
 33 | T = TypeVar("T")
 34 | 
 35 | 
 36 | def wait_for(
 37 |     condition: Callable[[], Tuple[T, bool]],
 38 |     max_sleep_time: int = 10,
 39 |     sleep_time: int = 3,
 40 | ) -> T:
 41 |     """Wait for a condition to be true."""
 42 |     start_time = time.time()
 43 |     last_e = None
 44 |     while time.time() - start_time < max_sleep_time:
 45 |         try:
 46 |             res, cond = condition()
 47 |             if cond:
 48 |                 return res
 49 |         except Exception as e:
 50 |             last_e = e
 51 |             time.sleep(sleep_time)
 52 |     total_time = time.time() - start_time
 53 |     if last_e is not None:
 54 |         raise last_e
 55 |     raise ValueError(f"Callable did not return within {total_time}")
 56 | 
 57 | 
 58 | @pytest.mark.skip("This test times out in CI")
 59 | async def test_nested_tracing():
 60 |     lt_py_311 = sys.version_info < (3, 11)
 61 |     mock_client = _get_mock_client()
 62 | 
 63 |     class State(TypedDict):
 64 |         value: str
 65 | 
 66 |     @ls.traceable
 67 |     async def some_traceable(content: State):
 68 |         return await child_graph.ainvoke(content)
 69 | 
 70 |     async def parent_node(state: State, config: RunnableConfig) -> State:
 71 |         if lt_py_311:
 72 |             result = await some_traceable(state, langsmith_extra={"config": config})
 73 |         else:
 74 |             result = await some_traceable(state)
 75 |         return {"value": f"parent_{result['value']}"}
 76 | 
 77 |     async def child_node(state: State) -> State:
 78 |         return {"value": f"child_{state['value']}"}
 79 | 
 80 |     child_builder = StateGraph(State)
 81 |     child_builder.add_node(child_node)
 82 |     child_builder.add_edge("__start__", "child_node")
 83 |     child_graph = child_builder.compile().with_config(run_name="child_graph")
 84 | 
 85 |     parent_builder = StateGraph(State)
 86 |     parent_builder.add_node(parent_node)
 87 |     parent_builder.add_edge("__start__", "parent_node")
 88 |     parent_graph = parent_builder.compile()
 89 | 
 90 |     tracer = LangChainTracer(client=mock_client)
 91 |     result = await parent_graph.ainvoke({"value": "input"}, {"callbacks": [tracer]})
 92 | 
 93 |     assert result == {"value": "parent_child_input"}
 94 | 
 95 |     def get_posts():
 96 |         post_calls = _get_calls(mock_client, verbs={"POST"})
 97 | 
 98 |         posts = [p for c in post_calls for p in json.loads(c.kwargs["data"])["post"]]
 99 |         names = [p.get("name") for p in posts]
100 |         if "child_node" in names:
101 |             return posts, True
102 |         return None, False
103 | 
104 |     posts = wait_for(get_posts)
105 |     # If the callbacks weren't propagated correctly, we'd
106 |     # end up with broken dotted_orders
107 |     parent_run = next(data for data in posts if data["name"] == "parent_node")
108 |     child_run = next(data for data in posts if data["name"] == "child_graph")
109 |     traceable_run = next(data for data in posts if data["name"] == "some_traceable")
110 | 
111 |     assert child_run["dotted_order"].startswith(traceable_run["dotted_order"])
112 |     assert traceable_run["dotted_order"].startswith(parent_run["dotted_order"])
113 | 
114 |     assert child_run["parent_run_id"] == traceable_run["id"]
115 |     assert traceable_run["parent_run_id"] == parent_run["id"]
116 |     assert parent_run["trace_id"] == child_run["trace_id"] == traceable_run["trace_id"]
117 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2024 LangChain, Inc.
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: test test_watch lint format
 2 | 
 3 | ######################
 4 | # TESTING AND COVERAGE
 5 | ######################
 6 | 
 7 | start-services:
 8 | 	docker compose -f tests/compose.yml up -V --force-recreate --wait --remove-orphans
 9 | 
10 | stop-services:
11 | 	docker compose -f tests/compose.yml down
12 | 
13 | TEST_PATH ?= .
14 | 
15 | test:
16 | 	make start-services && poetry run pytest $(TEST_PATH); \
17 | 	EXIT_CODE=$$?; \
18 | 	make stop-services; \
19 | 	exit $$EXIT_CODE
20 | 
21 | test_watch:
22 | 	make start-services && poetry run ptw . -- -x $(TEST_PATH); \
23 | 	EXIT_CODE=$$?; \
24 | 	make stop-services; \
25 | 	exit $$EXIT_CODE
26 | 
27 | ######################
28 | # LINTING AND FORMATTING
29 | ######################
30 | 
31 | # Define a variable for Python and notebook files.
32 | PYTHON_FILES=.
33 | MYPY_CACHE=.mypy_cache
34 | lint format: PYTHON_FILES=.
35 | lint_diff format_diff: PYTHON_FILES=$(shell git diff --name-only --relative --diff-filter=d main . | grep -E '\.py$$|\.ipynb$$')
36 | lint_package: PYTHON_FILES=langgraph
37 | lint_tests: PYTHON_FILES=tests
38 | lint_tests: MYPY_CACHE=.mypy_cache_test
39 | 
40 | lint lint_diff lint_package lint_tests:
41 | 	poetry run ruff check .
42 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff format $(PYTHON_FILES) --diff
43 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff check --select I $(PYTHON_FILES)
44 | 	[ "$(PYTHON_FILES)" = "" ] || mkdir -p $(MYPY_CACHE) || poetry run mypy $(PYTHON_FILES) --cache-dir $(MYPY_CACHE)
45 | 
46 | format format_diff:
47 | 	poetry run ruff format $(PYTHON_FILES)
48 | 	poetry run ruff check --select I --fix $(PYTHON_FILES)
49 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/scheduler-kafka/langgraph-distributed.png


--------------------------------------------------------------------------------
/libs/scheduler-kafka/langgraph/scheduler/kafka/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/scheduler-kafka/langgraph/scheduler/kafka/__init__.py


--------------------------------------------------------------------------------
/libs/scheduler-kafka/langgraph/scheduler/kafka/default_async.py:
--------------------------------------------------------------------------------
 1 | import aiokafka
 2 | 
 3 | 
 4 | class DefaultAsyncConsumer(aiokafka.AIOKafkaConsumer):
 5 |     pass
 6 | 
 7 | 
 8 | class DefaultAsyncProducer(aiokafka.AIOKafkaProducer):
 9 |     pass
10 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/langgraph/scheduler/kafka/default_sync.py:
--------------------------------------------------------------------------------
 1 | import concurrent.futures
 2 | from typing import Optional, Sequence
 3 | 
 4 | from kafka import KafkaConsumer, KafkaProducer
 5 | from langgraph.scheduler.kafka.types import ConsumerRecord, TopicPartition
 6 | 
 7 | 
 8 | class DefaultConsumer(KafkaConsumer):
 9 |     def getmany(
10 |         self, timeout_ms: int, max_records: int
11 |     ) -> dict[TopicPartition, Sequence[ConsumerRecord]]:
12 |         return self.poll(timeout_ms=timeout_ms, max_records=max_records)
13 | 
14 |     def __enter__(self):
15 |         return self
16 | 
17 |     def __exit__(self, *args):
18 |         self.close()
19 | 
20 | 
21 | class DefaultProducer(KafkaProducer):
22 |     def send(
23 |         self,
24 |         topic: str,
25 |         *,
26 |         key: Optional[bytes] = None,
27 |         value: Optional[bytes] = None,
28 |     ) -> concurrent.futures.Future:
29 |         fut = concurrent.futures.Future()
30 |         kfut = super().send(topic, key=key, value=value)
31 |         kfut.add_callback(fut.set_result)
32 |         kfut.add_errback(fut.set_exception)
33 |         return fut
34 | 
35 |     def __enter__(self):
36 |         return self
37 | 
38 |     def __exit__(self, *args):
39 |         self.close()
40 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/langgraph/scheduler/kafka/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/scheduler-kafka/langgraph/scheduler/kafka/py.typed


--------------------------------------------------------------------------------
/libs/scheduler-kafka/langgraph/scheduler/kafka/retry.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import logging
 3 | import random
 4 | import time
 5 | from typing import Awaitable, Callable, Optional
 6 | 
 7 | from typing_extensions import ParamSpec
 8 | 
 9 | from langgraph.types import RetryPolicy
10 | 
11 | logger = logging.getLogger(__name__)
12 | P = ParamSpec("P")
13 | 
14 | 
15 | def retry(
16 |     retry_policy: Optional[RetryPolicy],
17 |     func: Callable[P, None],
18 |     *args: P.args,
19 |     **kwargs: P.kwargs,
20 | ) -> None:
21 |     """Run a task asynchronously with retries."""
22 |     interval = retry_policy.initial_interval if retry_policy else 0
23 |     attempts = 0
24 |     while True:
25 |         try:
26 |             func(*args, **kwargs)
27 |             # if successful, end
28 |             break
29 |         except Exception as exc:
30 |             if retry_policy is None:
31 |                 raise
32 |             # increment attempts
33 |             attempts += 1
34 |             # check if we should retry
35 |             if callable(retry_policy.retry_on):
36 |                 if not retry_policy.retry_on(exc):
37 |                     raise
38 |             elif not isinstance(exc, retry_policy.retry_on):
39 |                 raise
40 |             # check if we should give up
41 |             if attempts >= retry_policy.max_attempts:
42 |                 raise
43 |             # sleep before retrying
44 |             interval = min(
45 |                 retry_policy.max_interval,
46 |                 interval * retry_policy.backoff_factor,
47 |             )
48 |             time.sleep(
49 |                 interval + random.uniform(0, 1) if retry_policy.jitter else interval
50 |             )
51 |             # log the retry
52 |             logger.info(
53 |                 f"Retrying function {func} with {args} after {interval:.2f} seconds (attempt {attempts}) after {exc.__class__.__name__} {exc}",
54 |                 exc_info=exc,
55 |             )
56 | 
57 | 
58 | async def aretry(
59 |     retry_policy: Optional[RetryPolicy],
60 |     func: Callable[P, Awaitable[None]],
61 |     *args: P.args,
62 |     **kwargs: P.kwargs,
63 | ) -> None:
64 |     """Run a task asynchronously with retries."""
65 |     interval = retry_policy.initial_interval if retry_policy else 0
66 |     attempts = 0
67 |     while True:
68 |         try:
69 |             await func(*args, **kwargs)
70 |             # if successful, end
71 |             break
72 |         except Exception as exc:
73 |             if retry_policy is None:
74 |                 raise
75 |             # increment attempts
76 |             attempts += 1
77 |             # check if we should retry
78 |             if callable(retry_policy.retry_on):
79 |                 if not retry_policy.retry_on(exc):
80 |                     raise
81 |             elif not isinstance(exc, retry_policy.retry_on):
82 |                 raise
83 |             # check if we should give up
84 |             if attempts >= retry_policy.max_attempts:
85 |                 raise
86 |             # sleep before retrying
87 |             interval = min(
88 |                 retry_policy.max_interval,
89 |                 interval * retry_policy.backoff_factor,
90 |             )
91 |             await asyncio.sleep(
92 |                 interval + random.uniform(0, 1) if retry_policy.jitter else interval
93 |             )
94 |             # log the retry
95 |             logger.info(
96 |                 f"Retrying function {func} with {args} after {interval:.2f} seconds (attempt {attempts}) after {exc.__class__.__name__} {exc}",
97 |                 exc_info=exc,
98 |             )
99 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/langgraph/scheduler/kafka/serde.py:
--------------------------------------------------------------------------------
 1 | from typing import Any
 2 | 
 3 | import orjson
 4 | 
 5 | from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer
 6 | 
 7 | SERIALIZER = JsonPlusSerializer()
 8 | 
 9 | 
10 | def loads(v: bytes) -> Any:
11 |     return SERIALIZER.loads(v)
12 | 
13 | 
14 | def dumps(v: Any) -> bytes:
15 |     return orjson.dumps(v, default=_default)
16 | 
17 | 
18 | def _default(v: Any) -> Any:
19 |     # things we don't know how to serialize (eg. functions) ignore
20 |     return None
21 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/langgraph/scheduler/kafka/types.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import concurrent.futures
 3 | from typing import Any, NamedTuple, Optional, Protocol, Sequence, TypedDict, Union
 4 | 
 5 | from langchain_core.runnables import RunnableConfig
 6 | 
 7 | 
 8 | class Topics(NamedTuple):
 9 |     ceo: str
10 |     executor: str
11 |     error: str
12 | 
13 | 
14 | class Sendable(TypedDict):
15 |     topic: str
16 |     value: Optional[Any]
17 |     key: Optional[Any]
18 | 
19 | 
20 | class MessageToceo(TypedDict):
21 |     input: Optional[dict[str, Any]]
22 |     config: RunnableConfig
23 |     finally_send: Optional[Sequence[Sendable]]
24 | 
25 | 
26 | class ExecutorTask(TypedDict):
27 |     id: Optional[str]
28 |     path: tuple[Union[str, int], ...]
29 | 
30 | 
31 | class MessageToExecutor(TypedDict):
32 |     config: RunnableConfig
33 |     task: ExecutorTask
34 |     finally_send: Optional[Sequence[Sendable]]
35 | 
36 | 
37 | class ErrorMessage(TypedDict):
38 |     topic: str
39 |     error: str
40 |     msg: Union[MessageToExecutor, MessageToceo]
41 | 
42 | 
43 | class TopicPartition(Protocol):
44 |     topic: str
45 |     partition: int
46 | 
47 | 
48 | class ConsumerRecord(Protocol):
49 |     topic: str
50 |     "The topic this record is received from"
51 |     partition: int
52 |     "The partition from which this record is received"
53 |     offset: int
54 |     "The position of this record in the corresponding Kafka partition."
55 |     timestamp: int
56 |     "The timestamp of this record"
57 |     timestamp_type: int
58 |     "The timestamp type of this record"
59 |     key: Optional[bytes]
60 |     "The key (or `None` if no key is specified)"
61 |     value: Optional[bytes]
62 |     "The value"
63 | 
64 | 
65 | class Consumer(Protocol):
66 |     def getmany(
67 |         self, timeout_ms: int, max_records: int
68 |     ) -> dict[TopicPartition, Sequence[ConsumerRecord]]: ...
69 | 
70 |     def commit(self) -> None: ...
71 | 
72 | 
73 | class AsyncConsumer(Protocol):
74 |     async def getmany(
75 |         self, timeout_ms: int, max_records: int
76 |     ) -> dict[TopicPartition, Sequence[ConsumerRecord]]: ...
77 | 
78 |     async def commit(self) -> None: ...
79 | 
80 | 
81 | class Producer(Protocol):
82 |     def send(
83 |         self,
84 |         topic: str,
85 |         *,
86 |         key: Optional[bytes] = None,
87 |         value: Optional[bytes] = None,
88 |     ) -> concurrent.futures.Future: ...
89 | 
90 | 
91 | class AsyncProducer(Protocol):
92 |     async def send(
93 |         self,
94 |         topic: str,
95 |         *,
96 |         key: Optional[bytes] = None,
97 |         value: Optional[bytes] = None,
98 |     ) -> asyncio.Future: ...
99 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph-scheduler-kafka"
 3 | version = "1.0.0"
 4 | description = "Library with Kafka-based work scheduler."
 5 | authors = []
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | repository = "https://www.github.com/langchain-ai/langgraph"
 9 | packages = [{ include = "langgraph" }]
10 | 
11 | [tool.poetry.dependencies]
12 | python = "^3.9.0,<4.0"
13 | orjson = "^3.10.7"
14 | crc32c = "^2.7.post1"
15 | aiokafka = "^0.11.0"
16 | langgraph = "^0.2.19"
17 | 
18 | [tool.poetry.group.dev.dependencies]
19 | ruff = "^0.6.2"
20 | codespell = "^2.2.0"
21 | pytest = "^7.2.1"
22 | pytest-mock = "^3.11.1"
23 | pytest-watcher = "^0.4.1"
24 | mypy = "^1.10.0"
25 | langgraph = {path = "../langgraph", develop = true}
26 | langgraph-checkpoint-postgres = {path = "../checkpoint-postgres", develop = true}
27 | langgraph-checkpoint = {path = "../checkpoint", develop = true}
28 | kafka-python-ng = "^2.2.2"
29 | 
30 | [tool.pytest.ini_options]
31 | # --strict-markers will raise errors on unknown marks.
32 | # https://docs.pytest.org/en/7.1.x/how-to/mark.html#raising-errors-on-unknown-marks
33 | #
34 | # https://docs.pytest.org/en/7.1.x/reference/reference.html
35 | # --strict-config       any warnings encountered while parsing the `pytest`
36 | #                       section of the configuration file raise errors.
37 | addopts = "--strict-markers --strict-config --durations=5 -vv"
38 | 
39 | 
40 | [build-system]
41 | requires = ["poetry-core"]
42 | build-backend = "poetry.core.masonry.api"
43 | 
44 | [tool.ruff]
45 | lint.select = [
46 |   "E",  # pycodestyle
47 |   "F",  # Pyflakes
48 |   "UP", # pyupgrade
49 |   "B",  # flake8-bugbear
50 |   "I",  # isort
51 | ]
52 | lint.ignore = ["E501", "B008", "UP007", "UP006"]
53 | 
54 | [tool.pytest-watcher]
55 | now = true
56 | delay = 0.1
57 | runner_args = ["--ff", "-v", "--tb", "short", "-s"]
58 | patterns = ["*.py"]
59 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/scheduler-kafka/tests/__init__.py


--------------------------------------------------------------------------------
/libs/scheduler-kafka/tests/any.py:
--------------------------------------------------------------------------------
 1 | import re
 2 | from typing import Union
 3 | 
 4 | 
 5 | class AnyStr(str):
 6 |     def __init__(self, prefix: Union[str, re.Pattern] = "") -> None:
 7 |         super().__init__()
 8 |         self.prefix = prefix
 9 | 
10 |     def __eq__(self, other: object) -> bool:
11 |         return isinstance(other, str) and (
12 |             other.startswith(self.prefix)
13 |             if isinstance(self.prefix, str)
14 |             else self.prefix.match(other)
15 |         )
16 | 
17 |     def __hash__(self) -> int:
18 |         return hash((str(self), self.prefix))
19 | 
20 | 
21 | class AnyDict(dict):
22 |     def __init__(self, *args, **kwargs) -> None:
23 |         super().__init__(*args, **kwargs)
24 | 
25 |     def __eq__(self, other: object) -> bool:
26 |         if not self and isinstance(other, dict):
27 |             return True
28 |         if not isinstance(other, dict) or len(self) != len(other):
29 |             return False
30 |         for k, v in self.items():
31 |             if kk := next((kk for kk in other if kk == k), None):
32 |                 if v == other[kk]:
33 |                     continue
34 |                 else:
35 |                     return False
36 |         else:
37 |             return True
38 | 
39 | 
40 | class AnyList(list):
41 |     def __init__(self, *args, **kwargs) -> None:
42 |         super().__init__(*args, **kwargs)
43 | 
44 |     def __eq__(self, other: object) -> bool:
45 |         if not self and isinstance(other, list):
46 |             return True
47 |         if not isinstance(other, list) or len(self) != len(other):
48 |             return False
49 |         for i, v in enumerate(self):
50 |             if v == other[i]:
51 |                 continue
52 |             else:
53 |                 return False
54 |         else:
55 |             return True
56 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/tests/compose.yml:
--------------------------------------------------------------------------------
 1 | name: scheduler-kafka-tests
 2 | services:
 3 |   broker:
 4 |     image: apache/kafka:latest
 5 |     ports:
 6 |       - "9092:9092"
 7 |   postgres:
 8 |     image: postgres:16
 9 |     ports:
10 |       - "5443:5432"
11 |     environment:
12 |       POSTGRES_DB: postgres
13 |       POSTGRES_USER: postgres
14 |       POSTGRES_PASSWORD: postgres
15 |     healthcheck:
16 |       test: pg_isready -U postgres
17 |       start_period: 10s
18 |       timeout: 1s
19 |       retries: 5
20 |       interval: 60s
21 |       start_interval: 1s
22 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/tests/conftest.py:
--------------------------------------------------------------------------------
 1 | from typing import AsyncIterator, Iterator
 2 | from uuid import uuid4
 3 | 
 4 | import kafka.admin
 5 | import pytest
 6 | from psycopg import AsyncConnection, Connection
 7 | from psycopg_pool import AsyncConnectionPool, ConnectionPool
 8 | 
 9 | from langgraph.checkpoint.postgres import PostgresSaver
10 | from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
11 | from langgraph.scheduler.kafka.types import Topics
12 | 
13 | DEFAULT_POSTGRES_URI = "postgres://postgres:postgres@localhost:5443/"
14 | 
15 | 
16 | @pytest.fixture
17 | def anyio_backend():
18 |     return "asyncio"
19 | 
20 | 
21 | @pytest.fixture
22 | def topics() -> Iterator[Topics]:
23 |     o = f"test_o_{uuid4().hex[:16]}"
24 |     e = f"test_e_{uuid4().hex[:16]}"
25 |     z = f"test_z_{uuid4().hex[:16]}"
26 |     admin = kafka.admin.KafkaAdminClient()
27 |     # create topics
28 |     admin.create_topics(
29 |         [
30 |             kafka.admin.NewTopic(name=o, num_partitions=1, replication_factor=1),
31 |             kafka.admin.NewTopic(name=e, num_partitions=1, replication_factor=1),
32 |             kafka.admin.NewTopic(name=z, num_partitions=1, replication_factor=1),
33 |         ]
34 |     )
35 |     # yield topics
36 |     yield Topics(ceo=o, executor=e, error=z)
37 |     # delete topics
38 |     admin.delete_topics([o, e, z])
39 |     admin.close()
40 | 
41 | 
42 | @pytest.fixture
43 | async def acheckpointer() -> AsyncIterator[AsyncPostgresSaver]:
44 |     database = f"test_{uuid4().hex[:16]}"
45 |     # create unique db
46 |     async with await AsyncConnection.connect(
47 |         DEFAULT_POSTGRES_URI, autocommit=True
48 |     ) as conn:
49 |         await conn.execute(f"CREATE DATABASE {database}")
50 |     try:
51 |         # yield checkpointer
52 |         async with AsyncConnectionPool(
53 |             DEFAULT_POSTGRES_URI + database, max_size=10, kwargs={"autocommit": True}
54 |         ) as pool:
55 |             checkpointer = AsyncPostgresSaver(pool)
56 |             await checkpointer.setup()
57 |             yield checkpointer
58 |     finally:
59 |         # drop unique db
60 |         async with await AsyncConnection.connect(
61 |             DEFAULT_POSTGRES_URI, autocommit=True
62 |         ) as conn:
63 |             await conn.execute(f"DROP DATABASE {database}")
64 | 
65 | 
66 | @pytest.fixture
67 | def checkpointer() -> Iterator[PostgresSaver]:
68 |     database = f"test_{uuid4().hex[:16]}"
69 |     # create unique db
70 |     with Connection.connect(DEFAULT_POSTGRES_URI, autocommit=True) as conn:
71 |         conn.execute(f"CREATE DATABASE {database}")
72 |     try:
73 |         # yield checkpointer
74 |         with ConnectionPool(
75 |             DEFAULT_POSTGRES_URI + database, max_size=10, kwargs={"autocommit": True}
76 |         ) as pool:
77 |             checkpointer = PostgresSaver(pool)
78 |             checkpointer.setup()
79 |             yield checkpointer
80 |     finally:
81 |         # drop unique db
82 |         with Connection.connect(DEFAULT_POSTGRES_URI, autocommit=True) as conn:
83 |             conn.execute(f"DROP DATABASE {database}")
84 | 


--------------------------------------------------------------------------------
/libs/scheduler-kafka/tests/messages.py:
--------------------------------------------------------------------------------
 1 | """Redefined messages as a work-around for pydantic issue with AnyStr.
 2 | 
 3 | The code below creates version of pydantic models
 4 | that will work in unit tests with AnyStr as id field
 5 | Please note that the `id` field is assigned AFTER the model is created
 6 | to workaround an issue with pydantic ignoring the __eq__ method on
 7 | subclassed strings.
 8 | """
 9 | 
10 | from typing import Any
11 | 
12 | from langchain_core.messages import AIMessage, HumanMessage
13 | 
14 | from tests.any import AnyStr
15 | 
16 | 
17 | def _AnyIdAIMessage(**kwargs: Any) -> AIMessage:
18 |     """Create ai message with an any id field."""
19 |     message = AIMessage(**kwargs)
20 |     message.id = AnyStr()
21 |     return message
22 | 
23 | 
24 | def _AnyIdHumanMessage(**kwargs: Any) -> HumanMessage:
25 |     """Create a human message with an any id field."""
26 |     message = HumanMessage(**kwargs)
27 |     message.id = AnyStr()
28 |     return message
29 | 


--------------------------------------------------------------------------------
/libs/sdk-js/.gitignore:
--------------------------------------------------------------------------------
 1 | index.cjs
 2 | index.js
 3 | index.d.ts
 4 | index.d.cts
 5 | client.cjs
 6 | client.js
 7 | client.d.ts
 8 | client.d.cts
 9 | node_modules
10 | dist
11 | .yarn
12 | 


--------------------------------------------------------------------------------
/libs/sdk-js/.prettierrc:
--------------------------------------------------------------------------------
1 | {}
2 | 


--------------------------------------------------------------------------------
/libs/sdk-js/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2024 LangChain, Inc.
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/libs/sdk-js/README.md:
--------------------------------------------------------------------------------
 1 | # LangGraph JS/TS SDK
 2 | 
 3 | This repository contains the JS/TS SDK for interacting with the LangGraph REST API.
 4 | 
 5 | ## Quick Start
 6 | 
 7 | To get started with the JS/TS SDK, [install the package](https://www.npmjs.com/package/@langchain/langgraph-sdk)
 8 | 
 9 | ```bash
10 | yarn add @langchain/langgraph-sdk
11 | ```
12 | 
13 | You will need a running LangGraph API server. If you're running a server locally using `langgraph-cli`, SDK will automatically point at `http://localhost:8123`, otherwise
14 | you would need to specify the server URL when creating a client.
15 | 
16 | ```js
17 | import { Client } from "@langchain/langgraph-sdk";
18 | 
19 | const client = new Client();
20 | 
21 | // List all assistants
22 | const assistants = await client.assistants.search({
23 |   metadata: null,
24 |   offset: 0,
25 |   limit: 10,
26 | });
27 | 
28 | // We auto-create an assistant for each graph you register in config.
29 | const agent = assistants[0];
30 | 
31 | // Start a new thread
32 | const thread = await client.threads.create();
33 | 
34 | // Start a streaming run
35 | const messages = [{ role: "human", content: "what's the weather in la" }];
36 | 
37 | const streamResponse = client.runs.stream(
38 |   thread["thread_id"],
39 |   agent["assistant_id"],
40 |   {
41 |     input: { messages },
42 |   }
43 | );
44 | 
45 | for await (const chunk of streamResponse) {
46 |   console.log(chunk);
47 | }
48 | ```
49 | 
50 | ## Documentation
51 | 
52 | To generate documentation, run the following commands:
53 | 
54 | 1. Generate docs.
55 | 
56 |         yarn typedoc
57 | 
58 | 1. Consolidate doc files into one markdown file.
59 | 
60 |         npx concat-md --decrease-title-levels --ignore=js_ts_sdk_ref.md --start-title-level-at 2 docs > docs/js_ts_sdk_ref.md
61 | 
62 | 1. Copy `js_ts_sdk_ref.md` to MkDocs directory.
63 | 
64 |         cp docs/js_ts_sdk_ref.md ../../docs/docs/cloud/reference/sdk/js_ts_sdk_ref.md
65 | 


--------------------------------------------------------------------------------
/libs/sdk-js/langchain.config.js:
--------------------------------------------------------------------------------
 1 | import { resolve, dirname } from "node:path";
 2 | import { fileURLToPath } from "node:url";
 3 | 
 4 | /**
 5 |  * @param {string} relativePath
 6 |  * @returns {string}
 7 |  */
 8 | function abs(relativePath) {
 9 |   return resolve(dirname(fileURLToPath(import.meta.url)), relativePath);
10 | }
11 | 
12 | export const config = {
13 |   internals: [],
14 |   entrypoints: { index: "index", client: "client" },
15 |   tsConfigPath: resolve("./tsconfig.json"),
16 |   cjsSource: "./dist-cjs",
17 |   cjsDestination: "./dist",
18 |   abs,
19 | };
20 | 


--------------------------------------------------------------------------------
/libs/sdk-js/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "@langchain/langgraph-sdk",
 3 |   "version": "0.0.32",
 4 |   "description": "Client library for interacting with the LangGraph API",
 5 |   "type": "module",
 6 |   "packageManager": "yarn@1.22.19",
 7 |   "scripts": {
 8 |     "clean": "rm -rf dist/ dist-cjs/",
 9 |     "build": "yarn clean && yarn lc_build --create-entrypoints --pre --tree-shaking",
10 |     "prepublish": "yarn run build",
11 |     "format": "prettier --write src",
12 |     "lint": "prettier --check src && tsc --noEmit"
13 |   },
14 |   "main": "index.js",
15 |   "license": "MIT",
16 |   "dependencies": {
17 |     "@types/json-schema": "^7.0.15",
18 |     "p-queue": "^6.6.2",
19 |     "p-retry": "4",
20 |     "uuid": "^9.0.0"
21 |   },
22 |   "devDependencies": {
23 |     "@langchain/scripts": "^0.1.4",
24 |     "@tsconfig/recommended": "^1.0.2",
25 |     "@types/node": "^20.12.12",
26 |     "@types/uuid": "^9.0.1",
27 |     "concat-md": "^0.5.1",
28 |     "prettier": "^3.2.5",
29 |     "typedoc": "^0.26.1",
30 |     "typedoc-plugin-markdown": "^4.1.0",
31 |     "typescript": "^5.4.5"
32 |   },
33 |   "exports": {
34 |     ".": {
35 |       "types": {
36 |         "import": "./index.d.ts",
37 |         "require": "./index.d.cts",
38 |         "default": "./index.d.ts"
39 |       },
40 |       "import": "./index.js",
41 |       "require": "./index.cjs"
42 |     },
43 |     "./client": {
44 |       "types": {
45 |         "import": "./client.d.ts",
46 |         "require": "./client.d.cts",
47 |         "default": "./client.d.ts"
48 |       },
49 |       "import": "./client.js",
50 |       "require": "./client.cjs"
51 |     },
52 |     "./package.json": "./package.json"
53 |   },
54 |   "files": [
55 |     "dist/",
56 |     "index.cjs",
57 |     "index.js",
58 |     "index.d.ts",
59 |     "index.d.cts",
60 |     "client.cjs",
61 |     "client.js",
62 |     "client.d.ts",
63 |     "client.d.cts"
64 |   ]
65 | }
66 | 


--------------------------------------------------------------------------------
/libs/sdk-js/src/index.ts:
--------------------------------------------------------------------------------
 1 | export { Client } from "./client.js";
 2 | 
 3 | export type {
 4 |   Assistant,
 5 |   AssistantVersion,
 6 |   AssistantGraph,
 7 |   Config,
 8 |   DefaultValues,
 9 |   GraphSchema,
10 |   Metadata,
11 |   Run,
12 |   Thread,
13 |   ThreadTask,
14 |   ThreadState,
15 |   ThreadStatus,
16 |   Cron,
17 |   Checkpoint,
18 |   Interrupt,
19 | } from "./schema.js";
20 | 
21 | export type { OnConflictBehavior, Command } from "./types.js";
22 | 


--------------------------------------------------------------------------------
/libs/sdk-js/src/utils/env.ts:
--------------------------------------------------------------------------------
 1 | export function getEnvironmentVariable(name: string): string | undefined {
 2 |   // Certain setups (Deno, frontend) will throw an error if you try to access environment variables
 3 |   try {
 4 |     return typeof process !== "undefined"
 5 |       ? // eslint-disable-next-line no-process-env
 6 |         process.env?.[name]
 7 |       : undefined;
 8 |   } catch (e) {
 9 |     return undefined;
10 |   }
11 | }
12 | 


--------------------------------------------------------------------------------
/libs/sdk-js/src/utils/eventsource-parser/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2024 Espen Hovlandsdal <espen@hovlandsdal.com>
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.


--------------------------------------------------------------------------------
/libs/sdk-js/src/utils/eventsource-parser/index.ts:
--------------------------------------------------------------------------------
 1 | // From https://github.com/rexxars/eventsource-parser
 2 | // Inlined due to CJS import issues
 3 | 
 4 | export { createParser } from "./parse.js";
 5 | export type {
 6 |   EventSourceParseCallback,
 7 |   EventSourceParser,
 8 |   ParsedEvent,
 9 |   ParseEvent,
10 |   ReconnectInterval,
11 | } from "./types.js";
12 | 


--------------------------------------------------------------------------------
/libs/sdk-js/src/utils/eventsource-parser/stream.ts:
--------------------------------------------------------------------------------
 1 | import { createParser } from "./parse.js";
 2 | import type { EventSourceParser, ParsedEvent } from "./types.js";
 3 | 
 4 | /**
 5 |  * A TransformStream that ingests a stream of strings and produces a stream of ParsedEvents.
 6 |  *
 7 |  * @example
 8 |  * ```
 9 |  * const eventStream =
10 |  *   response.body
11 |  *     .pipeThrough(new TextDecoderStream())
12 |  *     .pipeThrough(new EventSourceParserStream())
13 |  * ```
14 |  * @public
15 |  */
16 | export class EventSourceParserStream extends TransformStream<
17 |   string,
18 |   ParsedEvent
19 | > {
20 |   constructor() {
21 |     let parser!: EventSourceParser;
22 | 
23 |     super({
24 |       start(controller) {
25 |         parser = createParser((event: any) => {
26 |           if (event.type === "event") {
27 |             controller.enqueue(event);
28 |           }
29 |         });
30 |       },
31 |       transform(chunk) {
32 |         parser.feed(chunk);
33 |       },
34 |     });
35 |   }
36 | }
37 | 
38 | export type { ParsedEvent } from "./types.js";
39 | 


--------------------------------------------------------------------------------
/libs/sdk-js/src/utils/eventsource-parser/types.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * EventSource parser instance.
 3 |  *
 4 |  * Needs to be reset between reconnections/when switching data source, using the `reset()` method.
 5 |  *
 6 |  * @public
 7 |  */
 8 | export interface EventSourceParser {
 9 |   /**
10 |    * Feeds the parser another chunk. The method _does not_ return a parsed message.
11 |    * Instead, if the chunk was a complete message (or completed a previously incomplete message),
12 |    * it will invoke the `onParse` callback used to create the parsers.
13 |    *
14 |    * @param chunk - The chunk to parse. Can be a partial, eg in the case of streaming messages.
15 |    * @public
16 |    */
17 |   feed(chunk: string): void;
18 | 
19 |   /**
20 |    * Resets the parser state. This is required when you have a new stream of messages -
21 |    * for instance in the case of a client being disconnected and reconnecting.
22 |    *
23 |    * @public
24 |    */
25 |   reset(): void;
26 | }
27 | 
28 | /**
29 |  * A parsed EventSource event
30 |  *
31 |  * @public
32 |  */
33 | export interface ParsedEvent {
34 |   /**
35 |    * Differentiates the type from reconnection intervals and other types of messages
36 |    * Not to be confused with `event`.
37 |    */
38 |   type: "event";
39 | 
40 |   /**
41 |    * The event type sent from the server. Note that this differs from the browser `EventSource`
42 |    * implementation in that browsers will default this to `message`, whereas this parser will
43 |    * leave this as `undefined` if not explicitly declared.
44 |    */
45 |   event?: string;
46 | 
47 |   /**
48 |    * ID of the message, if any was provided by the server. Can be used by clients to keep the
49 |    * last received message ID in sync when reconnecting.
50 |    */
51 |   id?: string;
52 | 
53 |   /**
54 |    * The data received for this message
55 |    */
56 |   data: string;
57 | }
58 | 
59 | /**
60 |  * An event emitted from the parser when the server sends a value in the `retry` field,
61 |  * indicating how many seconds the client should wait before attempting to reconnect.
62 |  *
63 |  * @public
64 |  */
65 | export interface ReconnectInterval {
66 |   /**
67 |    * Differentiates the type from `event` and other types of messages
68 |    */
69 |   type: "reconnect-interval";
70 | 
71 |   /**
72 |    * Number of seconds to wait before reconnecting. Note that the parser does not care about
73 |    * this value at all - it only emits the value for clients to use.
74 |    */
75 |   value: number;
76 | }
77 | 
78 | /**
79 |  * The different types of messages the parsed can emit to the `onParse` callback
80 |  *
81 |  * @public
82 |  */
83 | export type ParseEvent = ParsedEvent | ReconnectInterval;
84 | 
85 | /**
86 |  * Callback passed as the `onParse` callback to a parser
87 |  *
88 |  * @public
89 |  */
90 | export type EventSourceParseCallback = (event: ParseEvent) => void;
91 | 


--------------------------------------------------------------------------------
/libs/sdk-js/src/utils/signals.ts:
--------------------------------------------------------------------------------
 1 | export function mergeSignals(...signals: (AbortSignal | null | undefined)[]) {
 2 |   const nonZeroSignals = signals.filter(
 3 |     (signal): signal is AbortSignal => signal != null,
 4 |   );
 5 | 
 6 |   if (nonZeroSignals.length === 0) return undefined;
 7 |   if (nonZeroSignals.length === 1) return nonZeroSignals[0];
 8 | 
 9 |   const controller = new AbortController();
10 |   for (const signal of signals) {
11 |     if (signal?.aborted) {
12 |       controller.abort(signal.reason);
13 |       return controller.signal;
14 |     }
15 | 
16 |     signal?.addEventListener("abort", () => controller.abort(signal.reason), {
17 |       once: true,
18 |     });
19 |   }
20 | 
21 |   return controller.signal;
22 | }
23 | 


--------------------------------------------------------------------------------
/libs/sdk-js/src/utils/stream.ts:
--------------------------------------------------------------------------------
  1 | // in this case don't quite match.
  2 | type IterableReadableStreamInterface<T> = ReadableStream<T> & AsyncIterable<T>;
  3 | 
  4 | /*
  5 |  * Support async iterator syntax for ReadableStreams in all environments.
  6 |  * Source: https://github.com/MattiasBuelens/web-streams-polyfill/pull/122#issuecomment-1627354490
  7 |  */
  8 | export class IterableReadableStream<T>
  9 |   extends ReadableStream<T>
 10 |   implements IterableReadableStreamInterface<T>
 11 | {
 12 |   public reader: ReadableStreamDefaultReader<T>;
 13 | 
 14 |   ensureReader() {
 15 |     if (!this.reader) {
 16 |       this.reader = this.getReader();
 17 |     }
 18 |   }
 19 | 
 20 |   async next(): Promise<IteratorResult<T>> {
 21 |     this.ensureReader();
 22 |     try {
 23 |       const result = await this.reader.read();
 24 |       if (result.done) {
 25 |         this.reader.releaseLock(); // release lock when stream becomes closed
 26 |         return {
 27 |           done: true,
 28 |           value: undefined,
 29 |         };
 30 |       } else {
 31 |         return {
 32 |           done: false,
 33 |           value: result.value,
 34 |         };
 35 |       }
 36 |     } catch (e) {
 37 |       this.reader.releaseLock(); // release lock when stream becomes errored
 38 |       throw e;
 39 |     }
 40 |   }
 41 | 
 42 |   async return(): Promise<IteratorResult<T>> {
 43 |     this.ensureReader();
 44 |     // If wrapped in a Node stream, cancel is already called.
 45 |     if (this.locked) {
 46 |       const cancelPromise = this.reader.cancel(); // cancel first, but don't await yet
 47 |       this.reader.releaseLock(); // release lock first
 48 |       await cancelPromise; // now await it
 49 |     }
 50 |     return { done: true, value: undefined };
 51 |   }
 52 | 
 53 |   // eslint-disable-next-line @typescript-eslint/no-explicit-any
 54 |   async throw(e: any): Promise<IteratorResult<T>> {
 55 |     this.ensureReader();
 56 |     if (this.locked) {
 57 |       const cancelPromise = this.reader.cancel(); // cancel first, but don't await yet
 58 |       this.reader.releaseLock(); // release lock first
 59 |       await cancelPromise; // now await it
 60 |     }
 61 |     throw e;
 62 |   }
 63 | 
 64 |   // eslint-disable-next-line @typescript-eslint/ban-ts-comment
 65 |   // @ts-ignore Not present in Node 18 types, required in latest Node 22
 66 |   async [Symbol.asyncDispose]() {
 67 |     await this.return();
 68 |   }
 69 | 
 70 |   [Symbol.asyncIterator]() {
 71 |     return this;
 72 |   }
 73 | 
 74 |   static fromReadableStream<T>(stream: ReadableStream<T>) {
 75 |     // From https://developer.mozilla.org/en-US/docs/Web/API/Streams_API/Using_readable_streams#reading_the_stream
 76 |     const reader = stream.getReader();
 77 |     return new IterableReadableStream<T>({
 78 |       start(controller) {
 79 |         return pump();
 80 |         function pump(): Promise<T | undefined> {
 81 |           return reader.read().then(({ done, value }) => {
 82 |             // When no more data needs to be consumed, close the stream
 83 |             if (done) {
 84 |               controller.close();
 85 |               return;
 86 |             }
 87 |             // Enqueue the next data chunk into our target stream
 88 |             controller.enqueue(value);
 89 |             return pump();
 90 |           });
 91 |         }
 92 |       },
 93 |       cancel() {
 94 |         reader.releaseLock();
 95 |       },
 96 |     });
 97 |   }
 98 | 
 99 |   static fromAsyncGenerator<T>(generator: AsyncGenerator<T>) {
100 |     return new IterableReadableStream<T>({
101 |       async pull(controller) {
102 |         const { value, done } = await generator.next();
103 |         // When no more data needs to be consumed, close the stream
104 |         if (done) {
105 |           controller.close();
106 |         }
107 |         // Fix: `else if (value)` will hang the streaming when nullish value (e.g. empty string) is pulled
108 |         controller.enqueue(value);
109 |       },
110 |       async cancel(reason) {
111 |         await generator.return(reason);
112 |       },
113 |     });
114 |   }
115 | }
116 | 


--------------------------------------------------------------------------------
/libs/sdk-js/tsconfig.cjs.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "./tsconfig.json",
 3 |   "compilerOptions": {
 4 |     "module": "CommonJS",
 5 |     "moduleResolution": "Node",
 6 |     "declaration": false
 7 |   },
 8 |   "exclude": ["node_modules", "dist", "**/tests"]
 9 | }
10 | 


--------------------------------------------------------------------------------
/libs/sdk-js/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@tsconfig/recommended",
 3 |   "compilerOptions": {
 4 |     "target": "ES2021",
 5 |     "lib": [
 6 |       "ES2021",
 7 |       "ES2022.Object",
 8 |       "DOM"
 9 |     ],
10 |     "module": "NodeNext",
11 |     "moduleResolution": "nodenext",
12 |     "esModuleInterop": true,
13 |     "declaration": true,
14 |     "noImplicitReturns": true,
15 |     "noFallthroughCasesInSwitch": true,
16 |     "noUnusedLocals": true,
17 |     "noUnusedParameters": true,
18 |     "useDefineForClassFields": true,
19 |     "strictPropertyInitialization": false,
20 |     "allowJs": true,
21 |     "strict": true,
22 |     "outDir": "dist"
23 |   },
24 |   "include": [
25 |     "src/**/*"
26 |   ],
27 |   "exclude": [
28 |     "node_modules",
29 |     "dist",
30 |     "coverage"
31 |   ],
32 |   "includeVersion": true,
33 |   "typedocOptions": {
34 |     "entryPoints": [
35 |       "src/client.ts"
36 |     ],
37 |     "readme": "none",
38 |     "out": "docs",
39 |     "plugin": [
40 |       "typedoc-plugin-markdown"
41 |     ],
42 |     "excludePrivate": true,
43 |     "excludeProtected": true,
44 |     "excludeExternals": false
45 |   }
46 | }
47 | 


--------------------------------------------------------------------------------
/libs/sdk-py/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2024 LangChain, Inc.
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/libs/sdk-py/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: lint format
 2 | 
 3 | test:
 4 | 	echo "No tests to run"
 5 | 
 6 | ######################
 7 | # LINTING AND FORMATTING
 8 | ######################
 9 | 
10 | # Define a variable for Python and notebook files.
11 | PYTHON_FILES=.
12 | MYPY_CACHE=.mypy_cache
13 | lint format: PYTHON_FILES=.
14 | lint_diff format_diff: PYTHON_FILES=$(shell git diff --name-only --relative --diff-filter=d main . | grep -E '\.py$$|\.ipynb$$')
15 | 
16 | lint lint_diff:
17 | 	poetry run ruff check .
18 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff format $(PYTHON_FILES) --diff
19 | 	[ "$(PYTHON_FILES)" = "" ] || poetry run ruff check --select I $(PYTHON_FILES)
20 | 	[ "$(PYTHON_FILES)" = "" ] || mkdir -p $(MYPY_CACHE) || poetry run mypy $(PYTHON_FILES) --cache-dir $(MYPY_CACHE)
21 | 
22 | format format_diff:
23 | 	poetry run ruff check --select I --fix $(PYTHON_FILES)
24 | 	poetry run ruff format $(PYTHON_FILES)
25 | 


--------------------------------------------------------------------------------
/libs/sdk-py/README.md:
--------------------------------------------------------------------------------
 1 | # LangGraph Python SDK
 2 | 
 3 | This repository contains the Python SDK for interacting with the LangGraph Cloud REST API.
 4 | 
 5 | ## Quick Start
 6 | 
 7 | To get started with the Python SDK, [install the package](https://pypi.org/project/langgraph-sdk/)
 8 | 
 9 | ```bash
10 | pip install -U langgraph-sdk
11 | ```
12 | 
13 | You will need a running LangGraph API server. If you're running a server locally using `langgraph-cli`, SDK will automatically point at `http://localhost:8123`, otherwise
14 | you would need to specify the server URL when creating a client.
15 | 
16 | ```python
17 | from langgraph_sdk import get_client
18 | 
19 | # If you're using a remote server, initialize the client with `get_client(url=REMOTE_URL)`
20 | client = get_client()
21 | 
22 | # List all assistants
23 | assistants = await client.assistants.search()
24 | 
25 | # We auto-create an assistant for each graph you register in config.
26 | agent = assistants[0]
27 | 
28 | # Start a new thread
29 | thread = await client.threads.create()
30 | 
31 | # Start a streaming run
32 | input = {"messages": [{"role": "human", "content": "what's the weather in la"}]}
33 | async for chunk in client.runs.stream(thread['thread_id'], agent['assistant_id'], input=input):
34 |     print(chunk)
35 | ```
36 | 


--------------------------------------------------------------------------------
/libs/sdk-py/langgraph_sdk/__init__.py:
--------------------------------------------------------------------------------
 1 | from langgraph_sdk.auth import Auth
 2 | from langgraph_sdk.client import get_client, get_sync_client
 3 | 
 4 | try:
 5 |     from importlib import metadata
 6 | 
 7 |     __version__ = metadata.version(__package__)
 8 | except metadata.PackageNotFoundError:
 9 |     __version__ = "unknown"
10 | 
11 | __all__ = ["Auth", "get_client", "get_sync_client"]
12 | 


--------------------------------------------------------------------------------
/libs/sdk-py/langgraph_sdk/auth/exceptions.py:
--------------------------------------------------------------------------------
 1 | """Exceptions used in the auth system."""
 2 | 
 3 | import http
 4 | import typing
 5 | 
 6 | 
 7 | class HTTPException(Exception):
 8 |     """HTTP exception that you can raise to return a specific HTTP error response.
 9 | 
10 |     Since this is defined in the auth module, we default to a 401 status code.
11 | 
12 |     Args:
13 |         status_code (int, optional): HTTP status code for the error. Defaults to 401 "Unauthorized".
14 |         detail (str | None, optional): Detailed error message. If None, uses a default
15 |             message based on the status code.
16 |         headers (typing.Mapping[str, str] | None, optional): Additional HTTP headers to
17 |             include in the error response.
18 | 
19 |     Example:
20 |         Default:
21 |         ```python
22 |         raise HTTPException()
23 |         # HTTPException(status_code=401, detail='Unauthorized')
24 |         ```
25 | 
26 |         Add headers:
27 |         ```python
28 |         raise HTTPException(headers={"X-Custom-Header": "Custom Value"})
29 |         # HTTPException(status_code=401, detail='Unauthorized', headers={"WWW-Authenticate": "Bearer"})
30 |         ```
31 | 
32 |         Custom error:
33 |         ```python
34 |         raise HTTPException(status_code=404, detail="Not found")
35 |         ```
36 |     """
37 | 
38 |     def __init__(
39 |         self,
40 |         status_code: int = 401,
41 |         detail: typing.Optional[str] = None,
42 |         headers: typing.Optional[typing.Mapping[str, str]] = None,
43 |     ) -> None:
44 |         if detail is None:
45 |             detail = http.HTTPStatus(status_code).phrase
46 |         self.status_code = status_code
47 |         self.detail = detail
48 |         self.headers = headers
49 | 
50 |     def __str__(self) -> str:
51 |         return f"{self.status_code}: {self.detail}"
52 | 
53 |     def __repr__(self) -> str:
54 |         class_name = self.__class__.__name__
55 |         return f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r})"
56 | 
57 | 
58 | __all__ = ["HTTPException"]
59 | 


--------------------------------------------------------------------------------
/libs/sdk-py/langgraph_sdk/py.typed:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langchain-ai/langgraph/main/libs/sdk-py/langgraph_sdk/py.typed


--------------------------------------------------------------------------------
/libs/sdk-py/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [tool.poetry]
 2 | name = "langgraph-sdk"
 3 | version = "0.1.48"
 4 | description = "SDK for interacting with LangGraph API"
 5 | authors = []
 6 | license = "MIT"
 7 | readme = "README.md"
 8 | repository = "https://www.github.com/langchain-ai/langgraph"
 9 | packages = [{ include = "langgraph_sdk" }]
10 | 
11 | [tool.poetry.dependencies]
12 | python = "^3.9.0,<4.0"
13 | httpx = ">=0.25.2"
14 | orjson = ">=3.10.1"
15 | 
16 | [tool.poetry.group.dev.dependencies]
17 | ruff = "^0.6.2"
18 | codespell = "^2.2.0"
19 | pytest = "^7.2.1"
20 | pytest-asyncio = "^0.21.1"
21 | pytest-mock = "^3.11.1"
22 | pytest-watch = "^4.2.0"
23 | mypy = "^1.10.0"
24 | 
25 | [tool.pytest.ini_options]
26 | # --strict-markers will raise errors on unknown marks.
27 | # https://docs.pytest.org/en/7.1.x/how-to/mark.html#raising-errors-on-unknown-marks
28 | #
29 | # https://docs.pytest.org/en/7.1.x/reference/reference.html
30 | # --strict-config       any warnings encountered while parsing the `pytest`
31 | #                       section of the configuration file raise errors.
32 | addopts = "--strict-markers --strict-config --durations=5 -vv"
33 | asyncio_mode = "auto"
34 | 
35 | 
36 | [build-system]
37 | requires = ["poetry-core"]
38 | build-backend = "poetry.core.masonry.api"
39 | 
40 | [tool.ruff]
41 | lint.select = [
42 |   "E",  # pycodestyle
43 |   "F",  # Pyflakes
44 |   "UP", # pyupgrade
45 |   "B",  # flake8-bugbear
46 |   "I",  # isort
47 | ]
48 | lint.ignore = ["E501", "B008", "UP007", "UP006"]
49 |