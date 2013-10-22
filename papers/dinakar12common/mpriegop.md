# Overview
This paper test machine learning methods (explicit) and common sense models (implicit) to detect cyberbullying. After that, it proposes some methods to solve this problem. It provides a lot of background about this topic.

# Algorithm
For supervised learning methods:
- Naïve Bayes
- JRip, rule learner
- J48, decision tree based classifier.
- SVM
 Feature design. General features and label specific features for detecting each label.
For common sense models [theorical models]:
- The Open Mind Common Sense Knowledge Base.
- The AnalogySpace Inference Technique.
- The Blending Knowledge Combination Technique.
- The BullySpace Knowledge Base. The representation of the data pickes up and focused is in the form of an assertion, connecting two concepts with one of the twenty kinds of relations in ConceptNet.

# Hypothesis
- Supervised learning methods are not capable of detecting subtle cyberbullying but fare well when it comes to detecting explicit forms of verbal abuse.
- Cyberbullying happens on the Internet (social networks) and can be detected using machine learning methods.
- There is a way to solve the last point.

# Data
- Youtube. 1500 Comments  posted on controversial and relatively non-controversial videos. Each of them were manually classified into three categories sexuality, race and culture, and intelligence. The inter-rater kappa agreement was 0.4 or higher were selected for the purpose of the use of supervised learning methods. 50% training, 30% validation, and 20% test data
- Formspring. Anonymized instances of bullying that were either user-flagged or caught by their moderation team. This data was more specific involving subtlety. They used their labels.
- They focused only on topics related to the LGBT community.

# Experimentals
For supervised learning methods:
- Tenfold cross-validation was applied for training, validation, and testing for both of the experiments.
- General features were common for both experiments but Label specific features for detection of each label consisted of unigrams that were observed in the training data.
- 200 unseen comments for each classifier. The labels assigned by the models were compared against the labels that were assigned to the instances during annotation
- A. Binary classifiers were trained on each of the three datasets for each of the three labels (caategories).
- B. Three datasets were combined to form a new dataset for the purpose of training a multiclass classifier.
For common sense models:
- C. The BullySpace Knowledge Base. They took 200 assertions related to LGBT topic from Formspring, they converted it into a sparse matrix representation of concepts versus relations. Afeter that they merged them together. Then, they extracted a list of concepts  and chose a set of canonical concepts for comparison with the con- cepts that have been extracted from the comment.
- D. 50 instances were tested, based on annotators decision.

# Results
- It was showed that common sense model can fail with a common sentence like 'Hey Brendan, you look gorgeous today' associating it to a female label.
- A. JRip was the best, although the kappa values were best with SVM. The first one showed an outstanding result with 80% at sexuality.
- B. Multiclass classifiers underperformed compared to binary classifiers.
- D. Same thing mentioned at the first point.

# Assumptions
- This model could work without previously selecting the comments. They always pick up comments related to cyberbullying or completely the opposite.
- The experiment Fakebook is similar to real Facebook scenario, or other social network.
- If an user answer into a survey something related to cyberbullying, this answer reflects the real situation.
- Comments on Youtube selected represents the real situation.

# Synthesis
- Bulling videos can have the complete opposite effect. People might start making fun of this.
- Poor experiment the Fakebook survey, it lacks of realism.
- Small dataset, much more of 1500 Youtube comments could have been picked up from that web site making the research and their assumptions stronger.
- I would have implemented this in a large-scale user community, without selecting previously the comments. 
- Maybe it could have been a good idea merging the two models, common sense and machine learning somehow. This imply a steady research but it could have been very interesting.
- Some results does not look like very good, like common sense models

# Solution
For the cyberbullying detected they proposed some kind of strategies for solving this issue:
- Reflective User Interfaces
- End-User Strategies.  Rather than give completely general advice, specific advice may be offered addressing the particular kind of bullying.
- Introducing Action Delays. Buttons asking to the user if he is sure or making him aware of the people who are going to wath that comment.
- Informing the User of Hidden Consequences with an 'undo' button.
- Suggesting Educational Material.
- Social Network Provider Strategies. Moderators intervene before serious problems arise.
- Flagging of Messages
After performing some experiments with Fakebook they assumes that targeted help is more appropiate.

# Related papers
- Ptaszynski, M., Dybala, P., Matsuba, T., Masui, F., Rzepka, R., & Araki, K. (2010). [Machine learning and affect analysis against cyber-bullying.](http://s3.amazonaws.com/academia.edu.documents/30944499/AISB_Cyberbullying.pdf?AWSAccessKeyId=AKIAIR6FSIMDFXPEERSA&Expires=1382463307&Signature=FOK5ogpR%2BLzjyZutP%2FAPIvNHOjg%3D&response-content-disposition=inline) the 36th AISB, 7-16.
  - This research looks like more realistic and concise, it does not digress that much. They focus on using machine learning methods to detect cyberbullying. Results were not ideal but encouraging. They used other features like vulgarities and mimetic expressions, ironic expressions.
- McGhee, I., Bayzick, J., Kontostathis, A., Edwards, L., McBride, A., & Jakubowski, E. (2011). [Learning to identify Internet sexual predation.](http://mesharpe.metapress.com/media/h8phxpuqvlhh19vhhl5x/contributions/m/2/0/8/m208w2x7624v623n.pdf) International Journal of Electronic Commerce, 15(3), 103-122.
  - They performed machine learning algortihms to detect sexual predation and found out that neither decision trees nor instance-based learning algorithms were able to significantly improve upon the 68 percent accuracy that they were able to achieve with rule-based methods. So, they reached to results similar to our paper.
