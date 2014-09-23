# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:37:44 2014

@author: Catherine
"""

c = 0
a = "abcdefghijklmnopqrstuvwxyz"
for i in a:
    c = c + 1
    for j in a[c:26]:
        print(i + j)
