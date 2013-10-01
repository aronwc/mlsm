####Overview####

This paper investigates whether measurements of collective mood states from Twitter are correlated to the value of the Dow Jones Industrial Average over time, using methods for sentiment classification.

####Algorithm####

In this paper the author uses two algorithms to determine public mood:

- OpinionFinder (OF) which measures positive versus negative mood from text content. It is based on a lexicon to determine the ratio of positive words over negative words.
- Google-Profile Of Mood States (GPOMS) which can measure human mood states in terms of 6 different mood dimensions: Clam, Alert, Sure, Vital, Kind and Happy. It is also based on a lexicon of 964 associated terms.
- To enable the comparison of OF and GPOMS, the results of these 2 algorithms are normalized into z-scores.
- Granger causality analysis and Self-organizing Fuzzy Neural Network are also used in this paper.

####Hypothesis####

- Public sentiment, expressed in large scale collections of Twitter posts, can be used to predict stock market.

####Data####

- Collection of public tweets recorded from February 28 to December 19th, 2008 (9,853,498 tweets posted by approximately 2.7M users)
- Only tweets which contain explicit statement of their author’s mood are taken into account. They are been selected if they match the expressions “I feel”, “I am feeling”, “I don’t feel”, “I’m”, “Im”, “I am” and “makes me”.

####Experimental####

- 1) To test if OF and GPOMS are able to capture public mood, the author applies these 2 algorithms on tweets from October 5, 2008 to December 5, 2008, corresponds to the US presidential election and Thanksgiving and compares their results to the expected emotional responses to these events.
- 2) The author also computes the correlation between OF lexicon and the six dimensions of GPOMS using multiple regressions.
- 3) The econometric technique of Granger causality analysis is applied to compare GPOMS and OF time series with the Down Jones Industrial Average (DJIA).
- 4) The SOFNN is computed to better address non-linear effects and assess the contribution that public mood assessments can make in predictive models of DJIA.

####Results####

- The experiment 1 shows that OF successfully identifies the public’s emotional responses of these 2 events. Moreover, this experiment shows that GPOMS’Happy dimension best approximates the mood trend of OF.
- OF is significantly correlated with Sure, Vital and Happy of GPOMS.
- The mood time series correlate with changes in the DJIA, particularly the Calm dimension of GPOMS which has the highest Granger causality relation with DJIA for lags ranging from 2 to 6 days.
- Adding Calm enables us to have the highest prediction accuracy for DJIA.

####Assumptions####
- OF and GPOMS can determine if a tweet has a positive or negative sentiment.
- Sentiment classification is not done on feelings about stock market, but on feelings about everything.
- Only using public mood information is not an optimal DJIA prediction model.

####Synthesis####

- I think geographical location can be important because each country has its own public mood and so it would predict only the stock market of its own country.
- We have to determine which Twitter users is useful to take into account. Maybe we can try to identify people working in finance and analyze their mood. It can be more appropriate than a teenager telling his life on Twitter.
- The predictions with twitter data can not predict particular events like the financial crisis I think.
- This method should be added to other prediction model to see if it improves in all the cases these models.

####Related Papers####

- Modelling the Stock Market using Twitter, M. Sebastian A. Wolfram 
	- This paper  builds different feature representations from the raw Twitter posts and combined them with the stock price in order to build a regression model using the Support Vector Regression algorithm. It investigates the prediction of future prices, on average predicting 15 minutes ahead of the actual price.

- Exploiting Topic based Twitter Sentiment for Stock Prediction, Jianfeng Si, Arjun Mukherjee, Bing Liu, Qing Li, Huayi Li, Xiaotie Deng
	- This paper proposes a technique to leverage topic based sentiments from Twitter to help predict the stock market

