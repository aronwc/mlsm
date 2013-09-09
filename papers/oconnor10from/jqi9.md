####Overview####

This paper try to use certain algorithm to prove that the text sentiment is linking to the public opinion, and the results show that the analysis of text stream could be a substitute and supplement for traditional polls.
               
####Algorithm####

Four main algorithms have been implemented in this paper, the author use them for message retrieval, opinion estimation, correlation analysis and forecasting analysis.
- 1.Message retrieval
-- The algorithm for message retrieval is super easy, just use keyword filter to locate certain message talking about the certain topic.
- 2.Opinion estimation
-- For opinion estimation, they defined a lexicon from opinionFinder which contains about 1600 and 1200 words marked as positive and negative. Then, they count positive and negative through all the data in one day or during certain period, the sentiment score means the ratio of positive versus negative messages on the topic during the certain period.
- 3.Correlation analysis
-- For correlation analysis, to earn more accuracy, they set two new parameter L and k to control the differences of data that brought by their different report circle (day to day or monthly). L is a lag hyperparameter and k is a fixed hyperparameter, these two parameters may reduce the effect of different report circle by smoothing. That makes it easier to find the links between data.
- 4.Forecasting analysis
-- They trained the model only on target historical data through day t-1, then predict the t+L date’s trend, then repeat and repeat, at the end when they finished the process of training, the model will cover most of their test dataset, then use the mature model to predict the real t+L date’s trend.
####Hypothesis####
- 1.They think the analysis of text stream will substitute the traditional polling activities. Since the quality tend to be the same but cost less and more efficient.
- 2.Test stream’s sentiment has a link with the public opinion at the certain topic during the certain period.
####Data####
- Twitter Corpus
They use 1billion Twitter messages posted from 2008 to 2009. But not all the messages around the world, they ignored other non-English language messages. 
- Public Opinion Polls
They chose several different reports from different provider for consumer confidence and political opinion. Such as CCI, ICS and Gallup for consumer confidence, Gallup’s daily tracking and 2008 presidential elections polling data from Pollster.com.

####Experimental#### 
Basically they used the time series analysis method, they count the positive and negative words in the text stream for certain topic during a certain time, then calculate the sentiment score for the period then draw a char to show the whole view of the sentiment trend, at the end they compare their char with the standard chart which provide by the polling organizations. After this, they can tell how accurate their char is. 

####Results####

After several comparisons, they found that the data show the same thing with their hypothesis, to analyze the real-time text stream on a social media will get the similar polling result with the traditional polling methods, and it is faster and cheap. But the problem is how to build a appropriate lexicon for both negative and positive words, it should not be so big, but can provide enough support to the analyze model.

####Assumption#### 

The most important assumption should be that as the populations of people that who use the twitter everyday grow to bigger and bigger, the result would be more and more closer to the truth.

####Synthesis#### 

First, I doubt about the accuracy about their opinion estimation, that is too simple, people always like to use irony to show their wisdom.

Second, you can only train the model with existed topic data, how to do it if a brand new topic need a sentiment evaluation before it publish? You may not be able to predict that kind of thing with this method.
It is a really good method to find public opinion’s trend, especially for business activities. Are people talking about our product? How are they thinking? The result of this analysis will help CEOs to make a better decision on advertisements on CM or improve the quality of product.

####Related paper####

- Data Mining and Analysis on Twitter, Pulkit Goyal, Sapan Diwakar
This report focus on how the twitter change people’s communication style, and how to use it to make certain information move faster then before.


- Detecting Sentiment Change in Twitter Streaming Data
Albert Bifet ,Bernhard Pfahringer ,Ricard Gavald,LARCA Research Group,UPC-Barcelona Tech, Catalonia
They use a tool call MOA (Massive Online Analysis) to read real time data from twitter and monitor the sentiment on twitter by their algorithm
