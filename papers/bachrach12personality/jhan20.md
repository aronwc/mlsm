####Overview####
- This paper examines correlations between users’ personality and the properties of their Facebook profiles.

####Algorithm ####
- They cluster together users with similar Facebook features and examine average values of personality trait scores of the groups. 
- They use multivariate linear regression algorithm to predict each of the traits using the profile information.

####Hypothesis####
- The general hypothesis is that users’ activity on Facebook relates to their personality.

####Data####
- The dataset consists of 180,000 users’ Facebook profile information and personality scores obtained using a Facebook application --- myPersonality. 
- The dataset has at least 15,000 data points per feature and over 50,000 data points for most of the features.

#### Experiment####
- They test the statistical significance of the correlations using a t-distribution test.
- They use a Mann-Whitney-Wilcoxon to determine whether the top and bottom thirds of the population differ significantly in terms of their mean personality score.
- They use the coefficient of determination and root mean squared error to measure the goodness of the prediction. 

####Results####
- Neuroticism has a negative correlation with the number of friends.
- Extraversion has a positive correlation with the number of friends.
- Agreeableness is positively correlated with the number of tags.
- Predictions regarding Extraversion and Neuroticism are reasonably accurate.

####Assumption####
- Since the dataset involves only users using the personality analysis application, an assumption is that the correlations are not systematically different from ones of other users.

####Synthesis####
- We can examine the correlations between user’s personalities and its friends’.
- Based on the user’s personality, we can define the similarities among friends and then we can try to build a friend recommendation system. 

####Related Papers####
- Gosling, Samuel D., et al. "Manifestations of personality in online social networks: Self-reported Facebook-related behaviors and observable profile information." Cyberpsychology, Behavior, and Social Networking 14.9 (2011): 483-488.
 - They find several connections between the Big Five personality traits and self-reported Facebook-related behaviors and observable profile information. 
- Kosinski, Michal, David Stillwell, and Thore Graepel. "Private traits and attributes are predictable from digital records of human behavior." Proceedings of the National Academy of Sciences 110.15 (2013): 5802-5805.
 - They show that Facebook Likes can be used to accurately predict a range of highly sensitive personal attributes including: sexual orientation, ethnicity, etc.
