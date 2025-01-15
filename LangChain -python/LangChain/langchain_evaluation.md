* `evaluation`

# `evaluation`#

**Evaluation** chains for grading LLM and Chain outputs.

This module contains off-the-shelf evaluation chains for grading the output of
LangChain primitives such as language models and chains.

**Loading an evaluator**

To load an evaluator, you can use the `load_evaluators` or `load_evaluator`
functions with the names of the evaluators to load.

    
    
    from langchain.evaluation import load_evaluator
    
    evaluator = load_evaluator("qa")
    evaluator.evaluate_strings(
        prediction="We sold more than 40,000 units last week",
        input="How many units did we sell last week?",
        reference="We sold 32,378 units",
    )
    

The evaluator must be one of `EvaluatorType`.

**Datasets**

To load one of the LangChain HuggingFace datasets, you can use the
`load_dataset` function with the name of the dataset to load.

    
    
    from langchain.evaluation import load_dataset
    ds = load_dataset("llm-math")
    

**Some common use cases for evaluation include:**

  * Grading the accuracy of a response against ground truth answers: `QAEvalChain`

  * Comparing the output of two models: `PairwiseStringEvalChain` or `LabeledPairwiseStringEvalChain` when there is additionally a reference label.

  * Judging the efficacy of an agent’s tool usage: `TrajectoryEvalChain`

  * Checking whether an output complies with a set of criteria: `CriteriaEvalChain` or `LabeledCriteriaEvalChain` when there is additionally a reference label.

  * Computing semantic difference between a prediction and reference: `EmbeddingDistanceEvalChain` or between two predictions: `PairwiseEmbeddingDistanceEvalChain`

  * Measuring the string distance between a prediction and reference `StringDistanceEvalChain` or between two predictions `PairwiseStringDistanceEvalChain`

**Low-level API**

These evaluators implement one of the following interfaces:

  * `StringEvaluator`: Evaluate a prediction string against a reference label and/or input context.

  * `PairwiseStringEvaluator`: Evaluate two prediction strings against each other. Useful for scoring preferences, measuring similarity between two chain or llm agents, or comparing outputs on similar inputs.

  * `AgentTrajectoryEvaluator` Evaluate the full sequence of actions taken by an agent.

These interfaces enable easier composability and usage within a higher level
evaluation framework.

**Classes**

`evaluation.agents.trajectory_eval_chain.TrajectoryEval` | A named tuple containing the score and reasoning for a trajectory.  
---|---  
`evaluation.agents.trajectory_eval_chain.TrajectoryEvalChain` | A chain for evaluating ReAct style agents.  
`evaluation.agents.trajectory_eval_chain.TrajectoryOutputParser` | Trajectory output parser.  
`evaluation.comparison.eval_chain.LabeledPairwiseStringEvalChain` | A chain for comparing two outputs, such as the outputs  
`evaluation.comparison.eval_chain.PairwiseStringEvalChain` | A chain for comparing two outputs, such as the outputs  
`evaluation.comparison.eval_chain.PairwiseStringResultOutputParser` | A parser for the output of the PairwiseStringEvalChain.  
`evaluation.criteria.eval_chain.Criteria`(value) | A Criteria to evaluate.  
`evaluation.criteria.eval_chain.CriteriaEvalChain` | LLM Chain for evaluating runs against criteria.  
`evaluation.criteria.eval_chain.CriteriaResultOutputParser` | A parser for the output of the CriteriaEvalChain.  
`evaluation.criteria.eval_chain.LabeledCriteriaEvalChain` | Criteria evaluation chain that requires references.  
`evaluation.embedding_distance.base.EmbeddingDistance`(value) | Embedding Distance Metric.  
`evaluation.embedding_distance.base.EmbeddingDistanceEvalChain` | Use embedding distances to score semantic difference between a prediction and reference.  
`evaluation.embedding_distance.base.PairwiseEmbeddingDistanceEvalChain` | Use embedding distances to score semantic difference between two predictions.  
`evaluation.exact_match.base.ExactMatchStringEvaluator`(*) | Compute an exact match between the prediction and the reference.  
`evaluation.parsing.base.JsonEqualityEvaluator`([...]) | Evaluate whether the prediction is equal to the reference after  
`evaluation.parsing.base.JsonValidityEvaluator`(...) | Evaluate whether the prediction is valid JSON.  
`evaluation.parsing.json_distance.JsonEditDistanceEvaluator`([...]) | An evaluator that calculates the edit distance between JSON strings.  
`evaluation.parsing.json_schema.JsonSchemaEvaluator`(...) | An evaluator that validates a JSON prediction against a JSON schema reference.  
`evaluation.qa.eval_chain.ContextQAEvalChain` | LLM Chain for evaluating QA w/o GT based on context  
`evaluation.qa.eval_chain.CotQAEvalChain` | LLM Chain for evaluating QA using chain of thought reasoning.  
`evaluation.qa.eval_chain.QAEvalChain` | LLM Chain for evaluating question answering.  
`evaluation.qa.generate_chain.QAGenerateChain` | LLM Chain for generating examples for question answering.  
`evaluation.regex_match.base.RegexMatchStringEvaluator`(*) | Compute a regex match between the prediction and the reference.  
`evaluation.schema.AgentTrajectoryEvaluator`() | Interface for evaluating agent trajectories.  
`evaluation.schema.EvaluatorType`(value[, ...]) | The types of the evaluators.  
`evaluation.schema.LLMEvalChain` | A base class for evaluators that use an LLM.  
`evaluation.schema.PairwiseStringEvaluator`() | Compare the output of two models (or two outputs of the same model).  
`evaluation.schema.StringEvaluator`() | Grade, tag, or otherwise evaluate predictions relative to their inputs and/or reference labels.  
`evaluation.scoring.eval_chain.LabeledScoreStringEvalChain` | A chain for scoring the output of a model on a scale of 1-10.  
`evaluation.scoring.eval_chain.ScoreStringEvalChain` | A chain for scoring on a scale of 1-10 the output of a model.  
`evaluation.scoring.eval_chain.ScoreStringResultOutputParser` | A parser for the output of the ScoreStringEvalChain.  
`evaluation.string_distance.base.PairwiseStringDistanceEvalChain` | Compute string edit distances between two predictions.  
`evaluation.string_distance.base.StringDistance`(value) | Distance metric to use.  
`evaluation.string_distance.base.StringDistanceEvalChain` | Compute string distances between the prediction and the reference.  
  
**Functions**

`evaluation.comparison.eval_chain.resolve_pairwise_criteria`(...) | Resolve the criteria for the pairwise evaluator.  
---|---  
`evaluation.criteria.eval_chain.resolve_criteria`(...) | Resolve the criteria to evaluate.  
`evaluation.loading.load_dataset`(uri) | Load a dataset from the LangChainDatasets on HuggingFace.  
`evaluation.loading.load_evaluator`(evaluator, *) | Load the requested evaluation chain specified by a string.  
`evaluation.loading.load_evaluators`(evaluators, *) | Load evaluators specified by a list of evaluator types.  
`evaluation.scoring.eval_chain.resolve_criteria`(...) | Resolve the criteria for the pairwise evaluator.  
  
© Copyright 2023, LangChain Inc.