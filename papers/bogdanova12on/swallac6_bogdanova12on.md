Overview
========

The authors suggest a list of high-level features which include sentiment and emotion, to detect online sexual predation. They note that pedophiles are known to be emotionally unstable, and that it should be possible to detect this instability in the patters of their communication with possible victims.

Algorithm
=========

The Bayes classifiers were trained using word leve unigrams, bigrams, and trigrams as well as character level bigrams and trigrams.

Hypothesis
==========

Because of the emotional instability of pedophiles, the communication patters the exhibit should be automatically discernible from communication of non-pedophiles.

Data
====

-   Chat logs from Perverted Justice.

-   Cybersex chat logs which contain 34 one-on-one cybersex logs. These were separated by lines of different authors yielding 68 total files.

-   NPS chat corpus for those adult authors who had more than 30 lines written giving 65 authors.

Experiments
===========

-   For the purposes of distinction between predators and non-predators a Naive Bayes classifier was used.

-   Extraction of positive and negative words was done using SentiWordNext.

-   Imperative sentences were detected as affirmative sentences starting with verbs.

-   Emoticons were captured using simple regular expressions.

Results
=======

-   The high level features used for classification results yielded the best results at 94% accuracy for cypersex logs and 90% accuracy for NPS dataset.

-   Average accuracy for low-level features was between 48% and 58%.

-   Bag of words had 61% accuracy.

-   Character trigrams had 72% accuracy.

Assumptions
===========

-   The biggest assumption is that pseudo-victims communicate in the same way as actual victims. Surely, the people who are responsible for catching these pedophiles have had quite a bit of practice and are likely quite good at this, but it’s still probably not exactly the same.

-   The other big assumption is that the chat data they were able to obtain is indeed indicative of other chat rooms. It’s very possible the data they obtained was misrepresented in some way.

Synthesis
=========

There are a few problems I have with the paper. First, and I understand this limitation, but they were only able to get data from a couple sources. Second, while their accuracy for the high-level features was quite good, I’m surprised that the authors noted that the low level features were actually more difficult.

Related Papers
==============

-   Egan, Hoskinson, and Shewan (2011) showed that the expression of certain emotions in text can be helpful in detecting pedophiles in social media.

-   Pendar (2007) in experimenting with Perverted Justice data, separated lines written by pedophiles from those written by pseudo-victims by using a kNN classifier based on word n-grams.

-   Mcghee et al. (2011) manually classified lines of chat data from PJ into 4 categories. Showed that kNN classification can achieve up to 83% accuracy and outperform rule-based approaches.

-   Peersman, Daelemans, and Van Vaerenbergh (2011) were able to use a support vector machine classification to discriminate between text written from those older than 16 and those younger with 71.3% accuracy.

-   Panchenko et al. (2013) were able to predict with high accuracy if a file contains child pornography by analysis of file name and textual description in P2P networks.

References
==========

Egan, Vincent, James Hoskinson, and David Shewan. 2011. *Perverted Justice: A Content Analysis of the Language Used by Offenders Detected Attempting to Solicit Children for Sex*. Nova Science Publishers. <http://hdl.handle.net/2381/8855>.

Mcghee, India, Jennifer Bayzick, April Kontostathis, Lynne Edwards, Alexandra Mcbride, and Emma Jakubowski. 2011. “Learning to Identify Internet Sexual Predation.” *Int. J. Electron. Commerce* 15 (3) (apr): 103–122. doi:10.2753/JEC1086-4415150305. <http://dx.doi.org/10.2753/JEC1086-4415150305>.

Panchenko, Alexander, Richard Beaufort, Hubert Naets, and Cédrick Fairon. 2013. “Towards detection of child sexual abuse media: categorization of the associated filenames.” In *Proceedings of the 35th European conference on Advances in Information Retrieval*, 776–779. Berlin, Heidelberg: Springer-Verlag. <http://dx.doi.org/10.1007/978-3-642-36973-5_82>.

Peersman, Claudia, Walter Daelemans, and Leona Van Vaerenbergh. 2011. “Predicting age and gender in online social networks.” In *Proceedings of the 3rd international workshop on Search and mining user-generated contents*, 37–44. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/2065023.2065035>.

Pendar, N. 2007. “Toward Spotting the Pedophile Telling victim from predator in text chats.” In *Semantic Computing, 2007. ICSC 2007. International Conference on*, 235–241. doi:10.1109/ICSC.2007.32.
