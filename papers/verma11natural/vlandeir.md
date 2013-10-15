####Overview####

The objective of this paper is to develop a tool able to detect Twitter messages that contain useful information in case of mass emergency.

####Algorithm####

They develop a situational awareness classifier using two machine learning methods :
- Naive Bayes
- Maximum Entropy

They also develop three classifiers to determine linguistic features by computing the distribution of objective, impersonal and formal tweets among situational aware tweets.

They tokenize the tweets after removing Twitter-specific symbols and standard words. They use the words and their frequency as features for classification as well as a part-of-speech tagger. Eventually, the features for the classifier are :

- Unigrams and their raw frequency
- Bigrams and their raw frequency
- Part-Of-Speech tags
- Subjectivity of tweets
- Register of tweets
- Tone of tweets

####Hypothesis####

- It is possible to inform the part of the population concerned by an emergency using machine learning techniques of tweets.

####Data####

They use tweets collected during four mass emergency events :
- the North American Red River floods of 2009 and 2010 (453 and 499 tweets respectively);
- the Oklahoma grassfires (527 tweets);
- the Haïti earthquake (486 tweets).

They use approximately 500 tweets for each event to allow the hand-annotations on the dataset. These data are annotated for four different qualities:
1. is it communicating situational awareness information?
2. is it objective or subjective?
3. is it written in informal or formal style?
4. is it written from a personal or impersonal standpoint?

####Experimentals####

- They evaluate the performance of the situational awareness (SA) classifier by introducing one feature at a time.
- They also create a new dataset from random selection of 500 SA and 500 non-SA tweets from all events.
- They compute the mean accuracy over 10 fold cross-validation (90% training/10% testing) to evaluate the performance.
- Finally, they try to predict each event by training on a different event.

####Results####

- They find high baseline accuracy for events using unigrams and their frequency.
- Using bigrams in addition to unigrams do not improve the performance significantly.
- Conversely, POS tagging improve the SA classifier accuracy.
- Using objectivity classification show a good improvement in performance as well as using formal/informal and personal/impersonal classifiers.

####Assumptions####

- Tweets contributing to situational awareness are likely to be written in an objective, impersonal, and formal style.
- A real-time analysis of tweets is conceivable for future applications.

####Synthesis###

- I do not understand something: they say they used unigrams and their frequency as a baseline for their experiments on "Experiments and Evaluation" and then declare that they "find high baseline accuracy for events using only word and raw frequency as feature".
- I am not sure that a collection of 2000 tweets on 4 events is sufficient to apply machine learning algorithms.

####Related Papers####

- Bruns, A., & Liang, Y. E. (2012). [Tools and methods for capturing Twitter data during natural disasters.]{http://pear.accc.uic.edu/ojs/index.php/fm/article/view/3937/3193} First Monday, 17(4).
	- This article focuses on the development of flexible and reliable research infrastructure for tracking and analysing Twitter feeds at scale and in close to real time.
- Neubig, G., Matsubayashi, Y., Hagiwara, M., & Murakami, K. (2011, November). [Safety Information Mining-What can NLP do in a disaster-]{https://www.aclweb.org/anthology/I/I11/I11-1108.pdf}. In IJCNLP (pp. 965-973).
	- This paper describes efforts of NLP researchers to create a system to aid the relief efforts during the 2011 East Japan Earthquake.
