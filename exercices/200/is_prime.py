# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 13:37:04 2014

@author: Camila
"""
def is_prime(num):
    if num <= 3:
        return num >= 2
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True 
