# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 16:02:06 2014

@author: Catherine
"""

import numpy as np

M = np.loadtxt('euler11.txt')

x = 0
# test horz
for i in range(20):
    for j in range(4, len(M[i, :])):
        if np.prod([n for n in M[i, (j - 4):j]]) > x:
            x = np.prod([n for n in M[i, (j - 4):j]])

# test vert
for i in range(20):
    for j in range(4, len(M[:, i])):
        if np.prod([n for n in M[(j - 4):j, i]]) > x:
            x = np.prod([n for n in M[(j - 4):j, i]])

# test diag down
for i in range(17):
    for j in range(17):
        if np.prod([M[i, j], M[i+1, j+1], M[i+2, j+2]]) > x:
            x = np.prod([M[i, j], M[i+1, j+1], M[i+2, j+2]])

# test diag up
for i in range(17):
    for j in range(17):
        if np.prod([M[17-i, j], M[16-i, j+1], M[15-i, j+2]]) > x:
            x = np.prod([M[17-i, j], M[16-i, j+1], M[15-i, j+2]])

print(x)
