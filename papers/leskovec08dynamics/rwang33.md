Overview
--------
They presented an analysis of a person-to-person recommendation network, consisting of 4 million people who made 16 million recommendations on half a million products. They used to a simple stochastic model to observe the propagation of recommendations and the cascade sizes. They presented a model that successfully identifies product and pricing categories for which viral marketing seems to be very effective.

Algorithm
---------
Simple model of propagating recommendations

1. Each individual will have p<sub>t</sub>, successful recommendations. We model p<sub>t</sub> as a random variable   
2. At time t+1, the total number of people in the cascade, N<sub>t+1</sub> = N<sub>t</sub> * (1+p<sub>t</sub>)    
3. Subtracting from both sides, and dividing by N<sub>t</sub>.     
4. Summing over long time periods.    
5. The right hand side is a sum of random variables and hence normally distributed.    
6. Integrating both sides, we find that N is lognormally distributed.    
7. The lognormal behaves like a power-law with exponent 1.     
8. We observe fat tails in cascade sizes.    
- All the formulas here are same to the paper.

Hypothesis
----------
1. > 50% of people do research online before purchasing electronics.   
2. Personalized recommendations based on prior purchase patterns and ratings.   
   - Amazon, “people who bought x also bought y”.  
   - MovieLens, “based on ratingsof users like you…”.   
   - Epinions, “based on the opinionsof the raters you trust” (Richardson & Domingos, 2002).    
3. Ratings have been shown to affect the likelihood of an item being bought.    
   - Resnick & Zeckhauser, 2001: eBay.     
   - Judith Chevalier and Dina Mayzlin, 2004: Amazon and BN.   
4. Senders and followers of recommendations receive discounts on products.     
5. Recommendations are made to any number of people at the time of purchase.     
6. Receiving more recommendations increase the likelihood of buying.     
7. Sending more recommendations influences more purchases.      

Data
----
Large online retailer (June 2001 to May 2003):    
1. 15,646,121 recommendations    
2. 3,943,084 distinct customers     
3.548,523 products recommended     
4.99% of them belonging 4 main product groups:   
   - books    
   - DVDs     
   - music    
   - VHS     

Experiments
-----------
1. Looking into the aggregate statistics of the recommendation network.      
2. Analyzing the probability of purchasing as one gets more and more recommendations.    
3. Measuring recommendation effectiveness as two people exchange more and more recommendations.    
4. Observing the recommendation network from the perspective of the sender of the recommendation.     

Results
-------
1. Receiving more recommendations does not always means increasing the likelihood of buying. The relationship is not liner. The probability of purchasing a product increases with the number of recommendations received, but quickly saturates.       
to a constant and relatively low probability. 
2. Sending more recommendations does not always influence more purchases. ONLY DVD has such an approximate liner relationship.    
3. The probability that the sender gets a credit with increasing numbers of recommendations is not liner aw well.    
4. Multiple recommendations between two individuals weaken the impact of the bond on purchases.      
5. There are limits to how influential high degree nodes are in the recommendation network.      

Assumptions
-----------


Synthesis
---------
With the right tools and metrics, marketers can diversify their marketing plans to incorporate viral marketing strategies. The research clearly shows that viral marketing can build unique and niche recommendation networks, bolster consumer engagement, and lift sales.     
       
And as consumers continue to favor a digitally-based, social network-centric world, it’s critical that Marketers become more expert at viral marketing. Key to this will be identifying amplifiers, focusing on congregation points, leveraging social media opportunities—all without overdoing it. As importantly, Marketers must discover new approaches to spread and scale viral marketing just as effectively as the flu seems to proliferate every flu season.      

Related Papers
--------------
[What is Twitter, a Social Network or a News Media?](http://85.25.97.242/archivos/download/2010-www-twitterlh49129.pdf)   
This is the ﬁrst quantitative study on the entire Twittersphere and information diffusion on it. They had analyzed a lot of detailed informantion deeply.    

[Group Formation in Large Social Networks: Membership, Growth, and Evolution](http://wiki.cs.columbia.edu/download/attachments/1979/Group+Formation+in+Large+Social+Networks-backstrom.pdf)   
Using two large sources of data: friendship links and community membership on LiveJournal, and co-authorship and conference publications in DBLP, they study how the evolution of these communities relates to properties such as the structure of the underlying social networks. They ﬁnd that the propensity of individuals to join communities, and of communities to grow rapidly, depends in subtle ways on the underlying network structure.    

[Earthquake Shakes Twitter Users: Real-time Event Detection by Social Sensors](http://csce.uark.edu/~tingxiny/courses/5013spring13/readingList/www2010.pdf)    
As described in this paper, they investigate the real-time interaction of events such as earthquakes, in Twitter, and propose an algorithm to monitor tweets and to detect a target event.


