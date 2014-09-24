# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 10:56:11 2014

@author: Camila
"""
import sys
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

a = int(a)
c = int(c)

if b == "^":
    b = "**"
  
operators = ["+", "-", "*", "/", "%", "**"]
values = [(a) + (c), (a) - (c), (a) * (c), (a) / (c), (a) % (c), (a) ** (c)]
#print (values)
f = 0
for e in range(len(operators)):
    if b == operators[e] : 
        print (float(values[e]))
        f = 1
if f ==0:
    print ("input error")
          