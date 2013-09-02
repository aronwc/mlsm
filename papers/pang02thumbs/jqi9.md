####Overview####
This paper is talking about how to implement sentiment classification by using the machine learning techniques, which using supervised learning method instead of unsupervised learning method that some people has used before.

####Algorithm####
Three very famous algorithms have been used during the experiment, 

1.	Naïve Bayes
2.	Maximum Entropy
3.	SVMs

All these algorithms need to be implemented by setting up a sentiment features-bag first, which collecting some words or phases that got high frequency in specific sentiment review, for example, “stink” in a negative review or “brilliant” in a positive review.

Naïve Bayes is relatively easy to understand, for certain feature, if a review contains this feature how much is the probability that the review is negative or positive, then compare the probability between positive and negative, the result will go to the bigger one. But it got the lowest accuracy among these algorithms.

Not like the Naïve Bayes, Maximum Entropy make every feature independent, just like some kind of trigger, some specific word will determine the result by itself. It is more accurate when features are not so independent.

SVMs is the most accurate algorithm, which use training data to build a hyper plane that will divide review into negative to positive, I do not really understand the how it works, but from the paper it seems pretty perfect for predicting things.


####Hypothesis####

Before the experiment, they got a hypothesis (which is wrong) that they just need to build two lists (negative and positive) of words, which can distinguish negative and positive review only by counting words that belong to two lists, if the review got more words from the negative list than the positive list, the review is negative.
Then they make another hypothesis that the algorithm that belong to machine learning which use to distinguish topic category can be used to distinguish sentiment.

####Data####
Their data source was the IMDb , to avoid domination of the corpus by a small number of people who write a lots of review for the same movie, they imposed a limit of fewer than 20 reviews per author per sentiment category, then a corpus of 752 negative and 1301 positive reviews.

####Experimentals####
Authors implemented three different algorithms with same feature-bags (actually several kinds I think: unigrams and bigrams etc.) and different combinations of feature-bags

And compare accuracy that algorithm got with certain feature-bags.

####Result####
The best approach is the SVMs, which almost got all the highest accuracy in the tests, and ME is better than Naïve Bayes, but ME is not quite efficient as the other two.

Initial unigram result: basically it shows that the machine learning techniques is much better than human-selected baselines.

Feature frequency vs. presence: since different algorithm use this features in a different way, so the frequency and presence are all important to different algorithms.

Bigrams: the test result for bigrams feature-bag are almost the same, it shows that different algorithm will make a little different for it, the important thing is different combinations of words will make a big difference.

Parts of speech: accuracy of Naïve Bayes improved, but declined for SVMs, unchanged for MaxEnt.

Position: some people would like to point out the defects first, then advantages; some people do the opposite things. But from the result we can see it will not make a big effect. 

####Assumptions####
The authors think the supervised learning method will be more efficient and accurate than the unsupervised learning methods.
Some kinds of reviews will turn to be really hard for machine learning technique to distinguish by algorithms mentioned before, for example there are some nonsenses in it, author think next step for more accurate classification will be identify which sentences are on-topic.

####Synthesis#### 
To know the attitude for a certain event or topic is very useful to retailers or politicians, maybe next step we should try to predict people’s attitude from a former predicted result of a similar topic or event, it will help people to know the effect of their decision.

####Related Papers####
Machine learning in automated text categorization, 
Fabrizio Sebastiani	Consiglio Nazionale delle Ricerche, Pisa, Italy
ACM Computing Surveys (CSUR) Volume 34 Issue 1, March 2002 
Pages 1-47
#This paper talks about almost all the methods about text categorization.


Sentiment classification of online reviews to travel destinations by supervised machine learning approaches
Qiang Ye, Ziqiong Zhang, Rob Law
Expert Systems with Applications, Volume 36, Issue 3, Part 2, April 2009, Pages 6527–6535
#Use character based N-gram model instead of ME.

A machine learning approach to sentiment analysis in multilingual Web texts
Erik Boiy, Marie-Francine Moens
#Mixed several algorithms to perform the prediction, got relatively high accuracy.
