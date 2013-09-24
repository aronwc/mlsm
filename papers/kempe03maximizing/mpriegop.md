####Overview#### 
They suggests a general approach for reasoning about the performance guarantees of algorithms for inﬂuence problems in social networks. They modeled this problem as finding a set of k seeds that maximizes the influence spread.

####Algorithm####
Two basic algorithms (using submodular functions): A- Operational models and B- Dynamic cascade models. Both consider an initial set of active nodes that start the diffusion proces
- a.The more active neighbours you have, the more probability you have to become an active user. The sum of the weigths of a user's neghbour is less than one. 
- a.Each user chooses a threshold uniformly at random from the interval 0 to 1.
- a. After this threshold an user will become an active user.
- b. Similar to a. An active user tries to activate it neighbour with some random probability.
- Domingos and Richardson firstly proposed the problem of mining the influence within a social network instead of a set of independent entities. They modeled the influence as a Markov random field.
- For setting up the intial active nodes they use the greedy, high-degree heuristic, distance centrality and random approach/algorithm.

####Hypothesis####
- People are likely to be affected by decisions of their friends and colleagues. Therefore, there on social networks there are individuals who influence others.
- It is possible to influence these individuals (the popular ones)

####Data####
- A collaboration graph obtained from co-authorships in physics publications from arXiv with 10748 nodes, and edges between
about 53000 pairs of nodes. They poolished some mistakes related to the names. 

####Experimentals####
- They compared the algorithms (last point at the algorithms section) in three different models of influence. 
  - In the linear threshold model they treated the multiplicity of edges as weights.
  - At the Cascade model they assigned a random probability between 0.01 and 0.1 or a fixed probability at the third one

####Results####
- They get a approximation guarantees ratio of 1 - 1/e with their model.
- At experiments performed at last section:
  - For the first the random approach performed really bad. As they increased the target size the rate of active between greedy, high-degree and distance centrality grew.
  - The results for the weighted cascade model and with the 0.01 probability performed similar to the last result.
  - For the 0.1 random performed slightly worse. And there were no much difference when augmenting the target set size.
- The best perform was greedy with a 63 %

####Assumptions####
- Viral marketing effects are related to how the usage of medical drugs is spread.
- Descriptive models (Domingos and Richardson) perform worse than operational models from mathematical sociology.
- Nodes can turn from inactive to active, but not the other way.
- Co-authorships graph is a good example of social network

####Synthesis###
- [Paper weakness] More background could be provided. For example, it is difficult to follow it with things like 'The optimal solution is NP-hard for most models that have been studied, including the model of [10]'. NP-hard? [10]?
- The diffusion and optimization algorithms are very well explained.
- Really good point about considering not every marketing models equal.
- Nowadays it is very easy to choose the influent nodes. For example at twitter the users with more retweets or more favorites.
- I would test/try to improve this model by, first, testing the network spreading some trend across twitter.Then, I would record how a neighbour influence other node and record it mixing with Cascade probability.
- For Linear Threshold, I would previously calculate the weight of a neighbour in Twitter by the number of retweets that was made by node v.

####Related Papers####
- Yuqing Zhu, Weili Wu, Yuanjun Bi, Lidong Wu, Yiwei Jiang, Wen Xu. [Better approximation algorithms for influence maximization in online social networks](http://link.springer.com/article/10.1007%2Fs10878-013-9635-7)
  - This paper outperforms the previous studies by achieving a 0.857 approximation ratio
- P. Domingos, M. Richardson. [Mining the Network Value of Customers.](http://dl.acm.org/citation.cfm?id=502525) Seventh International Conference on Knowledge Discovery and Data Mining, 2001.
  - They firstly proposed the problem of mining influence. They reduced the computational cost and optimize the amount of marketing funds on each customer
