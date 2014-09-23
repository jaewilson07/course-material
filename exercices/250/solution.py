# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 19:14:17 2014

@author: Catherine
"""


def draw_n_squares(n):
    x = '+---+'*n + '\n' + '|   |'*n
    for i in range(n-1):
        x = x + '\n' + '+---+'*n + '\n' + '|   |'*n
    x = x + '\n' + '+---+'*n
    return x
