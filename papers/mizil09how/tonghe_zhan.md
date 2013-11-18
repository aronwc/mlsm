Overview

The paper through various datas, algorithms and diagrams shows us how people 

evaluate the helpfulness votes on those book reviews in Amazon.com.  

Algorithm

Calculate the deviation of the average, they define the helpfulness ratio of a review 
to be the fraction of evaluators who found it to be helpful , and then define the product 
average for a review of a given product to be the average star rating given by all 
reviews of that product.

To signed the difference, not only does the median helpfulness as a function of 

signed difference in the graph, fall away on both sides of 0.


Analyze the variance, they associate with each product the variance of the star 

ratings assigned to it by all its reviews. And then group products by variance, and 

perform the signed-difference analysis above on sets of products having fixed levels 

of variance.


4. They define a “plagiarized” pair of reviews to be two reviews of different products 


with near-complete textual overlap, and enumerate the several thousand instances of 


plagiarized pairs on Amazon.

They employed a threshold of 70% or more nearly duplicate sentences, where 

near-duplication was measured via the code of Sorokina et al.


Hypothesis

The conformity hypothesis: when a review’s star rating is closer to the consensus 

star rating of a product, it is more helpful.

The individual bias hypothesis: When someone agree with the review’s opinion, 

they will think it is more helpful.

The brilliat-but-cruel hypothesis: negative reviews will considered more intelligent 

and professional.

The quality only staw-man hypothesis: maybe people who write long reviews or 

assign particular star ratings will get more trust from people.

Data

They choose over 4 million reviews of roughly 675000 books on Amazon’s U.S 

Site as dataset.

Also, they collect some reviews of books come from Amazon’s U.K, Germany and Japan sites.

Experimental

First of all, collect large scale of reviews through the website for them to do the 

research.


Then begin to handle those datas, get the deviation from the mean, find variance and 

individual bias, and use the “plagiarized” control the large number of  texts. And 

analyze the datas and diagrams.

Do some further related work. Built a model based on individual bias and mixtures of 

distribution. 

Results

The helpfulness review of  the book dependent on what the review said, and also the
relation of its star rating. This dependence on the star rating contrasts with a number of theories from sociology and social psychology, but through this we can built a model of individual bias and a mixture of opinion distributions. And It is still not sure about the text quality influence people and in what level.

Assumption
The helpfulness vote maybe have a relationship with the review’s text quality and maybe have the some corelated to what they have proved in the article.

Synthesis

What I really disagree with is the “plagiarized” review have a big impact on the helpfulness vote, firstly it is very hard to set the standard, what is a ‘plagiarized” review, if people think the same and write some short words, “That’s good” That’s really good”or “That’s what I need”. They are the same meaning, but is that belong to plagiarized? It is very hard to control. And what I support most is the negative review is the true review, really helps me a lot, and it can prevent many people to purchase some bad books.



Related Papers

F. Wu and B. A. Huberman. How public opinion forms. In
Proc. Wksp. on Internet and Network Economics (WINE), 2008.

It is opinion not towards a concrete thing or object, not like the article what I do this summary.



J. Liu, Y. Cao, C.-Y. Lin, Y. Huang, and M. Zhou. Lowquality
product review detection in opinion summarization. In
Proc. EMNLP-CoNLL, pages 334–342, 2007.

This article mainly talks about the bias of low quality product review and do not involve other kind of possibility which will influence the helpfulness level of a review. 
