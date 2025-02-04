# `smith`#

**LangSmith** utilities.

This module provides utilities for connecting to LangSmith. For more
information on LangSmith, see the LangSmith documentation.

**Evaluation**

LangSmith helps you evaluate Chains and other language model application
components using a number of LangChain evaluators. An example of this is shown
below, assuming you’ve created a LangSmith dataset called `<my_dataset_name>`:

    
    
    from langsmith import Client
    from langchain_community.chat_models import ChatOpenAI
    from langchain.chains import LLMChain
    from langchain.smith import RunEvalConfig, run_on_dataset
    
    # Chains may have memory. Passing in a constructor function lets the
    # evaluation framework avoid cross-contamination between runs.
    def construct_chain():
        llm = ChatOpenAI(temperature=0)
        chain = LLMChain.from_string(
            llm,
            "What's the answer to {your_input_key}"
        )
        return chain
    
    # Load off-the-shelf evaluators via config or the EvaluatorType (string or enum)
    evaluation_config = RunEvalConfig(
        evaluators=[
            "qa",  # "Correctness" against a reference answer
            "embedding_distance",
            RunEvalConfig.Criteria("helpfulness"),
            RunEvalConfig.Criteria({
                "fifth-grader-score": "Do you have to be smarter than a fifth grader to answer this question?"
            }),
        ]
    )
    
    client = Client()
    run_on_dataset(
        client,
        "<my_dataset_name>",
        construct_chain,
        evaluation=evaluation_config,
    )
    

You can also create custom evaluators by subclassing the `StringEvaluator` or
LangSmith’s RunEvaluator classes.

    
    
    from typing import Optional
    from langchain.evaluation import StringEvaluator
    
    class MyStringEvaluator(StringEvaluator):
    
        @property
        def requires_input(self) -> bool:
            return False
    
        @property
        def requires_reference(self) -> bool:
            return True
    
        @property
        def evaluation_name(self) -> str:
            return "exact_match"
    
        def _evaluate_strings(self, prediction, reference=None, input=None, **kwargs) -> dict:
            return {"score": prediction == reference}
    
    
    evaluation_config = RunEvalConfig(
        custom_evaluators = [MyStringEvaluator()],
    )
    
    run_on_dataset(
        client,
        "<my_dataset_name>",
        construct_chain,
        evaluation=evaluation_config,
    )
    

**Primary Functions**

  * `arun_on_dataset`: Asynchronous function to evaluate a chain, agent, or other LangChain component over a dataset.

  * `run_on_dataset`: Function to evaluate a chain, agent, or other LangChain component over a dataset.

  * `RunEvalConfig`: Class representing the configuration for running evaluation. You can select evaluators by `EvaluatorType` or config, or you can pass in custom_evaluators

**Classes**

`smith.evaluation.config.EvalConfig` | Configuration for a given run evaluator.  
---|---  
`smith.evaluation.config.RunEvalConfig` | Configuration for a run evaluation.  
`smith.evaluation.config.SingleKeyEvalConfig` | Configuration for a run evaluator that only requires a single key.  
`smith.evaluation.progress.ProgressBarCallback`(total) | A simple progress bar for the console.  
`smith.evaluation.runner_utils.ChatModelInput` | Input for a chat model.  
`smith.evaluation.runner_utils.EvalError`(...) | Your architecture raised an error.  
`smith.evaluation.runner_utils.InputFormatError` | Raised when the input format is invalid.  
`smith.evaluation.runner_utils.TestResult` | A dictionary of the results of a single test run.  
`smith.evaluation.string_run_evaluator.ChainStringRunMapper` | Extract items to evaluate from the run object from a chain.  
`smith.evaluation.string_run_evaluator.LLMStringRunMapper` | Extract items to evaluate from the run object.  
`smith.evaluation.string_run_evaluator.StringExampleMapper` | Map an example, or row in the dataset, to the inputs of an evaluation.  
`smith.evaluation.string_run_evaluator.StringRunEvaluatorChain` | Evaluate Run and optional examples.  
`smith.evaluation.string_run_evaluator.StringRunMapper` | Extract items to evaluate from the run object.  
`smith.evaluation.string_run_evaluator.ToolStringRunMapper` | Map an input to the tool.  
  
**Functions**

`smith.evaluation.name_generation.random_name`() | Generate a random name.  
---|---  
`smith.evaluation.runner_utils.arun_on_dataset`(...) | Run the Chain or language model on a dataset and store traces to the specified project name.  
`smith.evaluation.runner_utils.run_on_dataset`(...) | Run the Chain or language model on a dataset and store traces to the specified project name.  
  
© Copyright 2023, LangChain Inc.