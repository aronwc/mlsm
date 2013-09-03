####Overview####

The main goal of this paper is to study the classification of reviews written in natural language. The difference with usual topic-based classification algorithms is that the researchers focused on sentiment-based classification, e.g. decide if a review is a positive one or a negative one.

####Algorithm####

Three types of algorithm are used in this paper :

- Naive Bayes-based algorithm where the assumption is done that all the features are conditionnaly independent;
- Maximum entropy algorithm removes the assumption made previously. Moreover, it provides a additional parameter which is the weight of each feature considering a class c. The highest is the value of the weight, the stronger is the probability of the document to be in c;
- Support Vector Machines algorithm is the only tested algorithm which is not probabilistic.

####Hypothesis####
- It is possible to decide if a movie review is positive or negative by analysing its content;
- It is worthwhile to explore corpus-based techniques;
- Topic-based classification and sentiment-based classification are two different tasks.

####Data####
- They collected their data from the Internet Movie Database. 
- They collected 752 negative reviews and 1301 positive reviews.
- Of these, they randomly kept 700 positives reviews and 700 negatives.

####Experimentals####
- To obtain some results used as future baselines, their first experience involved features defined by students. It was then enhanced with stats on the dataset to get a baseline with a 69% accuracy.
- They divided the data in three equal-sized folds in order to apply cross-validation.
- They focused on both unigrams who appeared at least four times in their documents and on bigrams who appeared at least seven times.
- To get results, they run the three algorithms defined previously on several types of data :
	- the frequency of unigrams (with negation tag);
	- the presence of unigrams (with negation);
	- the presence of unigrams and bigrams;
	- the presence of bigrams;
	- the presence of unigrams, where unigrams are considered as a "part of a speech" giving informations on the unigram's (positive or negative) value;
	- the presence of adjectives as they seemed to be the words carrying the most of meaning when considering a movie review;
	- the presence of the most frequent unigrams;
	- the presence of unigrams considering their position in the review.

####Results####
- Each experimented method beats the baseline score of 69%;
- Computing on the frequency of unigrams shows a 78.7% accuracy on Naive Bayses and a 72.8% accuracy on SVM, which is lower than the usual scores of these algorithms (around 90% accuracy) on classification tasks;
- Unigrams presence accounting shows better performance for every algorithm;
- Using bigrams in addition to unigrams do not improve the results, and the use of bigrams only gives a lower score than the use of unigrams;
- Parts of speech tags do not improve the results;
- On the contrary, it seems that take into account the position of the unigrams in the review could increase the result score.


####Assumptions####
- Two students are sufficient to get the average vocabulary of humans in positive and negative reviews;
- These algorithms are the most effective ones when considering the sentiment classification task;
- Three folds cross-validation is enough to train correctly the different algorithms.

####Synthesis###
- As the obtained results contradict previous works on the superiority of frequence information over presence feature information, I would like to know what are the results on a larger data set or with better trained (10 folds cross-validation) algorithms.
- An additional experiment would be to refine the structure of a movie review to get a better position parameter. Then, the accuracy result would be computed using unigrams.
- My next experiment would be to test the algorithms on other kind of reviews (book, apps, etc) to see if the "thwarted-expectations rhetorical" is also present.
 
####Related Papers####
- J. Read; [Using emoticons to reduce dependency in machine learning techniques for sentiment classification](http://dl.acm.org/ft_gateway.cfm?id=1628969&type=pdf&CFID=242535240&CFTOKEN=35691198). Proceeding ACLstudent '05 Proceedings of the ACL Student Research Workshop.
- Kim, Soo-Min and Hovy, Eduard; [Determining the sentiment of opinions](http://dx.doi.org/10.3115/1220355.1220555). Proceedings of the 20th international conference on Computational Linguistics.
- Jin, Wei and Ho, Hung Hay and Srihari, Rohini K.; [OpinionMiner: a novel machine learning system for web opinion mining and extraction](http://doi.acm.org/10.1145/1557019.1557148). Proceedings of the 15th ACM SIGKDD international conference on Knowledge discovery and data mining.
