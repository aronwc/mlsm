####Overview####
This paper compares several machine learning algorithms used in text classification
and reports their utility in the task of sentiment analysis.

####Algorithm####
In initial experiments, a document is represented as a vector of word counts. Three classifiers are used.
- Naive Bayes
	- Assumes all the features are independent.
	- Uses Bayes rule to determine the probability for P(C | D).
- Maximum Entropy
	- Does not assume indepence of the features.
	- Estimates the conditional distribution of the class variable.
- Support Vector Machines
	- Unlike previous classifiers, SVMs are *large margin* rather than probabilistic.
	- Attempts to find hyperplane that separates the documents vectors in one class
	from the other, where the separation is as large as possible.

These techniques are used in subsequent experiments but with varying feature representations.

####Hypothesis####
The authors hypothesize that text categorization machine learning techniques can be used for the task of sentiment analysis.

####Data####
- Reviews were taken from the IMDb archive of the rec.arts.movie.reviews newgroup.
- Corpus consisted of 752 negative reviews and 1301 positive reviews, representing 144 reviewers.
- Only reviews with an explicit, discrete rating were used.

####Experiments####
700 positive and 700 negative reviews were randomly selected from the corpus, and then divided into 3 equal sized
folds. Initially, each document is treated as a feature vector of word counts and tested using Naive Bayes,
Maximum Entropy, and Support Vector Machine classification. Further experiments were then done which changed
the feature representation of the documents. These include:
- using feature presence rather than feature count
- including bigrams as features instead of a unigram only model
- attaching POS tags to each word
- using only adjectives
- including information about the position of each word in the document

####Results####
- SVMs generally outperformed the other classifiers, but not by that much.
- Unigram presence information proved to be the most effective representation.
- The machine learning algorithms produced better results than the human generated baselines.
- None of the results matched the accuracy of reported standard topic-based classification.

####Assumptions####
- The assumption behind all of their experiments that they hope to prove is that sentiment
analysis can be thought of as a case of text categorization, and that existing text categorization
techniques are appropriate for this task.
- The authors explicitly mention that they used a dataset with uniform class distribution, and that
skewed distributions were outside their scope.
- The authors, at least initially, consider all words in a document to be equally important. That is,
in their unigram model, they keep all the words in a document. They shift this assumption somewhat when
they consider things like using adjectives only, but even then, they still consider every adjective
that appears in a document, rather than using any techniques to limit the feature vector to words
that might be more predictive than others.

####Synthesis####
The authors demonstrate the utility of these types of algorithms in the task of seniment analysis.
They seem to have several intuitions that they tried to capture in subsequent experiments as they
manipulated their feature representation, i.e., that adjectives may be more important to consider,
that the position of words in a document matter, the importance of "context" that they tried to capture
with bigrams, etc. Although their results did not improve with the data they had, it would be interesting
to see more experiments with other datasets that attempt to capture these intuitions with other models
and whether or not the results are similar. The authors include a quote that for reviews, "the whole
is not necessarily the sum of its parts." All of this is to say, it seems that there are other variables
that could be predictive of sentiment, so it is worth exploring if there are better ways of capturing
those.

####Related Papers####
- Pang, B. and Lee, L. 2004. [A Sentimental Education: Sentiment Analysis Using Subjectivity Summarization Based on Minimum Cuts](http://acl.ldc.upenn.edu/acl2004/main/pdf/319_pdf_2-col.pdf). ACL '04 Proceedings of the 42nd Annual Meeting on Association for Computational Linguistics.
	- A follow up paper by the authors in which "subjectivity extracts" from documents in order to improve sentiment analysis results.
- Hu, M. and Liu, B. 2004. [Mining and Summarizing Customer Reviews](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.76.2378&rep=rep1&type=pdf)
	- With the goal of summarizing online reviews, the authors here develop a technique to find "opinions sentences" in each document and assign a sentiment class to each of those, rather than on the document as a whole.
