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

