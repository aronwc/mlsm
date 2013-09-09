####Overview####
The authors describe methods of using text sentiment to as a means of capturing public opinion.

####Algorithm####
The authors use a deterministic approach that counts instances of positive and negative sentiment
words in the context of a topic keyword to create a sentiment ratio of positive and negative words
by relativity frequency. They smooth this ratio by using a moving average over a window of the past
k days. They use a simple keyword approach for their message retrieval task.

####Hypothesis####
Sentiment analysis of Twitter messages can be used to predict public sentiment traditionally
captured by polling.

####Data####
- Tweets
  - 1 billion tweets posted over 2008-2009
  - range of 100,000 to 7 million a day
  - no preprocessing or filtering was done
- Polls
  - Index of Consumer Sentiment is used to capture consumer confidence.
  - Political opinion is captures using Gallup's daily tracking poll for Obama's performance
  and a set of tracking polls from the 2008 election cycle.

####Experiments####
Using simple topic keywords, the authors find tweets that correspond to their polls and calculate
a sentiment score using relativity frequencies of positive and negative sentiment words. They smooth
sentiment ratio using a moving average. They then do a correlation analysis of this sentiment ratio
with the polling data. To test is the text sentiment is a leading indicator of polls, the authors
introduce a lag parameter.

####Results####
Their model seems to capture broad trends in the polling data. Increasing smoothing tends to
increase correlation, but at the expense of smoothing over some of the more volatile polling
data points, so it seems the model is best used for identifying broad trends. Also, with the
data they had, the text data was a poor predictor early on but became better with time (as more
users joined Twitter and more tweets were produced.)

####Assumptions####
There are several sections in this paper where the authors describe certain problems:
- The data was not filtered to exclude non-U.S. or non-English tweets.
- Nothing was done to account for the change in demographics and behavior of Twitter users
over the time data was collected.
- There are problems with their sentiment detection due to a lack of POS tagging.

The authors are transparent in their description of the techniques they used and where
they can be improved, but there is an assumption that correcting for these issues will
change their results for the beter.

####Synthesis####
As described above, the authors point out several ways their experiments could be improved,
such as using a better suited lexicon for online text and doing more preprocessing of the
Twitter messages. They also discuss the possibility of using demographic information in order
create account for the stratified sampling done by traditional polls. It would be interesting
to try these techniques to see how they affect the authors' results. In addition, it would
be interesting to try other sentiment detection and analysis techniques and see if those improve
the results.

####Related Papers####
- Tumasjan, Andranik, et al. "Predicting Elections with Twitter: What 140 Characters Reveal about Political Sentiment." ICWSM 10 (2010): 178-185.
  - Uses tweets surrounding German elections and LIWC, a text analysis software, to generate profiles of politicians.
- Grimmer, Justin, and Brandon M. Stewart. "Text as data: The promise and pitfalls of automatic content analysis methods for political texts." Political Analysis (2013).
  - Survey paper of text analysis techniques for political scientists.
