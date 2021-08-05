# -*- coding: utf-8 -*-
"""
Consola calculo porcentaje grasa
@author: Felipe Guzmán Avendaño
"""
import calculadora_indices as calc

print("En esta función se va a calcular el porcentaje de grasa de una persona")

peso = input("Ingrese el peso de la persona (en Kg):")
altura = input("Ingrese la altura de la persona (en m):")
edad = input("Ingrese la edad de la persona:")
valor_genero = input("Ingrese 10.8 en caso de ser hombre y 0 en caso de ser mujer:")

PG = calc.calcular_procentaje_grasa(float(peso), float(altura), int(edad), float(valor_genero))
print("El porcentaje de grasa que tiene esta persona es: ", round(PG, 2), "%")
