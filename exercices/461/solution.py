# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 20:25:26 2014

@author: Catherine
"""

import numpy as np
import timeit
import euclid

# funcs = [euclid.euclidean, euclid.opt_euclidean, euclid.np_euclidean]

# a = np.random.randint(100, size = 100)
# b = np.random.randint(100, size = 100)


def benchmark(funcs, a, b):
    times = []
    for i in range(len(funcs)):
        func = funcs[i]
        times.append(timeit.Timer(lambda: 'func(a,b)').timeit())
    times_dict = dict([(funcs[i].__name__, times[i])
                      for i in range(len(funcs))])
    return times_dict
