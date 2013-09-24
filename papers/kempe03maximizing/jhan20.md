####Overview####
- This paper formulates the problem of selecting the most influential nodes in social network as a discrete optimization problem and shows that the problem has the property of submodularity. 
####Algorithm ####
- For selecting the set of most influential nodes, a greedy hill-climbing that selecting the most influential node in current step is guaranteed to achieve (1-1/e) approximation.
####Hypothesis####
- The general hypothesis is that the influence function is monotone and submodular.
####Data####
- The co-authorship data in the high energy physics theory section of the e-print arXiv consisting of 10748 nodes and 53000 edges.
#### Experiment####
- For estimating the influence, they simulate the influence spread process 10000 times for each targeted set.
- They compare the performance of algorithms which select targeted nodes randomly, high-degree nodes, high-centrality nodes,  and greedy algorithm.  
####Results####
- The greedy hill-climbing algorithm performs best for selecting initial targeted set under both models. 
####Assumption####
- The nodes are only influenced by their neighbors inside the social network, so other influence sources are ignored. 
####Synthesis####
- We can extend the model to incorporate the time delay during the process of influence spread with a deadline constraint.
- We can design more efficient approximation algorithms to estimate the influence of a given target set. 
- We can also consider the influence source outside the social network, such as the newspaper, TV and other media. 
####Related Papers####
- Kempe, David, Jon Kleinberg, and Éva Tardos. "Influential nodes in a diffusion model for social networks." Automata, languages and programming. Springer Berlin Heidelberg, 2005. 1127-1138.
 - This paper defined natural and general model of influence propagation called decreasing cascade model and showed that the influence maximization problem maintains submodularity.
- Mossel, Elchanan, and Sebastien Roch. "On the submodularity of influence in social networks." Proceedings of the thirty-ninth annual ACM symposium on Theory of computing. ACM, 2007.
 - This paper showed that under general threshold model where the activation function is monotone and submodular, the influence maximization problem maintains submodularity.
