####Overview####
- This paper proposes a classifier that is able to automatically detect Twitter messages that may contribute to situational awareness

####Algorithm ####
- A number of features are used to identify tweets that contribute to situational awareness
 - Unigrams and their raw frequency
 - Bigrams and their raw frequency
 - Part-of-speech tags
 - Subjectivity of tweets (Objective/Subjective)
 - Register of tweet (Formal/Informal)
 - Tone of tweet (Personal/Impersonal)
- They use Naïve Bayes (NB) and Maximum Entropy (MaxEnt) for classification.

####Hypothesis####
- The general hypothesis is that situational awareness tweets can be detected based on the above features

####Data####
- They collected a random sample of roughly 500 tweets broadcast during four natural disaster events that contained one of their keywords.

#### Experiment####
- They evaluated the performance of the SA classifier by introducing one feature at a time on datasets from four different events.
- They created a fifth dataset by randomly selecting 500 situational and 500 non-situational awareness tweets from all events. 
- Performance was evaluated by taking the mean accuracy over 10 fold cross-validation and splitting the data 90% for training and 10% for testing
- They used a classifier trained on data from previous events to classify data from new events

####Results####
- Using any one of the features including objective, impersonal and formal traits improved the accuracy for classifying tweets with SA content, and using all the features together helped improve overall performance even more.
- The amount the linguistic features helped varied from dataset to dataset.
- The performance is better when using events of similar type to classify each other, while the performance is poor when using events of different types.

####Assumption####
- Since this paper only analyzes tweets during four natural disaster events, one assumption is that tweets posted during other crisis events are similar to the ones in these events.

####Synthesis####
- Since they use historical data, they know what event was going on and hence are able to use some keywords to detect tweets that contribute to situational awareness. However for emergency events, we cannot predict and identify them. Thus we first need to detect the emergency events and then detect the tweets.
- We might be able to get more detailed information about the events and do fine-grained classification such as situations in different places and people’s reactions.
- The location information can also help to improve the classification as we can identify the tweets form locations where the events take place.

####Related Papers####
- Gupta, Aditi, and Ponnurangam Kumaraguru. "Credibility ranking of tweets during high impact events." Proceedings of the 1st Workshop on Privacy and Security in Online Social Media. ACM, 2012.
 - This paper finds that only 17% of the total tweets posted about the event contained situational awareness information were credible. So they propose a supervised machine learning approach using some features, e.g.  number of unique characters, swear words, pronouns, and emoticons in a tweet, to rank tweets according to their credibility score.
- Mendoza, Marcelo, Barbara Poblete, and Carlos Castillo. "Twitter Under Crisis: Can we trust what we RT?." Proceedings of the first workshop on social media analytics. ACM, 2010.
 - They analyze the activity related to the 2010 earthquake in Chile and find that the propagation of tweets that correspond to rumors differs from tweets that spread news.
