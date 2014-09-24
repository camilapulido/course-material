# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:38:10 2014

@author: Camila
"""
def is_alpha(word):
    import string    
    alphalower = list(string.ascii_lowercase)
    alphaup  = list(string.ascii_uppercase)
    t = 0
    for m in (range(len(word))):
        for b in range(len(alphalower)):
            if word[m] == alphalower[b] or word[m] == alphaup[b]:
                t += 1               
    if t == len(word):
        return True
    else:
        return False
