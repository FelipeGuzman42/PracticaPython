# -*- coding: utf-8 -*-
"""
Consola calculo IMC
@author: Felipe Guzmán Avendaño
"""
import calculadora_indices as calc

print("En esta función se va a calcular el IMC de una persona")

peso = input("Ingrese el peso de la persona (en Kg):")
altura = input("Ingrese la altura de la persona (en m):")

IMC = calc.calcular_IMC(float(peso), float(altura))
print("El IMC de esta persona es: ", round(IMC, 2))