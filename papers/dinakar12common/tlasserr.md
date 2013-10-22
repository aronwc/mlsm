####Overview####

This paper presents some solutions to detect potentially bullying messages in social network and shows that adding common sense reasoning technique to the state-of-the art natural language processing  improves the results.

####Algorithm####

- To identify the sensitive theme for a given comment, a bag-of-words supervised machine learning classification approach are used: Naives Bayes from toolkit WEKA, a rule-based learner (jRip), a tree-based learner (J48) and support-vector machine. 
-  Tenfold cross-validation was applied for training, validation, and testing for the experiments.
- To detect specific features, the authors use TF-IDF, Ortony Lexicon for negative effect, Part-of-speech tags and label specific features.
- Singular value decomposition (SVD) is used for dimensionality reduction.
- The blending knowledge combination technique is used to perform inference over multiple sources of data simultaneously by taking advantage of the overlap between them.
- Cosine Similarity

####Hypothesis####

- Supervised learning methods generally fare well when it comes to detecting explicit forms of verbal abuse owing to the presence of stable patterns.
- The instances of cyberbullying where the abuse is more indirect and does not involve the use of profanity or stereotypical words are likely to be misclassifies by supervised learning methods.

####Data####

Two datasets are used:

- The Youtube dataset contains comments posted on controversial and relatively non-controversial videos. 3 annotators labeled the comments as Sexuality, Race and culture and Intelligence. 1500 comments of each category were selected.
- Formspring dataset of anonymized instances of bullying that were either user-flagged or caught by their moderation team. It contains more subtlety bullying, with use of stereotypes. First filter with supervised learning methods trained with Youtube, then the 3 annotators pick instances about sexuality, namely, topics lesbian, gay, and transgender stereotypes.

####Experimental####

- E1: binary classifier were trained on each the three datasets for each of the three labels: sexuality, race and culture, and intelligence to predict if a given instance belonged to a label or not. The three datasets were combined to form a new dataset for the purpose of training a multiclass classifier using the aforementioned methods. The labels assigned by the models are compared against the labels that were assigned to the instances during annotation.
- E2: Similarity metrics are generated for each instances with canonical concepts “girls” and “boys” to evaluate common sense reasoning models.
- E3:  Evaluation of reflective user interface

####Results####

- E1 shows that multiclass classifiers underperformed compared to binary classifiers. In terms of accuracy, JRip was the best, although the kappa values were best with SVM. SVM’s high kappa values suggest better reliability for all labels. Naive Bayes classifiers for all labels perform much better than J48.
- E2 : about 72% of accuracy.
- E3 shows that static help could be used as n intermediate step to provide and-users with support.

####Assumptions####

- Computation detection of cyberbullying must address both the explicit and direct forms of abuse, as well as the subtler, indirect ways of insulting an individual.
- Specific features can be used to predict the label or the subject (sexuality, race and culture, and intelligence).
- It is specificity and uniqueness that matter the most for effective interaction analysis.

####Synthesis####

- The use of the Open Mind Common Sense Knowledge Base can be helpful but can it really detect irony? Irony can be misclassified. 
- I think it will be difficult to classify comparisons as bullying or not. It depends of the context. 
- Some people are more sensitive to bullying than others. Some will not be affected by this.

####Related Papers####

- Learning from Bullying Traces in Social Media, Jun-Ming Xu, Kwang-Sung Jun, Xiaojin Zhu, Amy Bellmore
	- This paper introduces some techniques like text classification, role labeling, sentiment classification and topic modeling to detect bullying in social media.
- In the Service of Online Order: Tackling Cyber-Bullying with Machine Learning and Affect Analysis,
Michal Ptaszynski, Pawel Dybala, Tatsuaki Matsuba, Fumito Masui, Rafal Rzepka, Kenji Araki, Yoshio Momouchi 
	- In this paper the authors analyze the entries with a multifaceted affect analysis system in order to find distinctive features for cyberbullying and apply them to a machine Learning classifier (SVM).
