#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:04:14 2020
Curso introductorio de Proba para python.
@author: ummyers
"""
while True:
    try:
        entero = int(input("Ingresa un número: "))
    except ValueError:
        print("Ingresaste un número inválido")
    else:
        print("Elegiste el número entero ", entero)
        break