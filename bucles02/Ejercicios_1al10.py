#1. Imprimir números del 1 al 10: Utiliza un bucle for para imprimir los números del 1 al 10
for i in range(1,11):
    print(i)
    
#2.Números pares del 1 al 100: Usa un bucle for para imprimir solo los números pares entre 1 y 100
for i in range(1,101):
    if(i%2==0):
     print(i)
     
"""3.Imprimir un patrón de estrellas: Crea un bucle que imprima el siguiente patrón:
*
**
***
****
*****"""
num=5
for i in range(1,num+1):
    print("@"*i)
    
"""
4.Imprimir un patrón invertido: Crea un bucle que imprima el siguiente patrón:
*****
****
***
**
*
"""
num1=5
for i in range(num1,0,-1):
    print("*"*i)

"""
5.Suma de los primeros N números: Usa un bucle para sumar los primeros N números
(donde N es ingresado por el usuario)
"""
N = int(input("Ingresa el valor de N: "))

suma = 0
for i in range(1, N + 1):
    suma += i
print(f"La suma de los primeros {N} números es: {suma}")

"""
6.Factorial de un número: Escribe un programa que calcule el factorial de un número
usando un bucle
"""
n = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"El factorial de {n} es: {factorial}")

"""7.Imprimir tabla de multiplicar: Solicita un número al usuario y genera su tabla de
multiplicar del 1 al 10."""
tabla=int(input("Dame el número dle cual quieres la tabla de multiplicar: "))
for i in range(0,11):
    print(f"{tabla}*{i}={tabla*i}")
    
"""
9.Imprimir los primeros N números impares: Escribe un programa que imprima los
primeros N números impares utilizando un bucle while
"""
N = int(input("Ingresa el valor de N: "))
contador = 0  
numero_impar = 1  
while contador < N:
    print(numero_impar)
    numero_impar += 2  
    contador += 1  
