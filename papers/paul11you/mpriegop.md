####Overview####
This paper try to find out if we can obtain valuable information about health care by aggregating Twitter messages.

####Algorithm####
They use a system based on:
Twitter --> filter for taking specific tweets --> ATAM --> structured information, ready for analyzing it. With a modification of ATAM.

- With ATAM we consider that users express about an ailment and maintains a distribution over symptoms and treatments.
 1 For selecting the tweets related to health care, a disease indexes a distribution over words, they used supervised machine learning (SVM classifier on 5k hand labeled tweets).
 2 Grouping data by ailment belonging using topic models. Inference of Gibbs sampling. Moreover, a word belonging to a health related tweet, can talk about a disease or its treatment or its symptons and we indentify this by using a list of keyphrases.
- For this paper add a feature to the ATAM model. For first selection of keywords of ailment distribution  they chose articles about most common diseases in Twitter. They have selected the Dirichlet distribution, and set up the mean as the distribution of the words in the article. Also, they have improved the parameter that measures the precision of the distribution.


####Hypothesis####
- Twitter users can auto-diagnose themselves.  For example, 'This flu is killing me'. This assumption can have not been diagnosed for a doctor.
- When twitter users talk about an ailment, they are talking about themselves or relatives, but not providing info about this disease.
- Twitter users do not over react about an ailment.
- Twitter users represent world population. This way this paper can study a general approach about health care even ignoring older people.
- When a user write about a disease in a tweet can also write about something non-related to this.

####Data####
- They have used 2B tweets from May 2009 to October 2010.
- After a simple keyword filter the end up with 11.7M tweets.

####Experimentals####
- A. Two people that do not belong to the project, labeled the ailments selected for the modification of ATAM.
- B. Syndromic Surveillance. From August 2009 to October 2010 (weekly). Instead of looking for the flu like other experiments, they have looked at all the diseases and extract an output for flu ailment.
- C. Geographic Behavioral Risk Factors. It measures the Pearson correlation between a state and this state's risk factor.
- D. Geographic Syndromic Surveillance. It combines the last two experiments
- E. The computed a distribution between treatments and symptomps for linking symptoms and medications.


####Results####
- A. They agreed on 17 labels, with 4 being incoherent. The experimen shows a regular performance when evaluating diseases with the same treatment or symptoms.
- B. They have achieved a reacher model with a 0.958 correlation with CDC output.
- C and D what do we learn from Twitter corresponds to what happens in real world.
- E Again, the output is coherent with the real situation with some noise.

####Assumptions####
- The results obtained by Google Flu Trends (contrasted with CDC in a lot of experiments) are similar to the ones obtained from Twitter data analysis.
- The best first step for analyzing the data from Twitter is grouping tweets about same disease.
- Geographic disease distribution is closely related to geographic distribution of phisical exercise


####Synthesis###
- As mentioned in every discussion class, I would have added another parameter to the distribution for locating the tweets. Actually they mentioned it, but the author did not include this at the model.
- This model allows a time analysis which makes a lot of sense when we talk about a disease. Actually, it might be possible to add this feature at the ATAM model too. For example, we increment the probability of the flue if we are running the programm in winter.
- I would try to figure out a way of include the information of older people who are not Twitter users.
- Although it is quite difficult, classifying tweets by age would provide useful information.
- The [lecture](http://videolectures.net/icwsm2011_paul_health/) offered was very interesting.

####Related Papers####
- Carneiro, H. A., & Mylonakis, E. (2009). [Google trends: a web-based tool for real-time surveillance of disease outbreaks.](http://cid.oxfordjournals.org/content/49/10/1557.short) Clinical infectious diseases, 49(10), 1557-1564.
  - This Google analysis has its basis on the information from its search queries. The huge disadvantage is that this information is private, and does not contain as much information as a tweet
- Culotta, A. (2010). [Detecting influenza outbreaks by analyzing Twitter messages.](http://arxiv.org/abs/1007.4748) arXiv preprint arXiv:1007.4748.
  - The present paper provides a change on how we classified health-related tweets obtaining a 95% of correlation on its experiment. The author proposes a supervised learning approach for classifying these tweets.

