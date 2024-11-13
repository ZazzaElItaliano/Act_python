import time
import random
"""Ejercicio 01. Tirada de Dados.
Simular el lanzamiento de dos dados de seis caras y mostrar el resultado de cada dado y la
suma total"""
dado1=random.randint(1,6)
dado2=random.randint(1,6)
print(f"El primer dado  ha sacado este valor:{dado1}, el segundo dado  ha sacado este valor:{dado2} y la suma de ambas caras da:{dado1+dado2}")

"""Ejercicio 02. La Ruleta.
Simular el funcionamiento de la ruleta. La ruleta tiene 36 números (del 1 al 36) y un número
especial, el 0 (Gana la banca). Realizar la simulación del giro de la ruleta y mostrar el número
resultante"""
apuesta=int(input("Haz tu apuesta pequeño ludópata:  "))
ruleta=random.randint(1,36)
print("La ruletita esta girando intensamente")
time.sleep(3)

if(ruleta==0):
    print(f"El resultado fue: {ruleta},la banca ha ganado y siempre gana")
elif(apuesta==ruleta):
    print(f"el resultado ha sido: {ruleta}.Has ganado PERO MÁS HAS PERDIDO JAJAJAJ")
else:
    print(f"Perdiste, el resultado es: {ruleta}")
    
"""Ejercicio 03. Baraja de Cartas.
Realizar la simulación de la mezcla de una baraja de cartas estándar (52 cartas) y realizar el
reparto de 5 cartas al azar.
Palos: Corazones, Diamantes, Tréboles, Picas
Valores: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A"""
palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
baraja=[f"{valor} de {palo}" for palo in palos for valor in valores]
random.shuffle(baraja)
mano=baraja[0:5]
print("Las 5 cartas repartidas son:")
for cartas in mano:
    print(cartas)