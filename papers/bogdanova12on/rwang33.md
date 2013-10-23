#Overview
In this paper, they have suggested a list of high-level features, including sentiment and emotion based ones, for detection of online sexual predation. 

#Algorithm
They formulate the problem of detecting pedophiles
in social media as the task of binary text categoriza
tion: given a text (a set of chat lines), the aim is to
predict whether it is a case of cyberpedophilia or not.

#Hypothesis



#Data
* For our study, we have extracted chat logs from the perverted-justice website.
* We need additional chat logs to build the negative dataset. We used two negative datasets in our experiments: cybersex chat logs and the NPS chat corpus.
* We have extracted chat lines only for those adult authors who had more than 30 lines written. Finally the dataset consisted of 65 authors. From each dataset we have left 20 files for testing.

#Experiments
1. To make the experimental data more balanced, we have created 5 subsets of PJ corpus, each of which contained chat lines from 60 randomly selected predators.
2. In order to prevent the classification algorithm from learning to distinguish this author from pedophiles, they used the author, which half of the chat sessions belong to him, for training, and the rest for testing.
3. For comparison purposes, they trained naive Bayes classifiers using word level unigrams, bigrams and trigrams. They also trained naive Bayes classifiers using character level bigrams and trigrams.

#Results
* The high-level features outperform all the low-level ones in both the cybersex logs and the NPS chat datasets and achieve 94% and 90% accuracy on these datasets respectively.
* Except for the character bigrams, all low-level features considered indeed work worse in case of cybersex logs.
* Low-level features do not work as good as we expected in case of the NPS chat dataset: bag of words provides only 61% accuracy.
* The high-level features yield a lower accuracy (90% accuracy) on the PJ-NPS dataset than in the case of PJ-cybersex logs (94% accuracy).

#Assumptions



#Synthesis
* From this paper, I think we can further investigate the misclassified data. The feature extraction they have implemented does not use any word sense disambiguation. We can employ word sense disambiguation techniques during the feature extraction phase.
* Since high-level features and low-level features have different merit and demerit, we can try to merge low-level and highlevel features in order to see if this could improve the results.

#Related papers
      
[SENTIWORDNET 3.0: An Enhanced Lexical Resource for Sentiment Analysis and Opinion Mining](http://www.esuli.it/wp-content/uploads/2011/07/LREC10.pdf)        
            
In this work they present SENTIWORDNET 3.0, a lexical resource explicitly devised for supporting sentiment classiﬁcation and opinion mining applications.          
            
[Using Lexical Chains for Text Summarization](http://acl.ldc.upenn.edu/W/W97/W97-0703.pdf)         
                
They investigate one technique to produce a summary of an original text without requiring its full semantic interpretation, but instead relying on a model of the topic progresston in the text derived from lexical chains. They present a new algorithm to compute lexical chains in a text, merging several robust knowledge sources the WordNet thesaurus, a part-of-speech tagger and shallow parser for the identification of nominal groups, and a segmentation algorithm dernved from (Hearst, 1994).                
                      
[Modelling Fixated Discourse in Chats with Cyberpedophiles](http://aclweb.org/anthology/W/W12/W12-0413.pdf)            
                     
In this paper they compute sexrelated lexical chains spanning over the conversation. Their study shows a considerable variation in the length of sex-related lexical chains according to the nature of the corpus, which supports our belief that this could be a valuable feature in an automated pedophile detection system.





