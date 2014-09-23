# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 10:16:57 2014

@author: Catherine
"""

station = {
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
    'number': 31705,
    'latitude': 48.8645278209514,
    'name': 'CHAMPEAUX (BAGNOLET)',
    'longitude': 2.416170724425901
}

print('latitude', station.get('latitude'))
print('longitude', station.get('longitutde'))
print('number', station.get('number'))
print('name', station.get('name'))
print('address', station.get('address'))
