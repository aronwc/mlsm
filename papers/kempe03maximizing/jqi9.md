####Overview####
- The main purpose of this paper is trying to find a method that makes a certain message, idea or product spread quickly by analyzing the probabilistic model of interaction to find the most influential member of a social network.

####Algorithm####
- The most important algorithm that the authors used is the greedy hill climbing algorithm, which means they attempted to find a better element to put in the model set time by time, until they got the best ones. And here better stand for more connection with other elements.
####Hypothesis####
    - The optimization problem cannot even be approximated to within a non-trivial factor.
- Approximation algorithms for maximizing the spread of influence in these models can be developed in a general framework based on submodular functions.
- Their algorithm out-performs node-selection heuristics based on the well-studied notions of degree centrality and distance centrality from the field of social network analysis.

####Data####
- They use collaboration between physicists as a test data pool (papers in the high energy physics theory section of the e-print arXiv (www.arxiv.org).), treat it like a social network, which mean if you publish a paper with the other physicists, then an invisible link will be established between you and the other co-authors, also it means you are kind of supporter of their ideas or thesis. All the one author paper had been ignored.

####Experiment####
    - They compared the algorithms in three different models of influence, linear threshold model, independent cascade model, weighted cascade model.
    - To implement the greedy hill climbing algorithm, they simulate the process 10000 times for each targeted set, why not more? Since previous runs indicate that the quality of approximation after 10000 iterations is comparable to that after 300000 or more iterations.

####Result####
- 1. In the linear threshold model, The greedy algorithm outperforms the high-degree node heuristic by about 18%, and the central node heuristic by over 40%.
- 2. In the weighted cascade model, network influences of the nodes are not reflected accurately by their degree or centrality. Since that in expectation, each node is influenced by the same number of other nodes in both models, the degrees are relatively concentrated around their expectation.
- 3.For the independent cascade model with probability 1%, each targeted node only activates three additional nodes. But the heuristic of choosing random nodes performs significantly better than in the previous two models.
- 4. Independent cascade model with probability 10%, performance of the “random nodes” heuristic is much higher 

####Assumption####
- The node will only effected by their neighbors, cannot be affected by others not nearby.
- The experimental result can be extended to the other models.

####Synthesis####
- I don’t really like their test data, too far from the life of common people, not representative, if I chose the test data, I will try to get some hot topic on twitter, then analyze their spread path, and try to find which set of user is more active and act as a transfer station of certain theme.
- This topic has been discussed for a long time, since it got great business value behind it, if you know something, who should you tell to make it reach the right person? Someone is always trying to control public opinion, they can use theory like this paper mentioned as a weapon.  But modern technology make things change much faster than before, people can get information from so many ways, it will be a relatively complicated problem to analyze.

####Related Paper####
Social Contagion: An Empirical Study of Information Spread on Digg and Twitter Follower Graphs,
Kristina Lerman, Rumi Ghosh, Tawan Surachawala
- This paper got same topic but more practical and related to social media.
Group Evolution Discovery in Social Networks, Piotr Bródka, Stanisław Saganowski, Przemysław Kazienko
- This paper will let you know social network better, also their theory may show a new way to analyze the spread of information among a social network.

