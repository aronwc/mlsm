####Overview####
This paper compares the sentiment measured from analysis of text from Twitter and measures of public opinion derived from polls.

####Algorithm & Experiment####
- Identify messages relating to the topic
 - For each topic they use messages that contain a topic keyword.

- Determine whether messages express positive or negative opinions 
 - They define positive and negative words according to the subjectivity lexicon from OpinionFinder.
 - They define the sentiment score on a day as the ratio of positive versus negative messages on the topic.
 - They smooth the sentiment ratio with a moving average over a window of the past several days.

- Correlation Analysis
 - The correlation is defined as the goodness-of-fit metric for fitting slope and bias parameters in a one variable linear least-squares model.
 - They compare the poll with the text window ending several days before the poll outcome.

- Forcasting analysis
 - They train the model only on historical data through day t-1, then predict using the window ending on day t.

####Hypothesis####
- The general hypothesis is that sentiment measured form Twitter can reflect public opinion.

####Data####
- 1 billion Twitter messages posted over the years 2008 and 2009.
- Gallup’s daily tracking poll for the presidential job approval rating for Barack Obama over the course of 2009.
- Tracking polls during the 2008 U.S. presidential election cycle, asking potential voters whether they would vote for Barack Obama or John McCain, consisting of 491 data points from 46 different polls.

####Results####
- The text sentiment is a leading indicator.
- The text sentiment measure captures information related to the polls.
- The text sentiment information is volatile, so it is best used to detect long-term trends.
- Topic frequency may not have a straightforward relationship to public opinion.

####Assumption####
- One important assumption in this paper is that the polls are treated as the ground truth that can reflect real public opinion. 

####Synthesis####
- The approach to sentiment analysis in this paper seems simple and might not reflect the real sentiment. We can apply other machine learning approach to analyze the sentiment from texts in Twitter.
- They only analyze the text in “tweets”. However the comments or “retweets” can also be good indicator of the sentiment.

####Related Papers####
- Kouloumpis, Efthymios, Theresa Wilson, and Johanna Moore. "Twitter sentiment analysis: The Good the Bad and the OMG!." ICWSM. 2011.
- Bollen, Johan, Huina Mao, and Xiaojun Zeng. "Twitter mood predicts the stock market." Journal of Computational Science 2.1 (2011): 1-8.
- Gilbert, Eric, and Karrie Karahalios. "Widespread Worry and the Stock Market." ICWSM. 2010.

