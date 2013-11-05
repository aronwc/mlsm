# Overview
The paper aims to predict the location of a tweet based on the region and topic of the tweet. Also, they present a model that is capable of identifying relevant words for topic and regional classification.

# Algorithm
- They designed what they called the cascading topic models. This model generates text from topics (random variables)
- They also count on a geographic topic model, which I did not understand.
- They mixed these two models to obtain the text and the location of a tweet.

# Hypothesis
- Geography and topic interact, as pure topical lexical distributions are corrupted by geographical factors. So, regions and topics interact to shape observed lexical frequencies.

# Data
- They took 15% of public tweets.
- They took localized tweets, from authors that at least published more than 20 messages and with less of 1k followers and following.
- A randomly-chosen 60% of authors are used for training, 20% for development, and the remaining 20% for final evaluation.

# Experimentals
- They tried to predict the location of unlabeled authors by taking the content by:
  - Latent variable models, using geographic topic model, mixture of unigrams and supervised latent Dirichlet Allocation.
  - Baseline approaches using text regression and k-means over their first 30 principal components to find the neighbors.
- They observed the mean and median error distance between the predicted and true location in kilometers.

# Results
- What performed better was the latent variable models with a regression of 900 (km) error mean dist 494 (km) median dist and with a 58% accuracy into a 4region classification and 24 in a state classification.
- The less the number of topics varies the better for the median regression error.
- The regional variants show words that are strong compared to both the base topic and the background.

# Assumptions
- Kwak et al. was right about finding dramatic shifts in behavior among users with social graph connectivity outside of the range of the dataset.


# Synthesis
- The paper is very difficult to understand. From my point of view is for people who really knows about Machine Learning algorithms. Maybe it is because of my english level, but I did not have the same troubles with the other papers. 'Cascading topic models generate text from a chain of random variables. Each element in the chain defines a distribution over words, and acts as the mean of the distribution over the subsequent element in the chain. Thus, each element in the chain can be thought of as introducing some additional corrup- tion. All words are drawn from the final distribution in the chain.
At the beginning of the chain are the priors, followed by unadulerated base topics, which may then be corrupted by other factors (such as geography or time).' --> no clue.
- It is sounds like tricky how for predicting the location of a tweet, it takes the region as input... I could not even understand the reference 6 at the end of page two.
- They could have used other resources as regional lexicon dataset as they mentioned in the analysis section.

# Related papers
- Cheng, Z., Caverlee, J., & Lee, K. (2010, October). [You are where you tweet: a content-based approach to geo-locating twitter users.](http://delivery.acm.org/10.1145/1880000/1871535/p759-cheng.pdf?ip=64.131.125.154&id=1871535&acc=ACTIVE%20SERVICE&key=986B26D8D17D60C8D8F3AE9724154A45&CFID=375968491&CFTOKEN=29619400&__acm__=1383612392_fb478aef3aa7e7545a7ce07a38dbaa79) In Proceedings of the 19th ACM international conference on Information and knowledge management (pp. 759-768). ACM.
  - Quite more clear, they are going to predict in which city is an user based on the content of a tweet. They used a classification of words, for knowing which one is relevant for the classification. They do not analyze this step that much like this paper. They do not bother on building a lot of mathematic models for this. A lattice model for classificating the tweet.
  - 51% of Twitter users within 100 miles of their real location.
- Hong, L., Ahmed, A., Gurumurthy, S., Smola, A. J., & Tsioutsiouliklis, K. (2012, April). [Discovering geographical topics in the twitter stream.](http://delivery.acm.org/10.1145/2190000/2187940/p769-hong.pdf?ip=64.131.125.154&id=2187940&acc=ACTIVE%20SERVICE&key=986B26D8D17D60C8D8F3AE9724154A45&CFID=375968491&CFTOKEN=29619400&__acm__=1383612443_8240a9cb6a75a2fd350a7bf45d7cec41) In Proceedings of the 21st international conference on World Wide Web (pp. 769-778). ACM.
  - This paper has a more functional vision. They addressed the advantages and the information that can be extracted from a geolocated tweet.
  - As one of the parts of this paper (the one analyzed), they identified interesting topics taking as inputs the location and the language.
