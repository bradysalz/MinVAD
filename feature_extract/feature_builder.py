# -*- coding: utf-8 -*-
"""
Feature builder Code

Created on Mon Nov 21 14:20:14 2016

@author: brady
"""

#%load_ext autoreload
#%autoreload 2

#%%
import os
import numpy as np
import scipy.signal

from .config import *
from .fe_utils import *


#%% Init file structure
POS = 1
NEG = 0

n_filt = 20
f_start = 100
f_stop = 4e3
f_center = np.logspace(np.log10(f_start), np.log10(f_stop), n_filt)
Q = 2

n_samples = 100e3

audio_data = np.zeros((0, n_filt))
audio_class = np.zeros((0,1))
audio_file = []

#%% Adding positive examples
cnt = 0
while (cnt < n_samples):
    # load a random positive sample file
    file, fs, data = loadRandomFile(POS, audio_file)

    # preload classes if already labeled
    if file.startswith('sp'):
        os.chdir(TRAIN_LABELS)
        with open(file[0:4] + '.csv', 'r') as f:
            classes_str = f.readline()
            classes = classes_str.split(',')

    filt_bank = [createFilter(f_center[n], Q, fs) for n in range(n_filt)]
    
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
        audio_file.append(file)

        if file.startswith('sp'):
            audio_class = np.append(audio_class, classes[frame_cnt])
        else:
            audio_class = np.append(audio_class, aboveFrameThreshold(frame))
        
        cnt += 1    

#%% Adding negatives examples
n_samples = 30e3
cnt = 0
done = 0

filt_bank = [createFilter(f_center[n], Q, fs) for n in range(n_filt)]

while (cnt < n_samples):
    # load a random positive sample file
    file, fs, data = loadRandomFile(NEG, audio_file)
    
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
        audio_class = np.append(audio_class, 0)
        audio_file.append(file)
        
        cnt += 1