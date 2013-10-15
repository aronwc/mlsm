####Overview####

This paper describes an approach for automatically indentifying messages on Twitter which contribute to situational awareness (SA) of an event. It also tries to identify new features to ameliorate the SA classifier.

####Algorithms####

- Naïve Bayes (NB) and Maximum Entropy (MaxEnt) are used for classification
- The SA classifier includes Unigrams or Bigrams and their raw frequency.
- It also uses Part-of-speech (POS) tags
- Subjectivity is measured by the subjectivity classifier or by OpinionFinder
- Register of tweet can be predicted by register classifier.
- Tone of tweets

####Hypothesis####

- Tweets demonstrating situation awareness can be identified with machine learning techniques.
- The add of linguistic features improves classification of SA tweets over standard-derivable features.

####Data####

1,965 tweets (all hand-annotated) broadcast during emergency events have been selected because they contain some of keywords:

- for the preliminary study:500 for the 2009 Oklahoma grassfire and 453 for the Red River flood in 2009
- Then the authors collected tweets for the Red River flood in 2010 during a 20-day period by searching relevant terms, and tweets for Haiti earthquake during a 23-day period. Then for each dataset, they took a sample of 500 random tweets.

####Experimental####

The performance of the SA classifier is evaluated by introducing one feature at a time:

- E1: All the tweets have been hand-annotated.
- E2: Comparison between the use of unigrams or bigrams and their raw frequency.
- E3: The use of POS tags is evaluated.
- E4: All tweets are annotated for objectivity and SA. Then a supervised MaxEnt classifier is trained to classify subjective and objective tweets with unigrams and POS as features. The use of OpinionFinder is also evaluated for this classification.
- E5: The use of predicting register and impersonal tone is evaluated.
- E6: The performance of the SA classifier with all the features giving the best results is evaluated on new events.

####Results####

- E1 shows that catastrophic disasters attaining global attention generate significantly more noise and traffic. Moreover a large proportion of tweets are objective, formal and impersonal in nature.
- E2 shows that using unigrams and raw frequency provides a high accuracy. Bigrams do not yield a significant improvement.
- E3: POS tags improve overall classification accuracy.
- E4: accuracy of 86.2%. The accuracy is the highest when objectivity is added as a feature. OpinionFinder is not really appropriate.
- E5: using the predicted tag yield similar accuracies as using hand-annotated tags.
- E6 shows that the MaxEnt performs better. Moreover the performance is better on similar type of events that those used to train the classifier.

####Assumptions####

- Tweets with information about situational awareness could be used to inform and update applications aimed at helping at members of the public or organizations understand and act accordingly during mass emergencies.
- tweets that contribute to situational awareness are likely to be written in a style that is objective, impersonal, and formal.

####Synthesis####

- The location of the tweet is important. A tweet sent from the place where the event happened is more helpful than a tweet sent from an other place.
- Maybe it would be better first to detect the event and then classify the tweets by location to have a very precise idea of what happen in a place and then run all the analysis.
- We can train the model on a lot of events and then compute a distance between the type of the detected events and the type of the events used to train the classifier. 

####Related Papers####

- Emergency Situation Awareness from Twitter for Crisis Management, Mark A. Cameron, Robert Power, Bella Robinson, Jie Yin
	-  This paper describes work to detect, asses, summarise messages of interest for crisis coordination by twitter.

- I See a Car Crash: Real-time Detection of Small Scale Incidents in Microblogs, Axel Schulz, Petar Ristoski, and Heiko Paulheim
	- This paper present a solution for a real-time identification of small scale incidents using microblogs, therby allowing to increase the situational awareness. The authors use machine learning algorithms combining text classification and semantic enrichment of microblogs.
