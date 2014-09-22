# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:54:10 2014

@author: Catherine
"""

import sys
if len(sys.argv) < 3:
    print("you must give two arguments")
else:
    print(int(sys.argv[1]) + int(sys.argv[2]))
