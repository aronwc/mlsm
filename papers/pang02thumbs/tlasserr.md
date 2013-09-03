####Overview####

This paper compares the efficiency of 3 machine learning algorithms in sentiment classification and exams if this problem can be treated like a special case of topic-based categorization

####Algorithm####

Each document is represented as a vector of the number of time its features occur in it.
3 machine learning algorithms are tested in this paper:
- Naive Bayes
- Maximum Entropy
- Support Vector Machines
These algorithms are usually used in topic-based categorization.

####Hypothesis####

- For the work described in this paper, reviews can only be positive or negative. They can not be neutral.
- A list of words would be enough to express a sentiment and so, classify a text.

####Data####

- The data source is the Internet Movie Database (IMDb) archive of the rec.arts.movies.reviews
- Data allow automatic processing because only reviews with author rating have been selected.
- Domination of the corpus by a small number of prolific reviewers is avoided because a limit of fewer than 20 reviews per author is imposed.


####Experimentals####

- As a preliminary experiment, two graduate students have chosen a list of indicator words to describe positive and negative sentiment. It was to test the hypothesis that a list of words could describe a sentiment. 
- A dataset is made of 700 positive-sentiment and 700 negative-sentiment documents randomly chosen in the data.
- The 3 algorithms (Naive Bayes, Maximum entropy and Support Vector Machines) are launched on the dataset to evaluate the effectiveness of certain parameters to consider (presence, frequency, unigrams, bigrams, parts of speech and position).
- Authors focused on features based on unigrams and bigrams. Only 16165 unigrams appearing four times and 16165 bigrams appearing seven times are considered.


####Results####

- There is a better performance by accounting for features presence, not feature frequency.
- Bigrams are not effective with these 3 algorithms. Unigrams are more effective than bigrams.
- Distinguishing the different usages of words is not really useful, as far as the use of the adjectives, or the position.
- Support Vector Machines tends to be the algorithm the most effective for sentiment classification. And Naïve Bayes the worst. Working on unigram presence information is the best way to evaluate a document. 
- Machine learning techniques have better performance(80%) than human-generated baseline(65%) in sentiment classification.


####Assumptions####

- Sentiment classification is a more challenging problem than topic-based categorization
- Machine learning algorithms can perform as well on sentiment classification as on traditional topic-based categorization.
- Machine learning techniques have better performance than human-generated baseline in sentiment classification.


####Synthesis####

- We can assign different weights to different keyword for sentiment classification, particularly for those which express stronger sentiment.
- We can try these 3 algorithms on different databases like travel and hotel reviews or food reviews.
- Expectations or previous assumption before watching the film from the reviewers should be ignore because they are not on-topic. 


####Related Papers####

- Machine learning : a review of classification and combining techniques, S.B. Kotsiankis, I.D. Zaharakis, P.E. Pintelas (2007)
- Machine Learning Approaches to sentiment Analysis using the Dutch Netlog Corpus, Sarah Schrauwen (2010)
- Sentiment Classification on Customer Feedback Data : Noisy Data, Large FeatureVectors and the Role of Linguistic Analysis, Gamon, M. (2004)

	
