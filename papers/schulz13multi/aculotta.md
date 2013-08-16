####Overview####
This paper proposes an algorithm to estimate the geographical coordinates of a tweet based on evidence from the message text and user profile.

####Algorithm####
A number of indicators are used to locate a tweet, including:
- They use [DBPedia](http://dbpedia.org) to map words in the text to places with known geocoordinates (e.g., Fedex Field)
- They follow links to services such as Foursquare and Flickr, which provide exact geocoordinates
- They lookup words in the location field of the profile in a list of known locations
- For general web addresses, they consider the top-level domain and the IP address, which is mapped to a location using [IPinfoDB](http://ipinfodb.com)
- The time zone from the profile

Each indicator above is mapped to polygon depending on the source. For example, web domains are mapped to country polygons.

To predict the location of a new tweet, the indicators above are combined by stacking each polygon. The center of polygon with the highest overlap is returned as the predicted location.

As part of this stacking, a weight is attached to each indicator. This weight is optimized on a held-out set of tweets to minimize error using the [downhill simplex method](http://en.wikipedia.org/wiki/Nelder–Mead_method).

####Hypothesis####
- The general hypothesis is that tweets can be accurately located based on these indicators
- A more specific hypothesis is that the optimization method described above significantly improves accuracy.

####Data####
- They collect 80 million tweets from the Spritzer Twitter stream from September 2011 to February 2012.
- Of these, they keep the 1.03 million which carry exact geocoordinates (from smartphones).
- Of these, they reserve 10% for optimizing the indicator weights. The remaining (103K) are used for testing the accuracy.

####Experimentals####
- For each of the 103K tweets in the test set, the predicted location is computed using the methods above.
- Three metrics are computed:
  - AED: Average error distance. 
  - MED: Median error distance.
  - MSE: Mean squared error
  - Recall: the percentage of tweets for which some prediction was made.
- The experiments compare each indicator in isolation, then compare them all together. Additionally, comparison is made between the optimize versus unoptimized method.

####Results####
- The best approach uses all indicators except for two (IP address and geoname lookup for individual words). This results in an average error of 1,400 km, with a recall of 92%.
- Optimizing the weights results in a big improvement in accruacy (average error of 1408km vs 1931km)
- The best individual indicator by far is the one based on location services (Foursquare, Flickr), which has an average error of 15km and a recall of 18%.

####Assumptions####
Since the accuracy measures are only computed on tweets that carry geocoordinates, one important assumption is that tweets that carry geocoordinates are not systematically different from other tweets. 

####Questions####
- What is the result without using the location service indicator? This seems to be a very important indicator, but seems to be an artifact of this data source. This will probably not generalize to geolocating other text sources.
- Is there a bias introduced by not splitting the data chronologically?
- What is the accuracy if the system is forced to predict every message (instead of the 92% they report)?
 
####Related Papers####
- Hale, S., and Gaffney, D. 2012. Where in the world are you? Geolocation and language identification in Twitter. In Proceedings of ICWSM’12, 518–521.
  - The present paper combines many more indicators besides simply evidence from the location field. 
- Cheng, Z.; Caverlee, J.; and Lee, K. 2010. You Are Where You Tweet : A Content-Based Approach to Geo-locating Twitter Users. In Proceedings of CIKM ’10, 759–768.
  - The present paper does not use only the text of the tweet. 
