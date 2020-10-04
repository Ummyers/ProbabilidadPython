#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 19:25:47 2020
Modificación de Guess My Number 
@author: ummyers
"""
import random

print("Trata de adivinar el número en el que estoy pensando, tienes 5 intentos")
the_number = random.randint(1,100)

guess = int(input("¿Qué número crees que sea?"))
intentos = 1

while guess != the_number and intentos < 5:
    if guess > the_number:
        print("Menos")
    else: 
        print("Más")
    guess = int(input("¿Qué número crees que sea?"))
    intentos+=1
print("Lo siento, se terminaron los intentos el número era: ", the_number)
