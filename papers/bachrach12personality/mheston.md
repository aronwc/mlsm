#### Overview
The authors present correlations between various high level features of Facebook profiles
and personality measures from the Five Factor Model.

#### Algorithm
They sort users into deciles according to their score on each Facebook feature. They cluster
users with similar features, and examine average values of personality scores. The users are sorted
according to the feature, and then partitioned into equal and disjoint sets based on that
order. They use these clusters in examining the personality traits correlation. They test
the significance of the correlation using a t-distribution test, as well as a MWW-test in comparing
the top and bottom thirds of the population.

#### Hypothesis
- Openness and Neuroticism are positively correlated with the number of status updates, photos, groups and likes of an individual
- Conscientioiusness is negatively correlated with all aspects of Facebook use: number of friends, likes, photos, etc.
- Extraversion is positively correlated with all aspects of Facebook use.
- Agreeableness is positively correlated with the number of friends, groups and likes.

#### Data
Data comes from 180,000 users, gathered using a Facebook app developed in 2007, where
users complete a personality test. Not all features were available for all users, but
each feature had at least 15,000 datapoints, and most had over 50,000.

#### Experiment
User results were clustered and corrlations between the Facebook features and personality
results were explored. The authors used a t-test and MWW-test to test the significance
of their results. They used miltivariate linear regression in experiments to test prediction
of individuals personalities.

#### Result
At a significance level of p < 1%, all correlations were found to be statistically significant.
The best accuracy for prediction of personality traits was for extraversion and neuroticism, with r-squared
of .33 and .26.

#### Assumptions
While they still had a lot of data points for each feature, they didn't really discuss which
features had significantly more or less data points. I wondered if there was something about
the personality traits and these features that was a confounding factor for which people
made this data available.

#### Synthesis
The authors mention at the end of their paper the use of lower level features for this task.
I think there would be value in seeing if using which groups certain types of people belong to,
if they "like" the same types of things, etc., and if that can be used to more accurately predict
personality types.

#### Related Papers
- Quercia, Daniele, et al. "Our Twitter profiles, our selves: Predicting personality with Twitter." Privacy, security, risk and trust (passat), 2011 ieee third international conference on and 2011 ieee third international conference on social computing (socialcom). IEEE, 2011.
  - Uses Twitter data to predict similar personality measures.
-  Ortigosa, Alvaro, Rosa M. Carro, and José Ignacio Quiroga. "Predicting User Personality by Mining Social Interactions in Facebook." Journal of Computer and System Sciences (2013).
  - Examines user interactions with machine learning techniques to predict personality types.
