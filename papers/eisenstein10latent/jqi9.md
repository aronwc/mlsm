####Overview####
The paper is trying to find out the potential relationships between lexical content and its author’s geographic location. Then use it to predict where the author is by analyzing raw text from their micro blog.
####Algorithm####
They use cascading topic model that is the model that can generate random text from certain topic, and assign different weight to the words that generated.
The geographic topic model is trying to find similarities of contents that posted by the people from similar place, and then use some math method to generate geographic location by topics. It is the extension of cascading topic model, but not to generate words, but location.
They use a combination of the methods above to finally determine where the author from.

####Hypothesis####
Different regions got different ways to talk. it is a common sense. The most obvious hypothesis that the authors raised is there are certain relationships between the way a man talk and his location, that is “you talk like where you are”.

####Data####
The final dataset is about 9500 different users’ 380000 messages totaling 4.7 millions word tokens. They only chose the user who wrote at least 20 message during first week of March 2010, and only follow under 1000 people and followed by under 1000 people, these users will not be a celebrities or marketers.

####Experiment####
First they initiate a Dirichlet process mixture model on a certain location, then using variational inference to determine the region, after this by running a standard latent Dirichlet allocation to obtain estimates of z for each token. The geographical model takes priors that are linked to the data: for each region, the mean is very weakly encouraged to be near the overall mean, and the covariance prior is set by the average covariance of clusters obtained by running K -means.

####Result####
The best result they got is using “Geographic topic model” got 900km distance mean regression accuracy and 494km median distance to the right place, 58% accuracy region identification accuracy and for the state “Most common class” got 27% accuracy.

####Assumptions####
They think word as a independent instant, not related to any other words.

####Synthesis####
This paper is really hard to understand, the cascading model is not really hard to understand but the implementation is kind of complicated, and also the accuracy of the predict and analysis is not really good enough, I think the most important thing that affect this is that people talks like where they grow up, not the place where they are now.

####Related Paper####
Protecting Privacy Against Location-based Personal Identiﬁcation
Claudio Bettini, X. Sean Wang, and Sushil Jajodia
This paper presents a preliminary investigation on the privacy issues involved in the use of location-based services. This paper shows that by analyze the requests that sent by mobile devices is a better method to find where the device owner is, and it is much accurate and efficient.


