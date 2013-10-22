####Overview####

This paper develops a method of bullying detection on social networks using natural language processing.

####Algorithm####

- They decompose the cyberbullying problem into several topics : profanity/negativity/subtlety over the sexuality/race/culture/intelligence/physical attributes of a person.
- They divide the corpus into 50% training, 30% validation, 20% test and they use 4 types of machine learning algorithms :
	- Naïve Bayes
	- Rule-based learner
	- Tree-based learner
	- Support-vector machines
- Common sense reasoning by using ConceptNet, AnalogySpace, SVD, blending technique

####Hypothesis####

- Instances of cyberbullying where the abuse is more indirect and does not involve the use of profanity or stereotypical words are likely to be misclassified by supervised learning methods.
- Supervised learning methods generally fare well when it comes to detecting explicit forms of verbal abuse owing to the presence of stable patterns.

####Data####

They use two datasets : one from YouTube and one from Formspring.

#####YouTube#####
- They scrap comments from controversial and relatively non-controversial videos from YouTube.
- The comments are then annotated by three different persons along three different labels : sexuality, race and culture, and intelligence.
- Once the comments annotated, they keep 1500 comments for each category.

#####Formspring#####
- Using a list of features extracted from the use of supervised learning on the YouTube dataset, they filter bullying comments from the Formspring corpus.
- Three annotators are asked to pick comments pertaining to topics of sexuality from the filtered comments.

####Experimentals####

- In a first experiment over the YouTube dataset, they train binary classifiers on each of the three datasets (sexuality, race and culture, and culture).
- In a second experiment, they combine the three datasets to train a multiclass classifier.

For those experiments, they use a feature space that can be divided into two categories : general features that are common for all labels and specific features for each label.

- In a third experiment, they evaluate their common sense reasoning models by selecting comments that do not contain any profanity but which are implicitly trying to attack or insult a victim. Annotators are then saying if they agree or disagree with the output of the common sense reasoning model.

####Results####

- The first experiment leads to an average F1-value of:
	- 0.55 for the Naïve Bayes
	- 0.61 for the rule-based learned
	- 0.52 for the tree-based learner
	- 0.66 for the SVM
- The second experiment gives a F1-value of:
	- 0.57 for the Naïve Bayes
	- 0.60 for the rule-based learned
	- 0.58 for the tree-based learner
	- 0.63 for the SVM

####Assumptions####

- Stereotypes are the main form of cyberbullying.
- Cyberbullying comments are correctly spelled.

####Synthesis###

- They seem very cautious while doing their experiments : tenfold cross-validation, dividing the data into three sets (training, validating, testing) and avoiding overfitting. I think it is an important point to support their results.
- They obtain nice results on detection of cyberbullying when the comments contain explicit insults but the results are way more mitigated when the attack is implicit. There might be an interesting work to do in the field of detecting implicit attacks.

####Related Papers####

- Liu, H., & Singh, P. (2004). [ConceptNet—a practical commonsense reasoning tool-kit](http://web.media.mit.edu/~hugo/publications/papers/BTTJ-ConceptNet.pdf). BT technology journal, 22(4), 211-226.
	- Details the way ConceptNet works.
- Ptaszynski, M., Dybala, P., Matsuba, T., Masui, F., Rzepka, R., Araki, K., & Momouchi, Y. (2010). [In the Service of Online Order: Tackling Cyber-Bullying with Machine Learning and Affect Analysis](http://arakilab.media.eng.hokudai.ac.jp/~ptaszynski/data/Ptaszynski_IJCLR2010-Cyberbullying_2011.02.23.pdf). International Journal of Computational Linguistics Research, 1(3), 135-154.
	- This paper aims to develop a set of tools that can automatically detect cyberbullying entries and report them.
