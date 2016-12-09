# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 01:29:01 2016

@author: brady
"""

import os
import ntpath
import numpy as np
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import feature_extract.fe_utils as fe
import time
import pandas as pd

from scipy import signal
from sklearn.metrics import accuracy_score, f1_score
from feature_extract.config import TRAIN_LABELS
from classifier.training_helpers import quantize
from classifier.tree_classifier import test_quant_classifiers

def check_test_data(module_path=None, dataset=0):
    """
    Checks test data accuracy
    :param module_path: leave as none for now
    :param dataset: index of sample set
        0 : UrbanSound
        1 : KitchenSound
        2 : 15dB NOIZEUS
        3 : 10dB NOIZEUS
        4 :  5dB NOIZEUS
        5 :  0dB NOIZEUS
    :param metric: scoring function to use
        0 : accuracy
        1 : f1
    :returns: precision list, scores list
    """
    if module_path is None:
        module_path = r'quant_trees_full'

    data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test'
    # use kitchen data        
    if dataset == 0:
        data_dir = os.path.join(data_dir, 'negative')
        filter_word = '_kitchen'
        
    # use urbansound data
    elif dataset == 1:
        data_dir = os.path.join(data_dir, 'negative')
        filter_word = '_urban'
        
    # use 0dB data
    elif dataset == 2:
        data_dir = os.path.join(data_dir, 'positive')
        filter_word = '_15dB'
        
    # use 5dB data
    elif dataset == 3:
        data_dir = os.path.join(data_dir, 'positive')
        filter_word = '_10dB'
        
    # use 10dB data
    elif dataset == 4:
        data_dir = os.path.join(data_dir, 'positive')
        filter_word = '_5dB'
     
    # use 15dB data
    elif dataset == 5:
        data_dir = os.path.join(data_dir, 'positive')
        filter_word = '_0dB'
    
    df = pd.DataFrame(columns=('input_prec', 'thresh_prec', 'f1', 'acc'))
    cnt = 0
    for file in os.listdir(data_dir):
        if filter_word in file:
            input_prec = int(file.split('_')[2][:-5])
            Xtest = np.load(os.path.join(data_dir, file))
            os.chdir(r'C:\Users\brady\GitHub\MinVAD\classifier')
            if dataset in [0, 1]:
                # fix this to be not hard-coded
                # requires you to know numtrees though
                ytest = np.zeros(Xtest.shape[0]) 
            else:
                ytest = np.load('../data/test/positive/positive_classes.npy')
            ntrees, prec, pred = test_quant_classifiers(Xtest, ytest, module_path)
            
            for t in range(ntrees):
                f1sc = f1_score(ytest, pred[:, t])
                acc = accuracy_score(ytest, pred[:, t])
                df.loc[cnt] = [input_prec, prec[t], f1sc, acc]
                cnt += 1
            #prec_arr.append(prec)
            #print(pred.shape, ytest.shape)
            #score_arr.append(score_func(ytest, pred))
            
    return df
            

def build_test_data(sample_set=0, precision=None, 
                   f_start=100, f_stop=4e3, filt_Q=2, n_filt=20):
    """
    Loads a test data set and returns results
    :param sample_set: index of sample set
        0 : UrbanSound
        1 : KitchenSound
        2 : 15dB NOIZEUS
        3 : 10dB NOIZEUS
        4 :  5dB NOIZEUS
        5 :  0dB NOIZEUS
        6 : example
    :param precision: number of bits to show the input file as
    :param f_start: BPF start frequency
    :param f_stop: BPF stop frequency
    :param filt_Q: BPF Q (fc/bw)
    :param n_filt: number of BPF filters
    :returns: numpy arrays
    """                        
                       
    f_center = np.logspace(np.log10(f_start), np.log10(f_stop), n_filt)

    audio_data = np.zeros((0, n_filt))
    audio_class = np.zeros((0,1))

    if sample_set == 0:
        data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\negative\urban_test'
        data_class = 0
        
    elif sample_set == 1:
        data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\negative\kitchen_test'
        data_class = 0

    elif sample_set == 2:
        data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\positive\15dB'
        data_class = 1
    
    elif sample_set == 3:
        data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\positive\10dB'
        data_class = 1
        
    elif sample_set == 4:
        data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\positive\5dB'
        data_class = 1
    
    elif sample_set == 5:
        data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\positive\0dB'
        data_class = 1
        
    elif sample_set == 6:
        data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\example'
        data_class = 0

    else:
        return

    for fname in os.listdir(data_dir):
        # load a random positive sample file
        file = os.path.join(data_dir, fname)
        file, fs, data = fe.parse_file(file)

        if precision is not None:
            data = quantize(data, precision)

        # preload positive trained data classes 
        file = ntpath.basename(file)         
        if data_class and file.startswith('sp'):
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
                filt_frame = signal.lfilter(bpf[0], bpf[1], frame)
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
                    
    return audio_data, audio_class
    
def build_all_test_data():
    # build the test set data    
    start_time = time.time()
    precision = np.arange(4, 16, 1)
    
    data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\positive'
    SNR = {2: '15dB', 3: '10dB', 4: '5dB', 5: '0dB'}    
    for i in SNR:
        for prec in precision:
            data, classes = build_test_data(sample_set=i, precision=prec)
            fname = 'positive_' + str(SNR[i]) + '_' +  str(prec) + 'b'
            fname = os.path.join(data_dir, fname)
            np.save(fname, data)            
            
            fname = 'positive_classes'
            fname = os.path.join(data_dir, fname)
            np.save(fname, classes)

            
#    data_dir = r'C:\Users\brady\GitHub\MinVAD\data\test\negative'    
#    datatype = {0: 'urban', 1: 'kitchen'}
#    for dt in datatype:
#        for prec in precision:
#            data, _ = build_test_data(sample_set=dt, precision=prec)
#            fname = 'negative_' + datatype[dt] + '_' + str(prec) + 'b'
#            fname = os.path.join(data_dir, fname)
#            np.save(fname, data)
      
    end_time = time.time()
    print("Building quantized test data took %g seconds" % (end_time - start_time))

if __name__ == "__main__":
    print(os.getcwd())
    mydata = check_test_data(dataset=3)
    print('done')