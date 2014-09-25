# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 11:29:22 2014

@author: Camila
"""
a = 1
b= 0
fiblist = []
for i in range (10):
    F = a + b
    fiblist+= [F]
    b = a  
    a = F 
fibstr = map(str, fiblist)
fibstr = ", ".join(fibstr)
print(fibstr, end= '.')
