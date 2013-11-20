#Overview
They propose a scalable, content-based approach to estimate the location of tweets using a novel yet simple variant of gaussian mixture models.

#Algorithm
1. For each n-gram that appears more than a threshold number of times in the training data, fit a GMM to the true origin points of the tweets in the training set that contain that n-gram. This n-gram/GMM mapping forms the trained location model.
2. To locate a test tweet, collect the GMMs from the location model which correspond to n-grams in the test tweet. The weighted sum of these GMMs — itself a GMM — is the geographic density function which forms the estimate of the test tweet’s location.

#Hypothesis
* A plausible hypothesis is that the more complex CAE metric is not needed, and algorithm accuracy can be sufficiently well judged with the simpler and faster SAE.
* Consistent with other methods, toponyms provide the most important signals.
* The mean weight assigned to a category over all n-grams in the good set is equal to the mean weight for the same category in the bad set.

#Data
1. They used the Twitter Streaming API to collect an approximately continuous 1% sample of all global tweets from January 25, 2012 to January 23, 2013,  depending on timeframe, contained a geotag,  yielding a total of approximately 13 million geotagged tweets.
2. They  tokenized the message text (tx), user description (ds), and user location (lo) fields, which are free-text, into bigrams by splitting on Unicode character category and script boundaries and then further subdividing bigrams which appear to be Japanese using the TinySegmenter algorithm.
3. For the language (ln) and time zone (tz) fields, they  form n-grams by simply removing whitespace and punctuation and converting to lowercase.

#Experiments
1. For each n-gram that appears more than a threshold number of times in the training data, fit a GMM to the true origin points of the tweets in the training set that contain that n-gram.
2. To locate a test tweet, collect the GMMs from the location model which corresponded to n-grams in the test tweet. The weighted sum of these GMMs — itself a GMM — was the geographic density function which forms the estimate of the test tweet’s location.
3. Weighting by quality properties
4. Weighting by error
5. Weighting by optimization
6. Baseline weighting algorithms

#Results
1. Considering accuracy (MCAE), GMM-Err-SAE10 is 10% better than the best optimization-based algorithm (GMM-OptID) and 26% better than the best property-based algorithm (GMM-Qpr-Covar-Sum-Prod),  These results suggest that a weighting scheme directly related to performance, rather than the simpler quality properties.
2. 


#Assumptions
It's jard to find a clear assumption.

#Synthesis


#Related papers
