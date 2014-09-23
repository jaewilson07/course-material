# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 16:57:34 2014

@author: Catherine
"""


def is_prime(n):
    x = True
    if n > 1:
        for i in range(2, int(n ** .5)):
            if (n % i) == 0:
                x = False
    return x

x = 0
for n in range(1000):
    if is_prime(n) is True:
        x = x + n
print(x)
