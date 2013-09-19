Overview
========

This paper seeks to accurately model the spread of infections diseases utilizing data obtained from large real-world social networks.

Algorithm
=========

Detecting Illness-Related Messages
----------------------------------

-   Formulated semi-supervised cascade-based approach to learning a support vector machine classifier with a large area under the ROC curve. This is done to accurately determine when a tweet is indicating the author is sick.

-   Trained two SVN classifiers using 5,128 previously classified as either “sick" or “other" by humans such that the misclassification penalty for one direction was always 100 times larger than in the opposite direction:

    -   \( C_8 \) - Highly penalized for inducing false positives.

    -   \( C_0 \) - Heavily penalized for creating false negatives.

-   After classifiers were trained, they were used to label 1.6 million tweets.

-   This resulting dataset was further supplemented by another sample of 200 million tweets that \( C_0 \) classified as “other" with a high probability.

Modeling the Spread of Disease
------------------------------

-   Two people are consider next to each other if they are within 100 square meter cell within a time window, \( T \in \{1, 4, 12\} \) hours.

-   To take into consideration friendship, the authors use Twitter’s built in friendship of the users.

Hypothesis
==========

It is possible to provide quantifiable estimates of the characteristics of disease transmission on a large scale without user participation.

Data
====

-   Used the Twitter Search API to collect a one month sample of tweets originating from within 100 kilometers of the New York City area.

-   Collected 16 million tweets authored by more than 630 thousand unique users.

-   Concentrated on the 6,237 accounts which posted more than 100 GPS-tagged tweets.

-   Mentions and re-tweets were removed, but hashtags were kept.

|**Item**|**Tweet Count**|
|:-------|--------------:|
|Unique Users|632,611|
|Unique Geo-Active Users|6,237|
|Total Tweets|15,944,084|
|GPS-Tagged Tweets|4,405,961|
|GPS-Tagged Tweets by “Geo-Active" Users|2,535,706|
|GPS-Tagged Tweets by Geo-Active Users that Show Symptoms|2,047|
|Distinct Visited Locations|57,109|
|“Follows" Relationships Between Geo-Active Users|102,739|
|“Friends" Relationships Between Geo-Active Users|31,874|

Experiments
===========

The SVM was trained on a held-out set of tweets. After this, the weights of various key phrases for the trained SVM were applied to the remainder of the dataset to produce the results.

Results
=======

-   Trained SVM \( C_f \) tested on held-out set of 700,000 tweets with 0.98 precision and 0.97 recall.

-   In the case of co-location, authors found that all three time intervals fit \( f(x) = C \times e^{0.055x} \) where \( C \) is a constant that works with the time overlap.

-   For sick friends, authors found similar result of \( f(x) = 0.003 \times e^{0.413x} \). By contrast, the number of friends in any health state has no impact on one’s health. When the number of friends is small, co-location has a weak additional effect.

Assumptions
===========

-   It seems as though the assumption is made that if you’re friends on Twitter than you’re also co-located.

-   Co-location within a 100 meter square area means shared physical contact. Especially for a city like NYC, this is probably true for the vast majority of locations, but what about places like parks?

Synthesis
=========

The authors removed mentions to other users, but I wonder if this is an area of future research. That is, if someone is tweeting at another user and also self-described as sick, perhaps they are indicating that user might then become sick?

Related Papers
==============

-   Anderson and May (1979) built computational epidemiology on building models of coarse-grained disease spread via differential equations, Eubank et al. (2004) used simulated populations, and Grenfell, Bjornstad, and Kappey (2001) provided analysis of official statistics. These works focus on simulated populations and hypothetical scenarios where as this work attempts to model the health of so called real-world populations.

-   Krieck and Dreesman (2011) explored changing the traditional notification channels about a disease outbreak with data obtained from Twitter. They found that self-reported symptoms are the most reliable in detecting if a tweet is relevant to an outbreak or not.

-   Culotta (2010; Lampos, De Bie, and Cristianini 2010; Chunara, Andrews, and Brownstein 2012) concentrated on identified the overall trend of a particular disease outbreak by monitoring social media.

-   Ritterman, Osborne, and Klein (2009) showed that noisy Twitter data is actually a valuable source for predicting public opinion regarding the likelihood of a pandemic.

-   Relating to determining the location of tweets, Cho, Myers, and Leskovec (2011; Sadilek, Kautz, and Bigham 2012) demonstrated that it is possible to accurately predict people’s location from their online behavior and interactions.

References
==========

Anderson, R. M., and R. M. May. 1979. “Population biology of infectious diseases: Part I.” In *Nature*, 280:361–367. <http://view.ncbi.nlm.nih.gov/pubmed/460412>.

Cho, Eunjoon, Seth A. Myers, and Jure Leskovec. 2011. “Friendship and mobility: user movement in location-based social networks.” In *Proceedings of the 17th ACM SIGKDD international conference on Knowledge discovery and data mining*, 1082–1090. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/2020408.2020579>.

Chunara, Rumi, Jason R. Andrews, and John S. Brownstein. 2012. “Social and News Media Enable Estimation of Epidemiological Patterns Early in the 2010 Haitian Cholera Outbreak.” *The American Journal of Tropical Medicine and Hygiene* 86 (1): 39–45. doi:10.4269/ajtmh.2012.11-0597. <http://www.ajtmh.org/content/86/1/39.abstract>.

Culotta, Aron. 2010. “Towards detecting influenza epidemics by analyzing Twitter messages.” In *Proceedings of the First Workshop on Social Media Analytics*, 115–122. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/1964858.1964874>.

Eubank, Stephen, Hasan Guclu, V. S. Anil Kumar, Madhav V. Marathe, Aravind Srinivasan, Zoltan Toroczkai, and Nan Wang. 2004. “Modelling disease outbreaks in realistic urban social networks.” In *Nature*, 429:180–184. Nature Publishing Group. doi:10.1038/nature02541. <http://dx.doi.org/10.1038/nature02541>.

Grenfell, B. T., O. N. Bjornstad, and J. Kappey. 2001. “Travelling waves and spatial hierarchies in measles epidemics.” In *Nature*, 414:716–723. doi:10.1038/414716a. <http://dx.doi.org/10.1038/414716a>.

Krieck, Manuela, and Johannes Dreesman. 2011. “A New Age of Public Health: Identifying Disease Outbreaks by Analyzing Tweets.” In *Proceedings of Health Web-Science Workshop, ACM Web Science Conference*. <http://www.websci11.org/fileadmin/websci/Papers/Health_WS_Workshop-Identifying_Disease_Outbreaks_by_Analyzing_Tweets.pdf>.

Lampos, Vasileios, Tijl De Bie, and Nello Cristianini. 2010. “Flu detector: tracking epidemics on twitter.” In *Proceedings of the 2010 European conference on Machine learning and knowledge discovery in databases: Part III*, 599–602. Berlin, Heidelberg: Springer-Verlag. <http://dl.acm.org/citation.cfm?id=1889788.1889832>.

Ritterman, Joshua, Miles Osborne, and Ewan Klein. 2009. “Using prediction Markets and Twitter to predict a Swine Flu Pandemic.” In *Proceedings of the 1st International Workshop on Mining Social Media*. Sevilla, Spain. <http://www.socialgamingplatform.com/msm09/proceedings/paper2.pdf>.

Sadilek, Adam, Henry Kautz, and Jeffrey P. Bigham. 2012. “Finding your friends and following them to where you are.” In *Proceedings of the fifth ACM international conference on Web search and data mining*, 723–732. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/2124295.2124380>.
