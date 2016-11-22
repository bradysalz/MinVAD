# -*- coding: utf-8 -*-
"""
Helper/utility functions for the feature extractor

Created on Mon Nov 21 12:40:05 2016

@author: brady
"""

import os
import random
import numpy as np
import wavio

from config import POS_DIRS, NEG_DIRS
from numpy import pi
from scipy import signal


def getFrameSize(fs, timeSize=20):
    """
    Read audio file, get sampling rate, return frame size.
    
    :param file: music file (only WAV for now)
    :param timeSize: frame length in milliseconds (default: 20ms)
    :returns: number of samples per frame
    """
    return fs*timeSize/1000
    
    
def createFilter(fc, Q, fs):
    """
    Returns digital BPF with given specs
    :param fc: BPF center frequency (Hz)
    :param Q: BPF Q (Hz/Hz)
    :param fs: sampling rate (Samp/sec)
    :returns: digital implementation of BPF
    """
    wc = 2*pi*fc
    num = [wc/Q, 0]
    den = [1, wc/Q, wc**2]
    dig_tf = signal.bilinear(num, den, fs)
    return dig_tf
    
    
def calcFrameAvg(frame):
    """
    Calculate + return spectral frame energy. 
    Assumes frame is filtered through createFilter()
    :param frame: timeSize clip of audio signal, np-array
    :returns: Frame RMS average
    """
    return np.sqrt(np.mean(frame**2))


def aboveFrameThreshold(frame_avgs):
    """
    Checks for silence in a single frame
    :param frame_avgs: np-array of average of filtered audio frame
    :returns: 1 if any frame is above threshold, else 0
    """
    return 1 if np.sum([f > 250 for f in frame_avgs]) > 0 else 0
    
def stereoToMono(audio):
    """
    Averages two channels to create mono signal
    """
    return (audio[:,0] + audio[:,1])/2


def normalizeAudio(audio, width):
    """
    Returns audio file that with range +/-1
    :param audio: numpy array of audio samples
    :param width: sample width in bytes (1 = 8 bit, 2 = 16 bit...)
    :returns: noramlized audio file
    """
    max_val = 2**(8*width-1)
    return audio/max_val


def loadRandomFile(audio_class):
    """
    Reads and returns random .WAV file from appropriate class
    :param audio_class: 1 if positive example, 0 if negative example
    :returns: filename, sampling rate, numpy array
    """    

    if audio_class == 1:
        use_dirs = POS_DIRS
    else:
        use_dirs = NEG_DIRS

    os.chdir(random.choice(use_dirs))
    
    if audio_class == 0:
        os.chdir(random.choice(os.listdir()))
        
    file = random.choice(os.listdir())
    mWav = wavio.read(file)
    
    if mWav.data.shape[1] == 2:
        mWav.data = stereoToMono(mWav.data)
        
    mWav.data = normalizeAudio(mWav.Data, mWav.sampwidth)
    
    return [file, mWav.rate, mWav.data]
    
        