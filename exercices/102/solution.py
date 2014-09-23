# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 19:38:04 2014

@author: Camila
"""

def check_my_city (city_name):
    m =0
    for i in range(len(velib)):
         a= velib[i]
         keys = a.keys()
         values = a.values()
         b = list(keys)
         c = list (values)
         if c[0]==city_name:
             for i in range(len(c)):
                 print (b[i], c[i])
                 m =1               
    if m == 0:
         print ("Sorry! No station for your city has been found!")
                 