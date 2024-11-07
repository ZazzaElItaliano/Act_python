"""
16.Tablas de multiplicar con for
a. Escribe un programa que imprima la tabla de multiplicar del 1 al 10 utilizando un bucle
for
"""
for i in range(1, 11):  
    print(f"\nTabla de multiplicar del {i}")
    for j in range(1, 11):  
        resultado = i * j
        print(f"{i} x {j} = {resultado}")


"""
17.Potencia de un número con for
a. Escribe un programa que calcule la potencia de un número dado utilizando un bucle
for.
"""

base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
resultado = 1
for i in range(exponente):
    resultado *= base
print(f"{base} elevado a {exponente} es: {resultado}")


"""
18.Calcular promedio con for
Escribe un programa que calcule el promedio de una lista de números utilizando un bucle
for
"""
lista18 = [19.99, 5.49, 12.99, 3.75, 45.00, 89.90, 7.25, 14.30, 27.99, 60.00]
total=0
for precio in lista18:
    total+=precio
media=total/len(lista18)
print(f"la media es: {media} ")

"""
19. Contar letras y dígitos con for
Escribe un programa que cuente cuántas letras y cuántos dígitos hay en una cadena
utilizando un bucle for
"""
print("Dime una palabra o frase y te contaré las palabras y números")
vocalizar=input("Frasecita/palabrita: ")

contadorNum=0
contadorLetras=0
for x in vocalizar:
    if(x.isalpha()):
        contadorLetras+=1
    
    elif(x.isdigit()):
        contadorNum+=1
        

print(f"Tu frase/palabra tiene: {contadorLetras} letras y {contadorNum} números")

"""
20.Comparación de listas con for
Escribe un programa que compare dos listas y cuente cuántos elementos coinciden utilizando
un bucle for
"""

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
contador = 0
for elemento in lista1:

    if elemento in lista2:
        contador += 1
print(f"El número de elementos que coinciden en las dos listas es: {contador}")


