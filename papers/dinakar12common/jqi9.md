####Overview####
This paper is talking about a serious social problem, cyber bully, it doesn’t just about machine learning algorithm, it likes a general scientific article, there are a lot of sociology definitions and details introduced by authors, and not only designing detect algorithms but also giving several solutions for the problem.
####Algorithm####
For detect cyber bully: 
1)	Statistical Machine Learning Techniques: they choose three types of supervised learning algorithms in addition to Naive Bayes from the toolkit, a rule-based learner, a tree-based learner, and support-vector machines.
2)	Cyber bully detection by using common sense reasoning: 
The Open Mind Common Sense Knowledge Base
The AnalogySpace Inference Technique
The Blending Knowledge Combination Technique
The BullySpace Knowledge Base
Cosine Similarity of Extracted and Canonical Concepts

####Hypothesis####
The main hypothesis is by using technique methods cyber bully will be prevented or spread slowly then cannot grow into a disaster within a certain community.
####Data####
They used two datasets for this work, YouTube and Formspring(a social network for teenagers), they collected comments from YouTube.com’s controversial and relatively non-controversial videos and labeled by three people, finally 1500 comments with label become training, testing and validation data of machine learning method. Formspring dataset are anonymous instances of bullying that were either user-flagged or caught by their moderation team， they are used to adjust and test the Common Sense Reasoning Models.
#### Experiment####
They do the evaluations for both machine learning method and common sense reasoning models, and error analysis for both of them; they also evaluated the Reflective User Interface which is the intervention strategies for cyber bully.
####Results####
For machine learning method:
Multiclass classifiers got a relatively low accuracy. Binary classifiers trained for individual labels fare better than multiclass classifiers trained for all the labels. JRip gives the best performance in terms of accuracy, whereas SMO is the most reliable as measured by the kappa statistic.

For Common Sense Reasoning Models:
Instances from the Formspring dataset were evaluated by the model to generate similarity scores for the canonical concepts “girl” and “boy”, compare with result generate by annotators, the accuracy is about 75%, not really good, but acceptable.

For Reflective User Interface:
    It turns out to be very effective that reflective user interface with in-context advices do help people in a bully situation no matter the victim or the bully.
####Assumption####
The better Canonical Concepts defined, the more accurate similar score will be obtained.
Customized advices for victim will give them a great help to go through the situation.
####Synthesis####
This machine learning method is not an innovation, but the reflective user interface is a great idea, if use it in commercial area, it will get great effort, for example, when you click “place the order” at Amazon, a delay processes with some recommendation items that you may really need, or some similar books or movies you may like too.
####Related Paper####
Cyberbullying Identification, Prevention, and Response  Sameer Hinduja, Ph.D. and Justin W. Patchin, Ph.D. Cyberbullying Research Center
-Not using computer science, but good article to know more about cyberbully.

Modeling the Detection of Textual Cyberbullying   Karthik Dinakar ,Roi Reichart ,Henry Lieberman
-Only find cyberbullying by analyze text, same conclusion with this paper, binary classifier works better than multiclassifier.
