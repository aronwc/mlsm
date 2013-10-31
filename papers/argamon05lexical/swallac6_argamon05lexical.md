Overview
========

The paper seeks to identify authors based on their personality in the way they write.

Algorithm
=========

There were four sets of lexical features used:

1.  Standard function word list.

2.  Conjunctive phrases.

3.  Modality indicators.

4.  Appraisal adjectives and modifiers.

SMO, a support vector machine learner, was used to learn these linear separators for high and low classes in each of the two tasks with 10 fold validation.

Hypothesis
==========

People, because of the mannerisms present in the writing styles, are identifiable by various machine learning techniques not requiring a corpus of documents from the same individual.

Data
====

Essays written by students at the University of Texas at Austin between 1997 and 2003. These students wrote both a stream-of-consciousness essay and an essay of deep self-analysis giving 1157 and 1106 documents, respectively. These students were also given the NEO-FFI Five-Factor Personality Inventory examination.

Experiments
===========

All of the documents collected in the corpus were processed into numeric feature vectors using various combinations of the following feature sets:

-   Function Word

-   Conjunction

-   Modality

-   Appraisal

Weka’s implementation of the SMO learning algorithm was used for learning classification models. 10-fold cross validation was used to estimate out-of-training classification accuracy. The most important features for stylistic classification were examined.

Results
=======

-   Neuroticism - 58.2% accuracy with SoC and 58.0% with DSA. Appraisal features gave highest accuracy.

-   Extraversion - None of the features do as well as function words (which had 57% accuracy).

Assumptions
===========

-   The undergraduate students sampled are good candidates for classification.

-   Though it has been demonstrated with reasonable accuracy, it still remains an assumption that people, by-and-large, write as their personality dictates.

Synthesis
=========

Overall a very interesting and scientifically rigorous paper. One thing that isn’t made clear in the paper is whether the authors attempted to classify the Big Five personality traits as a single feature. It would appear as though they did not. It would also be good to look into how demographics play a role in the development of these 5 personality features and whether or not this affects the overall accuracy.

Related Papers
==============

-   Mergenthaler (1996; Weintraub 1981; Rosenberg and Tucker 1979) used computers to attempt to capture psychological themes or people’s underlying emotional states that might be reflected in the words they used.

-   J. W. Pennebaker and Lay (2002) showed that when depressed or in an emotionally vulnerable situation, individuals exhibit increases in pronouns, drops in articles, and increases in their use of present tense auxiliary verbs.

-   Gortner and Pennebaker (Cohn, Mehl, and Pennebaker 2004) showed that when people face a sudden and collective change they increase their use of the first person plural and a drop in first person singular.

-   M. R. Mehl and Pennebaker (2003) showed that a certain words are useful in correlating a variety of personality marks such as the Big Five.

References
==========

Cohn, Michael A., Matthias R. Mehl, and James W. Pennebaker. 2004. “Linguistic markers of psychological change surrounding September 11, 2001.” *Psychological Science* 15 (10) (Oct): 687–693.

Gortner, E. M., and J. W. Pennebaker. “The anatomy of a disaster: Media coverage and community-wide health effects of the Texas A&M bonfire tragedy.” *Journal of Social and Clinical Psychology*.

Mehl, M. R., and J. W. Pennebaker. 2003. “The social dynamics of a cultural upheaval: social interactions surrounding September 11, 2001.” *Psychological Science* 14 (6): 579–585. [http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve\\&\\ 38;db=PubMed\\&\\ 38;dopt=Citation\\&\\ 38;list\\\_uids=14629689](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve\&\ 38;db=PubMed\&\ 38;dopt=Citation\&\ 38;list\_uids=14629689 "http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve\&\ 38;db=PubMed\&\ 38;dopt=Citation\&\ 38;list\_uids=14629689").

Mergenthaler, Erhard. 1996. “Emotion-abstraction patterns in verbatim protocols: A new way of describing therapeutic processes.” *Journal of Consulting and Clinical Psychology* 64: 1306–1318.

Pennebaker, J. W., and T. C. Lay. 2002. “Language use and personality during crises: Analyses of mayor rudolph giuliani’s press conferences.” *Journal of Research in Personality* 36: 271–282.

Rosenberg, S. D., and G. J. Tucker. 1979. “Verbal behavior and schizophrenia: The semantic dimension.” *Archives of General Psychiatry* 38: 1331–1337.

Weintraub, Walter. 1981. “Verbal behavior: adaptation and psychopathology.” *New York: Springer Pub. Co.*
