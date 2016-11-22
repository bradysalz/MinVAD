# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:40:05 2016

@author: brady
"""

import numpy as np

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