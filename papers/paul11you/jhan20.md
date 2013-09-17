####Overview####
- This paper suggests that from Twitter we can infer a broad range of public health informatics. 

####Algorithm ####
- They apply the Ailment Topic Aspect Model (ATAM) to created structured disease information from tweets.
- They use Gibbs sampling algorithm to learn ATAM’s parameters.
- They place a prior distribution over ailment’s word based on some disease articles.

####Hypothesis####
- The hypothesis is that social media sources can provide us a broad range of public health informatics on a range of ailments.

####Data####
- 2 billion tweets collected from May 2009 to October 2010
- 20 disease articles from WebMD.com
- Influenza rate from August 2009 to October 2010 measured by CDC FluView

#### Experiment####
- They compared the ailment distributions with distributions estimated from WebMD articles.
- They measured the correlation between the probability of the flu ailment with the influenza rate in the United States measured by the CDC
- They measured correlations between each risk factor and the related ailments measured for each state.
-  They compared several common medications for pain relief and allergy.

####Results####
- The prior knowledge from disease articles help ATAM produce more coherent ailments.
- ATAM had a correlation of 0.966 with statistics under FluView. 
- Strong correlations are found for some risker factors and diseases.

####Assumption####
- One important assumption is that the information from tweets is about the user himself and can represent behaviors of the whole population.

####Synthesis####
- We can try to combine the ATAM model with some machine learning algorithms to predict the future trend for the diseases.
- Is it possible to estimate the probability of a disease outbreak in certain areas based on the tweets? 
- We can apply the similar method on news websites and compare its performance with that of Twitter.

####Related Papers####
- Culotta, Aron. "Towards detecting influenza epidemics by analyzing Twitter messages." Proceedings of the first workshop on social media analytics. ACM, 2010.
 - They proposed several methods to identify inﬂuenza-related messages and compare a number of regression models to correlate these messages with CDC statistics.
- Sakaki, Takeshi, Makoto Okazaki, and Yutaka Matsuo. "Earthquake shakes Twitter users: real-time event detection by social sensors." Proceedings of the 19th international conference on World wide web. ACM, 2010.
 - They proposed an algorithm to monitor tweets and to detect a target event.

