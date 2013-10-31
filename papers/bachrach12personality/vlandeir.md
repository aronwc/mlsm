####Overview####

This paper focuses on how personality of Facebook users is manifested through their profiles.

####Algorithm####

For their machine learning algorithm, they use two types of features:
- features that depend exclusively on a user's actions:
	- number of published photos
	- events and groups uploaded or created
	- number of objects the user has liked
- features that depend on the actions of a user and their friends:
	- number of times a user has been tagged
	- size and density of the friendship network.

Their main algorithm aims to correlate Facebook features and personality traits. To do so, they use the following methodology :
1. For each Facebook feature, they sort users into deciles using their score on the feature;
2. They cluster users with similar Facebook features;
3. They examine average values of personality traits scores.

To display their correlation results in a clearer way, they use plots where the x-axis is the average Facebook feature value while the y-axis is the average personality score.

For their predicting algorithm, they use a multivariate linear regression algorithm with 10-fold cross validation.

####Hypothesis####

- It is possible to predict some personality traits of a person using its Facebook profile.
- Openness and Neuroticism are positively correlated with the number of status updates, photos, groups and "likes" of an individual.
- Conscientiousness is negatively correlated with all aspects of Facebook use: number of friends, likes, photos, etc.
- Extraversion is positively correlated with all aspects of Facebook use.
- Agreeableness is positively correlated with the number of friends, groups and "likes".

####Data####

- They use the personality profiles and Facebook profile data of 180,000 users.
- Due to security settings of some users, time constraints, and bandwidth limitations, not all features are available for every user.
- They have at least 15,000 data points per feature and over 50,000 data points for most of the features.
- For their predicting experiment, they use a subset of the previous dataset by keeping 5,000 users that have all of the features strongly correlated with a personality trait.

####Experimentals####

- **E1**: They correlate the *Openness to experience* of a person with (1) the number of users' likes, (2) group associations, and (3) status updates.
- **E2**: They correlate the *Conscientiousness* of a user with (1) the number of likes, (2) the number of group memberships, and (3) the number of uploaded photos.
- **E3**: They correlate the *Exraversion* of a Facebook user with (1) the number of status updates, (2) the number of likes, (3) the number of associations with Facebook groups, and (4) the number of friends.
- **E4**: They correlate a Facebook user's *Agreeableness* with (1) the number of tags and (2) the number of likes.
- **E5**: Finally, they correlate the *Neuroticism* of a user with (1) the number of likes, (2) the number of groups, and (3) the number of friends.
 
They also measure the strength and significance of the previously studied relationships (Facebook feature/personality trait) using a t-distribution test and a Mann-Whitney-Wilcoxon test.

Their last experiment tries to predict the user personality from its Facebook profile using the relationships measured before and a multivariate linear regression.

####Results####

- **E1**: They show a positive correlation between *Openness* to experience and features (1), (2), and (3).
- **E2**: The results display a negative correlation between *Conscientiousness* and (1) and (2) but a positive correlation between Conscientiousness and (3).
- **E3**: This experiment shows that *Extraversion* generally relates positively with (1), (2), (3), and (4).
- **E4**: They show a positive correlation between *Agreeableness* and (1) for users with more than 50 tags. Conversely, it is negatively related with (2).
- **E5**: *Neuroticism* seems to relate positively with (1) and (2). They also show that it relates positively with (3) until the number of friends reach 200, then it relates negatively.

They find strong support of their correlation in their statiscal analysis except for the relation between Agreeableness and the number of tags.

Their best result in predicting a personality trait is on *Extraversion* (R^2 = 0.33) and *Neuroticism* (R^2 = 0.26). They obtain average results for *Conscientiousness* and *Openness* and weak result for the prediction of *Agreeableness*.

####Assumptions####

- People are able to determine others' personalities using some aspects of a Facebook profile.
- Active users on Facebook is an unbiased representation of the general population.

####Synthesis###

- I think this paper is interesting as it is based on several related works and it is improving those works by trying to generalize their results using a larger dataset.
- However, they often give an explanation of the results based on their point of view. It seems like they try to find an explanation that supports their result instead of finding results that confirm their thoughts.

####Related Papers####

- Judge, T. A., Higgins, C. A., Thoresen, C. J., & Barrick, M. R. (1999). [The big five personality traits, general mental ability, and career success across the life span](http://people.tamu.edu/~mbarrick/Pubs/1999_Judge_Higgins_Thoresen_Barrick.pdf). Personnel psychology, 52(3), 621-652.
	- This paper studies the relation between the Big Five personality dimensions and three job performance. 
- Golbeck, J., Robles, C., & Turner, K. (2011, May). [Predicting personality with social media](http://dl.acm.org/citation.cfm?id=1979614). In CHI'11 Extended Abstracts on Human Factors in Computing Systems (pp. 253-262). ACM.
	- This paper presents a method to predict a user's personality using his public Facebook profile.
