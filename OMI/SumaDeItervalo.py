#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solución al problema presentado en OmegaUp
la liga es la siguiente: https://omegaup.com/arena/problem/Sumando-intervalos-de-enteros/#problems
@author: ummyers
"""


LI = int(input("Ingresa el LimiteIzquiero: "))
LD = int(input("Ingresa el LimiteDerecho: "))
    
LimiteDerecho = (LD)*(LD+1)/2
LimiteIzquiero = (LI-1)*(LI)/2
sumaTotal = LimiteDerecho - LimiteIzquiero
print("La solución es: ", sumaTotal)


