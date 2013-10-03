Overview
========

The authors present a method to identify influence and susceptibility in networks while attempting to avoid the biases that are inherent in estimates that are traditional to social contagion.

Algorithm
=========

A standard statistical approach called a continuous-time single-failure proportional hazards model was used. The existing techniques were further modified to distinguish between two types of peer adoption: spontaneous adoption and influence driven adoption. The average treatment effects of notifications were estimated by aggregating many individual experiments in which messages were randomized within the local networks of the original user.

Hypothesis
==========

-   The mass of information made available from so called “population-scale networks" can be used to investigate the diffusion of information and influence.

Data
====

1.  1.3 million Facebook users.

2.  Conducted over 44 days during which 7,730 product adopters sent 41,686 automated notifications.

3.  976 unique peer adoptions.

Experiments
===========

They started by randomly manipulating messages sent from a commercial Facebook application which allows user to share opinions about movies, actors, directors, etc. As the users adopted and used the application, automatic messages of their activities were sent to a randomly selected subset of their friends. This message included a link with instructions on how to adopt the application to their own profile.

Results
=======

-   Younger users are more susceptible to influence than older users (age 31+) by 18%.

-   Men are more influential than women by 49%.

-   Women are 12% less susceptible to influence than men.

-   Single individuals are 113% more influential than those in a relationship. Generally the higher the level of the relationship, the greater level of susceptibility.

-   The most influence is found on those of the same age (97% more influence).

-   Influential individuals are less susceptible to influence than noninfluential individuals.

-   Influential people with influential friends are instrumental to the spread of this product.

Assumptions
===========

-   The authors seem to assume that just because they’re choosing a specific (random) set of friends through which to propagate their messages that Facebook has no control over whether they actually get the message or if others that were not originally intended will also get the message.

-   They also assume that unobserved confounding factors are controlled for because randomly chosen peers are equally likely to be exposed to external stimuli…however, I don’t think this is the case. Most people who have Facebook use it to connect to long lost friends who are typically geographically quite separated from the user. In this case, a political advertisement for the Governor of Wisconsin would hardly be applicable to a person in Florida and would not be shown.

Synthesis
=========

Generally I think this paper is well done aside from my comments in the assumption section. However I worry that Facebook doesn’t give enough control to actually say that these results are completely free from bias of any sort. Looking forward off this research it might be interesting to see how different products compare in influence. For example, if I have a friend who’s a movie aficionado, I’m going to be more likely to click on something from him about movies than something about music, but does that hold up across a whole network?

Related Papers
==============

-   Aral (2012) designed an experiment which illustrates the power of social networks to spread behavioral change. Aral looked at a message sent out during the 2010 US congressional elections which influenced the voting behavior of millions of people.

-   Aral, Muchnik, and Sundararajan (2009) developed a dynamic matched sample estimation framework to distinguish influence and homophily effects in dynamic networks.

-   Rohilla Shalizi and Thomas (2010) similar to the last considered the effects of homophily, social contagion, and the causal effect of an individual’s covariates on their behavior or other measurable responses.

References
==========

Aral, Sinan. 2012. “Social science: Poked to vote.” *Nature* 489 (7415) (sep 13): 212–214. doi:10.1038/489212a. <http://dx.doi.org/10.1038/489212a>.

Aral, Sinan, Lev Muchnik, and Arun Sundararajan. 2009. “Distinguishing influence-based contagion from homophily-driven diffusion in dynamic networks.” *Proceedings of the National Academy of Sciences* 106 (51): 21544–21549. doi:10.1073/pnas.0908800106. <http://www.pnas.org/content/106/51/21544.abstract>.

Rohilla Shalizi, C., and A. \~. C. Thomas. 2010. “Homophily and Contagion Are Generically Confounded in Observational Social Network Studies.” *ArXiv e-prints* (apr).
