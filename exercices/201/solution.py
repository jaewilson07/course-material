# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:17:00 2014

@author: Catherine
"""

import string


def is_alpha(input):
    rez = True
    for x in input:
        if x not in string.ascii_letters:
            rez = False
            break
    return rez
