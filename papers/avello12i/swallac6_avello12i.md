Overview
========

Algorithm
=========

No algorithm presented.

Hypothesis
==========

The hypothesis (rather, assertion) made very clear by the author is: “No, you cannot predict elections with Twitter".

Data
====

No data given.

Experiments
===========

No experiments performed.

Results
=======

The author lists 8 flaws in current research regarding electoral predictions using Twitter data:

-   No papers actually make predictions, rather, they are post-hoc in their analysis.

-   There isn’t really chance in elections.

-   There isn’t a common way of counting votes in Twitter.

-   There isn’t a commonly accepted way of interpreting results.

-   Sentiment based classifiers are only slightly better than random classifiers.

-   All tweets are assumed to be trustworthy.

-   Demographics are neglected.

-   The voluntary nature of tweeting is ignored.

Then proceeds to list 8 pieces of advice:

-   Start making claims on future elections (after all, they’re happening all the time).

-   Factor in incumbency.

-   Clearly define what you consider to be a “vote" and provide arguments as to why you think this.

-   Clearly define and defend what you’re comparing your results to.

-   Sentiment analysis isn’t simple and is understudied in regards to trying to predict elections. Until that gets figured out, don’t use it to predict elections.

-   Make sure credibility checking is something you’ve put a good amount of time into.

-   Factor in demographics, that is, take into consideration the groups of people who voted in the previous election.

-   Make a solid effort towards identifying the silent majority.

The author also mentions a few core lines of future research:

-   Accurate sentiment analysis of political tweets.

-   Automatic detection of propaganda and disinformation.

-   Automatic detection of sock puppets.

-   Credibility checking.

-   Basic research on Twitter demographics and automatic profiling of users with regards to demographic attributes.

-   Basic research on user participation and self-selection bias.

Assumptions
===========

The biggest assumption I feel the author makes is that all of these flaws can be (relatively) simply fixed. I believe the author has correctly identified a number of core problems plaguing current research, but each of these problems is something one could spend their life on trying to solve and never get all the way there. It’s almost like the author is trying to say that all research up until this point using Twitter data is completely useless and should have never been done in the first place and these authors should have been spending their time trying to solve the “real" problems.

Synthesis
=========

While I generally agree that most papers I’ve come across in the machine learning world don’t tend to predict the future, I think there’s a very good reason for it. The author chalks this up to post-hot analysis with very few negative results. First, I don’t think a paper which was entirely (or at least mostly) based on “Obama will win the election based on our methods…" would ever get accepted into a peer reviewed journal. Simply put, peer reviewed papers shouldn’t try to be something they’re not (i.e., a discussion of results).

The author makes a point to say that one should clearly define the “golden truth" one uses to evaluate success and that it should be the “real thing" and not some poll. I agree completely, ideally the real thing should be used, but given literally this entire paper is on prediction it would require a time machine to get. What other than polls could be considered a “real thing" before an election even happens? It’s all just hedged bets at the end of the day.

As far as dealing with the silent majority, I’m really not sure how one could even start to accomplish this. I mean, if people don’t tweet, then what data is there? Just the difference between the expected and actual results? I agree with the author that this needs more attention, but I honestly wouldn’t even know where to start with this.

One direction I would certainly go in after reading this paper would be to attempt to classify the effect of media freedom on prediction (of any kind). This would be extremely difficult, especially given that in countries with very little freedom of media are likely not producing much data, but interesting nonetheless.

Related Papers
==============

-   Bollen, Pepe, and Mao (2009)

    -   Uses Profile of Mood States to distill from tweets time series corresponding to the evolution of 6 different emotional attributes (tension, depression, anger, vigor, fatigue, and confusion).

    -   Argued that Twitter data could be used for predictive purposes, though the author notes that no method is given.

-   O’Connor et al. (2010)

    -   Generated positive and negative scores for each tweet. Then used this data to compute a sentiment score.

    -   Author notes this paper clearly stated that there were many examples of incorrectly detected sentiment.

    -   No correlation found between electoral polls and Twitter sentiment data.

-   A. Tumasjan et al. (2010)

    -   “In all probability this is the paper which started all the fuzz regarding predicting elections using Twitter."

    -   Two parts:

        1.  Linguistic Inquiry and Word Count used to perform analysis of tweets related to different parties during German 2009 Federal election.

        2.  The count of tweets mentioning a party or candidate accurately reflected election results. Mean absolute error close to that of actual polls.

