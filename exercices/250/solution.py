# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 12:06:28 2014

@author: Camila
"""
def draw_n_squares(n):
    cruz="+---"  
    barra = "|   "
    print ((cruz)*n, end ="+\n", )
    for i in range (n):
        print ((barra)*n, end ="|\n")
        print ((cruz)*n, end ="+\n")
        