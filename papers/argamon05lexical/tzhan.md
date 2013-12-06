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
They assume that for Extraversion if they use advanced algorithm, and do the refinement in the feature sets, they will get a better result.

Synthesis

I think this paper can get better in more detailed classification. About the neuroticism and extraversion, man or woman will show different attitudes even when they use a same word or sentence, so about the essays which collect from student if we classify them into male and female, then do the research, the result may be more trustable.
Another problem is that when it comes to the result of extraversion, it is not a clear result in the figure, I think it is not only need to make their division of this section clear enough, but also need to make the Modality more detailed, in that way, this section may be better.

Related Papers

S. Argamon,M. Koppel, J. Fine, and A. R. Shimony. Gender, genre, and writing style in formal written texts. Text, 23(3), 2003.
So, this paper mainly presents the differences between male and female about their genre and language usage style in formal written. These two papers just have different classifications, the paper we discussed focus on the neuroticism and extraversion, and just like I mentioned in the Synthesis. Maybe add the gender factor in the classification of this paper, the result will be more trustable.

O. de Vel. Mining e-mail authorship. InWorkshop on Text Mining, ACMInternational Conference on Knowledge Discovery and Data Mining, Boston, MA, 2000. 

About this paper, it is paper focus on collect data in e-mails, the corpus are totally different with the paper we discussed. One are essays, the other are e-mails. And they are also use different methods to do their research. So why authors take this paper in the reference, I think though they seem like different, they are all focus on text mining, they have the same thinking method.



