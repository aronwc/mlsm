####Overview####

The main goal of this paper is to show that Twitter is an effective tool to analyze the health of American citizens. The researchers also look for the best use of Twitter mined data.


####Algorithm####

The main algorithm of this paper is based on Ailment Topic Aspect Model (ATAM).

######ATAM######
ATAM models how users express their illnesses and ailments in tweets. To do so, it assumes that each health related tweet refers to a health topic, i.e. an ailment. Each ailment *a* maintains a distribution over words, and one over symptoms and treatments. This way, it is possible to know by what kind of message (general, symptom or treatments) a word is generated.

To extend this model, researchers introduce prior knowledge using articles written about diseases. They select 20 articles and pair each one of them to an ailment to get a model they call ATAM+.


####Hypothesis####

- It is possible to mine data on different diseases/illnesses thanks to tweets and using a unique method.
- These data can be used to create useful polls covering several health topics (allergies, flu, etc).


####Data####

######Tweets######

- They start by collecting two billion tweets from May 2009 to October 2010.
- From those tweets, they filter the health related ones.
- Then they use a Support Vector Machine classifier trained on hand labeled tweets to identify health related messages.
- After this classification, they obtain 1,63 million tweets from which they remove punctuation, stop words, URLs and hashtags.

######Ailments######

Thanks to ATAM+, they get a list of ailments but those are not labeled. To solve this problem, two annotators label model output with ailment name or as incoherent. They agree on labels for 15 ailments amongst a total of 20.


####Experimentals####

**E1** : They measure the correlation between the probability of the "flu" ailment for each week and the influenza rate measured by CDC. <br>
**E2** : They compare their rates with the Google Flu Trends rates. <br>
**E3** : They assign a state to each tweet from which they can deduce location in order to track ailments. Then they compute the number of ailment occurences divided by the total number of tweets per state. They use this number to figure out the correlation between a risk factor and the related ailment for each state whith at least 500 tweets.<br>
**E4** : They try to track an ailment through time and location by focusing on seasonal allergies. They compute the rate of the allergy ailment by state and by month and draw it on a map.<br>
**E5** : To get quantitative validation of trends by time and location, they compute the influenza rates with flu ailment for each state and over 12 months from September 2009.<br>
**E6** : As a last experience, they compute the entropy of several medications and the most common ailments linked to each medication.

####Results####

**E1** : They obtain a 95.8% correlation with ATAM+ and a 93.4% correlation with ATAM. <br>
**E2** : They get a 96.8% correlation using ATAM+ and a 93.5% correlation using ATAM. <br>
**E3** : They find the highest correlation to be between the cancer ailment and the tobacco use. They also find interesting negative correlation between exercise and the frequency of posting any ailments showing that people who exercise tend to be less sick.<br>
**E4** : They get results similar to some known patterns of allergies.<br>
**E5** : The correlation with CDC value is 66% for ATAM+ and 23% for ATAM.<br>
**E6** : They find logical links between some treatments and some illnesses (for instance, vicodin is used in dental problems and infection) but they also show that antibiotics are misused in several cases (common cold and flu).

####Assumptions####
- Two annotators are enough to label the ailments output.
- Because people are posting less tweets about their ailments, they are less sick.


####Synthesis###
- It appears that Paul and Drezde developed a powerful tool, especially when considering that it is not focusing on a specific disease but use a general approach.
- I agree on the fact that it seems possible to generalize data mining to severals diseases. However, it is bounded by the public aspect of Twitter when health topics often implies privacy. Thus, I don't think that every disease/illness can be treated by the analyze of tweets.
- I would like to re-do the experiments focusing on location using actual amount of daily tweets and actual methods of geolocation via mobile posting or user profile analysis.
- As said in the paper, twitter users are not representative of the world population in term of age or location. It might be interested to retrieve data from other social networks or even weight tweets to get a distribution over age and location similar to the world distribution.

####Related Papers####
- Chew C, Eysenbach G (2010) [Pandemics in the Age of Twitter: Content Analysis of Tweets during the 2009 H1N1 Outbreak](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0014118). PLoS ONE 5(11): e14118.
	- This paper focuses on the H1N1 flu and aims to show that Twitter is a reliable real-time content source.
- Paul, M. J., & Dredze, M. (2012). [A model for mining public health topics from Twitter.](http://citeseerx.ist.psu.edu/viewdoc/download?rep=rep1&type=pdf&doi=10.1.1.226.4323) HEALTH, 11, 16-6.
	- This paper presents the Ailment Topic Aspect Model in details.
