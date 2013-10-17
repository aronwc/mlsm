Overview
========

During natural disasters, Twitter is a hotspot of information. However, the shere number of tweets posted during crises make it difficult for such disaster affected ares to process this information in a timely manner. To this end, the authors propose automatic (machine learning) methods for extracting information from microblogging sites such as Twitter.

Algorithm
=========

The binary features of the classifier considered a number of things including whether a tweet contains:

1.  The @ symbol or not.

2.  A URL or not.

3.  A hashtag or not.

4.  An emoticon or not.

5.  A number or not.

The scalar features only consisted of a number features indicating the tweet length.

The text features consisted of sparse linguistic features which included extracting things such as unigrams, bigrams, parts of speech, etc.

Hypothesis
==========

It would seem the primary hypothesis would be that tweets tweeted during times of crises can be used in time-critical situational awareness type scenarios.

Data
====

-   Joplin Dataset

    -   Tweets posted during the Joplin 2011 tornado that struck Joplin, Missouri late May 22,2011.

    -   Constructed by researchers at the University of Colorado.

    -   206,764 unique tweets gathered from Twitter Streaming API using hashtag *\#joplin* a few hours after tornado strike.

Experiments
===========

First, 4,406 tweets sampled uniformly at random were manually classified from the Joplin dataset. This was broken down into three tasks:

1.  Filtering informative messages - tweets were annotated according to whether they are of entirely personal nature, informative, or other. There were 190 “gold standard" messages.

2.  Classifying messages by type - 1,233 messages were examined and each was assigned an appropriate label from five categories. This resulted in 62 gold standard messages.

3.  Classifying messages by sub-type and extracting information nuggets - for each of the four types, workers classified a message by sub-type. In addition, they were also asked to extract a sub-string from the message that made them come to this conclusion.

Results
=======

In the quantitative assessment, 32% of the messages were labeled as “personal", 19% were labeled as “informative (direct)", 24% labeled as “informative (indirect)", 17% labeled as “informative (direct-indirect)" and the remaining 8% were labeled as “other". The level of agreement between those manually classifying these tweets was 55.94%.

In the machine learning section, the classifier was able to identify informative tweets with an AUC of 0.79 and a precision of 0.79 at a recall of 0.77 after a 10-fold cross validation. In the case of eye-witness tweets, the classifier had a precision of 0.57 at recall of 0.57.

Assumptions
===========

-   The biggest assumption here is that people who need help actually tweet during the time of crises.

Synthesis
=========

My first concern is that even in the manual classification the people ranking these messages only agreed about 56% of the time. Assuming that a human is better able to discern the nuances that are prevalent in communication, how can a computer do any better than that?

Related Papers
==============

-   S. Vieweg et al. (2010) and more recently S. Vieweg (2012) did almost exactly the same thing as this work in that they all looked at correctly identifying tweets sent during times of emergency with an aim to discern which constituted situational awareness.

-   Verma et al. (2011) was also very similar to this current work and also focused on identifying tweets during an emergency which had the greatest impact.

References
==========

Verma, S., S. Vieweg, W. J. Corvey, L. Palen, J. H. Martin, M. Palmer, A. Schram, and K. M. Anderson. 2011. “Natural Language Processing to the Rescue?: Extracting’Situational Awareness’ Tweets During Mass Emergency.” *Proc. ICWSM*.

Vieweg, Sarah. 2012. “Twitter communications in mass emergency: contributions to situational awareness.” In *Proceedings of the ACM 2012 conference on Computer Supported Cooperative Work Companion*, 227–230. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/2141512.2141584>.

Vieweg, Sarah, Amanda L. Hughes, Kate Starbird, and Leysia Palen. 2010. “Microblogging during two natural hazards events: what twitter may contribute to situational awareness.” In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 1079–1088. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/1753326.1753486>.
