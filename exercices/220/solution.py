# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:16:31 2014

@author: Catherine
"""

def is_prime(n):
    x = True
    if n > 1:
        for i in range(2, int(n ** .5)):
            if (n % i) == 0:
                x = False
    return x
    
s = []
for n in range(9999, 10051):
    if is_prime(n) is True:
        s.append(str(n))
print(', '.join(s))
