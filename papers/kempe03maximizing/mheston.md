####Overview####
The authors consider the problem of which nodes in a network to target to maximize
the spread of influence. They present an algorithm for solving this problem as well
as an empirical case supporting that there method outperforms existing methods in
the social networking literature.

####Algorithm####
The authors use a greedy hill climbing algorithm, which starts with the empty set,
and repeatedly adds an element that gives the maximum marginal gain.

####Hypothesis####
The linear threshold and independent cascade models can be used to efficiently
approximate the the optimal solution for influence maximization.

####Data####
They use a collaboration graph based on co-authorships in physics publications
from arXiv. They ignored single author papers and represented each author as a
node, where an edge exists between the nodes if those authors have co-authored
a paper. The resulting graph has 10748 nodes, and edges between about 53000 pairs
of nodes.

####Experiments####
The authors apply the linear threshold model and the independent cascade model
with different probability values (1% and 10%) to the network. They also apply
a version of the independent cascade model in which high degree nodes are assigned
smaller probabilities. They compare these models to existing heuristic methods
which rely on nodes' degree and centrality, along with a baseline of choosing
random nodes.

####Results####
In the linear threshold model, they find their greedy algorithm outperforms
heuristic methods. They see similar results in the weighted cascade model,
on a smaller scale, and an even smaller scale using the cascade model with
prbability 1%. The results show that the linear and weighted cascade models
rely heavily on low-degree nodes as multipliers.

####Synthesis####
I'm not sure what this would look like, but it would be interesting to consider
how networks change over time and incorporate the addition or loss of an edge
between nodes and model how that affects information diffusion.

####Related Papers####
- Weng, Jianshu, et al. "Twitterrank: finding topic-sensitive influential twitterers." Proceedings of the third ACM international conference on Web search and data mining. ACM, 2010.
  - Extends the PageRank algorithm to measure influence of users on Twitter.
- Leskovec, Jure, et al. "Cost-effective outbreak detection in networks." Proceedings of the 13th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2007.
  - Also uses submodular functions in developing an algorithm for outbreak detection.
- Gruhl, Daniel, et al. "Information diffusion through blogspace." Proceedings of the 13th international conference on World Wide Web. ACM, 2004.
  - Using weblogs as their domain, the authors formalize types of topics and topic propogation within the network, as well as how information flows through the network.
