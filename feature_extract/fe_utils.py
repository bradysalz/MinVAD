# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:40:05 2016

@author: brady
"""

import wave
import numpy as np

from numpy import pi
from scipy import signal


def getSampleFreq(file):
    """
    Return sampling frequency of an audio file (assumed WAV for now)
    """
    mWav = wave.open(file, 'r')
    fs = mWav.getframerate()
    mWav.close()
    return fs


def getFrameSize(file, timeSize=10):
    """
    Read audio file, get sampling rate, return frame size.
    
    :param file: music file (only WAV for now)
    :param timeSize: frame length in milliseconds (default: 10)
    :returns: number of samples per frame
    """
    fs = getSampleFreq(file)
    return fs*timeSize/1000
    
    
def createFilter(fc, Q, fs):
    """
    Returns digital BPF with given specs
    """
    wc = 2*pi*fc
    num = [wc/Q, 0]
    den = [1, wc/Q, wc**2]
    dig_tf = signal.bilinear(num, den, fs)
    return dig_tf
    
    
def calcFrameEnergy(frame):
    """
    Calculate + return spectral frame energy. 
    Assumes frame is filtered through createFilter()
    """
    return np.mean(frame)    
    