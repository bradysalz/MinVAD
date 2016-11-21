# -*- coding: utf-8 -*-
"""
Change all of CMU AN4 dataset from raw PCM to WAV

Created on Mon Nov 21 17:16:04 2016

@author: brady
"""

import os
from subprocess import Popen, PIPE

DIR = r'C:\Users\brady\Downloads\an4\wav\an4_clstk'

os.chdir(DIR)

for folder in os.listdir():
    os.chdir(folder)
    print("Entering folder ", folder)
    for file in os.listdir():
        [base, ext] = os.path.splitext(file)
        if ext == '.raw':
            print('Changing File: ', base)
            args = ['ffmpeg', 
                    '-f', 's16le', 
                    '-ar', '16k',
                    '-ac', '2',
                    '-i', file,
                    base + '.wav']
            p = Popen(args, stdin=PIPE, stderr=PIPE)
    os.chdir('..')

print("finished")