# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:04:20 2014

@author: Catherine
"""

import sys
if len(sys.argv) < 3:
    print("usage: python3 solution.py OP1 OP2")
else:
    print(int(sys.argv[1]) - int(sys.argv[2]))
