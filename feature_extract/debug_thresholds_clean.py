# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:22:28 2016

@author: brady
"""

import os
import wavio
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

from config import TRAIN_LABELS, TRAIN_MSAK 
from fe_utils import aboveFrameThreshold, getFrameSize

def run_sp_train(fname):
    """
    Visualize audio labels for a normal wav file. 
    Plots data and class
    :param file: filename as a string (spNN, no .wav extension)
    """
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
                
    time = np.arange(len(data))/mwav.rate
    plt.plot(time, data)
    
    time = np.arange(len(labels))/mwav.rate
    plt.plot(time, labels)
    #plt.xlim([0, 2])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend(['Data', 'Class'], loc='best')
    plt.show()

def run_nist_file(file):
    """
    Visualize audio labels for a NIST file. 
    Plots data and class
    :param file: filename as a string (msak0_NNN.wav)
    """
    os.chdir(TRAIN_MSAK)
    
    data, rate = sf.read(file, dtype='int16')
    if np.max(data) > 1:
        data = data/2.**15
        
    frame_len = getFrameSize(rate)
    
    labels = []

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
            
    labels = np.repeat(np.array(labels), 20e-3*rate)
                
    
    plt.plot(data)
    plt.plot(labels)

if __name__ == "__main__":
    # give it an fname
    # sp00 to sp30
    plt.style.use('research')
    #plt.style.use('fivethirtyeight')
    run_sp_train('sp05')
    #run_nist_file('msak0_102.wav')