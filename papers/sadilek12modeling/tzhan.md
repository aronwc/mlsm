Overview

The writer presents that they use Twitter data to present a framework that can identify people’s illness through the internet and even can estimate diseases without active user participation.

Algorithm

The writer used the Twitter Search API4, and collected a sample of public tweets that originated from the New York City . They also used  a Python script, and periodically queried Twitter for all recent tweets within 100 kilometers of the NYC city center. In order to avoid exceeding Twitter’s query rate limits and subsequently missing some tweets, we distributed the work over a number of machines with different IP addresses . 

Hypothesis

What roles do co-location and social ties play in the spread of infectious
diseases from person to person?

Data

To collect the data, the writer took one month long and started on May 18, 2010. And he used a Python script, and periodically queried Twitter for all recent tweets within 100 kilometers of the NYC city center. At the same time, they have logged nearly 16 million tweets authored by more than 630 thousand unique users.  To put these statistics in context, the entire NYC metropolitan area has an estimated population of 19 million people.

Experiments

Firstly, detecting Illness-Related Messages
They identify Twitter messages that indicate the author is infected with a disease of interest at the time of posting. And then they must learn to use the SVM classifiers. To overcome the class imbalance problem, where the
number of tweets about an illness is much smaller than the number of other messages, they should apply the ROCArea SVM learning method that directly optimizes the area under the ROC curve
Secondly, Modeling the Spread of Disease
They leverage users’ Twitter friendships and to combine other information to build a model.
Thirdly, they make sure that their observations are limited by the prevalence of public tweets in which users talk about their health, and by their ability to identify them in the flood of other types of messages

Results

The quantitatively shown as the green line in Fig. 5b in the paper, where they subtract out the effect of co-location from the influence of social ties. They do this by counting only sick friends who have not been encountered. Comparison with the red curve shows that for smaller numbers of friends (n ¤ 6), co-location has a weak additional effect over the proxy effect of social ties. However, for larger n, the residual impact of friendships plateaus, and co-location begins to dominate.

Assumptions

They focus on self-reported symptoms that appear in people’s Twitter status updates, and show that although such messages are rare, we can identify them with high precision as well as high recall. 
Prior work has developed a repertoire of powerful AI techniques for revealing hidden social ties and predicting user location—two features heavily leveraged by our public
health model. Therefore, there are opportunities for great synergy in these areas

Synthesis

In fact, the most opinions of the writer are reasonable and I agree with him. But there are still some small part that I think it is not accuracy enough. Just like they collected the users’ tweets, and estimated the the user is sick or not through some key words(feel sick and so on). It is a good way, but when people get some setbacks or something makes them depressed, they may use those key words, too. And it is not present that they get a real illness. 
Related Papers

Anderson, R., and May, R. 1979. Population biology of
infectious diseases: Part I. Nature 280(5721):361.

This article it totally different with the paper I did the summary. They are not the papers in a same  disciplinary. So I do  not know why it becomes one of the references of the paper. May be they have some relationships in the research about the spread of a disease.



Backstrom, L., and Leskovec, J. 2011. Supervised random
walks: predicting and recommending links in social
networks. In WSDM 2011, 635–644. ACM.

This paper has a similar goal with the paper I have read. But this paper’s choice of the social media is facebook. And they use different algorithm.
