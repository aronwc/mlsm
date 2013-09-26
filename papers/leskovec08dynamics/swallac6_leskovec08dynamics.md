Overview
========

The authors present an analysis of a person-to-person network of recommendations of products. To this end, they note how the network changes and grows in size over time as well as the effectiveness of the network.

Algorithm
=========

The authors used a stochastic model that allowed for the presence of relatively large cascades for a few products, but reflects well the general tendency of recommendation chains to terminate after just a short number of steps.

Hypothesis
==========

1.  The characteristics of recommendation networks influence the purchase patterns of their members.

2.  The category of the product makes a difference in the likelihood that recommendations will be followed.

3.  Different times of the day affect the likelihood that a recommendation will be followed.

Data
====

1.  15,646,121 recommendations made among 3,943,084 distinct users collected from June 5, 2001 to May 16, 2003.

2.  548,523 products were recommended with 99% of them belonging to 4 main product groups: Books, DVDs, Music and Videos.

3.  5813 (1%) of products were discontinued.

Experiments
===========

First, they tracked successful recommendations as they influence purchases and further recommendations. They define successful recommendations as those which resulted in a purchase the first time. They then analyzed the probability of a purchase given a recommendation. Next, they looked at the effectiveness of a recommendations passed between two people over time. Finally, they observed the recommendation network from the perspective of the sender of that recommendation.

Results
=======

-   The probability of recommendation success (that is, resulting in a purchase) decreases with repeated interaction.

-   The probability of purchasing a product increases with the number of recommendations received, but quickly saturates to a constant and relatively low probability.

-   There are limits to how influential high degree nodes are in the recommendation network.

Assumptions
===========

1.  The biggest assumption is that a recommendation from one person to another will result in a purchase (if there would be one) from the same retailer as was recommended. This doesn’t take into consideration that someone might buy a product, but they might first shop around for it.

2.  They also assume that the recommendation is the only reason that the product got purchased. It might be the case that the recommendation was simply a reminder for something the person was going to buy anyway.

Synthesis
=========

The methods undertaken in the paper are very conclusive and well supported by tons of data. Looking forward it would be good to take into consideration perhaps demographics of the users as well as considering how the overall health of the economy affects the likelihood of recommendations working. When people are struggling to make ends meet, it’s probably the case that recommendations play a more significant role than they would have otherwise.

Related Papers
==============

-   Montgomery (2001) proposed quantitative marketing techniques and Resnick and Zeckhauser (2002; Chevalier and Mayzlin 2003) showed that the rating of products and merchants affect the likelihood of a producing being purchased.

-   Linden, Smith, and York (2003) showed that people who bought product *x* are more likely to buy *y* if they are recommended it.

-   Richardson and Domingos (2002) used Epinions’ reviewer network to make an algorithm which maximized viral marketing efficiency which assumed that individuals’ probability of purchasing a product depends on the opinions on the trusted peers in their network.

-   Kempe, Kleinberg, and Tardos (2003) evaluated the efficiency of several algorithms for maximizing the size of influence set given various models of adoption.

References
==========

Chevalier, Judith A., and Dina Mayzlin. 2003. “The Effect of Word of Mouth on Sales: Online Book Reviews.” *Working Paper Series* (10148) (December). <http://www.nber.org/papers/w10148>.

Kempe, David, Jon Kleinberg, and Éva Tardos. 2003. “Maximizing the spread of influence through a social network.” In *Proceedings of the ninth ACM SIGKDD international conference on Knowledge discovery and data mining*, 137–146. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/956750.956769>.

Linden, G., B. Smith, and J. York. 2003. “Amazon.com recommendations: item-to-item collaborative filtering.” *Internet Computing, IEEE* 7 (1): 76–80. doi:10.1109/MIC.2003.1167344.

Montgomery, Alan L. 2001. “Applying Quantitative Marketing Techniques to the Internet.” *Interfaces* 31 (2) (mar): 90–108. doi:10.1287/inte.31.2.90.10630. <http://dx.doi.org/10.1287/inte.31.2.90.10630>.

Resnick, Paul, and Richard Zeckhauser. 2002. “Trust Among Strangers in Internet Transactions: Empirical Analysis of eBay’s Reputation System.” In *The Economics of the Internet and E-Commerce*, ed. M. R. Baye. Elsevier Science. <http://www.amazon.com/exec/obidos/redirect?tag=citeulike07-20\&path=ASIN/0762309717>.

Richardson, Matthew, and Pedro Domingos. 2002. “Mining knowledge-sharing sites for viral marketing.” In *Proceedings of the eighth ACM SIGKDD international conference on Knowledge discovery and data mining*, 61–70. New York, NY, USA: ACM. <http://doi.acm.org/10.1145/775047.775057>.
