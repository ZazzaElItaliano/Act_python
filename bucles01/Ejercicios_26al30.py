"""26.Imprimir pirámide de números con for
Escribe un programa que imprima una pirámide de números utilizando bucles for."""

filas = int(input("Introduce el número de filas para la pirámide: "))
for i in range(1, filas + 1):
    print(" " * (filas - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")

    print()

"""
27.Simular lanzamiento de monedas con while
Escribe un programa que simule el lanzamiento de una moneda hasta que salga cara tres
veces consecutivas utilizando un bucle while"""

import random
cara_consecutiva = 0
while cara_consecutiva < 3:

    lanzamiento = random.choice(["cara", "cruz"])
    print(f"Lanzamiento: {lanzamiento}")

    if lanzamiento == "cara":
        cara_consecutiva += 1
    else:
        cara_consecutiva = 0  
print("¡Han salido tres caras consecutivas!")

"""
28.Dibujar un cuadrado con for
Escribe un programa que dibuje un cuadrado de asteriscos de tamaño N utilizando bucles
for
"""
n = int(input("Introduce el tamaño del cuadrado: "))

for i in range(n):
    print('*' * n)
    
"""29.Comparar cadenas con while
Escribe un programa que compare dos cadenas carácter por carácter utilizando un bucle
while"""

cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

i = 0


while i < len(cadena1) and i < len(cadena2):
    if cadena1[i] != cadena2[i]:
        print(f"Las cadenas son diferentes en el índice {i}.")
        break
    i += 1

if i == len(cadena1) and i == len(cadena2):
    print("Las cadenas son iguales.")
else:
    if i == len(cadena1):
        print("La primera cadena es más corta que la segunda.")
    elif i == len(cadena2):
        print("La segunda cadena es más corta que la primera.")

    """30.Contador de intentos con else en while
Escribe un programa que intente adivinar un número ingresado por el usuario y use un bucle
while. Si no logra adivinar después de 5 intentos, muestra un mensaje en el bloque else.
    """
numero_secreto = int(input("Introduce un número secreto entre 1 y 100: "))
intentos = 0
max_intentos = 5
while intentos < max_intentos:
    suposicion = int(input(f"Intento {intentos + 1}: ¿Cuál es tu suposición? "))
    if suposicion == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
    else:
        print("Intenta nuevamente.")
   
    intentos += 1
else:
    print(f"No has adivinado el número en {max_intentos} intentos. El número secreto era {numero_secreto}.")
