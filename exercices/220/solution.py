# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 18:37:45 2014

@author: Camila
"""

import is_prime
d = 0
prime= []
for i in range(10000, 10050):
    a = is_prime.is_prime(i)
    if a ==True:
        d+=1
        prime =  prime + [i]
primelst = map(str, prime)
primelst = ", ".join(primelst)
print(primelst)
           