import math
from datetime import datetime

#1.FACTORIAL: Escribir una función que calcule el factorial de un número dado
fact=int(input("Dame un numerín para calcular el factorial: "))
def Factorial(num):
    acumulador=1
    for x in range(num,0,-1):
        acumulador=x*acumulador
    return acumulador
print(Factorial(fact))

#2.PRIMO: Crear una función que determine si un número es primo
primoh=int(input("Introduce un numerín para saber si es primo"))
def es_primo(numero):
    if numero < 2:
        return "No es primo"
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return "No es primo"
    return "Es primo"
print(es_primo(primoh))

#3CONVERSIONES: Crear una función que convierta temperaturas de grados Celsius a Fahrenheit.

def Conversion(Celsius):
    farenheit=0
  
    farenheit=((Celsius*9/5)+32)
    return farenheit
print(Conversion(27.2))

#4SUMAS: Escribir una función que reciba una lista y devuelva la suma de sus elementos.

def SumaLista(lista):
    acumulacion=0
    for i in lista:
        acumulacion+=i
    return acumulacion
print(SumaLista([1,2,3,4]))

#5FIBONACCI: Crear una función que genere la serie de Fibonacci hasta un número dado de término.
num=int(input("Introduce un numerín para darte la serie de fibbonaci"))
def Fibbonaci(num):
    a=0
    b=1
    serie=[0,1]
    if(num==1):
        return a
    elif(num==2):
        return (a,b)
    elif(num>=3):
        for i in range(3,num+1):
            c=a+b
            serie.append(c)
            a,b=b,c
    return serie
            

print(Fibbonaci(num))

#5MCD: Escribir una función que encuentre el MCD (Máximo Común Divisor) de dos números utilizando el algoritmo de Euclides.

def mcd(a, b):
    while b != 0:  
        a, b = b, a % b 
    return a
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print(f"El MCD de {num1} y {num2} es: {mcd(num1, num2)}")

#6 CONTAR: Generar una función que cuente cuántas vocales hay en una cadena.
frase=str(input("Dime una frase y te cuento las vocales: "))
def Vocalista(sentence):
    contador=0
    vocales=["a","e","i","o","u"]
    for x in sentence:
        if(x in vocales):
            contador+=1
    return contador
print(f"La frase tiene estas vocales: {Vocalista(frase)}")

#7ORDEN: Crear una función que ordene una lista de números de menor a mayor sin usar el método sort() 
lista=[1,43,2,22,5,67,66,45,34,67,88,82,97,2,5,6,7,10,14,23]
#def Ordenacion(lista):




#8ÁREA: Escribir una función que calcule el área de un círculo dado su radio. 
radio=float(input("Dame el radio del círculo"))
def Area(radio):
    return math.pi*(radio**2)
print(Area(radio))


#9TIEMPO: Generar una función que tome un número total de horas, minutos y segundos,y devuelva el tiempo total en segundos.
hora_actual = datetime.now()
def Segundos(hora,minutos,second):
    return (hora*3600)+(minutos*60)+second
hora=hora_actual.hour
minutos=hora_actual.minute
segundos=hora_actual.second
print(Segundos(hora,minutos,segundos))

#10TIEMPO SEGUNDOS: Generar una función que tome un número total de segundos y lo convierta a horas, minutos y segundos. 
segundos=int(input("Dame una cifra en segundos: "))
def Horas(segundos):
    minutos_completos=segundos//60
    segundos_restantes=segundos%60
    horas=minutos_completos//60
    minutos=minutos_completos%60
    return f"Obtienes {horas} horas, {minutos} minutos y {segundos_restantes} segundos."
print(Horas(segundos))

"""#10PASOS: Crear una función que calcule la distancia aproximada recorrida, dado un
número de pasos, asumiendo que la longitud media de un paso es de 0.78 metros
(promedio para adultos). Convertir la cantidad de pasos a kilómetros.""" 