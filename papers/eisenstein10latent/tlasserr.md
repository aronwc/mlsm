####Overview####

This paper presents a method for identifying geographically-aligned lexical variation directly from raw text.

####Algorithm####

- First the authors train a Dirichlet process mixture model on the location y, using varaitional inference on the truncated stick-breacking approximation.
- Then, they run standard latent Dirichlet allocation to obtain estimates of topics for each token.
- Finally, the geographical model takes priors that are linked to the data.


####Hypothesis####

Geography and topic interact, as “pure” topical lexical distributions are corrupted by geographical factors.

####Data####

The dataset is composed of tweets collected over the first week of March 2010 from the “Gardenhose” sample stream.
- Only messages with physical coordinate pairs are used.
- The authors filtered the dataset to include only authors who follow fewer than 1,000 other people, and have fewer than 1,000 followers.
- Finally, the final sample contains about 9,000 users and 380,000 messages, totaling 4.7 million word tokens.

####Experimentals####

The authors want to assess their model's ability to predict the geographic location of unlabeled authors based on their text alone. They compare several approaches  for predicting author location:
- Their geographic topic model.
- They also test their system by running it with only a single topic.
- For unlabeled authors, they estimate latitude and longitude by estimating the topic proportions and then applying geographical distributions.
- They perform linear regression to learn the relationship between words and locations.
- They applied supervised K-nearest neighbors to predict the location yd as the average position of the K most  similar authors in the training set.


####Results####

- The geographic topic model achieves the strongest performance on all metrics.
- Text regression and supervised LDA performs especially poorly on the classification metric.
- Performance of K-nearest neighbors is poor at all value of K.

####Assumptions####

- Term frequency are influenced by a variety of factors, such as topic of discourse.
- Text in computer-mediated communication is often more vernacular, and as such it is more likely to reveal the influence of geographic factors than text written in a more formal genre.

####Synthesis####

- I think this subject is interesting because regions have their own way of speaking hovewer this paper is very difficult to understand, especially the mathematical part. 
- It can be good to evaluate these distributions by time also.
- Maybe user-declared location metadata is more sensitive to temporal change than the text of Twitter messages. 

####Related Papers####

- Q. Mei, C. Liu, H. Su, and C. X Zhai. 2006. A probabilistic approach to spatiotemporal theme pattern mining on weblogs.
	- This paper aims to analyze webblogs by analyzing their spatiotemporal petterns. (Influence of non-linguistic factors over language usage). In particular, it introduces a probabilistic approach to model the subtopic themes and spatiotemporal theme patterns together for weblogs.

- You Are Where You Tweet: A Content-Based Approach to Geo-locating Twitter Users, Zhiyuan Cheng, James Caverlee, Kyumin Lee
	- This paper evaluates a probabilistic framework for estimating a Twitter user’s city-level location based purely on the content of the user’s tweets 


 
