import random

"""Ejercicio 01. Tirada de Dados.
Simular el lanzamiento de dos dados de seis caras y mostrar el resultado de cada dado y la
suma total"""
dado1=random.randint(1,6)
dado2=random.randint(1,6)
print(f"El dado 1 ha sacado este valor:{dado1}, el dado 2 ha sacado este valor:{dado2} y la suma de ambas caras da:{dado1+dado2}")