####Overview####
This paper checks the effectiveness of predicting the sentiment of a review based on the presence or frequency of some keywords.

####Algorithm####
A document is represented with a vector, in which every coordinate represents the number of times a keyword appears in the text. These keywords are previously definited.
The author proposes three algorithms previously used in topic categorization:
- Naive Bayes. This one assumes that there is no dependency between two keywords.
- Maximum Entropy. This algorithm does not assume the independency between two keywords.
- Support Vector Machine. Instead of using probability it applies the dual optimization problem building an hyperplane for classifying the document.


####Hypothesis####
- Keywords can determine if a review is positive or negative.
- It is useful to apply corpus-based techniques for picking up the keywords.

####Data####
- The main data source are reviews with stars or numerical value from IMDb. 2053 reviews were evaluated, 1301 positive and 752 negative.
- They limited it to 20 reviews per author and sentiment. 144 reviewers represented.
- Also the recolected the selection of keywords from two graduate students.

####Experimentals####
First, they perform an experiment to check the effectiveness of humans when selecting keywords for the sentiment prediction.
Then, they applied the three algortihms to these experiments:
- Unigram keywords, based on the frequency that a keyword appears.
- Unigram keywords, based on the presence of a keyword.
- Bigram keywords, based on the presence of a keyword.
- Unigrams and bigrams
- Unigrams and POS with negative tags.
- Just selecting adjectives keywords.
- unigrams and the position in the review of the keyword.

####Results####
- All the results perform over the 50% baseline.
- Machine learning results were far better than humans results. The humans obtained no more than 64% accuracy versus an average of 79% for machine learning techniques.
- From all of these experiments the one with best percentage of success was unigram based on the presence of a keyword using SVM. 82.9%
- The algorithm that performs better was SVM.
- The adjectives measure obtained the worst results.

####Assumptions####
- The result of the experiment with the data of two students represents all humans performance. As these results are worse than machine learning's then it is better using machine learning algorithms.
- Those three algorithms are the most suitable for sentiment classification.
- If in unigram, frequency results were worse than presence ones, then for the other experiments too.
- Sentiment classification is more difficult than topic-based classification.
- Movie reviews are good enough to check the effectiveness of this machine learning techniques.

####Synthesis###
- I would have took neutral reviews too. A real situation include neutral reviews. What happen if you use these techniques with a neutral review? Which output would we obtain? In a real situation we would have more neutral reviews than possitive or negatives, so we are skipping a big part of the picture.
- Also I would try to filter the sentences in which the word 'wish' or thought appears like 'I wish this film would have been amazing and outstanding' or 'I thought that the movie was going to be awful and boring' because it can provide fake information.
- My next step would be trying this algorithms with food reviews where adjectives are very important. For example, 'The salad was too salty' or 'the meat was undercooked'.

####Related Papers####

