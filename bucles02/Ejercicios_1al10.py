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

"""