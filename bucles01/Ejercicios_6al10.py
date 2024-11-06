"""
6.Sumar dígitos de un número con while
Escribe un programa que sume los dígitos de un número utilizando un bucle while
"""
numero=int(input("Dime un numerito campeón: " ))
suma=0

while(numero>0):
    suma+=numero%10
    numero=numero//10
    
print(f"La suma de los dígitos es: {suma}")

"""
7.Adivinar el número con while
Crea un juego en el que el usuario intente adivinar un número secreto. El programa deberá
seguir solicitando al usuario que adivine hasta que lo haga correctamente
"""
n=77
acertado=True
while( acertado): 
    preguntita = int(input(("Se ha generado un numerín secreto entre el 1 y el 100. Trata de averiguarlo mastodonte: ")))    
    if(preguntita==n):
            
            print("Enhorabuena acertaste el numerín") 
            acertado=False
    else:
        print("Has fallado, sigue intentándolo.")       
        
        
"""
8.Conversión de temperaturas con for
Escribe un programa que convierta un rango de temperaturas de Celsius a Fahrenheit
utilizando un bucle for.(ejercicio de listas)
"""
celsius= [23.5, 18.2, 30.0, 25.8, 19.1, 27.4, 22.3, 21.0, 26.5, 24.3, 20.0, 29.5]
farenheit=[]
for temperatura in celsius:
    farenheit.append((temperatura*9/5)+32)
print(farenheit)



"""
9.Serie de Fibonacci con for
Escribe un programa que genere los primeros N números de la serie de Fibonacci utilizando
un bucle for
"""


"""
10. Conteo de vocales con for
a. Escribe un programa que cuente cuántas vocales hay en una palabra dada utilizando un
bucle for y una condición if
"""
print("Dime una palabra o frase y te contaré las vocales e incluso te dire cuantas de cada una hay")
vocalizar=str(input("Frasecita/palabrita: "))
vocalizar=vocalizar.lower()
vocales=["a","e","i","o","u"]
contador=0
mapeador={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
for x in vocalizar:
    if(x in vocales):
        contador+=1
        mapeador[x]+=1
print(f"Tu frase/palabra tiene: {contador} vocal/es")
print(f"Tu frase/palabra tiene las siguientes vocales {mapeador} ")





