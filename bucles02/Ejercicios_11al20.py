#11.Par o impar: Escribe un programa que determine si un número es par o impar
par=int(input("Dame un número y te si es par o no"))
if(par%2==0):
    print("Este número es par")
else:
    print("Es impar")
    
#12Positivo, negativo o cero: Dado un número, usa condicionales para verificar si es positivo, negativo o cero.
# Solicita un número al usuario
numero = float(input("Introduce un número y te diré si es positivo, negativo o cero: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

#13Comparación de dos números: Escribe un programa que compare dos números eimprima el mayor.

numero1 = float(input("Introduce un número: "))
numero2=float(input("Introduce un número: "))
if numero1 > numero2:
    print(numero1)
else:
    print(numero2)

#14Determinar el mayor de tres números: Dado tres números ingresados por el usuario,usa condicionales para determinar cuál es el mayor
numero3 = float(input("Introduce un número: "))
numero4=float(input("Introduce un número: "))
numero5=float(input("Introduce un número: "))
if numero3 > numero4 and numero3>numero5:
    print(numero3)
elif(numero4>numero5 and numero4>numero3):
    print(numero4)
else:
    print(numero5)

#15Año bisiesto: Escribe un programa que determine si un año es bisiesto
año = int(input("Introduce un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")

#16Calcular la calificación: Dado un puntaje entre 0 y 100, imprime la calificación
puntaje = int(input("Introduce el puntaje (0-100): "))
if puntaje >= 90:
    calificacion = "A"
elif puntaje >= 80:
    calificacion = "B"
elif puntaje >= 70:
    calificacion = "C"
elif puntaje >= 60:
    calificacion = "D"
else:
    calificacion = "F"
print(f"La calificación es: {calificacion}")

#17 Verificar si un carácter es una vocal: Escribe un programa que verifique si un carácter
caracter = input("Introduce un carácter: ").lower()
if caracter in 'aeiou':
    print("Es una vocal")
else:
    print("No es una vocal")
#18. Números dentro de un rango: Verifica si un número dado está dentro de un rango (por ejemplo, entre 1 y 100).
numero = int(input("Introduce un número: "))
if 1 <= numero <= 100:
    print("El número está dentro del rango de 1 a 100")
else:
    print("El número está fuera del rango")

#19Calculadora simple: Solicita dos números y una operación (+, -, *, /) al usuario y realiza la operación usando condicionales.
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: división por cero"
else:
    resultado = "Operación no válida"
print("El resultado es:", resultado)

#20Número primo: Escribe un programa que determine si un número es primo.
numero = int(input("Introduce un número: "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")
