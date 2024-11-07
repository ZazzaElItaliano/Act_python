"""
11. Contador decreciente con while
a. Escribe un programa que imprima los números del 10 al 1 utilizando un bucle while
"""
i=10
while(i>=1):
    print(i)
    i-=1

"""
12. Mínimo común múltiplo (MCM) con while
a. Escribe un programa que encuentre el MCM de dos números utilizando un bucle while
"""
a = int(input("Dame un numerito guapo: "))
b = int(input("Dame un segundo numerito guapetón: "))
mcm = max(a, b)
while True:
    if mcm % a == 0 and mcm % b == 0:
   
        break
    mcm += 1
print(f"El MCM de {a} y {b} es: {mcm}")

"""
13. Palabras que empiezan con una letra con for
a. Escribe un programa que recorra una lista de palabras y cuente cuántas empiezan con
una letra específica utilizando un bucle for.
"""
letrita=str(input("Escribe la letra que quieres contar: "))
lista13=[
    "crepúsculo", "nebulosa", "amanecer", "travesía", "cúspide", "efímero",
    "serenidad", "laberinto", "infinito", "melodía", "horizonte", "alquimia",
    "libertad", "intrépido", "sempiterno", "destino", "fragmento", "renacer",
    "nostalgia", "luminiscencia", "arcano", "eternidad", "perenne", "eclipse",
    "resplandor", "susurro", "fragancia", "cenit", "tempestad", "relámpago"
]
contador=0
for x in lista13:
    if(x[0]==letrita):
            contador+=1
print(f"Hay un total de {contador} palabras que empiezan por la letra que buscas ")            
    
"""
14c Buscar máximo en una lista con for
a. Escribe un programa que busque el número más grande en una lista utilizando un bucle
for.
""" 
listaNum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
maximo=listaNum[0] 
for num in listaNum:
    if(num>maximo):
        maximo=num
        
print(maximo)        

"""
15.Suma de números en un rango con for
a. Escribe un programa que sume todos los números en un rango dado utilizando un bucle
for.
"""
inicio = int(input("Introduce el número inicial del rango: "))
fin = int(input("Introduce el número final del rango: "))
suma_total = 0
for numero in range(inicio, fin + 1):
    suma_total += numero
print(f"La suma de todos los números de {inicio} a {fin} es: {suma_total}")

        
            
            
            

