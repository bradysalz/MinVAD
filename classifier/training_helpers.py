# -*- coding: utf-8 -*-
"""
Helper functions for classification and quantization

Created on Mon Dec  5 14:50:27 2016

@author: brady
"""
import os
import numpy as np
from sklearn.tree import tree, _tree


def quantize(data, precision):
    """
    Turns floating point into fixed point data
    :param data: vector to quantize, assumes np-array
    :param precision: number of fixed points bits to used
    :returns: vector of length[data], with precision bits
    """
    data = np.array(data)
    data = data*1e5
    
    xmax = np.amax(np.abs(data))
    #if xmax <= 0:
    #    xmax = 0.000001 # helps with stability
    xq = xmax * np.minimum(
                    np.round(data*(2**(precision-1))/xmax) / (2**(precision-1)),
                    1-1/(2**(precision-1))
                )
    return xq/1e5


def tree_to_code(tree, feature_names, precision):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    
    valid_thresh = [t if t > 0 else np.min(np.abs(tree_.threshold)) for t in tree_.threshold]
    quant_thresh = quantize(valid_thresh, precision)
    print("def tree_{}b(features):".format(precision))

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            #threshold = quantize(tree_.threshold[node], precision)
            threshold = quant_thresh[node]
            print("{}if {} <= {}:".format(indent, name, threshold))
            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return {}".format(indent, np.argmax(tree_.value[node])))
            pass

    recurse(0, 1)
    print(set(quant_thresh), len(set(quant_thresh)))
    
    
def build_quant_trees(tree, precisions):
    for p in precisions:
        names = ['features['+str(x)+']' for x in range(20)]
        tree_to_code(tree, names, p)
        
        
if __name__ == '__main__':    
    DIR = r'C:\Users\brady\GitHub\MinVAD\feature_extract'

    tr_data = np.load(os.path.join(DIR, 'train_130k.npy'))
    tr_class = np.load(os.path.join(DIR, 'train_130k_class.npy'))
    
    myData = np.hstack((tr_data, tr_class))
    np.random.shuffle(myData)

    cutoff = int(np.floor(0.8 * len(tr_class)))
    clf = tree.DecisionTreeClassifier(max_depth = 5)
    clf = clf.fit(myData[:cutoff, :19], myData[:cutoff, 20])
    build_quant_trees(clf, np.arange(16, 3, -1))