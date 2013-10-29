####Overview####

This paper tries to demonstrate that personality traits are correlated with features of Facebook profile.

####Algorithm####

The big five personality model is used to model personality of facebook profile with openness, conscientiousness, extraversion, agreeableness and neuroticism.

The algorithm to make the correlation between personality traits and facebook profile features is:
- Sorting users into deciles according to their features
- Clustering users with similar Facebook features.
-  Examining average values of personality traits scores.

Multivariate linear regression with 10-fold cross validation is used to predict individual’s personality.

####Hypothesis####

- Openess and Neuroticism are positively correlated with the number of status updates, photos, groups and “likes” of an individual.
- Conscientiousness is negatively correlated with all aspect of Facebook use: number of friends, likes, photos, etc.
- Extraversion is positively correlated with all aspects of Facebook use.
- Agreeableness is positively correlated with the number of friends, groups and likes.
- By combining signals from different Facebook features it is possible to reliably predict personality of individuals

####Data####

- The dataset is composed of 180,000 users (average age: 24.15 and 58% of females), and was obtained using myPersonality, a Facebook application.
- The users completed a standard Five Factor Model questionnaire.
- Many Facebook users have incomplete profile information but there are at least 15,000 data points per feature and over 50,000 data points for most of the features.

####Experimental####

- E1 correlate openness with number of user’s likes, group associations and status updates.
- E2 correlates conscientiousness with number of likes, group membeship and uploaded photos.
- E3 correlates extraversion with number of like and Facebook friends.
- E4 correlates agreeableness with number of likes and the number of times a user was tagged in photos.
- E5 correlates neuroticism with number of likes, groups and friends.
- E6 measures the difference between top and bottom thirds of population of their mean personality scores using a Mann-Witney-Wilcoxon test.
- E7 tries to predict individual’s personality based on multiple profile features.

####Results####

- E1 shows the positive correlation between openness and number of user’s likes, group associations and status updates.
- E2 shows a negative relation between conscientiousness and number of like and group membership. It also shows positive relation between conscientiousness and number of uploaded photos.
- E3 shows a positive correlation between extraversion with number of like and number of friends. 
- E4 shows agreeableness is negatively correlated with the number of likes, but positively correlated with the number of times a user was tagged in photos. However, agreeableness appears to be less correlated with high-level Facebook features than the others.
- E5 shows that neuroticism is positively related with the number of Facebook likes and slightly positively related with number of groups. Neuroticism is positively related with friends until 200 and after reaching this peak it decreases.
- E7 shows that the best accuracy is achieved for extraversion and neuroticism, the lowest accuracy is obtained for agreeableness.

####Assumptions#### 

People’s personality can be judged by the others based on their Facebook profiles, because it reflects the actual personality of its owner.

####Synthesis####

- I think Facebook profile reflects an idealized projection of desirable traits rather than actual personality of its owner.
- It can be interesting to analyze the influence of friends. Do friends encourage individual to share the same personality traits?
- In this paper, the authors only show that their hypothesis are verified but it does not prove anything for me. How can we know if it is the best correlations?

####Related Papers####

- Our Twitter Profiles, Our Selves:Predicting Personality with Twitter, Daniele Quercia, Michal Kosinski, David Stillwell, Jon Crowcroft
	- In ths paper, the authors use following, followers and listed counts to predict personality of twitter users based on openess, neuroticism and conscientiousness.

- Predicting Personality from Twitter, Golbeck, J. ; Univ. of Maryland, College Park, MD, USA ; Robles, C. ; Edmondson, M. ; Turner, K.
	- In this paper, the authors present a method by which a user's personality can be accurately predicted through the publicly available information on their Twitter profile
