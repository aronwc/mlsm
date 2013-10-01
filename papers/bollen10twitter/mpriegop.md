####Overview####
The paper evaluates if its possible to predict the behavior of the stock market by using and Twitter information (sentiment classification info). They used GPOMS and OF tools for categorize tweets and examined the correlation between this categorization and the Dow Jones variations in closing values.

####Algorithm####
The algorithm or the technique to measure if Twitter can predict stock market is:
1 Obtain public mood daily variation series with OF and GPOMS.
  - Opinion Finder provides a positive or negative range, so we obtain one time series of daily mood.
  - GPOMS has 6 mood dimensions, so six time series.
  - They normalize the values before studying them.
  - For the DIJA values we calculated the day value based on the difference between day t and t-1
2 They performed a Granger causality for correlating DIJA to GPOMs and OF values of the past n days.
  - This model is based on two sums. One is the sum of lagged values of one time series (the one that can be predicted) and the other is the sum of the last plus the lagged values of the other time series.
3 For the evaluation of the results (test if prediction can be assert) by deploying a SelfOrganizing Fuzzy Neural Network
  - They are going to mix the data of the past three days of DIJA closing values with the values of other mood series (3 days also). This formed the input data of the SOFNN.
  - The forecasting precision was measured with the MAPE and the direction accuracy

####Hypothesis####
- OpinionFinder and GPOMS provide real information about the general sentiment. They, previously test this by performing an experiment during Thanksgiving and Presidential Election
- The stock market can be predicted

####Data####
- Twitter: 9.8M tweets from February 28 to December 19th.~ 2.7M users.
  - They filter, and pick only the tweets with words like 'I feel...'
- Stock Market: a time series of daily DIJA closing-values from Yahoo! Finance.

####Experimental####
- They performed a previous experiment to test if OF and GPOMS can predict sentiment variation on days like Presidential Election and ThanksGiving.
There are three phases in this paper for testing the prediction of the stock market.
- 1. Creation and validation of the GPOMS, OF and DIJA time series. (Oct-Dec 2008)
  - They normalized the values, in order to be able to make a comparison.
- 2. Granger Causality (Aug-Dec 2008). This model was specially designed to test if a time series can forecast another. By observing changes in a X variable, we can see if at Y we obtain immediate changes then it is called Granger causal.
- 3. Training of a SelfOrganizing Fuzzy Neural Network (March-Dec 2008)
  - They point of this step is as the Granger analysis is based on time linear models, they are going to mix the input data in order to avoid the linearity.
  - The training set was evaluated until November. December was chosen to be the testing period, for being a more stable.
  - They performed a binomial distribution for testing the accuracy of Calm input mixed with DIJA values.

####Results####
For the previous testing of the OF and GPOMS, we observe that:
  - OF can track easily an event like President Election, but have more difficulties at tracking Thanksgiving's mood variation.
  - GPOMS performed the opposite.
  - GPOMS Happy dimension is alike to Opinion Finder.
For the step 2:
  - After performing the Granger analysis, we observe that we can assess a high correlation of the DIJA values with Calm values for lags ranging from 2 to 6 days. The Calm series performed very well at predicting the future 3 days DIJA values as the graph shows.
For the step 3:
  - OpinionFinder does not provide useful information.
  - The best forecasting accuracy based on MAPE was performed by the input of DIJA values + Calm values (86.7%).
  - When testing this assumed accuracy with a binomial distribution they obtained bad results. 0.32% in a 20 days trial with a 50% of success.

####Assumptions####
- All tweets has influence on the stock market. Big Assumption
- By measuring correlation we prove prediction
- Granger causality is the best model for examining correlation, although it is based on linear regression

####Synthesis###
- I would definitely categorize the Twitter information before analyzing the tweets. For example, some Twitter users, like the one that provide news, can have more influence on the stock market. Also, people between 20 - 60 who have more influence at the market. Of course, as they said they are not interested in performing the best prediction model.
- I would have filter the tweets based on GeoLocation. For example, someone at Spain will not have the same influence at Dow Jones as someone in America.
- I consider as a good point that the author previously showed how tools like OF and GPOMS are very powerful at sentiment classification.
- It is not very clear why we are studding correlation if it directly does not imply prediction.
- As it specifically says, unexpected news got to trigger three standard deviation of DIJA values from Calm values, so a good point would be mixing these two sources of information.
- A lot of points mentioned in this section were mentioned also at the paper, so it analyzed itself very well. I think that it is an excellent paper.
- The method to measure the forecasting precision SOFNN it is not explained very well, just how the input data is organized, and the outputs.
- Then which is better Granger causality analysis of SOFNN?

####Related Papers####
- Bollen, J., Mao, H., & Pepe, A. (2011, July). [Modeling public mood and emotion: Twitter sentiment and socio-economic phenomena.](http://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/viewFile/2826/3237) In ICWSM.
  - Paper from the same authors. It is like the previous study of this paper.
  - Same data source, but they performed sentiment classification and analyze the output targeting in socio-cultural events.
  - The paper is more immature. For example, they used POMS instead of GPOMS with only 65 terms.

- Zhang, X., Fuehres, H., & Gloor, P. A. (2011). [Predicting stock market indicators through twitter “I hope it is not as bad as I fear”.](http://ac.els-cdn.com/S1877042811023895/1-s2.0-S1877042811023895-main.pdf?_tid=1126fdcc-2a44-11e3-90da-00000aab0f01&acdnat=1380595938_50e69af61b876f9fd2ab2132aef2ed11) Procedia-Social and Behavioral Sciences, 26, 55-62.
  - Their sentiment classification was based tracking hope, fear and worry. Their stock market information was based on indices of Dow Jones, S&P 500, and NASDAQ.
  - Their results were that if one day there were a lot of these sentiments, the next day DIJA values go down and vice versa. Sounds pretty familiar to calm sentiment.

- Zhang, X., Fuehres, H., & Gloor, P. A. (2012). [Predicting asset value through twitter buzz.](http://link.springer.com/chapter/10.1007/978-3-642-25321-8_3) In Advances in Collective Intelligence 2011 (pp. 23-34). Springer Berlin Heidelberg.
  - For testing the accuracy of prediction they performed the Granger Causality analysis too.
  - They focused on specific stock markets like gold, oil or dollar which made it easier when filtering the useful information from Twitter. (They filtered the data with keywords related to the topic)
