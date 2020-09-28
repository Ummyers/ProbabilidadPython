#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:28:00 2020
Ejercicio 3, tarea 1 de Probabilidad 2021-1
@author: ummyers
"""

while True:
    try:
        entero = int(input("Ingresa un número: "))
    except ValueError:
        print("Ingresaste un número inválido, intentalo de nuevo")
    else:
        s = entero * (entero+1)/2
        print("Elegiste el número entero ",entero , "y la suma de los primeros ", entero," números es: ",s)
        
        break
