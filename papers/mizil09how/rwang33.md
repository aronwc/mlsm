Overview:

In this paper, the authors try to understand and model how opinions are evaluated within online communities. For example, on Amazon.com, the users not only write product reviews, but also provide us with an indication of the helpfulness of the reviews ("26 of 32 people found the following review helpful"). Previous work have shown that helpfulness votes of reviews on Amazon.com are not necessarily strongly correlated with certain measures of review quality. Rather, various complex social feedback mechanisms tend to affect how Amazon users evaluate each others' reviews in practice.


Algorithm:

Deviation from the mean.
Variance and individual bias. 
Controlling for text: Taking advantage of “plagiarism”. 


Hypothesis:

The conformity hypothesis: 
a review is evaluated as helpful when its star rating is closer to the consensus (or average) star rating for the product.

The individual-bias hypothesis: 
a user will rate a review more highly if it expresses an opinion that he or she agrees with. Notice that if a diverse range of users apply this rule, then the overall helpfulness evaluation would be hard to distinguish from one based on conformity.

The brilliant-but-cruel hypothesis: 
negative reviewers are perceived as more intelligent, competent and expert than positive reviewers.

The quality-only straw-man hypothesis: 
the helpfulness of the review is being evaluated, purely based on the textual content of the reviews.


Data:

The authors try to investigate how data on star ratings and helpfulness votes can support or contradict these hypotheses, using a dataset consisting of over four million reviews of roughly 675,000 books on Amazon's US site as well as smaller but comparably sized corpora from Amazon's UK, Germany and Japan sites.


Experiments:

Deviation from the mean:
The helpfulness ratio of a review is the fraction of evaluators who found it helpful. The product average for a review of a given product is the average star rating given by all reviews of the product. The authors found that the median helpfulness ratio of reviews decreases monotonically as a function of the absolute difference between their star rating and the product average. This finding seems to be consistent with the conformity hypotheses but a closer look raises some issues. Looking at the signed difference, which is positive or negative depending on whether the star rating is above or below average, the authors found that not only does the median helpfulness as a function of signed difference fall away on both sides of 0, it does so asymmetrically: slightly negative reviews are punished more strongly, with respect to helpfulness evaluation, than slightly positive reviews. Not only does this disprove the brilliant-but-cruel hypothesis, this finding is at odds with the conformity hypothesis in its pure form because closeness to the average is not being equally rewarded; overly positive ones are rewarded more.

Variance and individual bias:
To explain the above phenomena, the authors associated with each product the variance of the star ratings assigned to it by all its reviews. They then grouped products by variance, and performed the signed-difference analysis on sets of products having ﬁxed levels of variance. They found that:
• When the variance is very low, the reviews with the highest helpfulness ratios are those with the average star rating.
• With moderate values of the variance, the reviews evaluated as most helpful are those that are slightly above the average star rating.
• As the variance becomes large, reviews with star ratings both above and below the average are evaluated as more helpful than those that have the average star rating (with the positive reviews still deemed somewhat more helpful)
It turns out that these findings are consistent with a simple model of individual bias in the presence of controversy. Suppose that opinions are drawn from a mixture of two single-peaked distributions, one with larger mixing weight with mean above the overall mean of the mixture, and one with smaller mixing weight whose mean is below it. If each user has an opinion from this mixture, corresponding to their own personal score for the product, and they evaluate reviews as helpful if the review’s star rating is within some ﬁxed tolerance to their own, we will observe that as variance increases from 0, the reviews evaluated as most helpful are slightly above the overall mean, with a “dip” in helpfulness around the mean.

Controlling for text: Taking advantage of “plagiarism”:
As a final experiment, the authors try to prove that the quality-only strawman hypothesis does not actually hold. To do this, the author took advantage of the rampant plagiarism and duplication of reviews on Amazon.com. The authors found that very often, the two members of a “plagiarized” pair are associated with different products with different averages and variances and have very different star ratings. They found that within a “plagiarized” pair, the copy of the review that is closer to the average has the higher helpfulness ratio. Thus even for reviews with the same textual content, the scores differ based on its relation to other scores and to the mean score.


Results:

A review’s perceived helpfulness depends not just on its content, but also the relation of its score to other scores.


Assumptions:
