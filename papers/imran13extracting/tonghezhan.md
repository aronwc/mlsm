Overview

Finding those self-contained information items which called “information nuggets”, can accelerate disaster response and alleviate the property and human losses.


Algorithm

Using Crowd Flower to do the classification manually, and also let the trained workers do the different kinds of classification and extraction , then caculate the percentage of each type and sub-type.
And the extract different nuggets in different steps, such as, for Caution and Advice Nuggets: 1) Location references; 2) Time references; 3)Caution/Advice; 4) Source; and 5) Type of Caution. Then, they take similiar steps to extract the other information nuggets from the tweets. 

Hypothesis

People will share the information about disaster and people can get the information from 
The information about disaster in the tweets can be classified and extracted manually.

Data

There are 206,764 unique tweets selecting during the Joplin 2011 tornado that struck Joplin, Missouri in the late afternoon of Sunday, May 22, 2011.

Experimentals

Manual classification and extraction with crowdsourcing: 1.Filtering informative messages 2.Classifying messages by type 3.Classifying messages by sub-type and extracting information nuggets
Then, Filtering Informative Tweets
Identifying Eye-Witness Tweets
Classify informative tweets into one of the following four categories: Caution/Advice; Donation; Casualty/Damage; and Information Source.

Results

The results of their experiments show that indeed machine learning can be utilized to extract structured information nuggets from unstructured text-based microblogging messages with good precision and recall.

Assumptions

They assumes that though some classifiers do have a low ratio, this just because the extractors are over conservative.

Synthesis

In the evaluation section of this paper, from his table we can see the precision of Damaged Object Extractor does not very good, the author assumes that it is just because the extractors are over conservative. But all other extractors have a good precision on extracting certain information, there are no excuse that they have such a big different on the precision. So, to make the work perfect, I think maybe they should change some extractors next time, or just revise the keywords, or change the judge standard to make sure whether the tweets focus on which area.  

Related Papers

Kipper, K., Dang, H. and M. Palmer. (2000) Class-Based Construction of a Verb Lexicon. In
Proceedings of the Seventeenth National Conference on Artificial Intelligence, Austin, TX, 691-696.

This paper mainly introduces an approach to build a wordnet with some functions, that people can use it directly. But the paper I do the summary focus on extract information on tweets about disaster, it is a specific area that apply the approach. And this approach inspires the author to create his method in the experiment.
 
Balana, C.D. (2012) Social media: major tool in disaster response. Inquirer Technology, 5 pp.

When I found it through the internet, It seems like a piece of news, not a completed research paper. In the article, the author mentioned that nowadays the social media must play an important role in helping people in the disaster, reporting the instant news from the area. To sum up, the social media must take more responsibilities in those kinds of events. And he also expected that experts can build a monitoring system and websites for quick response.
