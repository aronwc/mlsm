**Overview**

	This experiment uses features such as the presence of emotive words and other indicators to detect whether given chat text is a case of cyberpedophilia.

**Algorithm**

	The experiment uses a Naïve Bayes classifier to say whether cyberpedophilia is present using several different methods. It appears to be set up simply that if a feature is present, the feature is either logged as such, or counted, depending on the approach. 

**Hypothesis**

	The primary hypothesis of this data is that cyberpedophilia chats have recognizable characteristics that differentiate them from other online chat styles/topics.

**Data**

	The data used in this experiment consists of three types of online communication: between verified predators and adults acting as children, between consenting adults in a cybersex chat, and between adults in a general chat room corpus.
	The cyberpedophilic texts were mixed with the other corpuses in the hope that they be detected automatically through the classification experiments.

**Experiments**

	The experiments in this paper tested the identification of cyberpedophilic texts amongst either of the two other text examples. The identification was done through a variety of means: specific high-level features, bag-of-words, and word and character bigrams and trigrams. The high-level features were selected with regards to typical patterns of predators and pedophilic texts; the features were comprised of emotional markers (positive & negative words, “joy” words, “anger” words, etc), context-relevant words identified in a previous experiment (relationship words, family words, information words, etc), neuroticism-indicative words (pronouns and obligation verbs), psychological profile features (morality, fixated discourse, etc), and other possible indicators (emoticons and imperative sentences). 

**Results**

	The results of the high-level features were quite astounding: 94% average accuracy in the pedophilic + cybersex chat data and 92% average accuracy in the pedophilic + general chat data. The other, lower-level data features had significantly lower accuracy: between 48% and 58% for pedophilic + cybersex data and between 42% and 72% for pedophilic + general chat data.

**Assumptions**

	The main assumption is that the data gained through the cyberpedophilia data set, which was created by actors pretending to be children interacting with predators, is indicative of genuine child-predator interaction.
	Also, the system is trained on those predators that interacted with the actors, and thus got caught. There could be different patterns to those people who have been able to avoid detection and/or notice the actors’ true identities.

**Synthesis**

	No information is given about the effectiveness of each high-level feature individually. Although the combined results are quite astounding, it could all be due to a single feature or a specific combination of features. 

**Related Papers**
Peersman, Claudia, et al. "Conversation Level Constraints on Pedophile Detection in Chat Rooms." CLEF (Online Working Notes/Labs/Workshop). 2012.
	Uses features related to the conversation and user as well as individual post characteristics. Also targets “grooming” words often used in chat room conversations as features.

Kontostathis, April, et al. "Identifying Predators Using ChatCoder 2.0." CLEF (Online Working Notes/Labs/Workshop). 2012.
	Detects predatory authors with a previously-created, rule-based automatic system using line-by-line analysis.
