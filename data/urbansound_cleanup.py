# -*- coding: utf-8 -*-
"""
Urban Sound Clean-up Script

Created on Tue Nov 22 13:57:31 2016

@author: brady
"""

import os

ROOT = r'C:\Users\brady\GitHub\MinVAD\data\negative\UrbanSound\data'

os.chdir(ROOT)
for folder in os.listdir():
    os.chdir(folder)
    print("Enter folder: ", folder)
    for file in os.listdir():
        [base, ext] = os.path.splitext(file)
        if ext.lower() != '.wav':
            os.remove(file)
            
    os.chdir('..')
    
print("Finished.")