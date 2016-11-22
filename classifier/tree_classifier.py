# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:38:57 2016

@author: brady
"""

import numpy as np
from sklearn import tree
from sklearn.metrics import confusion_matrix

cutoff = np.floor(0.8 * len(audio_class))
clf = tree.DecisionTreeClassifier()
clf = clf.fit(audio_data[:cutoff, :], audio_class[:cutoff])
#%%
pred = clf.predict(audio_data[cutoff:, :])

confusion_matrix(audio_class[cutoff:], pred)