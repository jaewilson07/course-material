# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:16:31 2014

@author: Catherine
"""

import is_prime

x = []
for n in range(9999, 10051):
    if is_prime.is_prime(n) is True:
        x.append(str(n))
print(', '.join(x))
