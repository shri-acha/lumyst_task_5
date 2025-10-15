This document outlines a hybrid approach for classifying source code functions by combining deterministic analysis with a fine-tunable Natural Language Processing (NLP) model. The methodology is designed to be adaptive, leveraging existing codebase knowledge where available and discovering new patterns in unfamiliar codebases. The primary challenge addressed is the mitigation of dependencies on large, pre-labeled datasets through an iterative, self-improving architecture.

## 1. Methodology

The solution currently only contains heuristic inference. I've decided to implement frequency threshold and regex-based pattern matching. These results from these two tests can be used in provisioning of the NLP model, which can be finetuned to understand and categorize results on the basis of the modified data.

## 2. Design Rationale

The whole reason this technique is usable is solely because of existing knowledge of the codebase. If pre-existing knowledge of the framework/general patterns is unknown, then less common keywords have to be picked up using the NLP method, which then feeds to this deterministic existing method, which then in result could be used to get better results, in general.

## 3. Limitations and Future Work

The limitations of this is mostly is as I discuss, the lack of properly labelled data to finetune models, which can be dealt with. Currently, I've not considered the code within the function definition which can also be used to create better context of the function.
