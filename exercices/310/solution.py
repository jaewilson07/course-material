# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:54:05 2014

@author: Catherine
"""

f = open('word')
print(f.read().replace('\n', '').count('e'))
