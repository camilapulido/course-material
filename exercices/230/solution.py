# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 11:05:46 2014

@author: Camila
"""
import is_prime
b = (100000000)
for i in range(b,i+b):
    a = is_prime.is_prime(i)
    if a ==True:
        print (i)
        break
        