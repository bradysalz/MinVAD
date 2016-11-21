# -*- coding: utf-8 -*-
"""
Change all of CMU AN4 dataset from raw PCM to WAV

Created on Mon Nov 21 17:16:04 2016

@author: brady
"""

import os
import subprocess

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
                    '-ar', '8k',
                    '-ac', '2',
                    '-i', file,
                    base + '.wav']
            subprocess.run(args)
    os.chdir('..')

print("finished")