Overview
This paper presents that from a author’s informal text, they can distinguish high from low neuroticism and extraversion from the author, so that they can know the personality style of this man.

Algorithm
Taking four different feature sets(FW, Con, Mod, App), and their combination into consideration, and for learning classification models they use the SMO learning algorithm with a linear kernel.

Hypothesis
The way of people how to use words can reflect social and psychological states of them.
Data
The data derived from essays written by students at the University of Texas at Austin between 1997 and 2003. There works are part of their course responsibilities, and they are all write in a stream-of- consciousness essay and an essay of deep self-analysis. And the scores of those essays also take into the dataset.

Experimentals
They evaluated the use of functional lexical features for stylistic classification.
All documents in each corpus were processed into numeric feature vectors using various combinations of  feature sets:FW, Con, Mod, App.
For learning classification models they use the SMO learning algorithm with a linear kernel.
And 10-fold crossvalidation was used throughout to estimate out-of-training classification accuracy.


Results

About Neuroticism
the Appraisal lexical taxonomy is the most useful functional lexical features
About Extraversion
the results are not that clear, but if we focus on expressions to norms, (in)completeness, and (un)certainty, testing of  the function words still could develop more effective features.
In a word, the results show the utility of functional lexical features for neuroticism, and if improve overall accuracy of algorithm and feature sets, the result of extraversion will be more clear.
Assumptions
If the authors use advanced algorithm, and do the refinement in the feature sets, they will get a better result.

Synthesis
I think this paper can get better in more detailed classification. About the neuroticism and extraversion, man or woman will show different attitudes towards a same word or sentence

Related Papers

