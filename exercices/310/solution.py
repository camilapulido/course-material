# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 15:55:42 2014

@author: Camila
"""
with open('words') as file:
    data = file.read()
    d =0
    for i in range(len(data)):
        for a in data[i]:
            if a == "e":
              d+=1
    print(d)
            
        