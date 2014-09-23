# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 18:51:08 2014

@author: Catherine
"""


a, b = 1, 2
x = ['1']
for i in range(9):
    x.append(str(b))
    a, b = b, a+b
print(', '.join(x) + '.')
