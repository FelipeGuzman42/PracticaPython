# -*- coding: utf-8 -*-
"""
Consola calculo calorías para adelgazar
@author: Felipe Guzmán Avendaño
"""
import calculadora_indices as calc

print("En esta función se va a calcular la cantidad de calorías recomendadas que una persona debe consumir a diario, en caso de que desee adelgazar.")

peso = input("Ingrese el peso de la persona (en Kg):")
altura = input("Ingrese la altura de la persona (en cm):")
edad = input("Ingrese la edad de la persona:")
valor_genero = input("Ingrese 5 en caso de ser hombre y -161 en caso de ser mujer:")

TMB = calc.calcular_calorias_recomendado_para_adelgazar(float(peso), float(altura), int(edad), int(valor_genero))
print(TMB)
