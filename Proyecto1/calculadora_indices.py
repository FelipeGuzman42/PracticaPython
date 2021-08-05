# -*- coding: utf-8 -*-
"""
Calculos de los indicadores
@author: Felipe Guzmán Avendaño
"""

def calcular_IMC(peso: float, altura: float)->float:
    IMC = peso/(altura ** 2)
    return IMC

def calcular_procentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float)->float:
    porcentaje_grasa = 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero
    return porcentaje_grasa

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int)->float:
    calorias_reposo = (10*peso) + (6.25*altura) - (5*edad) + valor_genero
    return calorias_reposo

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float)->float:
    calorias_actividad = calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * valor_actividad
    return calorias_actividad

def calcular_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int)->str:
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    minimo = round(TMB * 0.8,2)
    maximo = round(TMB * 0.85,2)
    rango_calorias = "Para adelgazar es recomendado que consumas entre "+str(minimo)+" y "+str(maximo)+" calorías al día."
    return rango_calorias
    