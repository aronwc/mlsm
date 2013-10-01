####Overview####

This paper aims to show that the public mood has an impact over the general economy and that this public mood can be measured via an analysis of Twitter feed.

####Algorithm####

The main algorithm of this paper consists of creating public mood time series using two models.

- They use OpinionFinder to classify the tweets as conveying a positive or a negative sentiment and therefore create OpinionFinder public mood time series.
- They create their own tool : Google-Profile Of Mood States (GPOMS), an extended version of POMS-bi. It is based on a lexicon of 964 terms and can measure human mood states in six mood dimensions : *Calm, Alert, Sure, Vital, Kind* and *Happy*.
- They normalize the results obtained thanks to both of these methods in order to compare them.

Then, the researchers use several tools such as bivariate Granger Causality Analysis and Self-Organizing Fuzzy Neural Network (SOFNN).

####Hypothesis####

- Public mood analysis from Twitter feeds can predict DJIA closing values.

####Data####

- They collect a total of 9,853,498 tweets from 2.7M users. These tweets were recorded from February 28th to December 19th 2008. They remove stop-words and punctuation for each tweet.
- From these tweets, they only keep those were the author clearly talks about his mood. They also remove spam tweets.

####Experimentals####

Once they obtain the public mood time series from OF and GPOMS, the researchers run several experiments :

1. They validate those time series by showing that they respond effectively to particulary happy social events (Presidential Election and Thanksgiving).
2. They compute the correlation between OF and each GPOMS' mood-dimension.
3. After that, they look for a causality link between their mood time series and the DJIA closing values doing a bivariate Granger causality analysis.
4. Finally, they compare the performance of a SOFNN that predicts DJIA values on two sets of inputs : the past 3 days of DJIA values, and the same set but combined with some public mood time series.

####Results####

The results of the experiments are the following :

1. The OF time series identifies the public's emotional response to the social events. The GPOMS measurements show different results for different mood-dimensions :
	- *Calm* indicator drop drastically just before the election day and then peak on the day of the election. It is not elevated for Thanksgiving.
	- There is a significant increase in *Vital*, *Happy* and *Kind* scores on election day but there is only a peak for the *Happy* indicator at Thanksgiving.
It seems like GPOMS' *Happy* dimension best approximates the OF mood trend.
2. The results of correlation between OF and GPOMS show that OF is significantly correlated with *Sure*, *Vital* and *Happy* dimensions.
3. The bivariate Granger causality analysis shows that the *Calm* dimension has the highest causality relation with DJIA for lags in 2 to 6 days.
4. Their final experiment supports the hypothesis that adding the *Calm* dimension to the past 3 days of DJIA values allow them to obtain better results on the DJIA closing value predictions.

####Assumptions###
- Punctuation is not important when trying to evaluate the mood of users thanks to their tweets.
- The number of collected tweets is sufficient to realize a machine learning study.
- Because the POMS-bi has been correctly tested and has proved to output correct results then their extended version (GPOMS) has got the same characteristics.
- Parameters of a SOFNN do not change when they add the public mood components.
- Measure the direction accuracy is sufficient to show the efficiency of a SOFNN.

####Synthesis###
- Relatively to Figure 1, why did they run the first phase (OF-GPOMS) on two months only while they trained the SOFNN on 9 months data? Moreover, it seems like they used 90% of their data for training and 10% for testing; weren't they able to run cross-validation? They also appear to choose the window of testing and training as it fits their model the best.
- Their dataset does not seem to be available anymore.
- Why do they exclude the Presidential Election and Thanksgiving from their Granger causality analysis. If they want to show a correlation between the general mood and the DJIA, I think they have to keep all the data.

####Related Papers####
- Pak, A., & Paroubek, P. (2010, May). [Twitter as a Corpus for Sentiment Analysis and Opinion Mining](http://incc-tps.googlecode.com/svn/trunk/TPFinal/bibliografia/Pak%20and%20Paroubek%20(2010).%20Twitter%20as%20a%20Corpus%20for%20Sentiment%20Analysis%20and%20Opinion%20Mining.pdf). In LREC.
	- This paper studies in depth the sentiment analysis from Twitter feeds. 
- Edmans, A., Garcia, D., & Norli, Ø. (2007). [Sports sentiment and stock returns](http://59.67.100.12/JPK/hbyhx/ckwx/ywwx/j.1540-6261.2007.01262.x.pdf). The Journal of Finance, 62(4), 1967-1998. 
	- This paper studies the influence of sports results on stock market.
