#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classification experiments on the Pang et al data. Note that I'm not using the
same splits as in the paper (random instead). Example run:

$ python classify.py

read 1400 documents and 1400 labels
model        	binary	f1	pre	rec	acc	f1_std	pre_std	rec_std	acc_std
LogisticRegre	True	0.82	0.82	0.82	0.82	0.02	0.02	0.03	0.01
MultinomialNB	True	0.81	0.83	0.79	0.81	0.02	0.04	0.01	0.02
LogisticRegre	False	0.79	0.79	0.78	0.79	0.03	0.04	0.03	0.02
MultinomialNB	False	0.79	0.80	0.79	0.79	0.03	0.03	0.03	0.02
"""

from collections import Counter
import os
import urllib
import zipfile

import numpy as np
from sklearn import cross_validation  # , metrics
from sklearn.feature_extraction import DictVectorizer
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Binarizer
from sklearn.naive_bayes import MultinomialNB


def read_tokens(filename):
    return Counter(open(filename).read().split())


def read_files(path, label, x, y):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for fname in filenames:
            x.append(read_tokens(dirpath + '/' + fname))
            y.append(label)


def score(y_true, y_pred):
    '''Compute evaluation metrics. Note pos_label=1 parameter of
    f1/precision/recall. Thus, we only compute precision of the positive class
    (as opposed to computing the precision for both classes and taking the
    average).'''
    return {
        'acc': metrics.accuracy_score(y_true, y_pred),
        'f1': metrics.f1_score(y_true, y_pred, pos_label=1),
        'pre': metrics.precision_score(y_true, y_pred, pos_label=1),
        'rec': metrics.recall_score(y_true, y_pred, pos_label=1),
    }


def metric_names():
    '''Name of metrics. Gotcha: keep in sync with score function'''
    metric_names = ['f1', 'pre', 'rec', 'acc']
    return metric_names + [m + '_std' for m in metric_names]


def summarize(evals, n):
    '''Compute average and standard deviation for evaluation metrics'''
    avg = {}
    for key in evals[0].iterkeys():
        scores = np.array([e[key] for e in evals])
        avg[key] = np.average(scores)
        avg[key + '_std'] = np.std(scores)
    return avg


# download and unzip data if doesn't exist yet.
if not os.path.exists('tokens/pos/cv699_tok-10425.txt'):
    urllib.urlretrieve('http://www.cs.cornell.edu/people/pabo/movie-review-data/mix20_rand700_tokens_cleaned.zip', 'data.zip')
    zipfile.ZipFile('data.zip').extractall()

# read data
docs = []
y = []
read_files('tokens/pos', 1., docs, y)
read_files('tokens/neg', 0., docs, y)
print 'read', len(docs), 'documents and', len(y), 'labels'
y = np.array(y)

# construct preprocessing + models
pipeline_bin = Pipeline([('vec', DictVectorizer()),
                         ('bin', Binarizer())
                         ])
pipeline_counts = Pipeline([('vec', DictVectorizer())])

classifiers = [
    LogisticRegression(),  # this is equivalent to MaxEnt from the paper
    MultinomialNB(),
]

cv = cross_validation.KFold(len(y), 3, shuffle=True,
                            random_state=1234)

metric_names = metric_names()
print '\t'.join(['model        ', 'binary'] + metric_names)
for pipeline in [pipeline_bin, pipeline_counts]:
    x = pipeline.fit_transform(docs).toarray()
    for clf in classifiers:
        results = []
        for (train, test) in cv:
            clf.fit(x[train], y[train])
            pred = clf.predict(x[test])
            results.append(score(y[test], pred))
        results_avg = summarize(results, 3)
        print str(clf)[:13] + '\t' + str(pipeline is pipeline_bin) + '\t' + '\t'.join(['%.2f' % results_avg[m]
                                                                                    for m in metric_names])
