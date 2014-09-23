# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 16:13:03 2014

@author: Camila
"""

station = { 'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
 'number': 31705,
 'latitude': 48.8645278209514,
 'name': 'CHAMPEAUX (BAGNOLET)',
 'longitude': 2.416170724425901}
keys = station.keys()
values = station.values()

a= list(keys)
b = list(values)
for i in range(len(a)):
    print (a[i], b[i])
    