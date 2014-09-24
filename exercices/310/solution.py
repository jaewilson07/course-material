# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:54:05 2014

@author: Catherine
"""

f = open('words')
print(f.read().replace('\n', '').count('e'))
