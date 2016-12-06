# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:22:28 2016

@author: brady
"""

import os
import wavio
import matplotlib.pyplot as plt
import numpy as np

from config import TRAIN_LABELS
from fe_utils import aboveFrameThreshold, getFrameSize

def run(fname):
    os.chdir(TRAIN_LABELS)
    
    with open(fname + '.csv') as f:
        labels = f.readline()    
    
    mwav = wavio.read(fname + '.wav')
    data = mwav.data/2**15
    old_labels = np.array([int(l) for l in labels.split(',')])
    old_labels = np.repeat(old_labels, 20e-3*mwav.rate)
    
    labels = []
    frame_len = getFrameSize(mwav.rate)
    for frame_cnt in range(int(len(data)/frame_len)):
        if frame_cnt*frame_len > len(data):
            end_pt = frame_cnt = len(data)
        else:
            end_pt = (frame_cnt+1) * frame_len
        frame = data[frame_len*frame_cnt : end_pt]
        
        if aboveFrameThreshold(frame):
            labels.append(1)
        else:
            labels.append(0)
            
    labels = np.repeat(np.array(labels), 20e-3*mwav.rate)
                
    
    plt.plot(data)
    plt.plot(labels)
    plt.plot(old_labels)
    plt.show()

if __name__ == "__main__":
    # give it an fname
    # sp00 to sp30
    run('sp05')