# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 14:57:07 2014

@author: Catherine
"""


def is_prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False
