# Overview
The paper aims to demonstrate that surveys could be replaced by social media analysis which is far cheaper. The experiments go through political and economical sentiment.

# Algorithm
As the interesting part of a tweet is only contained in a small part of it, they have used a transparent and deterministic approach by counting positive and negative messages using OpinionFinder. This tool contains a list of 1.6k postive words and 1.2k marked as negative words.
- >= 1 positive word -> positive message. Same thing happens for negative messages. Then a ratio is evaluated between the positive and negative messages on a day about the same topic.
- Moving Average Aggregate Sentiment. As the daily sentiment analysis at Twitter varies more than at polls, they have decided to smooth the Twitter results.

# Hypothesis
- If people are writing about the topic, they are giving their opinion, so there is presence of sentiment words in a message.
- For consumer confidence the most suitable keywords are 'economy', 'job' and 'jobs'. For presidential approval is 'obama'. For elections, 'obama' and 'mccain'.
- Polls provide 100% clear the population sentiment.

# Data
Two main sources: Twitter and polls.
- [Twitter] 1 billion tweets with no distinction of language or location. ~100k to 7m tweets per day.
- [Poll] Surveys about consumer confidence from ICS and Gallup Organization’s “Economic Conﬁdence”. The first one was based on five questions/month to a representative population about the health of the economy
and their ﬁnances. Two daily questions that rate the overall economic health of the country.
- [Poll] Surveys about political opinion. Two sets, one was a daily tracking about rating Obama, and the other was an election survey during the election cycle from pollster.com (491 data points from 46 surveys).

# Experimentals
Procedure:
- Message Retrieval. First they selected the tweets that contained a topic keyword manually specified.
- Opinion Estimation. A tweet is categorized as positive, negative or both. As the method or algorithm to determine the category of a tweet was based on a lexicon for well-written standard, the results obtained were not good at all.

Experiments performed:
- [Related experiments] Classification in aggregate sentiment is worthwhile (MacDonald, Hopkins and Kings). Tested at Facebook posts (Lindsay)
- The text-poll correlation is calculated as the sum of a bias parameter plus daily average data multiplied by a bias parameter more Gaussian noise. For the comparison they have introduced a lag hyperparameter L into the model.
- Forecasting analysis. With the lag parameter, it is checked how well text-based model could predict poll values.
- Obama 2009 job acceptance and 2008 elections.

# Results
- The text sentiment prediction based on OpinionFinder on tweets is not a good experiment because of the types of lexicons.
- If we take the average of 15 days of tweets, they obtained a 73.1% of correlation.
- This lag parameter allows to show a better performance of correlation if text leads polls. Also, as smoothing increases the correlation augments: for Gallup, 7, 15, and 30-day windows peak at r = 71.6%, 76.3%, and 79.4% respectively.
- With 30 day smoothing, the sentiment ratio results obtained were 63.5%.
- For the terms job and economy correlate with the Gallup poll: 10% and 7% respectively
- Text sentiment is a poor predictor of consumer conﬁdence and polls results, but these bad results are justified with the bad representation of Twitter of the world population in 2008.
- The results obtained for Obama job approval were good in terms of correlation with polls and with other experiments, as Facebook experiment.
- The results obtained for elections were not that good, as the experiment was more difficult to be performed.

# Assumptions
- No neutral opinions. It is ok to treat neutral opinions as positive and negative opinions.

# Synthesis
 - For performing these experiments, as Twitter has improved, I would definitely use hashtags instead of keywords. In this case maybe we can obtained a better results for the election correlation.
 - I would restrict the location of tweets for more correlation accuracy. I would make polls location similar to tweets location

# Related papers
- Tumasjan, A., Sprenger, T. O., Sandner, P. G., & Welpe, I. M. (2010). [Predicting Elections with Twitter: What 140 Characters Reveal about Political Sentiment.](http://www.aaai.org/ocs/index.php/ICWSM/ICWSM10/paper/viewFile/1441/1852) ICWSM, 10, 178-185.
  - This paper has a depth vision of Twitter reflecting election sentiment. It analyzes more data, even politician profile. They obtained better results as they took more data and made the experiments in 2009.
- Conover, M. D., Gonçalves, B., Ratkiewicz, J., Flammini, A., & Menczer, F. (2011, October). [Predicting the political alignment of twitter users.](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=6113114&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6113114) In Privacy, security, risk and trust (passat), 2011 ieee third international conference on and 2011 ieee third international conference on social computing (socialcom) (pp. 192-199). IEEE.
  - The present paper provides a good background at machine learning applied to twitter. It is based only on political predictions using more methods. For example, they performed the SVM trained on hash tag metadata. They got to obtain a 91% accuracy.
