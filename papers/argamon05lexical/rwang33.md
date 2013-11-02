#Overview
This paper addresses distinguishing high from low neuroticism and extraversion in authors of informal text with four different sets of lexical features.

#Algorithm
* They use four different sets of lexical features for this task: a standard function word list, conjunctive phrases, modality indicators, and appraisal adjectives and modifiers.
* SMO, a support vector machine learner, was used to learn linear separators for the high and low classes in each of the two tasks.
* 10-fold crossvalidation was used throughout to estimate out-of-training classification accuracy.

#Hypothesis
Personality can be classified from the informal text written by four different sets of lexical features.

#Data
* The corpus used for this experiment was derived from essays written by students at the University of Texas at Austin between 1997 and 2003.
* Undergraduate students wrote a stream-of-consciousness essay and an essay of deep self-analysis; in toto these data sets comprised 1157 and 1106 documents, respectively.
* They were also given the NEO-FFI Five-Factor Personality Inventory.

#Experiments
* All documents in each corpus were processed into numeric feature vectors using various combinations of the four feature sets.
* Weka’s implementation of the SMO learning algorithm with a linear kernel was used for learning classification models. Throughout, 10-fold cross-validation was used throughout to estimate out-of-training classification accuracy.
* They take the top features indicating each class and find all sibling oppositions.

#Results
* In both cases the most useful feature set for this task was Appraisal, with accuracies of 58.2% (SoC) and 58.0% (DSA).
* None of the functional feature sets do as well as function words, and they even reduce accuracy overall to chance levels when added to function words. We interpret this to mean that extraversion is expressed in aspects of meaning different from Conjunction, Modality, or Appraisal.

#Assumptions



#Synthesis



#Related papers
