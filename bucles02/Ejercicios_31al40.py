#31. Palíndromo: Dada una palabra, usa un bucle para determinar si es un palíndromo.
palabra=input("Dime una palabrita")
palabra = palabra.lower().replace(" ", "")
izquierda=0
derecha=len(palabra)-1
palabra_comprobada=True

while(izquierda<derecha):
        if(palabra[izquierda]!= palabra[derecha]):
            palabra_comprobada=False
            break
        izquierda+=1
        derecha-=1
        
if(palabra_comprobada):
    print("Es palíndromo")
else:
    print("No es palíndroma")
#32. Encontrar el número mayor en una lista: Escribe un programa que encuentre el número más grande en una lista usando un bucle.
lista = [int(x) for x in input("Introduce los números de la lista separados por espacios: ").split()]
mayor = lista[0]

for num in lista:
    if num > mayor:
        mayor = num

print("El número mayor en la lista es:", mayor)

#33. Contar números primos en un rango: Dado un rango de números, cuenta cuántos son primos.
inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el fin del rango: "))
contador_primos = 0

for num in range(inicio, fin + 1):
    es_primo = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    if es_primo:
        contador_primos += 1

print(f"Hay {contador_primos} números primos entre {inicio} y {fin}.")

#34. Verificar si una lista está ordenada: Usa un bucle para verificar si una lista está ordenada de manera ascendente.
lista = [23,34,5,2,2,34,5,6,3,2,1,4,56,6,3,33,3,3]
ordenada = True

for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False
        break

if ordenada:
    print("La lista está ordenada de manera ascendente.")
else:
    print("La lista no está ordenada.")

#35. Números perfectos: Escribe un programa que encuentre todos los números perfectos entre 1 y 1000 (un número perfecto es igual a la suma de sus divisores propios).
for num in range(1, 1001):
    suma_divisores = sum(i for i in range(1, num) if num % i == 0)
    if suma_divisores == num:
        print(num, "es un número perfecto")

"""36. Juego del "FizzBuzz": Imprime los números del 1 al 100. Para múltiplos de 3 imprime
"Fizz", para múltiplos de 5 imprime "Buzz", y para múltiplos de ambos imprime
"FizzBuzz"."""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""37. Generar números aleatorios hasta que sea cero: Usa un bucle para generar números
aleatorios entre 1 y 10 hasta que se genere un cero."""

import random

while True:
    numero = random.randint(1, 10)
    print("Número generado:", numero)
    if numero == 0:
        break

"""38. Determinar el segundo número más grande en una lista: Usa bucles y condicionales
para encontrar el segundo número más grande en una lista."""
lista = [int(x) for x in input("Introduce los números de la lista separados por espacios: ").split()]
mayor = segundo_mayor = float('-inf')

for num in lista:
    if num > mayor:
        segundo_mayor, mayor = mayor, num
    elif num > segundo_mayor and num != mayor:
        segundo_mayor = num

print("El segundo número más grande es:", segundo_mayor)

"""39. Pares e impares separados: Dada una lista de números, separa los números pares e
impares en dos listas diferentes."""
lista = [int(x) for x in input("Introduce los números de la lista separados por espacios: ").split()]
pares = [num for num in lista if num % 2 == 0]
impares = [num for num in lista if num % 2 != 0]

print("Pares:", pares)
print("Impares:", impares)

"""40. Convertir números decimales a binarios: Escribe un programa que convierta un número
decimal a binario usando un bucle."""
decimal = int(input("Introduce un número decimal: "))
binario = ""

while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal //= 2

print("El número en binario es:", binario)
