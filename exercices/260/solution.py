# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 13:20:40 2014

@author: Camila
"""
def euclidean (a, b):
    d = 0
    for i in range (len(a)):
        d = d+ ((b[i]-a[i])**2)
    d = d **(0.5)
    print (d)
    
# ========================================
def opt_euclidean(a, b):
    import math
    d = 0
    for i in range (len(a)):
        d = d+ (math.pow((b[i]-a[i]),2))
    d = math. sqrt(d)
    print (d)
    
# ==========================================
def np_euclidean(a, b):
    import numpy as np
    d = 0
    for i in range (len(a)):
        d = d+ (numpy.power((b[i]-a[i]),2))
    d = numpy. sqrt(d)
    print (d)
        
    