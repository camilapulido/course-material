# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:10:53 2014

@author: Camila
"""
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','o', 'p']
for i in range(len(data)):
    for t in range(len(data)):
        if i!=t:
            print (data[i]+data[t] )