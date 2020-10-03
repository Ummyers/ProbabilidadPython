#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:13:11 2020
Lanzar una moneda 100 veces y decir cuantas veces cayó cara y cruz
@author: ummyers
"""

import random 
i = 1
cara = 0
cruz = 0

while i <= 100:
    moneda = random.randint(0,1)
    #i = 1 + i
    i+=1
    if moneda == 1:
        cara+=1
    if moneda == 0:
        cruz+=1
        
print("Cara cayó ", cara, "veces y cruz ", cruz)

        
    

