# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 18:42:03 2014

@author: Camila
"""

data = ["a", "b", "c", "d", "e", "f", "g", "h"]
for i in range(len(data)):
    for f in range(len(data)):
        if i!=f:
            print (data[i]+data[f])