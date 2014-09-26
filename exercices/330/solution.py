# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 13:43:33 2014

@author: Camila
"""

23514624000

##============================
o = 1
result= []
for i in range (len(data)-13):
    for t in range(i,i+13,1):
        b  = o* data[t]
        o  = b
    result.append(b)
    o=1
print(max(result))