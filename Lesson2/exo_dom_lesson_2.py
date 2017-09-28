#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:04:04 2017

@author: Marion
"""

import requests
from bs4 import BeautifulSoup


def getSoupFromURL(url, method='get', data={}):
    
    if method == 'get':
        res = requests.get(url)
    elif method == 'post': 
        res = requests.post(url, data=data)
    else:
        return None
    
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    else:
        return None


def Compte (url, class_name, i):
    soup = getSoupFromURL(url)
    if soup:
        data = soup.find_all(class_=class_name)
        return data [i].text.strip()
    else:
        	0

for year in range(2010, 2015):
    url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=' + str(year)
    print('ANALYSE DE L\'EQUILIBRE DES COMPTES DE LA COMMUNE DE PARIS POUR L\'ANNEE ', str(year))
    print('')
    print('')
    print('Total des produits de fonctionnement (=A) :')
    print('Euros par habitant: ', Compte(url, 'montantpetit G', 1))
    print('Moyenne de la strate: ', Compte(url, 'montantpetit G', 2))
    print('')
    print('Total des charges de fonctionnement (=B) :')
    print('Euros par habitant: ', Compte(url, 'montantpetit G', 4))
    print('Moyenne de la strate: ', Compte(url, 'montantpetit G', 5))
    print('')
    print('Total des ressources d\'investissement (=C) :')
    print('Euros par habitant: ', Compte(url, 'montantpetit G', 10))
    print('Moyenne de la strate: ', Compte(url, 'montantpetit G', 11))
    print('')
    print('Total des emplois d\'investissement (=D) :')
    print('Euros par habitant: ', Compte(url, 'montantpetit G', 13))
    print('Moyenne de la strate: ', Compte(url, 'montantpetit G', 14))
    print('')
    print('')
    print('')