#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 17:39:41 2025

@author: albertovargas
"""

# Datos
x = [1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00]
y = [1.23, 2.13, 1.42, -0.69, 4.29, 3.64, 9.30, 10.62, 7.42, 8.40, 12.30, 10.30]

# Sumatorias
n = len(x)
sum_x = 0
sum_y = 0
sum_x2 = 0
sum_xy = 0

for i in range(n):
    sum_x = sum_x + x[i]
    sum_y = sum_y + y[i]
    sum_x2 = sum_x2 + (x[i] * x[i])
    sum_xy = sum_xy + (x[i] * y[i])

# Promedios
x_media = sum_x / n
y_media = sum_y / n

# Beta 1
beta1 = (sum_xy - n * x_media * y_media) / (sum_x2 - (sum_x * sum_x) / n)
print('beta1: '+ str(beta1))

# Beta 0
beta0 = y_media - beta1 * x_media
print('beta0: '+ str(beta0))

# Resultado
print("y = " + str(beta0) + " + " + str(beta1) + "x")