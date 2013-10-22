####Overview####
- This paper presents an approach for bullying detection based on state-of-the-art natural language processing and a common sense knowledge base.

####Algorithm ####
- A number of natural language processing techniques are used for cyberbullying detection
 - Machine learning technique
  - Naïve Bayes, rule-based learner, tree-based learner, SVM
 - The open mind common sense knowledge base
  - ConceptNet
 - AnalogySpace inference technique
 - Blending knowledge combination technique

####Hypothesis####
The general hypothesis is that potentially bullying messages in social networks can be detected with natural language processing techniques. 

####Data####
- 1500 comments in Youtube labeled into three categories:  sexuality, race and culture and intelligence
- a dataset of anonymized instances of bullying that were either user-flagged or caught by their moderation team in Formspring

#### Experiment####
- They evaluate each statistical models and classifer against 200 unseen instances.
- Three metrics are computed
 - Accuracy
 - F1-score 
 - Kappa statistic
- They evaluate the reflective user interface strategy in a small user study with a mock conversation between three imaginary persons staged to present a bullying interaction.

####Results####
- The state-of-the-art natural language processing, augmented by common sense reasoning technique result in accuracies approaching 80% in identifying potentially bullying messages.

####Assumption####
- One assumption is that all cyberbullying messages can be classified into three categories:  sexuality, race and culture and intelligence

####Synthesis####
- Is there a bias introduced by not labeled the data with different categories?
- What is the accuracy if they evaluate a larger set of instances including both non-cyberbulling and cyberbullying messages in Formspring?

####Related Papers####
- Macbeth, Jamie, et al. "Script-based story matching for cyberbullying prevention." CHI'13 Extended Abstracts on Human Factors in Computing Systems. ACM, 2013.
 - They develop intelligent interfaces to social media that use commonsense knowledge bases and automated narrative analyses of text communications between users to trigger selective interventions and prevent negative outcomes.
- Xu, Jun-Ming, et al. "Learning from bullying traces in social media." Proceedings of the 2012 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. Association for Computational Linguistics, 2012.
 - They identify several key problems in using social media data sources and formulate them as NLP tasks, including text classification, role labeling, sentiment analysis, and topic modeling.

