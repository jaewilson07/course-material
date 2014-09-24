# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 20:54:35 2014

@author: Catherine
"""

import numpy as np
import math


def euclidean(a, b):
    x = 0
    for i in range(len(a)):
        x = x + ((a[i]-b[i]) ** 2)
    return (x ** .5)


def opt_euclidean(a, b):
    x = 0
    for i in range(len(a)):
        x = x + ((a[i]-b[i]) ** 2)
    return (math.sqrt(x))


def np_euclidean(a, b):
    return (np.sqrt(np.sum(np.square(np.asarray(a)-np.asarray(b)))))
