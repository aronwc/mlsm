**Overview**
This paper presents a method of identifying a Twitter user's location using the twitter message's text and the user's profile information and features inferred from this data and compares it against the message's geotag for accuracy.

**Algorithm**
The data collected and processed from tweets were analyzed with a geographic gaussian mixture model with several focuses in order to identify the best-performing tests. If there is a significantly prominent marker in any feature, the location is then identified as some probability distribution across the entire globe. 

**Hypothesis**
As in the other location-identification experiments, the main hypothesis is that there are location-specific features that can be identified in tweets with any significant accuracy.

**Data**
1% of twitter data was collected globally for about a year, then filtered for those messages which contained geotags. This resulted in a set of 13 million tweets with a clear location.
The features of these tweets that were analyzed in tests were the text itself, the user's description, the user's self-reported location, the language in which the message was composed, and the message's listed time zone.

**Experiments**
The calibration methods vary the weights either by quality, error, or optimization. Each of these have a different way of setting GMM weights. For quality methods, a higher weight is assigned to GMMs which better fit the data; this produced two methods worthy of testing. Error methods are weighted against the error of the GMM for each n-gram. This produced three error methods, which the exponent varying for each. Lastly, weighting by optimization involves learning the weight directly from the data features. For comparison purposes, there are also two baseline methods produced: GMM-All-Tweets, which fits a GMM to all tweets, and GMM-One, which weights all n-gram mixtures equally.

**Results**
The results of these experiments are evaluated with several different metrics: CAE, MCAE, SAE, and MSAE all represent accuracy, where PRA and MPRA represent precision.
To avoid directly reproducing the results directly, GMM-Er-SAE10 performs the best for MCAE and MSAE tests, as well as MPRA50. However, GMM ERR-SAE4 performs the best for OC50, where GMM-All-Tweets performs best for OC90.
They also vary several parameters they use to calibrate their testing efficiently: training duration, minimum number of n-gram instances, and train-test delay. In the same vein, they individually and comparatively analyze the tweet features to find those which are most indicative of location, finding that user location is most helpful, but user language is most accurate. 

**Assumptions**
There are several assumptions in the features analyzed: the paper is trusting that self-reported data is accurate and updated whenever the user moves or travels; that the user has the language set as their native language, and they are from a location where their native language is predominant, and other accuracy-conflating statements. 
However, most of these issues do not frequently occur and can likely be ignored with such a large data set. 

**Synthesis**
It may be interesting to expand this to a longitudinal study to see what changes may occur in predictive terms and distributions. 

**Related Papers**
Mahmud, Jalal, Jeffrey Nichols, and Clemens Drews. "Where Is This Tweet From? Inferring Home Locations of Twitter Users." ICWSM. 2012.
 	Using tweet contents and posting features, this paper describes a method of identifying the author's location: city-level, state-level, or time-zone level. However, this paper focus on classification, rather than distribution.

Paradesi, Sharon Myrtle. "Geotagging Tweets Using Their Content." FLAIRS Conference. 2011.
	This paper attempts to geotag tweets using just their content. This relies on specific mentions of addresses and landmarks within the tweets. 
