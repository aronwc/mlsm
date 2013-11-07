Overview
========

The authors propose a scalable, content-based approach to estimating the location of tweets using a simple variant of Gaussian mixture models. They also propose metrics of accuracy, precision, and calibration.

Algorithm
=========

1.  For each n-gram that appears more than a certain threshold number of times in the training data, a Gaussian mixture model is fit to the true origin points of the tweets in the training set that contain that n-gram. This forms the trained location model.

2.  To locate a given tweet, the GMMs from the location model which correspond to n-grams in the tweet are collected. The weighted sum of these GMMs is the geographic density function which forms the estimate of the tweet’s location. The weights of these GMMs are set by three methods:

    1.  Weighting by quality properties - in this approach, higher weight GMMs are assigned if they have a crisper signal or fit the data beter.

    2.  Weighting by error - weigh each n-gram by its error among the training set.

    3.  Weighting by optimization - assign each n-gram a set of features with their own weights, let each n-gram’s weight be a linear combination of the feature weights, and use gradient decent to find feature weights such that the total error across all n-grams is minimized.

Hypothesis
==========

The main hypothesis of the paper seems to be that even without geotagging, the location from which a tweet was published can be accurately (that is, with quantitative confidence) determined.

Data
====

-   The Twitter Streaming API was used to collect an approximately continuous 1% sample of all global tweets from Janurary 24, 2012 to Janurary 23, 2013.

-   Between 0.8% and 1.6% of these contained a geotag giving about 13 million geotagged tweets.

Experiments
===========

Each experiment first generates a test schedule with four parameters:

1.  Training duration - the length of time from which to select training tweets.

2.  Test duration - The length of time from which to select test tweets.

3.  Gap - the length of time between the end of the training data and the beginning of the test data.

4.  Stride - The length of time from the beginning of one training set to the beginning of the next.

Each experiment was tested using one of the following algorithms:

-   GMM-Err-SAE10

-   GMM-Err-SAE4

-   GMM-Opt-ID

-   GMM-Err-SAE2

-   GMM-Qpr-Covar-Sum-Prod

-   Gaussian Opt-ID

-   GMM-Opt-Both

-   GMM-Opt-Attr

-   GMM-One

-   GMM-Qpr-AIC

-   GMM-All-Tweets

Results
=======

-   The GMM-based approach yielded global mean accuracy of about 1800 kilometers in the best case and a precision of less than 900,000 square kilometers.

-   Training on only about 30,000 tweets was enough to accurately determine location of tweets.

-   In terms of fields, the user’s location and timezone provided the best results.

Assumptions
===========

Honestly, I’m hard pressed to come up with any assumptions made by the authors. All of the work is incredibly well studied and almost no

Synthesis
=========

This paper is really quite amazing, save the best for last I guess. Now being able to accurately determine the location of tweets as presented, it would be interesting to see how well the number of tweets coming from a particular area matches up with its population. That is, does a big city tweet more than a smaller one just because it has more people, or are there cases of vocal minorities?

Related Papers
==============

-   Schulz et al. (2013) reported accurate results using a scheme which combines multiple geocoding sources, including Internet queries.

-   Numerous authors have worked on similar work such as this but to pre-defined regions such as cities and counties. Cheng, Caverlee, and Lee (2010) applied a variant of naive Bayes to classify message by city, Hecht et al. (2011) used a similar classifier at the state and county level, Kinsella, Murdock, and O’Hare (2011) used language models to classify message by neighborhood, city, state, zip code, and country. Mahmud, Nichols, and Drews (2012) classified users by city with higher accuracy than Cheng, Caverlee, and Lee (2010) by combining a hierarchical classifier with many heuristics and gazetters.

-   Chang et al. (2012) is closest to the current work. They classified tweet text by city using GMMs.

References
==========

Chang, Hau-wen, Dongwon Lee, M. Eltaher, and Jeongkyu Lee. 2012. “@Phillies Tweeting from Philly? Predicting Twitter User Locations with Spatial Word Usage.” In *Advances in Social Networks Analysis and Mining (ASONAM), 2012 IEEE/ACM International Conference on*, 111–118. doi:10.1109/ASONAM.2012.29.

Cheng, Zhiyuan, James Caverlee, and Kyumin Lee. 2010. “You are where you tweet: a content-based approach to geo-locating twitter users.” In *Proceedings of the 19th ACM international conference on Information and knowledge management*, 759–768. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/1871437.1871535>.

Hecht, Brent, Lichan Hong, Bongwon Suh, and Ed H. Chi. 2011. “Tweets from Justin Bieber’s heart: the dynamics of the location field in user profiles.” In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 237–246. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/1978942.1978976>.

Kinsella, Sheila, Vanessa Murdock, and Neil O’Hare. 2011. “‘I’m eating a sandwich in Glasgow:’ modeling locations with tweets.” In *Proceedings of the 3rd international workshop on Search and mining user-generated contents*, 61–68. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/2065023.2065039>.

Mahmud, Jalal, Jeffrey Nichols, and Clemens Drews. 2012. “Where Is This Tweet From? Inferring Home Locations of Twitter Users.” In *ICWSM*, ed. John G. Breslin, Nicole B. Ellison, James G. Shanahan, and Zeynep Tufekci. The AAAI Press. [http://dblp.uni-trier.de/db/conf/icwsm/icwsm2012.html MahmudND12](http://dblp.uni-trier.de/db/conf/icwsm/icwsm2012.html MahmudND12 "http://dblp.uni-trier.de/db/conf/icwsm/icwsm2012.html MahmudND12").

Schulz, Axel, Aristotelis Hadjakos, Heiko Paulheim, Johannes Nachtwey, and Max M������ser. 2013. “A Multi-Indicator Approach for Geolocalization of Tweets.” In *International AAAI Conference on Weblogs and Social Media*. <https://aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/view/6063/6397>.
