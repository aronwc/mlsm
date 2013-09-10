####Overview####

This paper connects traditional measures of public opinion from polls with sentiment measured from analysis of text from Twitter. It also demonstrates that simple text analysis techniques are correlated with polling data on consumer confidence and political opinion.

####Algorithm####

-	Message retrieval: To identify with keywords the topic of a message. 
- Opinion Estimation: Messages are referenced as positive or negative with the ration of positive words over negative words in the message. These positive and negative words are defined by the lexicon OpinionFinder. The ration can be also smoothed.
- Correlation Analysis: the text-poll correlation is the goodness-of-fit metric for fitting slope and bias parameters. The aim of this algorithm is to measure the correlation of the poll and a text window ending L days before the poll outcome.
- Forecasting Analysis: It consists to train a model until a day to predict the evolution the L next days.


####Hypothesis####

- Twitter messages can describe public opinion.
- Text sentiment is a leading indicator.

####Data####
To experiment sentiment measured from text, text data come from the microblogging site Twitter:
- It is made of 1 billion Twitter messages posted over the year 2008-2009, which represent 100,000 to 7 million messages per day.
- The analysis will ignore non-English messages.

To compare the sentiment measured from text to public opinion measured, public opinion surveys from multiple polling organizations are used. 
3 polls are used for consumer confidence:


- Consumer Confidence Index from the Consumer Board.
- The index of Consumer Sentiment (ICS) from the Reuters/University of Michigan Surveys of consumers.
- The Gallup Organization’s “Economic Confidence” index.


2 other polls are used for political opinion:


- Gallup’s daily tracking poll for the presidential job approval rating for Barack Obama over the course of 2009.
- A compilation of 491 data points from 46 different tracking polls during the 2008 U.S. presidential election cycle provided by Pollster.com
It can be noticed that Gallup’s polls are reported as three-day rolling averages.

####Experimental####

- The experiment consists to apply the algorithms on the consumer confidence and political opinion data. 
- The author of the article uses the 2 first algorithms to obtain the text analysis of Twitter messages.
- (1) “jobs” sentiment ratio is compared to the two measures of consumer confidence.
- (2) Correlation analysis algorithm is applied to know which data is the leading indicator.
- (3) Forecasting analysis is also applied to measure if text analysis can predict poll.
- (4) The sentiment ration for “Obama” is analyzed and compared to two series of polls, presidential job approval in 2009 and presidential election polls in 2008.
- These experiments are repeated with different smoothing.

####Results####

- Experiment 1 shows that the correlation between the two analysis is 73.1%.
- Experiment 2 shows that correlation is higher for text leading the poll. Text sentiment is a leading indicator.
-  Text sentiment information is better than polls to determine long-term trends.
- The larger the smoothing window is, the better the correlation is. 
-  Forecasts for one month in future achieve 77.5% correlation.
- For experiment 4, topic frequencies correlate much more with polls than the sentimental scores.
- Text analysis is a faster and less expensive substitute for traditional polling.

####Assumptions####

- Keywords are sufficient to distinguish topics.
- Polls are the gold standards.

####Synthesis####

- It would be good for me to distinguish two groups: opinion-makers and opinions-holders
-  Twitter messages which are “retweetted” deserves more important weight because they show a larger opinion.


####Related Papers####

- Samantha Finn and Eni Mustafaraj, Real-Time Filtering for Pulsing Opinion in Social Media
- David Osimo and Francesco Mureddu, Research Challenge on Opinion Mining and Sentiment

