"""13.PASOS: Crear una función que calcule la distancia aproximada recorrida, dado un
número de pasos, asumiendo que la longitud media de un paso es de 0.78 metros
(promedio para adultos). Convertir la cantidad de pasos a kilómetros."""
pasitos=int(input("Cuantos pasos has dado hoy??"))
def Pasos(pasos):
    cantidad_metros=pasos*0.78
    cantidad_km=cantidad_metros/1000
    return f"Hoy has andado {round(cantidad_km,2)} km"
print(Pasos(pasitos))

#14Elevar una función al cuadrado. Utilizar una función lambda para elevar un número al cuadrado.
cuadrado=lambda x: x**2
print(cuadrado(3))

#15Suma de dos números. Crear una función lambda que sume dos números
suma=lambda x,y:x+y
print(suma(3,2))

#16Revertir una cadena. Utiliza una función lambda para invertir una cadena de texto.
revertir=lambda cadena: cadena[::-1]
print(revertir("hola"))

#17Obtener el mayor de dos números. Crear una función lambda que devuelva el mayor de dos números
comparacion= lambda x,y: x if x>y else y
print(comparacion(2,49))

#18Filtrar números pares en una lista. Usa una función lambda con filter() para obtener sólo los números pares de una lista.
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
filtrador=filter(lambda x: x%2==0, lista)
print(list(filtrador))

#19 Verificar si una cadena es palíndromo. Utilizar una función lambda para verificar si una cadena es un palíndromo (se lee igual al derecho y al revés)
palindromo= lambda frase:frase==frase[::-1]
print(palindromo("ojo"))