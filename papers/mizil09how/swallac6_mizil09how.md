Overview
========

The paper proposes a framework for understanding and modeling how
opinions are evaluated within on-line communities. The primary focus is
on evaluating not the opinions provided by people about a subject, but
on the evaluation of the opinions themselves as perceived by other
members of the public. To this end, the authors attempt to quantify the
“helpfulness" of opinions in on-line communities.

Algorithm
=========

Hypothesis
==========

The authors list concretely 3 hypotheses as well as a fourth so-called
“straw-man" hypothesis in regards to how social effects influence a
group’s reaction to an opinion:

-   *The conformity hypothesis.* Reviews are more helpful when the star
    rating of the review is closer to the average star rating.

-   *The individual-bias hypothesis.* Reviews are considered more
    helpful by a user if that review shares a similar opinion as the
    user.

-   *The brilliant-but-cruel hypothesis.* Negative reviews are
    considered more helpful because the reviewers are perceived as more
    intelligent, competent, and expert than those with positive reviews.

-   *The quality-only straw-man hypothesis.* The basic idea to this
    hypothesis is that there are a seemingly random assortment of
    factors that contribute to reviews being considered more helpful.

Data
====

The data used in the experiments is a dataset consisting of 4,043,103
reviews of 674,018 books on Amazon’s US site, as well as smaller
datasets from Amazon’s UK, Germany, and Japan sites. The authors would
have liked to work with all book reviews, but because of a limitation in
the Amazon Web Services API, they were not able to find a list of all
Amazon book ASIN’s. However, they were able to query (up to 4000
results) the best-selling titles from 3,855 categories. They also
aggregated the reviews from different versions (such as hard cover and
soft cover) of the same book. While the maximum number of reviews
obtainable from AWS is 100, the authors found that 99.3% of all books
had 100 or fewer reviews. The authors however focused primarily on the
1,008,466 reviews that had at least 10 “helpfulness" votes.

Experiments
===========

Generally speaking, the authors performed analysis for each of the four
hypotheses given.

-   *Deviation experiments.* The authors checked (by calculating the
    deviation from the mean) the conformity hypothesis.

-   *Experiments with “plagiarism".* The authors note (interestingly if
    I might add) that there is a large, yet unknown, percentage of the
    reviews which are almost identical across distinct yet related
    products. However, they note there is nothing that they can do about
    that; human filtering would be too time consuming and a machine
    learned approach would almost certainly skew the results. Their
    answer to this was to focus on reviews which were 70% or more nearly
    duplicate.

Results
=======

-   As far as the conformity hypothesis is concerned, the results from
    the experiments performed by the authors seems to suggest that the
    helpfulness ration declines as the review deviates further from the
    mean star rating. Interestingly, this happens in both
    directions–both more negative and more positive. The authors note
    that if the absolute value of the deviation is used, then the
    conformity hypothesis is a natural fit, but other factors could be
    contributing. They also note that when the signed deviation is used,
    it is inconsistent with both the brilliant-but-cruel and the
    conformity hypothesis.

-   When quantifying the number of plagiarized reviews, the authors
    found that 8,313 pairs of reviews were plagiarized.

Assumptions
===========

-   The authors assume that reviews from different versions of the same
    product should be aggregated because the difference between the
    products is merely presentation.

Synthesis
=========

I certainly wouldn’t consider multiple versions of the same product the
same in terms of reviews. I can understand why they did it, a book is a
book, but that could be a rather faulty assumption to make. What if, for
example, a major publisher decides to start cutting costs on its
paperback versions of its books? The reviews would likely reflect this
across the board for all the books they produced and therefore would
produce different reviews for difference versions of the same product.
What’s more, to consider an audio book the same as printed word versions
seems incorrect as well. Maybe helpful reviews for that product are that
the accent of the person reading the book is hard to understand.

Related Papers
==============

There are a number of related works which also focused on helpfulness
votes:

-   J. Liu, Y. Cao, C.-Y. Lin, Y. Huang, and M. Zhou. Low-quality
    product review detection in opinion summarization. In procof
    EMNLP-CoNLL, pages 334–342, 2007. Poster paper.

    -   Used about 23,000 digital camera reviews of wich around 4900 had
        helpfulness votes.

-   A. Ghose and P. G. Ipeirotis. Estimating the socio-economic impact
    of product reviews: Mining text and reviewer characteristics. SSRN
    working paper, 2008. Available at http://ssrn.com/paper=1261751.
    Version dated September 1.

    -   Considered an unknown number of reviews for about 400 popular
        audio and video players, video players, digital cameras, and
        DVDs.

-   S.-M. Kim, P. Pantel, T. Chklovski, and M. Pennacchiotti.
    Automatically assessing review helpfulness. In procof EMNLP, pages
    423–430, July 2006.

    -   Used about 26,000 MP3 and digital-camera reviews after filtering
        of duplicate versions and duplicate reviews with fewer than 5
        helpfulness votes.

-   [Zhu Zhang , Balaji Varadarajan, Utility scoring of product reviews,
    Proceedings of the 15th ACM international conference on Information
    and knowledge management, November 06-11, 2006, Arlington, Virginia,
    USA](http://dl.acm.org/citation.cfm?id=1183626&CFID=358296960&CFTOKEN=71669304)

    -   Used about 2,500 reviews of electronics, engineering books, and
        PG-13 movies with no more than 10 helpfulness votes after
        filtering.

