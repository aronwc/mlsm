####Overview####
This paper is talking about how to predict stock market by analyzing the twitter mood; as a result they find an accuracy of 87.6% in predicting the daily up and down changes in the closing values of the DJIA and a reduction of the mean Average Percentage Error by more than 6%. They investigate public sentiment from large-scale of daily twitter posts to predict the stock market, over all this idea is great and valuable.

####Algorithm####
They analyzed research data by using OpinionFinder and Google-Proﬁle of Mood States to get sentiment scores, then for linear model, they try to use granger causality to analysis the mood time series and the DJIA. For non-linear, they used self-organizing Fuzzy Neural Network model to predict DJIA base on the former result value and sentiment score during the period.

####Hypothesis####
The main hypothesis is a common sense, that the sentiment of people will affect what they act, for  this paper it specify the financial  investment part.

####Data####
A collection of public tweets recorded from February 28 to December 19th, 2008 (9,853,498 tweets posted by approximately 2.7M users) with a tweet identifier and tweets had been modified by removing the stop words and punctuation. At last only the tweets which contain the sentiment elements will be used.

#### Experiment####
First, use president election and thanksgiving data to test whether they can capture the moods among the tweets, then compared correlation between OF lexicon and the six dimensions of GPMOS by using multiple regressions; at last they try to investigate permutations of DJIA, the GPOMS and SOFNN model.

####Results####
With linear model they find calm has the highest granger causality relation with DJIA, “Calm down” please Since the SOFNN prediction is more accurate, they conclude that a nonlinear relation among the different dimensions of moods.

####Assumption####
GPOMS and OpinionFinder can catch the right mood time series and do a good job with identifying the moods, and moods got certain relation with stock market.

####Synthesis####
We can all get the idea of the paper, and so many people are attracted by the result they got, but I think predict a single stock’s trend is much useful and valuable, since even DJIA value increased, so many stocks also dropped, but it may be useful for Stock Index Futures. And stock market changed so fast, how to prediction go timely is another question need to be discussed.

####Related Paper####
-	Predicting Stock Market Indicators Through Twitter “I hope it is not as bad as I fear”
Xue Zhang, Hauke Fuehre, Peter A. Gloor
    They found that emotional tweet percentage significantly negatively correlated with Dow Jones, NASDAQ and S&P 500, but displayed significant positive correlation to VIX. It therefore seems that just checking on twitter for emotional outbursts of any kind gives a predictor of how the stock market will be doing the next day.
-	Predicting the NFL Using Twitter
Shiladitya Sinha, Chris Dyer, Kevin Gimpel, and Noah A. Smith
    Another paper that predict game result by using twitter mood analysis, but algorithm is much easier.
