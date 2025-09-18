#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 18:50:36 2025

@author: albertovargas
"""

import turtle
import random

# Configurar
screen = turtle.Screen()
screen.setup(width=800, height=600)
t = turtle.Turtle()
t.speed(0)

# Dibujar 50 círculos
for i in range(50):
    # Posición aleatoria
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    
    # Radio aleatorio
    radio = random.randint(10, 20)
    
    # Color aleatorio (usando if simple)
    numero_color = random.randint(1, 4)
    if numero_color == 1:
        color = 'red'
    elif numero_color == 2:
        color = 'blue'
    elif numero_color == 3:
        color = 'green'
    else:
        color = 'black'
    
    # Dibujar círculo
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.circle(radio)

turtle.done()