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
    
    valid_thresh = [
        t if t > 0 else np.min(np.abs(tree_.threshold))
        for t in tree_.threshold
    ]
    
    quant_thresh = quantize(valid_thresh, precision)

    def recurse(node, depth, quant_tree_str):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = quant_thresh[node]
            
            quant_tree_str += "{}if {} <= {}:\n".format(indent, name, threshold)
            quant_tree_str += recurse(tree_.children_left[node], depth + 1, '')
            
            quant_tree_str += "{}else:  # if {} > {}\n".format(indent, name, threshold)
            quant_tree_str += recurse(tree_.children_right[node], depth + 1, '')
            
            return quant_tree_str
        else:
            quant_tree_str += "{}return {}\n".format(indent, np.argmax(tree_.value[node]))
            return quant_tree_str

    quant_tree_str = "def tree_{}b(features):\n".format(precision)
    quant_tree_str = recurse(0, 1, quant_tree_str)
    return quant_tree_str

      
def gen_quant_trees_str(tree, precisions):
    func_list_str = ''
    for p in precisions:
        names = ['features['+str(x)+']' for x in range(20)]
        func_list_str += tree_to_code(tree, names, p)
        func_list_str += "##################################################\n"
    
    return func_list_str
    
    
def make_quant_trees_module(filename, tree, precisions):
    trees_str = gen_quant_trees_str(tree, precisions)
    
    with open(filename, 'w') as f:
        f.write(trees_str)

    
def get_tree_results(tree, Xtest):
    """
    Runs data through a quantized DecisionTreeClassifier
    :param tree: DTC function handle
    :param Xtest: data to test
    :returns: predicted results
    """
    results = [tree(X) for X in Xtest]
    return np.array([results]).T
    
    
if __name__ == '__main__':    
    DIR = r'C:\Users\brady\GitHub\MinVAD\feature_extract'

    tr_data = np.load(os.path.join(DIR, 'train_130k.npy'))
    tr_class = np.load(os.path.join(DIR, 'train_130k_class.npy'))
    
    myData = np.hstack((tr_data, tr_class))
    np.random.shuffle(myData)

    cutoff = int(np.floor(0.8 * len(tr_class)))
    clf = tree.DecisionTreeClassifier(max_depth = 5)
    clf = clf.fit(myData[:cutoff, :19], myData[:cutoff, 20])
    test_str = gen_quant_trees_str(clf, np.arange(16, 15, -1))
    print(test_str)