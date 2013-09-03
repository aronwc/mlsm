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
- Movie reviews are good enough to check the effectiveness of this machine learning techniques.

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
- Unigrams and POS
- Adjectives
- unigrams and the position in the review of the keyword.

####Results####


####Assumptions####


####Synthesis###

 
####Related Papers####
