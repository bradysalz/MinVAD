# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:38:57 2016

@author: brady
"""

import numpy as np
from sklearn import tree
from sklearn.metrics import confusion_matrix

audio_class = np.reshape(audio_class, (-1, 1))
myData = np.hstack((audio_data, audio_class))
np.random.shuffle(myData)

#%%
cutoff = int(np.floor(0.8 * len(audio_class)))
clf = tree.DecisionTreeClassifier()
clf = clf.fit(myData[:cutoff, 0:19], myData[:cutoff, 20])

#%%
pred = clf.predict(myData[cutoff:, 0:19])

confusion_matrix(myData[cutoff:, 20], pred)