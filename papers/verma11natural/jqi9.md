####Overview####
- This paper explain a method that can find useful information from tweets when mass emergency happens which will help other people rescue victim or provide certain support to them.

####Algorithm####
- Naïve Bayes (NB) and Maximum Entropy (MaxEnt) are used for classification.
- They tag all the tweets by six important features, objective, subjective, formal, informal, personal, impersonal. Then extract all the tweets that got certain feature which imply it will contribute to the SA.
- They also analyzed the frequency of words or bigram phases.
- 
####Hypothesis####
- The most important hypothesis of this paper is they think the valuable information will be extracted in time with their method when certain mass emergency emerges.

####Data####
- They collected tweets that posted during four different emergency events; every emergency event got roughly 500 on-topic tweets that are manageable set for human annotation and provide sufficient training data for machine learning classification.

####Experiment####
- First, they tried to evaluate the performance of classifier by processing one feature at a time on all the datasets. Then, they created another dataset, which got 500 SA and 500 non-SA tweets from all four events.
They use mean accuracy over 10 fold cross-validation to measure performance and used a classifier trained on data from certain event to test data from other event. After all they compared the results and get the conclusion, most important features for a valuable tweet.

####Result####
- One feature (personal or impersonal, formal or informal) can decide whether the tweet is useful for SA, the combination of features can tell it more clear, classifier from same type events are much accurate than use classifier from different type of events, people act similar when similar events happen.

####Assumption####
- All the events will not affect the communication system; people from disaster area can still connect with outside people. Or it cannot be timely enough to indicate emergency situation.

####Synthesis####
- Did not mention how to find on-topic tweets, it should be a very important part.
- If people still can connect with other people who can post tweet they can get connect with rescuer too, maybe the priority is not really high. Call 911 is a better way than write a tweet I think.

####Related Paper####
- Machine Learning Applied to Object Recognition in Robot Search and Rescue Systems    Helen Flynn, Keble College University of Oxford
Practical tech, robot can adopt to more complex environment than human in emergency rescue.

- Classifying Text Messages for Emergency Response   
Cornelia Caragea, Hyun-Woo Kim, Prasenjit Mitra, and John Yen
Also provide the priority handle, which can identify what is really emergency.
