"""
#1.Escribe un programa que imprima todos los números pares entre 1 y 100 utilizando un bucle
for. Utiliza una condición if para verificar si el número es par
"""
for i in range(0,101):
    if(i%2==0):
        print(i)
        
"""
#2 Escribe un programa que calcule el factorial de un número dado utilizando un bucle while.
"""
numero=int(input("Dame un número: "))
acumulador=1

if numero==1:
    print("El factorial es 1")
else:
    while(numero>1):
        acumulador=acumulador*numero
        numero=numero-1
print(f"El factorial es: {acumulador}")

"""
#3 Escribe un programa que determine si un número es primo utilizando un bucle for con una
condición if
"""
numero1=int(input("Dame un numerín: "))
contador1=0
for i in range(1,numero1+1):
    if numero1%i==0:
        contador1+=1

if contador1>2:
    print("El número no es primo")
else:
    print("El número si es primo")
    
    
"""
4 Escribe un programa que busque un número en una lista utilizando un bucle for, y si no lo
encuentra, muestra un mensaje en el bloque else
"""

lista=[1,2,3,4,5,6,7,9]
eleccion=int(input("No te voy a decir los valores. Introduce un número y descubre si está en la lista:"))

for x in lista:
    if x in lista:
        print("Enhorabuena bro eres demasiado listo")
        break
    else:
        print("Lo siento no vales ni para esto")
        break
    
"""
5. Palíndromo con while
Escribe un programa que verifique si una palabra es un palíndromo utilizando un bucle
while.
"""
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

