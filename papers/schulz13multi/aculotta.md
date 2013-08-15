####Overview####
This paper proposes an algorithm to estimate the geographical coordinates of a tweet based on evidence from the message text and user profile.

####Algorithm####
A number of indicators are used to locate a tweet, including:
- They use DBPedia to map words in the text to places with known geocoordinates (e.g., Fedex Field)
- They follow links to services such as Foursquare and Flickr, which provide exact geocoordinates
- They lookup words in the location field of the profile in a list of known locations
- For general web addresses, they consider the top-level domain and the IP address, which is mapped to a location using IPinfoDB
- The time zone from the profile

Each indicator above is mapped to polygon depending on the source. For example, web domains are mapped to country polygons.

To predict the location of a new tweet, the indicators above are combined by stacking each polygon. The center of polygon with the highest overlap is returned as the predicted location.

As part of this stacking, a weight is attached to each indicator. This weight is optimized on a held-out set of tweets to minimize error using the downhill simplex method.

####Hypothesis####
- The general hypothesis is that tweets can be accurately located based on these indicators
- A more specific hypothesis is that the optimization method described above significantly improves accuracy.

####Data####
Describe the data used in the experiments

####Experimentals####
Briefly describe how are the experiments are organized.

####Results####
Describe the results and their significance.

####Assumptions####
List some of the important assumptions the authors make in their work.

####Questions####
List 2-3 questions you have about the paper.

####Related Papers####
List 2-3 papers that are most similar to this paper. For each, briefly list how this paper is different.
