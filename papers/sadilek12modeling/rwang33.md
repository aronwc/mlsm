##Overview
This paper focuses on fine-grained modeling of the spread of infectious diseases throughout a large real-world social network. 

##Algorithm
The authors developed a SVM model using a semi-supervised cascade-based approach. Firstly, they identified two classifiers, Cs and Co. Cs is usding to solves the problems that mistakenly labeling a normal tweet as one about sickness, while Co is using to solve labeling symptomatic tweets as normal. Then they use all unigram, bigram, and trigram word to achieve the tokenization. After the manual training, they final come up with the final function, Cf, to do the prediction.

##Hypothesis
1. Social ties and interactions between specific individuals play in the progress of a contagion.
2. The tweets abouot health state is not joking.
3. The tweets are sending by geo-active users.

##Data
Using the Twitter Search API, they collected a sample of public tweets that originated from the New York City (NYC) metropolitan area. The collection period was one month long and started on May 18, 2010.

##Experiments
#Step 1:
