# Overview
They correlate the properties of the Facebook profile and user's personality to see if with the first one you can predict the second one.

# Algorithm
- They took the results of a phychological test Facebook application, based on the big five personality model, called myPersonality.
- Examine profile features from two categories,  user’s actions and the actions of a user and their friends. 
  - Number of Facebook friends
  - Number of associations with groups
  - Number of Facebook “likes”
  - Number of photos uploaded by user
  - Number of status updates by user
  - Number of times others “tagged” user in photos

# Hypothesis
- Openness and Neuroticism are positively correlated with the number of status updates, photos, groups and “likes” of an individual. 
- Conscientiousness is negatively correlated with all aspects of Facebook use: number of friends, likes, photos, etc. 
- Extraversion is positively correlated with all aspects of Facebook use 
- Agreeableness is positively correlated with the number of friends, groups and “likes”

# Data
- 180000 Faceboook users
- They completed a Facebook application test and allowed to give some of their Facebook features information.

# Experimentals
- They sorted users into deciles according to their score on each Facebook feature. They clustered together users in 10 different groups with similar Facebook features, and examined average values of personality trait scores. With this they computed graphs based on two dimensions. One the average Facebook feature value of the given group and the other the average personality trait score for this group.
- B. They tested statistical significance with a t-distribution test.
- C. Mann-Whitney-Wilcoxon test.
- D. Prediction of the personality. They took the 5000 users that agreed to share all of their Fb features. They tried to predict a user's personality using multivariate linear regression with 10-fold cross validation.

# Results
- Openness is positively correlated with number of users’ likes, group associations and status updates.
- Conscientiousness is negatively related to the number of likes and group membership, but positively related to the number of uploaded photos.
- For extraverts we observe positive correlation with sharing status updates, number of likes and Fb groups. Not a clear positive corralation with the number of friends.
- Agreeableness negatively correlated with the number of likes. Agreeableness appeared to be less correlated with high-level Facebook features.
- Neuroticism is positively correlated with the number of Facebook likes and slightly positively correlated with number of groups.
- B. The results agreed with the previous experiment's results.
- C. Samething than B except for Agreeableness. It showed that was positively correlated with the number of tags.
- D. Extraversion and Neuroticism were the only two features that can be more less predicted.

# Assumptions
- Because of a 58% of women completed the application test, they spend more time on Facebook and that they are more interested in getting feedback on their personality. 58% is not a big deal.
- 'One way to help alleviate these is to seek support from friends' Generally big phychological assumptions when they gave explanations to plot results.
- The personality test were correctly answered by users and it is a reliable psychology model.

# Synthesis
- It was difficult to find assumptions to this research. For example, they counted on a large dataset.
- It was weird not to have an uniform dataset. Some of the users had restricted their access to some features. Maybe it could have been good to have an uniform dataset. As they said at the conclusion there are limitations for circumstances. 
- The paper talked at the intro about how to predict the personality, but at the end they just tried with one single user. With their dataset they could have performed better experiments with prediction.
- It sounded weird when the assumed, from the Agreeableness results for number of likes, that the reason was for not bothering other people. Usually Facebook content and photos are more about positive and natural things rather than religious (or other topic) related.
- Good points when they talked about future research.

# Related papers
-
