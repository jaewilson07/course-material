# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 19:14:17 2014

@author: Catherine
"""


def draw_n_squares(n):
    for i in range(n):
        print('+---+'*n + '\n' + '|   |'*n)
    print('+---+'*n)
