####Overview####

This paper seeks to demonstrate that influence models based on submodular functions associated with a greedy algorithm can get better results than usual heuristics when looking to find an optimal k-set in an influence propagation graph.

####Algorithm####

###### Influence Models
The goal of the two main algorithms is to choose a k-set of nodes (the *active* ones) in a graph G such that the propagation of the information owned by those nodes is optimized. As this problem is NP-hard, it uses a greedy hill-climbing algorithm to approximate the optimum.

Two diffusion models are used :

- Linear Threshold
- Independent Cascade

The accuracy of both of these models are guaranteed by the fact that they are submodular functions. Hence, they provide a (1-1/e)-approximation (approx. equals to 63.2%).

###### Experiments algorithms

In their experiences, researchers compare different algorithms which are :

- their greedy hill-climbing algorithm;
- the high-degree heuristic;
- the distance centrality influence measure;
- the uniformly random choice of nodes.

####Hypothesis####

When aiming to get the most influencing k-set of nodes in a graph, it is possible to outperform the classical heuristics used in sociology with a greedy algorithm and influence models based on submodular functions.

####Data####

They use a collaboration graph made from co-authorships in [arXiv](http://www.arxiv.com) physics publications. Each vertex of the graph represents a researcher who wrote at least one paper with a co-author. Each pair of authors who collaborated on a paper is linked by an edge. 

Once the data from arXiv processed, they obtain a 10748 nodes graph with edges between about 53000 pairs of nodes.

####Experimentals####

As experiments, they compare the algorithms in three different models of influence :

- the linear threshold model where the multiplicity of edges is used as weight.
- the independant cascade model where a uniform probability p of 1% (and then 10%) is applied to each edge of the graph. The probability of a node u to activate a neighbour v is 1-(1-p)^{c_{u,v}} where c_{u,v} is the number of edges between u and v.
- the "weighted cascade" model where high-degree nodes are assigned smaller probabilities.

####Results####

- In the linear threshold model, the greedy algorithm ouperforms the high-degree node heuristic by about 18%, and the central node heuristic by over 40%.
- In the weighted cascade model, the behavior of each algorithm is similar to the one in the linear threshold model.
- In the indenpendant cascade model with p = 1%, the network effects are way less noticeable than in the two previous models but the greedy algorithm still outperforms the heuristics.
- In the independant cascade model with p = 10%, the "random nodes" algorithm surprisingly outperforms the heuristics when more than 12 nodes are targeted.

####Synthesis###

- Greedy hill-climbing algorithms find *local* optimum which is not always equal to the *global* optimum. Those algorithms are efficient and finding a *local* optimum can be enough but is it possible that this characteristic of greedy algorithms provokes inaccurate results for some graph configurations?
- Did the researchers run their algorithm on data from an actual social network? If not, I think it might be made on Twitter once a correct graph representation of the users and their relations is made.
- I wonder if it is doable to combine the models described by this paper (Linear Threshold and Independant Cascade) and usual methods (high-degree heuristic and distance centrality) to get better results in looking for the optimal initial k-set.

####Related Papers####

- Domingos, P. (2005). [Mining social networks for viral marketing](http://ncwebcenter.com/domingos05.pdf). IEEE Intelligent Systems, 20(1), 80-82.
	- This paper is a follow-up paper focusing on viral marketing plans design.
- Remondino, M. (2011). [Word-Of-Mouth Marketing And Enterprise Strategies: A Bottom-Up Diffusion Model](http://anale-economie.spiruharet.ro/files/anale/Issue2_2011.pdf#page=101). Annals of Spiru Haret University, Economic Series, 2(2), 101-105.
	- This papers seeks to show the dynamics of social diffusion using a bottom-up approach conversely to the summarized paper which uses submodular functions.
