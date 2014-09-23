# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:17:24 2014

@author: Catherine
"""

x = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        x = x + i
print(x)
