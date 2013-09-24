####Overview####

This paper tries to answer the question which set of individuals should we target if our goal is to trigger a large cascade of further adoption. So, it shows that the greedy strategy obtains the best performance, and proves it with computational experiment on large collaboration networks.

####Algorithm####

The authors compare use two basic diffusion models to represent the spread of an idea through a social network:
- The linear threshold model where each node’s tendency to become active increases monotonically as more of its neighbors become active.
- The Independent Cascade Model: when a node become active, it has a single chance to activate each currently inactive neighbor with a probability p.


But these algorithms involve an initial set of active node. And the authors analyze the results of 4 algorithms to resolve the influence maximization problem (to find the top influential nodes in the social network):
- The greedy algorithm.
- The high-degree heuristic consists to choose nodes in order of decreasing degrees.
- The “distance centrality” consists to select nodes in order of increasing average distance to other nodes in the network.
- The fourth algorithm consists of choosing nodes uniformly at random.

####Hypothesis####

- The linear threshold and the Independent Cascade Models can determine the spread of an idea through a social network
- A greedy strategy is better to find the top influential nodes.

####Data####

A collaboration graph is used as dataset
- It was obtained from co-authorships in physics publications, with simple settings of the influence parameters.
- It contains 10748 nodes and edges between about 53000 pairs of nodes.
- It contains a node for each researcher who has at least one paper with co-author in the arXiv database (high-energy physics theory section)

####Experimental####

This paper compares the algorithms (the greedy algorithm, the high-degree heuristic, central node heuristic and the "random algorithm") in three different models of influence:
- 1. In the linear threshold model where the multiplicity of edges is treated as weights.
- In the independent cascade model where a uniform probability of p is assigned to each edge of the graphs with p between 1% and 10%.
- In a special case of the Independent Cascade Model where each edge from node u to v is assigned probability 1/d of activating v.
 
####Results####

- In the linear threshold model, the greedy algorithm outperforms the high-degree node heuristic by about 18% and the central node by over 40%
- Better marketing results can be obtained by explicitly considering the dynamics of information in a network rather than relying on structural properties of the graph.
- For the weighted cascade model, the behavior is the same as the linear threshold model but the scale is slightly different.
- For the independent cascade model with probability 1%, it is very similar to the previous experiments. The network effects are much weaker in with model.
- The linear threshold and weighted cascade models rely heavily on low-degree nodes as multipliers, even though targeting high-degree nodes is a reasonable heuristic.
- In all the models, the greedy algorithm outperforms the others.
- The algorithm that achieves the best performance is a natural greedy hill-climbing strategy (63%).

####Assumptions####

- An idea can be spread from a node to another node only if it exists a link between them.

####Synthesis####

- Maybe we could try other algorithms for the influence maximization problem.
- The greedy algorithm seems good but what happens if the person represented by the node with the highest degree does not adhere to the idea? Maybe we can try to implement another method to use to broadcast the idea differently.
- How to determine who is the most influential? Is it really the person with a lot of connection? She can be influenced. So I think we can doubt about this. 
- We can take into account user preferences.

####Related Papers####
- P. Domingos, M. Richardson. Mining the Network Value of Customers. Seventh International Conference on Knowledge Discovery and Data Mining, 2001.
  - This paper proposes to model the customer’s network value as a Markov random field and to see that as a social network, to determine which potential customers to market to.
- Yu Zhang, Zhaoqing Wang ; Chaolun Xia Dept. of Comput. Sci., Zhejiang Sci-Tech Univ., Hangzhou, China Identifying Key Users for Targeted Marketing by Mining Online Social Network
  - Like our paper, this paper compares different techniques on the real world social network to identify key users with great influence
- Yunlong Zhang, Jingyu Zhou, and Jia Cheng, Preference-based Top-K Inﬂuential Nodes Mining in Social Networks 
  - This paper proposes to find the top influential nodes in social networks in taking into account user preferences. 
