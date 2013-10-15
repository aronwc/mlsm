#### Overview
The authors attempted to use machine learning techniques to identify tweets that contribute to situational awareness during emergency events.

#### Algorithm
- Tweets are manually coded on several dimensons, including situational awareness content, objectivity, register, and personal/impersonal content.
- This set of labeled tweets were used to classify both a Naive Bays and MaxEnt classifier.

#### Hypothesis
Tweets that contribute to situational awareness can be automatically identified by their linguistic features using machine learning techniques.

#### Data
- Roughly 500 tweets from each emergency by individual users.
- Tweets were collected by random sample that contain one of their keywords.

#### Experiment
The authors use a MaxEnt classifier with various feature sets with their labeled data. The feature sets include:
 - Unigrams (baseline)
 - Unigrams, Bigrams
 - Unigrams, POS
 - Objective (annotated), POS, unigrams
 - Objective (predicted), POS, unigrams
 - Objective (OpinionFinder), POS, unigrams
 - Formal (annotated), POS, unigrams
 - Formal (predicted), POS, unigrams
 - Impersonal (annotated), POS, unigrams
 - Impersonal (predicted), POS, unigrams
 - All features (predicted), POS, unigrams 

#### Result
In general, inclusion of lingusitic features improved classifier performance. But the results vary from dataset to dataset. It doesn't seem like there's any clear feature that drastically improves results across all datasets. 

#### Synthesis
I find it curious that the authors always included unigrams in their model. Presumably, each disaster would have a specific vocabulary used to describe it, so I don't know how generalizable those methods would be. I would instead focus on trying to accurately predict linguistic features that are common across all types of disasters. For example, can we find objective tweets across the different datasets, and how well can we use that information to detect whether or not it contributes to situational awareness?

It would also be useful to try to identify disasters as they are happening. For example, by using some lexicon and seeing if a number of tweets in a specific location start appearing that use disaster words. It might be useful to do experiments to see how effectively this can be done.

#### Related Paper
- Neubig, Graham, et al. "Safety Information Mining-What can NLP do in a disaster-." IJCNLP. 2011.
  - Describes text analysis techniques used in system created to aid relief efforts in 2011 Japanese earthquake.
- Corvey, William J., et al. "Foundations of a Multilayer Annotation Framework for Twitter Communications During Crisis Events." LREC. 2012.
  - Newer paper by the authors that expands on previous work by introducing lingusitic and behaviorial annotations.
