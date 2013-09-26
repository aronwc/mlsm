Overview
--------
They presented an analysis of a person-to-person recommendation network, consisting of 4 million people who made 16 million recommendations on half a million products. They used to a simple stochastic model to observe the propagation of recommendations and the cascade sizes. They presented a model that successfully identifies product and pricing categories for which viral marketing seems to be very effective.

Algorithm
---------
Simple model of propagating recommendations

1.Each individual will have p,,t,, successful recommendations. We model p,,t,, as a random variable
2.At time t+1, the total number of people in the cascade, Nt+1 = Nt * (1+pt)
3.Subtracting from both sides, and dividing by Nt, we have

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

Data
----
Large online retailer (June 2001 to May 2003):   
1. 15,646,121 recommendations
2. 3,943,084 distinct customers
3.548,523 products recommended
4.99% of them belonging 4 main product groups:
  - books
  - DVDs
  - music
  - VHS

Experiments
-----------


Results
-------


Assumptions
-----------


Synthesis
---------


Related Papers
--------------
