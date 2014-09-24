# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:54:08 2014

@author: Catherine
"""

import numpy as np

f = open('digit')
s = f.read()
x = 0

for i in range(13, len(s)):
    if np.prod(np.asarray([int(n) for n in s[(i - 13):i]])) > x:
        x = np.prod(np.asarray([int(n) for n in s[(i - 13):i]]))
print(x)
