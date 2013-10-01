####Overview####
- This paper investigates whether measurements of collective mood states derived from Twitter are correlated to the value of the Dow Jones Industrial Average (DJIA) over time. 

####Algorithm ####
- For linear model, they apply Granger causality analysis to the mood time series and the DJIA.
- For non-linear,  they apply a Self-organizing Fuzzy Neural Network (SOFNN) model to predict DJIA values based on the past DJIA values and various permutations of our mood time series. 

####Hypothesis####
- The general hypothesis is that public mood measurement can improve predictive models of DJIA values.

####Data####
- They used a collection of public tweets recorded from February 28 to December 19th, 2008 (9,853,498 tweets posted by approximately 2.7M users).
- They only used tweets that contain explicit statements of their author’s mood states.

#### Experiment####
- They tested the correlation between the trend obtained from OpinionFinder and the six dimensions of GPOMS using multiple linear regression.
- The used only n lagged values of DJIA for prediction. 
- They used the n lagged values of both DJIA and the GPOMS plus the OpinionFinder mood time series.
- They investigate different permutations of values of both DJIA and the GPOMS to the SOFNN model.

####Results####
- They found that certain GPOMS mood dimension partially overlap with the mood values provided by OpinionFinde
- For linear model, they observed that “ Calm” has the highest Granger causality relation with DJIA. The other four mood dimensions of GPOMS do not have significant causal relations with changes in the stock market, and neither does the OpinionFinder time series.
- For non-linear model
 - Positive/negative sentiment obtained from OF has no effect on prediction accuracy compared to using only historical DJIA values
 - Adding Calm achieved the highest prediction accuracy.
 - Some mood dimensions reduced prediction accuracy significantly. 

####Assumption####
- The relationship between DJIA and mood state can be linear. 
- The mood time series derived from twitter using GPOMS and OpinionFinder is reliable.

####Synthesis####
- Besides mood, other tweets containing keywords related to stock market or economy may also be related to DJIA, e.g. the number of such tweets per day.
- I don’t think the mood state derived from twitter can predict the stock market, but we probability is able to predict the mood state with the DJIA as it is related to current economic events.

####Related Papers####
- Bollen, Johan, Huina Mao, and Alberto Pepe. "Modeling public mood and emotion: Twitter sentiment and socio-economic phenomena." ICWSM. 2011.
 - They find that events in the social, political, cultural and economic sphere do have a signiﬁcant, immediate and highly speciﬁc effect on the various dimensions of public mood.
- Metaxas, Panagiotis Takis, Eni Mustafaraj, and Daniel Gayo-Avello. "How (not) to predict elections." Privacy, security, risk and trust (PASSAT), 2011 IEEE third international conference on and 2011 IEEE third international conference on social computing (SocialCom). IEEE, 2011.
 - They ﬁnd that electoral predictions using the published research methods on Twitter data are not better than chance. They also reveal some major challenges that limit the predictability of election results through data from social media.
