---
title: CS595 - Network Analysis
---

## CS595
## Machine Learning and Social Media
### **Lecture 4: Network Analysis Overview**
<br>
####Aron Culotta
####Assistant Professor
####Computer Science
####Illinois Institute of Technology

---

- Easley & Kleinberg: "Networks, Crows, and Markets", Ch 1

---

## Examples of networks

---

## Email

![email](images/email.png)

Source: E & K

---

## Banks / Loans

![banks](images/banks.png)

Source: E & K

---

## Nonprofits

![nonprofits](images/nonprofits.png)

---

## Trade Routes

![trade](images/trade.png)

---

## Tuberculosis

![disease](images/disease.png)

---

## Facebook

<img src='images/fb.png' width='40%'/> One data set, many graphs

Source: E & K

---

## Applications

- fraud detection
- marketing
- epidemiology

---

## What is a network?

**Graph theory**

- $G = (E, V)$
  - $G$: graph
  - $V$: vertices / nodes
  - $E$: edges / links
    - weighted or unweighted
	- directed or undirected

---

## Graph Properties

- **Degree**$(v\_i)$: number of edges from $v_i$
  - for directed edges: indegree, outdegree

![graph1](images/graph1.png)

Degree$(B)$ = 3

---

## Graph Properties

- **Path**: set of edges connecting two nodes

![graph1](images/graph1.png)

Path$(A,D) = \\{e\_{AB}, e\_{BD}\\}$

---

## Graph Properties

- **Cycle**: path that starts and ends with the same node

![graph1](images/graph1.png)

$\\{e\_{BD}, e\_{DC}, e_{CB}\\}$

---

## Graph Properties

- **Distance**$(v\_1, v\_2)$: length of shortest path between $v\_1$ and $v\_2$

![graph1](images/graph1.png)

Distance$(A, D) = 2$

---

## Graph Properties

- **Diameter**$(G)$: distance between the two nodes in $G$ that are farthest apart

![graph1](images/graph1.png)

Diameter$(G) = 2$

---
## Graph problems

- Search

---

## Milgram's experiment

![milgram](images/milgram.png)

Source: E & K

---

## Small worlds

![small](images/small.png)

![watts](images/watts.png)


---

## Small worlds

![path](images/path.png)


- $L$: average shortest path
- $C$: *clustering coefficient* - fraction of your friends that are also friends

---

## Scale-free networks

![power](images/power.png) $P(k) \sim k^{-\gamma}$

- $P(k)$: fraction of nodes with degree $k$
- $\gamma \in [2,3]$: network parameter
- Describes diverse types of networks: internet, email, ...

---

## Influencers

- Who has the biggest influence on the rest of the network?

---

## Spread of influence

- How does the network change over time?
  - $\sigma(v\_i) = \sum\_{v\_j\in N(v\_i)} f(v\_j, v\_i)$
- $N(v\_i)$: neighbors of $v\_i$
- $f(v\_j, v\_i)$: influence of $v\_j$ on $v\_i$
- $v\_i$ becomes *activated* when $\sigma(v\_i) > \theta$

*Granovetter [1978]*: "Linear threshold model"

---

## Community detection

- What are the most connected components?

---

## Link prediction

- Will an edge between $v\_1$ and $v\_2$ form?

---

## Attribute prediction

- Homophily

![homophily](images/homophily.png)

Source: [UMD](http://www.cs.umd.edu/hcil/science20/)

---

## Discussion questions

- What types of nodes and edges exist in Twitter? in Facebook?

---

## Discussion questions

- What is an example of a network that is not a "small world"?

---

## Discussion questions

- What are other examples of homophily?

