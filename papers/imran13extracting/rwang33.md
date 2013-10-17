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
#####Classifying Messages By Type:         
1,233 messages were examined and each was assigned an appropriate label from five categories - Caution and advice/ Casualties and damage/ Donations of money, goods or services/ People missing, found, or seen/ Information source. They created 62 gold standard messages for this task, equally distributed among the categories.

#####Classifying Messages By Sub-Type and Extracting Information Nuggets:           
for each of the four types, workers classified a message by sub-type. In addition, they were also asked to extract a sub-string from the message that made them come to this conclusion.

#####Automatic Classification
Features:
* Binary - hashtags, URL, emotions, etc.
* Scalar - tweet length
* Text feature - Unigram, bigram, POS tags, Verbnet, etc.

###Extraction
* Caution and Advice Nuggets
* Casualty and Damage Nuggets
* Donation and Offer Nuggets
* Information Source Nuggets


#Results
Extraction Evaluation:      
* Training 2/3 Joplin and testing 1/3 Joplin get recall of 0.78 and precision of 0.9
* Training 2/3 Sandy and testing 1/3 Sandy get recall of 0.41 and precision of 0.79
* Training Joplin and testing Sandy get recall of 0.11 and precision of 0.78
* Training Joplin plus 10% Sandy and testing 90% Sandy get recall of 0.21 and precision of 0.81

The results of our experiments show that indeed machine learning can be utilized to extract structured information nuggets from unstructured text-based microblogging messages with good precision and recall.


#Assumptions
They assume that testing their techniques on different disaster-related datasets maybe gain insight on how dataset tailored our techniques should be. 


#Synthesis
* Machine learning software can be provided as a service such as Google Prediction API.
* Can we provide crisis-related tweet classification as a service? Maybe we can collect tweets automaticly, reuse ontologies or default training set.


#Related papers
[Chatter on The Red: What Hazards Threat Reveals about the Social Life of Microblogged Information](https://www.cs.colorado.edu/~palen/chatter_on_the_red.pdf)      
      
This paper considers a subset of the computer-mediated communication (CMC) that took place during the flooding of the Red River Valley in the US and Canada in March and April 2009. They identified mechanisms of information production, distribution, and organization. They examine the social life of microblogged information, identifying generative, synthetic, derivative and innovative properties that sustain the broader system of interaction.      
      
[“Respectfully Yours in Safety and Service”: Emergency Management & Social Media Evangelism](http://www.iscram.org/ISCRAM2010/Papers/152-Latonero_etal.pdf)      
      
In this paper they consider how emergency response organizations utilize available social media technologies to communicate with the public in emergencies and to potentially collect valuable information using the public as sources of information on the ground.
