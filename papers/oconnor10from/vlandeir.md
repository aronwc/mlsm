####Overview####

This paper seeks to correlate the sentiments expressed by people via twitter and those which are obtained by polls. The researchers worked on different topics : the economy confidence and politics (presidential job approval in 2009 and american 2008 presidential elections).


####Algorithm####

The main algorithm of this paper resides in the text analysis of the Twitter messages.

To do so, researchers divide their work in two parts :

1. the identification of messages relative to topics;
2. the measurement of the opinion expressed by the topics-related messages.

######Message retrieval######
In order to remove messages which are unrelated to the studied topics, they search for specific keywords in the Twitter messages and only keep messages that contain at least one keyword. Thereafter, the list of topics with the list of associated words :

- **consumer confidence** : *economy*, *jobs* and *job*;
- **presidential approval** : *obama*;
- **presidential elections** : *obama*, *mccain*.

######Opinion estimation######
To measure the sentiment expressed by a message, researchers use a lexicon from OpinionFinder that classify 2800 words as negative or positive words. A message is said positive or negative as soon as it contains a positive (repectively negative) word. Thus, a message can be positive and negative at the same time.

They are not making distinction between strong and weak word, and because they are not using a part-of-speech (POS) tagger they find some errors in their text analysis.

Once each message is classified as positive or negative, they compute a daily sentiment **x_t** score which is the number of positive on-topic messages over the number of negative on-topic messages. 

To finish, they smooth the obtained results saying that the sentiment score on day **t** is equal to the average of every sentiment score on the **k** days before where **k** can be easily changed.


####Hypothesis####
- Text analysis of Twitter messages can provide opinion measurement equivalent to usual survey methods;
- Text analysis is a leading indicator of polls in some cases.


####Data####
As this paper intents to show the correlation between two types of measurement, there are two types of data.

######Data from Twitter######
They use 1 billion Twitter messages from 2008 and 2009. They do not apply a geographic filter on these messages such that even if most of the Twitter users where Americans in 2008 and 2009, they also use messages from non American users to measure sentiment on american topics. Moreover, as seen in the section "Algorithm", they filter Twitter messages to keep topics-related messages which reduce the amount of data to 0.1-0.5% of the original data.
At the end, they use between one and five million Twitter messages for each topic.

######Polls data######
For their first topic - consumer confidence - researchers use two surveys : 

- the Index of Consumer Sentiment (ICS) which is a monthly index;
- the Gallup Organization's "Economic Confidence" index which is administered daily.

For their second topic - politics - they use :

- the Gallup's daily tracking poll for the presidential job approval in 2009;
- a compilation of polls from pollster.com to show the voters preference in the presidential election of 2008.


####Experimentals####
- They begin by comparing the *jobs* sentiment score with two measures of consumer confidence. **(E1)**
- To go further, they integrate a new parameter into their correlation equation : **L** is an offset value allowing to compare the sentiment score computed via text analysis for the day **t** with the poll value from day **t+L**. This way, it should be possible to see if Twitter messages are a lead indicator for polls. For this experimentation, they make the **k** value (the smoothing window) vary between 7, 15, 30 and 60 and **L** varies in the **[-90, 90]** interval. **(E2)**
- They also test how accurate is the text analysis in predicting poll's values. To do so, they train the model on data through day **t-1** and predict the value for day **t**. **(E3)**
- At the end, they compute the sentiment score for political topics with *obama* and *mccain* keywords. **(E4)**

####Results####
- The first experience **(E1)** shows that the Twitter messages analysis is correlated at 73.1% with the Gallup poll. However, it seems that this method gets high false positive sometimes as it appears in the May-June 2008 trend.
- For the second experiment, the text analysis method is correlated with both Gallup and ICS polls.
	- For Gallup : the correlation is 71.6% for a 7-day smoothing window (**k**), 76.3% for a 15-day **k** and 79.4% for a 30-day **k**. Moreover, the correlation results seem to demonstrate that text is be a leading indicator for polls.
	- For ICS, the 60-day smoothing window gives a better correlation than the 30-day one. This shows that the text sentiment is unstable, thus it has to be used to study a long-term trends.<br><br>
	During **(E2)**, researchers also compute the correlation of Gallup and ICS showing a best result of 86.4% when the offset value **L** is set to 20. This result reveals that Gallup is a leading indicator for ICS.
	Eventually, they also compute the sentiment scores for the keywords *job* and *economy* which are poorly correlated with Gallup : 10% and 7% respectively.
- Predictions with text sentiment score achieve a 77.5% correlation which is worse than predicting the poll with its past self (80.4% correlation). Moreover, it demonstrates that the text sentiment is a volatile predictor as the first half of the predictions is wrong but the second half seems to be in relation with the actual data.
- The results for the fourth experience are not convincing as neither the correlation with the poll on Obama job approval nor the correlation with the poll on 2008 elections return high values.


####Assumptions####
- Every word is equally strong when expressing an opinion;
- When considering a large amount of data, errors in opinion estimation are compensating;
- The use of keywords is sufficient to get the sentiment of a Twitter message.


####Synthesis###
- From my point of view, the experimentation part is not easy to follow and especially the part where they study politic trends.
- The absence of weight on positive and negative keywords bothers me a little, as well as the use of keywords without POS tagging.
- I would like to re-do this experimentation with actual Twitter data which have a more constant size. Moreover, I would like to know the results with a more advanced text analyzer.


####Related Papers####
- Metaxas, P.T.; Mustafaraj, E.; Gayo-Avello, D., [*How (Not) to Predict Elections*](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6113109&isnumber=6113084) Privacy, security, risk and trust (passat), 2011 ieee third international conference on and 2011 ieee third international conference on social computing (socialcom) , vol., no., pp.165,171, 9-11 Oct. 2011
- Conover, M.D.; Goncalves, B.; Ratkiewicz, J.; Flammini, A.; Menczer, F., [*Predicting the Political Alignment of Twitter Users*](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6113114&isnumber=6113084) Privacy, security, risk and trust (passat), 2011 ieee third international conference on and 2011 ieee third international conference on social computing (socialcom) , vol., no., pp.192,199, 9-11 Oct. 2011
- Chung, J. E., & Mustafaraj, E. (2011, April). [*Can collective sentiment expressed on twitter predict political elections?*](http://www.christopia.net/data/school/2011/Fall/social-media-mining/project_proposal/sources/chung-2011.pdf). In AAAI.