-   E. Mustafaraj and Metaxas (2010)

    -   Introduces the concept of *Twitter-bomb*: use of fake accounts in Twitter to spread disinformation.

    -   Describes the way a smear campaign by on party against another, how it was detected and aborted.

-   Mislove et al. (2011)

    -   Sample of Twitter users in US were analyzed on geography, gender, and race/ethnicity.

    -   Data was inferred from the user profiles. Geographical information from self-reported location, gender and race/ethnicity were inferred from username. Gender was based on statistical data.

-   Ratkiewicz et al. (2011)

    -   Truthy project–a system to detect astroturf political campaigns either to simulate support for or against a candidate.

-   P. T. Metaxas, Mustafaraj, and Gayo-Avello (2011)

    -   One of the few papers which doubts the abilities for machine learned techniques to predict elections.

    -   Concluded that Twitter data is only slightly better than chance when predicting elections.

    -   Echos 3 of the authors prescribed solutions to flaws found in most research.

-   Livne et al. (2011)

    -   Describes a method to predict elections based not only on Twitter data but also related information such as incumbency.

    -   Claims 7% increase in accuracy over traditional means alone.

-   Jungherr, Jurgens, and Schoen (2011)

    -   Argued that results from A. Tumasjan et al. (2010) were based on arbitrary choices and its results varied depending on the time window used to compute them.

-   Andranik Tumasjan et al. (2012)

    -   Responded to Jungherr, Jurgens, and Schoen (2011) saying essentially that the results did not vary based on the time window used to compute them.

    -   According to the author, these attempts aren’t good enough.

-   Bermingham and Smeaton (2011)

    -   Discusses different approaches to incorporating sentiment analysis into a predictive method.

    -   Trained using polling data for the elections it aimed to predict.

-   D. Gayo-Avello (2011)

    -   Discusses why previous predictions failed.

-   E. Mustafaraj et al. (2011)

    -   Discusses two very different behaviors in social media: a minority of users produce the majority of the content and there is majority of users who produce hardly any content.

-   Castillo, Mendoza, and Poblete (2011)

    -   Describes an automatic method to separate credible tweets from not credible ones using features which are extracted from tweets to generate a decision tree.

-   Sang and Bos (2012)

    -   Authors of this paper concluded that tweet counting was not a good predictor for, at least, the 2011 Dutch Senate election.

-   Skoric et al. (2012)

    -   Like the previous paper, shows only a certain amount of correlation between Twitter data and real votes and it’s not enough to make any accurate prediction.

    -   Discusses other problems such as democratic maturity of the country, competitiveness of the election, and media freedom.

-   Morris et al. (2012)

    -   Another paper attempting to establish the credibility of a tweet, though not automatic.

    -   Found that content alone is not enough alone to assess truthfulness.

References
==========

Bermingham, Adam, and Alan F. Smeaton. 2011. “On Using Twitter to Monitor Political Sentiment and Predict Election Results.” In *Proceedings of the Workshop on Sentiment Analysis Where AI Meets Psychology (SAAIP 2011), Asian Federation of Natural Language Processing, Chiang Mai, Thailand*, pp.2–10.

Bollen, Johan, Alberto Pepe, and Huina Mao. 2009. “Modeling public mood and emotion: Twitter sentiment and socio-economic phenomena.” *CoRR* abs/0911.1583.

Castillo, Carlos, Marcelo Mendoza, and Barbara Poblete. 2011. “Information credibility on twitter.” In *Proceedings of the 20th international conference on World wide web*, 675–684. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/1963405.1963500>.

Gayo-Avello, Daniel. 2011. “Don’t turn social media into another ’Literary Digest’ poll.” *Commun. ACM* 54 (10) (oct): 121–128. doi:10.1145/2001269.2001297. <http://doi.acm.org/10.1145/2001269.2001297>.

Jungherr, Andreas, Pascal Jurgens, and Harald Schoen. 2011. “Why the Pirate Party Won the German Election of 2009 or The Trouble With Predictions: A Response to Tumasjan, A., Sprenger, T. O., Sander, P. G., & Welpe, I. M. ?Predicting Elections With Twitter: What 140 Characters Reveal About Political Sentiment?” *Social Science Computer Review*. doi:10.1177/0894439311404119. <http://ssc.sagepub.com/content/early/2011/04/05/0894439311404119.abstract>.

