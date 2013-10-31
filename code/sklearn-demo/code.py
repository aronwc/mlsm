# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# In this example, I walk through how to use sklearn to classify users into male or female
# based on their user description.

# First, we need to get some tweets in JSON format.
# Create a tweets.json file with something like:
# twitter-curl --query "track=obama" > tweets.json
# This will query twitter for tweets containing the word obama.

# Now, we'll parse that file into a list of (name, description) tuples.
import json
import io
# open the json file
fp = io.open('tweets.json', mode='rt', encoding='utf8')
# read the names and description fields from each tweet.
data = []
for line in fp:
    js = json.loads(line)  # parse into a JSON object.
    name = js['user']['name']
    description = js['user']['description']
    if name and description:  # if fields aren't blank
        data.append((name.lower(), description.lower()))
print 'read', len(data), 'users'
print 'example:', data[0]

# <codecell>

# Now, we need to label them as male or female. 
# To do that, we get the top 500 male/female names from census
import requests  # This is a very handy library for html requests.
males = requests.get('http://www.census.gov/genealogy/www/data/1990surnames/dist.male.first').text.split('\n')
males = [m.split()[0].lower() for m in males[:500]]  # lower case and take top 500
print 'first male is', males[0]
females = requests.get('http://www.census.gov/genealogy/www/data/1990surnames/dist.female.first').text.split('\n')
females = [f.split()[0].lower() for f in females[:500]]  # lower case and take top 500
print 'first female is', females[0]

# Remove ambiguous names (those that appear on both lists)
# Note that the plus operator is overloaded to mean concatentation for lists.
ambiguous = [f for f in females + males if f in males and f in females]
print 'ambiguous is', ambiguous[0]
males = [m for m in males if m not in ambiguous]
females = [f for f in females if f not in ambiguous]
print 'got', len(males), 'males and', len(females), 'females'

# <codecell>

# sort male, female users
male_users = [d for d in data if len(d[0].split()) > 0 and d[0].split()[0] in males]
print len(male_users), 'males'
print male_users[0]
female_users = [d for d in data if len(d[0].split()) > 0 and d[0].split()[0] in females]
print len(female_users), 'females'
print female_users[0]

# <codecell>

# Make target vector. Female=1, Male=0
import numpy as np
y = np.array([0.] * len(male_users) + [1.] * len(female_users))
data = [d[1] for d in male_users + female_users]
print 'first label=', y[0]
print 'first description=', data[0]

# <codecell>

# Convert descriptions into feature vectors.
from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer()
X = vec.fit_transform(data)
print data[0],'\nis transformed into the sparse vector\n', X[0]
print 'the word THE is mapped to index', vec.vocabulary_['the']
print 'there are', len(vec.vocabulary_), 'unique features'

# <codecell>

# Compute cross validation accuracy
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
print 'avg accuracy=%.3f' % np.average(cross_validation.cross_val_score(clf, X, y, cv=5, scoring='accuracy'))

# <codecell>

# Try Naive Bayes
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
print 'avg accuracy=%.3f' % np.average(cross_validation.cross_val_score(clf, X, y, cv=5, scoring='accuracy'))

# <codecell>

# Try adding bigrams
vec = CountVectorizer(ngram_range=(1,2))
X = vec.fit_transform(data)
print 'there are', len(vec.vocabulary_), 'unique features'
print 'ten feature examples:', vec.vocabulary_.keys()[:10]
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
print 'avg accuracy with bigrams=%.3f' % np.average(cross_validation.cross_val_score(clf, X, y, cv=5, scoring='accuracy'))

# <codecell>

# Print top feature weights for female
clf = LogisticRegression()
clf.fit(X, y)  # fit on all data
top_indices = clf.coef_[0].argsort()[::-1] # sort in decreasing order
# reverse the alphabet to map from idx->word
vocab_r = dict((idx, word) for word, idx in vec.vocabulary_.iteritems())
print 'female words:\n', '\n'.join(['%s=%.3f' % (vocab_r[idx], clf.coef_[0][idx]) for idx in top_indices[:20]])
top_indices = clf.coef_[0].argsort() # sort in increasing order
print '\n\nmale words:\n', '\n'.join(['%s=%.3f' % (vocab_r[idx], clf.coef_[0][idx]) for idx in top_indices[:20]])

# <codecell>

# Use PCA to reduce the dimensionality of X to only 2 dimensions,
# then compute cross-validation accuracy of resulting data X2.
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X2 = pca.fit_transform(X.toarray())
print 'first document with reduced representation'
print X2[0]
dim1 = pca.components_[0]
print 'first PCA dimension (eigenvector):', dim1
top_indices = dim1.argsort()[::-1]
print 'top words of first dimension:\n', '\n'.join(['%s=%.3f' % (vocab_r[idx], dim1[idx]) for idx in top_indices[:20]])
dim2 = pca.components_[1]
print 'second PCA dimension (eigenvector):', dim2
top_indices = dim2.argsort()[::-1]
print 'top words of second dimension:\n', '\n'.join(['%s=%.3f' % (vocab_r[idx], dim2[idx]) for idx in top_indices[:20]])
print 'avg accuracy using only 2 dimensions=%.3f' % np.average(cross_validation.cross_val_score(clf, X2, y, cv=5, scoring='accuracy'))

# <codecell>


