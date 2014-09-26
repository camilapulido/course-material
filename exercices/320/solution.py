# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 17:38:08 2014

@author: Camila
"""
with open('words') as file:
    data = file.read()
    import string
    import math
    alphalower = list(string.ascii_lowercase)
    alphaup  = list(string.ascii_uppercase)
    count = []
    d =[0]
    for b in range(len(alphalower)):
        for i in range(len(data)):
            for a in data[i]:
                if a == alphalower[b] or a == alphaup[b]:
                    d[0]+=1
        count= count + d
    total = sum(count)
    for i in range (len(count)):
        count[i]= round(count[i]/total,3)
        print (alphalower[i], end=": ")
        print (count[i], end="\n")
