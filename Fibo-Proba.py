#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:43:49 2020
Serie de Fibonacci en Python, Spider
@author: ummyers
"""

x0 = 0
x1 = 1

while x1 < 30:
    print(x0)
    #x0, x1 = x1, x1 + x0
    x3 = x0 + x1
    x0 = x1
    x1 = x3

