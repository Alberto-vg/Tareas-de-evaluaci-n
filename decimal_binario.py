#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 18:32:11 2025

@author: albertovargas
"""

# Decimal 1024 a Binario
print("CONVERSIÓN 1024 (DECIMAL) → BINARIO")
num = 1024
resultado_binario = ""

# Calculamos cada bit de izquierda a derecha
for i in range(11):
    exponente = 10 - i  # 10, 9, 8, ..., 0
    potencia = 2 ** exponente
    if num > potencia or num == potencia:
        resultado_binario = resultado_binario + "1"
        num = num - potencia
    else:
        resultado_binario = resultado_binario + "0"

print("Resultado Binario:", resultado_binario)

# Binario 110101 a Decimal  
print("\nCONVERSIÓN 110101 (BINARIO) → DECIMAL")
binario = "110101"
resultado_decimal = 0

# Recorremos cada dígito del binario
for posicion in range(len(binario)):
    digito = binario[posicion]
    if digito == "1":
        # Calculamos 2 elevado a la posición (de derecha a izquierda)
        valor = 2 ** (len(binario) - 1 - posicion)
        resultado_decimal = resultado_decimal + valor

print("Resultado Decimal:", resultado_decimal)