"""
21.Suma condicional de números con while
Escribe un programa que sume números ingresados por el usuario hasta que ingrese un
número negativo utilizando un bucle while
"""
verdadero=True
suma_total = 0
while verdadero:
    numero = float(input("Ingresa un número (o un número negativo para terminar): "))
    if numero < 0:
        verdadero=False
    suma_total += numero


print(f"La suma de los números ingresados es: {suma_total}")

"""
22. Encontrar múltiplos con for
Escribe un programa que encuentre todos los múltiplos de un número en un rango dado
utilizando un bucle for.
"""
numero = int(input("Introduce el número para encontrar sus múltiplos: "))
inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el fin del rango: "))

print(f"Múltiplos de {numero} entre {inicio} y {fin}:")

for i in range(inicio, fin + 1):
    if i % numero == 0:  
        print(i)

""" 23.Números perfectos con for
Escribe un programa que verifique si un número es perfecto (igual a la suma de sus divisores)
utilizando un bucle for"""

numero = int(input("Introduce un número para verificar si es perfecto: "))
suma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:  
        suma_divisores += i

if suma_divisores == numero:
    print(f"El número {numero} es perfecto.")
else:
    print(f"El número {numero} no es perfecto.")

"""24.Número mayor y menor con for
Escribe un programa que encuentre el número mayor y el menor de una lista utilizando un
bucle for"""
numeros = [15, 7, 23, 4, 89, 2, 10, 50]
mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")

"""25.Cifrar una cadena con for
Escribe un programa que cifre una cadena desplazando cada letra una posición en el alfabeto
utilizando un bucle for."""

cadena = input("Introduce una cadena para cifrar: ")
cadena_cifrada = ""
for char in cadena:

    if char.isalpha():

        if char.islower():
            cadena_cifrada += chr(((ord(char) - 97 + 1) % 26) + 97) 
        else:
            cadena_cifrada += chr(((ord(char) - 65 + 1) % 26) + 65)  
    else:
        cadena_cifrada += char


print(f"La cadena cifrada es: {cadena_cifrada}")
