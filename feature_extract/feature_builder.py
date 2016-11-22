# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:20:14 2016

@author: brady
"""

%load_ext autoreload
%autoreload 2

#%%
import os
import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.signal

from config import *
from fe_utils import *
from scipy.io import wavfile

#%% Init file structure
n_filt = 20
f_start = 100
f_stop = 4e3
f_center = np.logspace(np.log10(f_start), np.log10(f_stop), n_filt)
Q = 2

n_samples = 20e3

audio_data = np.zeros((0, n_filt))
audio_class = np.zeros((0,0))
audio_file = []

#%% Adding positive examples
cnt = 0
done = 0
os.chdir(ROOT_CLEAN_AN4)
while (cnt < n_samples):
    # load a random positive sample file
    file = random.choice(os.listdir())
    fs, data = wavfile.read(file)

    filt_bank = [createFilter(f_center[n], Q, fs) for n in range(n_filt)]
    
    if len(data.shape) == 2:
        data = stereoToMono(data)
    
    # process a single frame
    frame_len = getFrameSize(fs)
    for frame_cnt in range(int(len(data)/frame_len)):
        if frame_cnt*frame_len > len(data):
            end_pt = frame_cnt = len(data)
        else:
            end_pt = (frame_cnt+1) * frame_len
        frame = data[frame_len*frame_cnt : end_pt]
        
        frame_avg = np.zeros((1, n_filt))
        for i, bpf in enumerate(filt_bank):
            filt_frame = scipy.signal.lfilter(bpf[0], bpf[1], frame)
            frame_avg[0][i] = calcFrameAvg(filt_frame)
        
        # add data vectors
        audio_data = np.append(audio_data, frame_avg, axis=0)
        audio_class = np.append(audio_class, aboveFrameThreshold(frame_avg))
        audio_file.append(file)
        
        cnt += 1    

#%% Adding negatives examples
