---
title: CS595 - Reading Research
---

## CS595
## Machine Learning and Social Media
### **Lecture 3: Machine Learning Overview**
<br>
####Aron Culotta
####Assistant Professor
####Computer Science
####Illinois Institute of Technology

---

- Dietterich: "Machine Learning"
- Domingos: "A few useful things to know about machine learning"

---

## What is machine learning?

---

## What is machine learning?

"Study of methods for programming computers to learn." 

-- Dietterich

---

## What machine learning?

Study of systems that "automatically learn programs from data" 

-- Domingos

---

## What is machine learning?

A problem-solving technique that solves future problem instances based on
patterns found in past problem instances

---

## What is machine learning?

Often relies on *Big Data* and statistics

---

## Examples

---

![spam](images/spam.png)

---

<img src='images/search.png' width='50%'/>

---

<img src='images/netflix.png', width='70%'/>

---

<img src='images/bw.png' width='50%'/>

---

<img src='images/chopper.png' width='70%'>

---

<img src='images/car.jpg' width='70%'/>

---

![money](images/money.png)

---

<img src='images/doc.png' width='40%'/>

---

<img src='images/siri.png' width='40%'/>

---

<img src='images/watson.png' width='70%'/>

---

## Notation

- $\vec{x} \in \mathcal{X}$ &nbsp;&nbsp;&nbsp;&nbsp; *instance*, *example*, *input*
  - e.g., an email
- $y \in \mathcal{Y}$ &nbsp;&nbsp;&nbsp;&nbsp; *target*, *class*, *label*, *output*
  - e.g., $y=1$: spam ; $y=0$: not spam
- $f: \mathcal{X} \mapsto \mathcal{Y}$ &nbsp;&nbsp;&nbsp;&nbsp; *hypothesis*, *learner*, *model*, *classifier*
  - e.g., if $x$ contain the word *free*, $y$ is $1$.

---

## Problem types

- **Classification**
  - $\vec{x}$: image of a person ;  $y$: gender
- **Regression**
  - $\vec{x}$: image of a person ; $y$: age
- **Clustering**
  - $\vec{x}$: images of people ; $y$: cluster id of people that look similar
- **Structured classification**
  - $\vec{x}$: image of a person ; $\vec{y}$: location of their eyes and ears
  - $X$: sequence of images of people ; $Y$: subsequences containing people running

---

## Workflow

1. **Collect** raw data: emails
2. Manually **categorize** them:  spam or not
3. **Vectorize**: email -> word counts [**features**]
4. **Train** / **Fit**: create $f(x)$
5. **Collect** new raw data
6. **Predict**: compute $f(x)$ for new $x$


---

## Example: Spam Classification

---

**Steps 1 & 2: Collect and categorize**

**Spam:**

> Free credit report!


> Free money!


**Not spam:**

> Are you free tonight?

> How are you?

---

**Step 3: Vectorize**

> 'Free money!'

becomes

```
free: 1
money: 1
!: 1
?: 0
credit: 0
...
```

**Representation**: "Feature engineering is the key" -- Domingos

---

**Step 4: Train/Fit**

Which model to use?

- Naive Bayes
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors
- Support Vector Machines
- ... many many more

---

**Steps 5-6: Predict on new data**

> Free vacation!

**Spam**

---

How do you know if it works?

---

Simplest machine learning algorithm:

```
f = dict()

def train(X, Y):
	for x, y in zip(X, Y):
	  f(x) = y

def predict(x):
	return f(x)
```

---

Second simplest machine learning algorithm:

```
f = dict()

def train(X, Y):
	for x, y in zip(X, Y):
	  f(x) = y

def predict(x):
	x_closest = find_most_similar(x)
	return f(x_closest)
```

---

<img src='images/knn.png' width='80%'/>

<http://www.scholarpedia.org/article/K-nearest_neighbor>

---

## Generalization

How accurate will I be on a new, unobserved example?

---

How do you know if it works?

1. Train on data ${\mathcal D_1}$
2. Predict on data ${\mathcal D_2}$
3. Compute accuracy on ${\mathcal D_2}$.
   - Why not ${\mathcal D_1}$?

---

How do you know if it works?

1. Train on data ${\mathcal D_1}$
2. Predict on data ${\mathcal D_2}$
3. Compute accuracy on ${\mathcal D_2}$.
4. Tweak algorithm / representation
5. Repeat

---

How do you know if it works?

1. Train on data ${\mathcal D_1}$
2. Predict on data ${\mathcal D_2}$
3. Compute accuracy on ${\mathcal D_2}$.
4. Tweak algorithm / representation
5. Repeat

How many times can I do this?


---

## Measuring Generalization

- Cross-validation
  - train on 90%, test on 10%, repeat 10 x's
	- each example appears only once in test set

---

## Experimental Design

1. Collect data
2. Build model
3. Compute cross-validation accuracy
4. Tune model
5. Repeat

---

## Experimental Design

1. Collect data
2. Build model
3. Compute cross-validation accuracy
4. Tune model
5. Repeat
6. **Report accuracy on new data**


---

## Discussion Questions

- What is the difference between machine learning and statistics?

---

## Discussion Questions

- What is the impact of making an i.i.d. assumption among examples?
  - *independent and identically distributed*

---

## Discussion Questions

- What is overfitting? How do you know it is happening? How do you fix?

---

## Discussion Questions

- What is the hypothesis space and why does its size matter?

---

## Discussion Questions

- What is bias? variance?

---

<img src='images/biasvariance.png' width='70%'/>

<http://scott.fortmann-roe.com/docs/BiasVariance.html>

---



## Discussion Questions

- What is curse of dimensionality?
