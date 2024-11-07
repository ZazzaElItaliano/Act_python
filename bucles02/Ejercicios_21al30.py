# 21.Suma de números pares en un rango: Usa un bucle para sumar todos los números pares
inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el fin del rango: "))
suma_pares = sum(i for i in range(inicio, fin + 1) if i % 2 == 0)
print("La suma de los números pares en el rango es:", suma_pares)

#22. Imprimir números divisibles por 3 y 5: Usa un bucle para imprimir los números entre 1 y 100 que sean divisibles por 3 y 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#23.Contar números positivos, negativos y ceros: Dado un conjunto de números ingresados
positivos = negativos = ceros = 0
cantidad = int(input("¿Cuántos números vas a ingresar? "))

for _ in range(cantidad):
    numero = int(input("Introduce un número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)

#24
numeros = [int(x) for x in input("Introduce números separados por espacios: ").split()]
suma_positivos = sum(num for num in numeros if num > 0)
print("La suma de los números positivos es:", suma_positivos)

#25
cadena = input("Introduce una cadena de texto: ").lower()
vocales = "aeiou"
num_vocales = sum(1 for char in cadena if char in vocales)
num_consonantes = sum(1 for char in cadena if char.isalpha() and char not in vocales)
print("Vocales:", num_vocales)
print("Consonantes:", num_consonantes)

#26 . Imprimir los primeros N números primos: Usa bucles y condicionales para imprimir los primeros N números primos

n = int(input("Introduce la cantidad de números primos a imprimir: "))
contador = 0
num = 2

while contador < n:
    es_primo = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    if es_primo:
        print(num, end=" ")
        contador += 1
    num += 1

#27Juego de adivinanza: Crea un programa donde el usuario debe adivinar un número entre 1 y 100, dándole pistas de si el número es mayor o menor

import random

numero_secreto = random.randint(1, 100)
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número entre 1 y 100: "))
    if intento < numero_secreto:
        print("El número es mayor")
    elif intento > numero_secreto:
        print("El número es menor")
    else:
        print("¡Felicidades! Adivinaste el número.")
        adivinado = True

#28 Calculadora de promedio: Solicita al usuario ingresar números hasta que ingrese un cero, luego calcula el promedio de los números ingresados.

suma = 0
contador = 0
while True:
    numero = float(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print("El promedio es:", promedio)
else:
    print("No se ingresaron números para calcular el promedio.")

#29 Invertir una cadena: Escribe un programa que invierta una cadena ingresada por el usuario usando un bucle for.

cadena = input("Introduce una cadena: ")
cadena_invertida = "".join(cadena[i] for i in range(len(cadena) - 1, -1, -1))
print("Cadena invertida:", cadena_invertida)

#30Suma de dígitos: Dado un número, usa un bucle while para sumar todos sus dígitos.

numero = int(input("Introduce un número: "))
suma_digitos = 0

while numero > 0:
    suma_digitos += numero % 10
    numero //= 10

print("La suma de los dígitos es:", suma_digitos)
