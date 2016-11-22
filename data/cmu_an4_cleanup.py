# -*- coding: utf-8 -*-
"""
Change all of CMU AN4 dataset from raw PCM to WAV

Created on Mon Nov 21 17:16:04 2016

@author: brady
"""

import os
import shutil
from subprocess import Popen, PIPE

DIR = r'C:\Users\brady\GitHub\MinVAD\data\positive\an4_clstk'

os.chdir(DIR)

#%% Changing raw PCM to WAV
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
            os.remove(file)
    os.chdir('..')

print("finished")

#%% Moving all WAV to top level dir
for folder in os.listdir():
    os.chdir(folder)
    print("Entering ", folder)
    for file in os.listdir():
        shutil.copy(file, '../' + file)

    os.chdir('..')        
    