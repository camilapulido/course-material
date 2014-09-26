# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 13:15:15 2014

@author: Camila
"""

def mul(a):
    import sys
    o = 1
    for i in range (len(a)):
       if i < len(a):
           b = o* a[i]
           o = b
    print (b)