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
A central assumption of language psychology is that the words people use reflect who they are.

#Synthesis
From my point of view, the extention of this paper can be developing shallow parsing techniques for extracting phrases and using them in classification. 

#Related papers
* [Measuring the Usefulness of Function Words for Authorship Attribution](http://tomcat-stable.hcmc.uvic.ca:8080/ach/site/xhtml.xq?id=162)      
Their results argue for the importance of using larger data sets for evaluating the relative utility of different attribution feature sets or techniques. As in their case of comparing frequent words with frequent collocations, changing the scale of the data set may affect the relative power of different techniques, thus leading to different conclusions. They suggest that the authorship attribution community should now work towards developing a large suite of corpora and testbed tasks, to allow more rigorous and standardized comparisons of alternative approaches.
                          
* [Mining E-mail Authorship](http://rybkaforum.net/mwf/rybkaattach/82/256182/DeVel_TM.pdf)      
In this paper they report an investigation into the learning of authorship identication or categorisation for the case of e-mail documents. They use various e-mail document features such as structural characteristics and linguistic evidence together with the Support Vector Machine as the learning algorithm. Experiments on a number of e-mail documents give promising results with some e-mail document features and author categories giving better categorisation performance results.
