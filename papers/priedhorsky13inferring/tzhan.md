Overview

The authors of this paper use a scalable, content-based approach to estimate the location of tweets. And, they also propose novel metrics of accuracy, precision, calibration to evaluate their findings.


Algorithm

They use an inference method based on Gaussian mixture models(GMMs). And for each unique n-gram, fit a two-dimensional GMM to model its geographic distribution. 
Then they focus on more specific areas, they evaluate the accuracy: the comprehensive accuracy error(CAE), an simple accuracy error(SAE). About the precision, they propose the area region(PRA). And for the calibration, it is tested by measuring the difference between anestimate’s claimed probability that a particular point is the true origin and its actual probability.
They also consider the GMM-All-Tweets and GMM-One as the baseline weighting algorithms.

Hypothesis

The tweets can help public health, politics and other domains get some useful information and those tweets will contain the signals of location of people who creates them.
 
Data

They used the Twitter Streaming API to collect an approximately continuous 1% sample of all global tweets from January 25, 2012 to January 23, 2013. About 0.8% to 1.6% of these tweets, depending on timeframe, had a geotag , so it is about 13 million geotagged tweets.
Then they tokenized the message text (tx), user description (ds), anduser location (lo) fields, which are free-text, into bigramsby splitting on Unicode character category and script boundaries.
For the language (ln) and time zone (tz) fields, they form n-grams by simply removing whitespace and punctuation and converting to lowercase.

Experimental

Each experiment is implemented using a Python script, and the schedule of the script has four parameters: Training duration, Test duration, Gap, Stride.
Then, they present their geographic gaussian mixture model approach. Motivation, Weighting by quality properties, Weighting by error, Weighting by optimization, Baseline weighting algorithms.

Results

Considering accuracy (MCAE), GMM-Err-SAE10 is 10% better than the best optimization-based algorithm and 26% better than the best property-based algorithm the baselines GMM-One and
GMM-All-Tweets performed poorly.
About the precision (MPRA50), the advantage of GMM-Err-SAE10 is further highlighted; it is 50% better than GMM-Opt-ID and 38% better than GMM-Qpr-Covar-Sum-Prod.
Through the authors’ research, we can see something about calibration. While GMMErr-
SAE10 is somewhat overconfident at coverage level 0.5(OC50 = 0:453 instead of the desired 0.5), GMM-Err-SAE4is calibrated very well at this level (OC50 = 0:497) and has better calibration at coverage 0.9.
While the informativeness of each individual n-gram may be low, the fact that low-frequency words occur in so many tweets can impact overall accuracy
User location and time zone are the mostaccurate fields, with tweet text and language important for
success rate.

Assumptions

Frankly, I do not find any assumptions.

Synthesis

There is no denying that this paper is almost a perfect paper. Yeah, that is the truth. And I only have some suggestions about it, the paper mentions that they predict the location of the people create the tweets also by what language they use. And except some little used languages, they collect the tweets have different languages as dataset. To translate those tweets will be a large workload, and different languages comes with different cultures, sometimes the city name or something else appears in their tweets do not mean they are in there, it is hard to understand the meaning of their twitter (there are many Americans could not get my point when I talk to them). So there must have many errors of predict those kinds of tweets, it may affects the result finally. 

Related papers

H. Akaike. A new look at the statistical model identification. Automatic Control, 19(6):716–723, 1974.
10.1109/TAC.1974.1100705.
This paper presents some kinds algorithms of statistic model identification, it is just provide you a good way to do the related research, you can use the way they offer to do the statistic model identification. But in the paper we do the summary, the authors focus on more specific areas, and use really a lot of methods to do the research.

S. Chandra et al. Estimating Twitter user location using social interactions – A content based approach. In Proc.Privacy, Security, Risk and Trust (PASSAT), 2011.10.1109/PASSAT/SocialCom.2011.120.
This paper also shows some researches on the location of people create tweets. Besides they have different evaluate way to a tweet with the paper we do this summary, the most obvious different is that this paper only focus on the dialogue and reply-tweet message in a tweet, without the use of any external information to predict the location. But in that paper, we use the contain of tweets, but also the time zone, the language and etc., to help us predict the location of people create tweets.
