# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 18:07:51 2014

@author: Camila
"""
import is_prime
d = 0
for i in range(1000):
    a = is_prime.is_prime(i)
    if a ==True:
        d+=1
print (d)
        
        
        
