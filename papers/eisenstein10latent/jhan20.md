####Overview####
- This paper presents a multi-level generative model that reasons jointly about latent topics and geographical regions.

####Algorithm ####
- Cascading topic model
- Mean-field variational inference

####Hypothesis####
- The general hypothesis is that lexical variation is influenced geographical regions and an author’s geographic location can be predicted from raw text.

####Data####
- They use messages collected over the first week of March 2010 from the “Gardenhose” sample stream.
- They use only messages that are tagged with physical (latitude, longitude) coordinate pairs from a mobile client.
- They use messages only from authors who follow fewer than 1,000 other people, and have fewer than 1,000 followers.

#### Experiment####
- They compare several approaches for predicting author location
 - Mixture of Unigrams
 - Supervised Latent Dirichlet Allocation
 - Text Regression
 - K-Nearest Neighbors 
- The error metrics are the mean and median distance between the predicted and true location in kilometers.

####Results####
- The geographic topic model achieves the strongest performance on all metrics.
- K-nearest neighbors performs poorly at all values of K.

####Assumption####
- One important modeling assumption is tweets that carry geocoordinates are not systematically different from other tweets. 

####Synthesis####
- My next step would be to involve other factors such as post time and users mentioned to improve the prediction accuracy.
- What is the accuracy if we predict all the tweets with geocoordinates without filtering tweets form some authors.

####Related Papers####
- Cheng, Zhiyuan, James Caverlee, and Kyumin Lee. "You are where you tweet: a content-based approach to geo-locating twitter users." Proceedings of the 19th ACM international conference on Information and knowledge management. ACM, 2010.
 - They propose a probabilistic framework for estimating a Twitter user's city-level location based purely on the content of the user's tweets.
- Hecht, Brent, et al. "Tweets from Justin Bieber's heart: the dynamics of the location field in user profiles." Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. ACM, 2011.
 - This paper performed a simple machine learning experiment to determine whether they can identify a user's location by only looking at what that user tweets.

