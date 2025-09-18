#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 18:20:54 2025

@author: albertovargas
"""

# Método de rectángulos para calcular la integral
# ∫ desde -1 hasta 3 de [4 - (x - 1)^2] dx

# Configuración
inicio = -1
fin = 3
n_rectangulos = 1000
ancho = (fin - inicio) / n_rectangulos

# Calcular el área sumando rectángulos
area_total = 0

for i in range(n_rectangulos):
    x = inicio + i * ancho
    y = 4 - (x - 1)**2  # Calculamos directamente la función
    area_rectangulo = y * ancho
    area_total = area_total + area_rectangulo

print("Resultado de la integral:", area_total)
print("Valor exacto (32/3):", 32/3)