# Overview
They analyzed  tweets from four different crisis events and built a classifier
to automatically detect messages that may contribute to situational awareness. They tried to extract useful information from Twitter of disasters.

# Algorithm
- Once they have their datasets, the perform situational awareness (that can provide useful information) with Bayes and Maximum Entropy algorithms.
- They categorized tweets by impersonal, objective and formal tweets for situational awareness (hand-labeled).
  - For this classification they performed some features like:
    - Unigrams and their raw frequency
    - Bigrams and their raw frequency
    - Part-Of-Speech tags
    - Subjectivity of tweets
    - Register of tweets
    - Tone of tweets

# Hypothesis
- Useful information can be extracted, analyzed and categorized from Twitter at disasters

# Data
- 500 tweets collected during a 20 days period more less after a disaster (Matching a list of their keywords) obtaining four datasets.
- They collected the data from The Red River floods occurred in March-April 2009 and 2010, the 2009 Oklahoma grassfires, and the Haiti earthquake.

# Experimentals
- A. They observed and categorized if a tweet is impersonal, objective or formal. Later, they observed the percentage of tweets categorized like situational awareness by their algorithm.
- B. They used the features described before for the situational awareness classification. After that they compute the mean accuracy over 10 fold cross-validation 90% training and 10% testing to evaluate the performance.
- C. Prediction of other disaster

# Results
- For the Red River flood just one tweet from 500 was off topic
- A. Haiti disaster showed less SA tweets for being international commented. It was confirmed that those three categories contained SA information.
- B. Good performance with features using unigrams and their frequency. They observed that POS tagging as well as objectivity classification improve the SA classifier accuracy. 

# Assumptions
- People tweet when a disaster has occurred.
- Tweets at a disaster are useful.
- 500 tweets provide enough data for machine learning classification. Big assumption.
- Veracity at those tweets.

# Synthesis
- They use too much adjectives and you get to lose the point of what are they saying.
- It is not clear how this is useful, they could have provided a clear example
- Analyzing tweets during 20 days about a disaster? Is a tweet posted 20 days after going to provide useful information?
- 500 tweets that they have selected (from their keywords) sounds weird…. It is not a big quantity, it sounds that they forced this tweets to provide useful information.
- It is not very clear why sentiment tweets are as important as those that provide situational awareness. Why is useful that I tweet saying ‘What a shame what just happened at Haiti earthquake’?

# Related papers
- William J. Corvey∗ Sudha Verma∗∗∗ Sarah Vieweg∗∗ Martha Palmer∗ James H. Martin∗∗∗  [Foundations of a Multilayer Annotation Framework for Twitter Communications During Crisis Events.]( http://lrec.elra.info/proceedings/lrec2012/pdf/1008_Paper.pdf)
- Five disaster instead of four.
- This paper is more concise with less useless adjectives. They seem to have made a deeper work.
- Now, the methods are well explained
- Neubig, G., Matsubayashi, Y., Hagiwara, M., & Murakami, K. (2011, November). [Safety Information Mining-What can NLP do in a disaste.]( https://www.aclweb.org/anthology/I/I11/I11-1108.pdf) InIJCNLP (pp. 965-973).
- Looks like to be a more steady work and more concise. Data mining during just one disaster
