Overview

This paper presents a way through analyzing the chats of predators and pseudo-victim, and states the list of high-level features which include sentiment and emotion based ones to detect the online sexual predation. 

Algorithm

Detect pedophiles with natural language processing (NLP) techniques.
Use Naive Bayes classification method to distinguish between predators and not predators.

Hypothesis

The corpus get from the www.perverted-justice.com are reliable

Data

They downloaded the cybersex chat logs available at www.oocities.org/urgrl21f/. The archive contains 34 one-on-one cybersex logs. After they have separated lines of different authors, they got 68 files.
They also used the subset the of NPS chat corpus, and extracted chat lines only for those adult authors who had more than 30 lines written. The dataset consisted of 65 authors. From each dataset they have left 20 files for testing.

Experimentals

Used a Naive Bayes classifier to distinguish between predators and not predators.
Used SentiWordNet To extract positive and negative words

Borrowed the features from McGhee et al. (2011), and detected with the list of words authors made available for them.

To make the experimental data more balanced, they have created 5 subsets of PJ corpus, each of which contained chat lines from 60 randomly selected predators.

Results

The high-level features outperform all the low-level ones in both the cybersex logs and the NPS chat datasets and achieve 94% and 90% accuracy on these datasets respectively.

Except for the character bigrams, all low-level features considered indeed work worse in case of cybersex logs.

Assumptions

The accuracy of low-level features better than the accuracy high-level features is due to the data diversity: cybersex chat is a very particular type of a conversation.
The amount of misclassified data will not have a great impact on the result.

Synthesis

After read this paper, I still doubt about the dataset they download from the website. No one can ensure whether the chat content can present the true situation between the predators and victims or not, so the chatting in this paper is between the “predators” and “pseudo-victims”. If they can get some authority datasets, like the detail conservation of those cases in the reality from newspaper or the records of polices. Then, to compare them with the online chat, to check them is reliable, that may make this experiment more trustable.
And, in the result the author mentions that the accuracy of low-level features of cybersex logs is not very good and they plan to merge the low-level features and high-level features together to see if there are improvement of accuracy, but they do not find the answer of why the low-level features of cybersex logs is not accuracy as expected. They can do more on this area, and I think the problem of low-level features of cybersex logs is that they share the same vocabulary with perverted-justice data, if they change some key vocabularies, the result may be better.

Related Papers

Regina Barzilay and Michael Elhadad. Using lexical chains for text summarization. In Proceedings of
the Intelligent Scalable Text SummarizationWorkshop, 1997.

This paper presents a paper empirical results on the tdent~catlon of strong chains and of slgmfieant sentences. And the paper we discussed takes the paper as reference because a similar method the author has used in the paper. But it is start with “sex”, and focus on the relate words of it.

India McGhee, Jennifer Bayzick, April Kontostathis, Lynne Edwards, Alexandra McBride and Emma Jakubowski. Learning to identify Internet sexual predation. International Journal on Electronic Commerce 2011.  

This paper focus on the internet sexual predation, but they use different methods to complete each work. This paper used phrase-matching and rule-based approaches to classify and label lines of chat logs and used machine learning algorithms to classify posts. That is different with the paper we discussed.

