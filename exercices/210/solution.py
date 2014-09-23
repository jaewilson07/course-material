# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 16:57:34 2014

@author: Catherine
"""

import is_prime

x = 0
for n in range(1000):
    if is_prime.is_prime(n) is True:
        x = x + n
print(x)
