# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:38:57 2016

@author: brady
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from training_helpers import make_quant_trees_module, get_tree_results

data_dir = r'C:\Users\brady\GitHub\MinVAD\feature_extract'

tr_data = np.load(os.path.join(data_dir, 'train_130k.npy'))
tr_class = np.load(os.path.join(data_dir, 'train_130k_class.npy'))

X_train, X_test, y_train, y_test = train_test_split(tr_data, tr_class, test_size=0.9)

cutoff = int(np.floor(0.8 * len(tr_class)))
clf = tree.DecisionTreeClassifier(max_depth = 5)

clf = clf.fit(X_train, y_train)
prec = np.arange(16, 1, -1)
fname = 'quant_trees.py'

make_quant_trees_module(fname, clf, prec)

qtrees = __import__(fname[:-3])
tree_funcs = [f for _, f in qtrees.__dict__.items() if callable(f)]

prec = []
scores = []
for tf in tree_funcs:
    prec.append(int(tf.__name__[5:-1]))
    print(tf, prec[-1])
    pred = get_tree_results(tf, X_test)
    print(accuracy_score(y_test, pred)+0.01-np.sum(np.equal(y_test, pred))/len(y_test))
    scores.append(accuracy_score(y_test, pred))
    print(confusion_matrix(y_test, pred), scores[-1])

    
prec = np.array(prec)
scores = np.array(scores)
pscores = np.array([prec, scores])
pscores.sort(axis=1)
plt.plot(pscores[0, :], pscores[1, :])

plt.xlabel('Quantization [bits]')
plt.ylabel('Accuracy [%]')