Livne, Avishay, Matthew Simmons, Eytan Adar, and Lada Adamic. 2011. “The Party Is Over Here: Structure and Content in the 2010 Election.” In . <http://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/view/2852>.

Metaxas, P. T., E. Mustafaraj, and D. Gayo-Avello. 2011. “How (Not) to Predict Elections.” In *Privacy, security, risk and trust (passat), 2011 ieee third international conference on and 2011 ieee third international conference on social computing (socialcom)*, 165–171. doi:10.1109/PASSAT/SocialCom.2011.98.

Mislove, Alan, Sune Lehmann, Yong-Yeol Ahn, Jukka-Pekka Onnela, and J. Rosenquist. 2011. “Understanding the Demographics of Twitter Users.” In . <https://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/view/2816>.

Morris, Meredith Ringel, Scott Counts, Asta Roseway, Aaron Hoff, and Julia Schwarz. 2012. “Tweeting is believing?: understanding microblog credibility perceptions.” In *Proceedings of the ACM 2012 conference on Computer Supported Cooperative Work*, 441–450. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/2145204.2145274>.

Mustafaraj, Eni, Samantha Finn, Carolyn Whitlock, and Panagiotis Takis Metaxas. 2011. “Vocal Minority Versus Silent Majority: Discovering the Opionions of the Long Tail.” In *SocialCom/PASSAT*, 103–110. IEEE. [http://dblp.uni-trier.de/db/conf/socialcom/socialcom2011.html MustafarajFWM11](http://dblp.uni-trier.de/db/conf/socialcom/socialcom2011.html MustafarajFWM11 "http://dblp.uni-trier.de/db/conf/socialcom/socialcom2011.html MustafarajFWM11").

Mustafaraj, Eni, and Panagiotis Metaxas. 2010. “From Obscurity to Prominence in Minutes: Political Speech and Real-Time Search.” In *Proceedings of the WebSci10: Extending the Frontiers of Society On-Line*. Raleigh, NC, US. <http://journal.webscience.org/317/>.

O’Connor, Brendan, Ramnath Balasubramanyan, Bryan R. Routledge, and Noah A. Smith. 2010. “From Tweets to Polls: Linking Text Sentiment to Public Opinion Time Series.” In *Proceedings of the International AAAI Conference on Weblogs and Social Media*.

Ratkiewicz, Jacob, Michael Conover, Mark Meiss, Bruno Gonçalves, Alessandro Flammini, and Filippo Menczer. 2011. “Detecting and Tracking Political Abuse in Social Media.” In *Proc. 5th International AAAI Conference on Weblogs and Social Media (ICWSM)*. <http://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/view/2850>.

Sang, Erik Tjong Kim, and Johan Bos. 2012. “Predicting the 2011 dutch senate election results with Twitter.” In *Proceedings of the Workshop on Semantic Analysis in Social Media*, 53–60. Stroudsburg, PA, USA: Association for Computational Linguistics. <http://dl.acm.org/citation.cfm?id=2389969.2389976>.

Skoric, M., N. Poor, P. Achananuparp, Ee-Peng Lim, and Jing Jiang. 2012. “Tweets and Votes: A Study of the 2011 Singapore General Election.” In *System Science (HICSS), 2012 45th Hawaii International Conference on*, 2583–2591. doi:10.1109/HICSS.2012.607.

Tumasjan, A., T. O. Sprenger, P. G. Sandner, and I. M. Welpe. 2010. “Predicting elections with Twitter: What 140 characters reveal about political sentiment.” In *Proceedings of the Fourth International AAAI Conference on Weblogs and Social Media*, 178–185. <http://scholar.google.de/scholar.bib?q=info:mc319eHjea8J:scholar.google.com/\&output=citation\&hl=de\&as\_sdt=0\&ct=citation\&cd=28>.

Tumasjan, Andranik, Timm O. Sprenger, Philipp G. Sandner, and Isabell M. Welpe. 2012. “Where There is a Sea There are Pirates: Response to Jungherr, Jurgens, and Schoen.” *Social Science Computer Review* 30 (2): 235–239. doi:10.1177/0894439311404123. <http://ssc.sagepub.com/content/30/2/235.abstract>.
