# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:37:53 2014

@author: Catherine
"""


def is_prime(n):
    x = True
    if n > 1:
        for i in range(2, int(n ** .5)):
            if (n % i) == 0:
                x = False
    return x

x = 100000000
while is_prime(x) is not True:
    x = x + 1
print(x)
