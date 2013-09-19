##Overview
This paper focuses on fine-grained modeling of the spread of infectious diseases throughout a large real-world social network. 

##Algorithm
The authors developed a SVM model using a semi-supervised cascade-based approach. Firstly, they identified two classifiers, Cs and Co. Cs is usding to solves the problems that mistakenly labeling a normal tweet as one about sickness, while Co is using to solve labeling symptomatic tweets as normal. Then they use all unigram, bigram, and trigram word to achieve the tokenization. After the manual training, they final come up with the final function, Cf, to do the prediction.

##Hypothesis
Social ties and interactions between specific individuals play in the progress of a contagion.

##Data
Using the Twitter Search API, they collected a sample of public tweets that originated from the New York City (NYC) metropolitan area. The collection period was one month long and started on May 18, 2010.

##Experiments
Step 1: Manual training the classfiers and coming out the final SVM Cf;
Step 2: Using their algorithm and method to handle the data and generating the results of the functions with several parameteres;
Step 3: Analyzing the interaction of these parametersm, such as time, encounters,  number of sick friends and so on.

##Results
1. Evaluation of the final SVM Cf got high accurate precision and recall.
2. There is a definite exponential relationship between probable physical encounters and ensuing sickness.
3. The number of sick friends also has an exponential effect on the probability of getting sick.
4. For smaller numbers of friends, co-location has a weak additional effect over the proxy effect of social ties. However, for larger n, the residual impact of friendships plateaus, and co-location begins to dominate.

##Assumption
1. The friends on Twitter are friends in real.
2. The tweets abouot health state is not joking.
3. The tweets are sending by geo-active users.
4. People really have physical encounters within the threshold of 100m.

##Synthesis
1. If this paper has focusec on prediction, why the whole paper almost talked about analysis.
2. Most of the reaults are analysis. The results tell us that if someone have more sick friends or stay in the 'sick' area too long will be easily to get sick. Isn't it an conmmon sense?
3. In my opnion, the prediction should be like true or false. The probability like 60% is not convincing.
4. I still confused about what dose the model use of. To warn people some of their friends may get ill, or to warn people not to go in some unhealthy area?
5. As previous work, the genelization is still not captured. Since the method is well-performed in NYC, using another dataset can it work efficiently as well?
6. I think it is also a post-hoc as using Twitter to predict election.

#Related Papers
[Predicting Disease Transmission from Geo-Tagged Micro-Blog Data](http://www.aaai.org/ocs/index.php/AAAI/AAAI12/paper/viewFile/4844/5130)
    
They considered the task of ﬁnegrained prediction of the health of speciﬁc people from noisy and incomplete data. They constructed a probabilistic model that can predict if and when an individual will fall ill with high precision and good recall on the basis of his social ties and co-locations with other people, as revealed by their Twitter posts.
   
[Separating Fact from Fear: Tracking Flu Infections on Twitter](http://www.aclweb.org/anthology/N/N13/N13-1097.pdf)
  
They demonstrated signiﬁcant improvements on inﬂuenza surveillance using Twitter by discriminating ﬂu tweets that report infection with those that express concerned awareness of the ﬂu.

