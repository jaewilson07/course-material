# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:13:36 2014

@author: Catherine
"""

import string

f = open('words')
s = f.read().replace('\n', '')

for x in string.ascii_letters:
    if x in s:
        print(x + ': ' + '%1.2f' % (s.count(x) / len(s)))
