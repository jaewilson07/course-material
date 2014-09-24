# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 20:12:43 2014

@author: Catherine
"""

import string

forward = 1
backward = -1


def caesar_cypher(s, key, method):
    rez = ''
    alph = string.ascii_lowercase
    Alph = string.ascii_uppercase
    for i in range(len(s)):
        if s[i] in alph:
            rez = rez + alph[(alph.index(s[i]) + method * key) % 26]
        elif s[i] in Alph:
            rez = rez + Alph[(Alph.index(s[i]) + method * key) % 26]
        else:
            rez = rez + s[i]

    return rez
