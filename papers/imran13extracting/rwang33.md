#Overview
They describe automatic methods for extracting information from microblog posts and focus on extracting valuable “information nuggets”, brief, self-contained information items relevant to disaster response.

#Algorithm
They differentiate the tweets into two categories: Personal Only and Informative. Their designed filter is used to only select informative messages. After filtering, they use these tweets to train the classfiers manually. At last they use the well-trained classfiers to extract information automaticly.


#Hypothesis
Given the importance of on-topic tweets for time-critical situational awareness, disaster-affected communities and professional responders may benefit from using an automatic system to extract relevant information from the Twitter.


#Data
The dataset consists of tweets posted during the Joplin 2011 tornado that struck Joplin, Missouri in the late afternoon of Sunday, May 22, 2011. The dataset was originally constructed by researchers at the University of Colorado at Boulder. The 206,764 unique tweets were selected by monitoring the Twitter Streaming API using the hashtag #joplin a few hours after the tornado hit. This monitoring process continued until the number of tweets about the tornado became particularly sparse.


#Experiments
###Filtering
* Is the tweet disaster-related?
* Does the tweet contributes to situational awareness?           
The filter will select the tweets whose answers are "Yes"s to above two questions.      
These selected tweets will be the training data.      

###Classification





#Results



#Assumptions



#Synthesis



#Related papers
