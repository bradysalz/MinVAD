# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:38:57 2016

@author: brady
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from classifier.training_helpers import make_quant_trees_module, get_tree_results


def build_classifiers(tr_data=None, tr_class=None, 
                      clf=None,
                      module_name='quant_trees.py', 
                      min_precision=4,
                      max_precision=16):
    """
    Construct fixed point decision tree classifiers
    :param tr_data: filepath of training data (assumes *.npy file, NxM)
    :param tr_class: filepath of training class (assumes *.npy file. Nx1)
    :param clf: DecisionTreeClassifier from sklearn
    :param module_name: name of module that holeds created quantized tree functions
    :param min_precision: minimium quantization level in bits
    :param max_precision: maximum quantization level in bits
    """
    data_dir = r'C:\Users\brady\GitHub\MinVAD\feature_extract'
    if tr_data is None:
        tr_data = np.load(os.path.join(data_dir, 'train_90k.npy'))
    
    if tr_class is None:
        tr_class = np.load(os.path.join(data_dir, 'train_90k_class.npy'))
    
    if clf is None:
        clf = tree.DecisionTreeClassifier(max_depth = 5)
    
    clf = clf.fit(X_train, y_train)
    prec = np.arange(16, 3, -1)
    fname = 'quant_trees_full.py'
    
    #if not os.path.exists(fname):
    make_quant_trees_module(fname, clf, prec)
    
    
def test_quant_classifiers(x_test, y_test, clf_module):
    """
    Iterate through and test all quantized trees    
    
    :param x_test: test data,  numpy array (NxM)
    :param y_test: test class, numpy array (Nx1)
    :param clf_module: **string** module name that holds the quant_trees
    :returns: precisions and predictions, numpy arrays
    """
    
#    module, ext = os.path.splitext(clf_module)
    qtrees = __import__(clf_module)
    
    tree_funcs = [f for _, f in qtrees.__dict__.items() if callable(f)]
    num_trees = len(tree_funcs)
    
    prec = np.zeros((num_trees))
    pred = np.zeros((y_test.shape[0], num_trees))

    for cnt, tf in enumerate(tree_funcs):
        prec[cnt] = int(tf.__name__[5:-1])
        data = get_tree_results(tf, x_test)
        pred[:, cnt] = np.squeeze(data)

    return num_trees, prec, pred


if __name__ == '__main__':
    data_dir = r'C:\Users\brady\GitHub\MinVAD\feature_extract'
    tr_data = np.load(os.path.join(data_dir, 'train_90k.npy'))
    tr_class = np.load(os.path.join(data_dir, 'train_90k_class.npy'))
    
    X_train, X_test, y_train, y_test = train_test_split(tr_data, 
                                                        tr_class, 
                                                        test_size=0.3)

    fname = 'quant_trees.py'
    build_classifiers(X_train, y_train, module_name=fname)
    
    #qtrees = __import__(fname[:-3])
    #tree_funcs = [f for _, f in qtrees.__dict__.items() if callable(f)]
    
    num_trees, prec, pred = test_quant_classifiers(X_test, y_test, fname)

    scores = np.zeros((num_trees))    
    for i in range(num_trees):
        scores[i] = f1_score(y_test, pred[:, i])
        
    pscores = np.array([prec, scores])
    pscores.sort(axis=1)
    
    plt.style.use('research')
    plt.plot(pscores[0, :], pscores[1, :], '-*')
    
    plt.xlabel('Quantization [bits]')
    plt.ylabel('Accuracy [%]')