# -*- coding: utf-8 -*-
"""
Extracts features from audio files

Created on Mon Nov 21 14:20:14 2016

@author: brady
"""

import os
import numpy as np
import scipy.signal

from config import TRAIN_LABELS
import fe_utils as fe

def build_features(data_class, n_samples=50e3, f_start=100, f_stop=4e3,
                   filt_Q=2, n_filt=20, exclusion_list=set()):
    """
    Constructs data and class arrays for audio data

    Will return at least n_samples data, however it only updates on a per-file basis
    e.g. if n_samples=50e3, and sample_cnt=49.9e3, but the next song has 10e3 samples,
    then the returned data will have 59.9e3 entries

    TODO: add override to fix this? make an exact variable?

    :param data_class: 1 for positive, 0 for negative
    :type data_class: int
    :param n_samples: 
    """
    f_center = np.logspace(np.log10(f_start), np.log10(f_stop), n_filt)
    cnt = 0

    audio_data = np.zeros((0, n_filt))
    audio_class = np.zeros((0,1))
    while (cnt < n_samples):
        # load a random positive sample file
        file, fs, data = fe.loadRandomFile(data_class, exclusion_list)

        if data_class and file.startswith('sp'):
            # preload positive trained data classes
            fpath = os.path.join(TRAIN_LABELS, file[0:4])
            with open(fpath + '.csv', 'r') as f:
                classes_str = f.readline()
                classes = [int (c) for c in classes_str.split(',')]


        # this is inefficient but without knowing sampling rate 
        # i'm not sure how to improve it
        # maybe make a list at the top with filt_bank_8k,16k,44,1k etc?
        # throw error if invalid?
        filt_bank = [fe.createFilter(f_center[n], filt_Q, fs) for n in range(n_filt)]
        
        # process a single frame
        frame_len = fe.getFrameSize(fs)
        for frame_cnt in range(int(len(data)/frame_len)):
            if frame_cnt*frame_len > len(data):
                end_pt = frame_cnt = len(data)
            else:
                end_pt = (frame_cnt+1) * frame_len
            frame = data[frame_len*frame_cnt : end_pt]
            
            frame_avg = np.zeros((1, n_filt))
            for i, bpf in enumerate(filt_bank):
                filt_frame = scipy.signal.lfilter(bpf[0], bpf[1], frame)
                frame_avg[0][i] = fe.calcFrameAvg(filt_frame)
            
            # add data features
            audio_data = np.append(audio_data, frame_avg, axis=0)

            # append data class
            if data_class:
                if file.startswith('sp'):
                    audio_class = np.append(audio_class, classes[frame_cnt])
                else:
                    # this is ONLY VALID IF THE POSITIVE DATA IS NOISELESS
                    audio_class = np.append(audio_class, fe.aboveFrameThreshold(frame))
            else:
                audio_class = np.append(audio_class, 0)
            
            cnt += 1    

        # append file to exclusion set
        exclusion_list.add(file)
        
        return audio_data, audio_class, exclusion_list
        
if __name__ == '__main__':
    audio_data, audio_class, excl_list = build_features(1, n_samples=1e3)
    
    # save data, optional for testing
    if 0:
        np.save('train_data.npy', audio_data)
        np.save('train_class.npy', audio_class)
        # save used files? eh...