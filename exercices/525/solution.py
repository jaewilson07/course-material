# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 17:32:40 2014

@author: Catherine
"""


def collatz_len(n):
    x = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            x.append(n)
        else:
            n = 3 * n + 1
            x.append(n)
    return len(x)

print(max([collatz_len(n) for n in range(1000000)]))
