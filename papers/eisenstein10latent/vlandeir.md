####Overview####

This paper presents a model that :

- identifies words with high regional affinity;
- identifies the relationship between regional and topic variation.

This model is developed using a corpus extracted from Twitter and is evaluated by trying to predict a user's location from his/her tweets.

####Algorithm####

- Their algorithm is a modified cascading topic model applied to geolocation. From what I understood, a cascading topic model is an extension of a supervised latent Dirichlet allocation (sLDA). Each document corresponds to the entire Twitter feed of a given author and for each author, the latent variable r corresponds to the geographical region of the author.
- Such a model can generate text from a chain of random variables and the goal is to be able to reverse this model in order to infer the random variables (unobserved) from the observed data (the tweets here).
- They build their models in three main steps :
	- They generate the base topics and generate the regional variants;
	- They generate regions;
	- They generate text and locations for each document.
- As in a sLDA, they can apply a mean-field variational inference to infer topics and region from the tweets.

####Hypothesis####

- Their main hypothesis is that geography and topic of discourse interact.

####Data####

- They use an archive of messages collected over the first week of March 2010 from the "Gardenhose" which represent 15% of all public messages over this period.
- They filter those tweets in several ways :
	- First, they only keep messages which are tagged with coordinates;
	- They keep authors only if they had written at least 20 messages over this period;
	- They remove the author if it follows more than 1,000 people or if it has more than 1,000 followers;
	- They remove messages with URL;
	- They keep messages from the US only;
- In the end, they obtain a corpus of 380K messages written by 9,500 users. Over those messages, they count 4.7M word tokens.

- To reduce the vocabulary size, they remove word types that appear in fewer than 40 feeds to obtain a vocabulary of 5,216 words.

####Experimentals####

- Their experimentation consists of evaluating their model by trying to predict the geographic location of an author based on his Twitter feed. They use 60% of the corpus for training, 20% for development, and 20% for testing. They compare their method with several approaches for predicting locations: 
	- latent variable generative models:
	    - Mixture of unigrams
	    - sLDA
	- discriminative approaches:
	    - Text regression
	    - K-Nearest Neighbors
- To quantitatively evaluate their method, they use two metrics:
	- the mean and median distance between the predicted and true location in kilometers;
	- the accuracy of classification by state and by region.

- They also analyze the geographical variation in the context of topics. They show in a table the results of a randomly-initialized run including 5 topics out of 50 in 5 five regions out of 13. They show the ten strongest terms in each topic for the base topics. For the regional variants, they show terms that are strong both regionally and topically.

####Results####

- On both tasks (regression and classification), they observe that their geographic topic model is the one that performs the best. It obtains a mean distance of 900 km and a median distance of 494 km on the regression task. Moreover, on the classification task, it gets an accuracy of 58% for the region classification and 24% for the state classification.
- Their analysis of the map and the table is not very clear. One thing they claim is that slang may depend on geography more than standard English does.

####Assumptions####

- Colloquial language is more likely to reveal the influene of geographic factors than formal language.
- Modeling topical variation will improve their ability to understand geographical variation.

####Synthesis###

- I think that this paper is quite complicated to understand because it requires some mathematical knowledge that I do not have (standard LDA, uniform diagonal covariance, Gamma distribution, Wishart distribution, Kullback-Leibler divergence, etc). The parts 3, 4, and 5 are not clear at all for me.
- Approximately 25% of the vocabulary is not in the English, French, or Spanish dictionaries. Thus a detailed analysis of slang might be useful to improve the results.
- In the introduction, they say that they are going to evaluate their approach both qualitatively and quantitatively but I did not find the qualitative evaluation.
- In part 5 (Implementation), they explain their process to initialize their model but in the experiments, they say that they do a randomly-initialized run. Why do they do that?
- From the map they draw, they say that there are "two large regions that partition the country roughly into north and south" but the red ellipse is covering almost all the USA.
- Less important, I noticed that they always talk about the "48 contiguous states and **the District of Columbia**". I don't know if there is a reason for taking the District of Columbia apart.

####Related Papers####

- Hong, L., Ahmed, A., Gurumurthy, S., Smola, A. J., & Tsioutsiouliklis, K. (2012, April). [Discovering geographical topics in the twitter stream](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.5366&rep=rep1&type=pdf). In Proceedings of the 21st international conference on World Wide Web (pp. 769-778). ACM.
	- In this paper, the researchers focus on Twitter and present an algorithm by modeling diversity in tweets based on topical diversity and geographical diversity.
- O'Connor, B., Krieger, M., & Ahn, D. (2010, May). [TweetMotif: Exploratory Search and Topic Summarization for Twitter](http://brenocon.com/tweetmotif_submission_icwsm10.pdf). In ICWSM.
	- This paper presents the tokenizer that Eisenstein et al. are using.
