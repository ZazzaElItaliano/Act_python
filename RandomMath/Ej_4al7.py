import random
import time

"""Ejercicio 04. Número de la Ruleta
La computadora debe girar la ruleta y el jugador debe adivinar el número. El programa debe
indicar si el usuario ha acertado o no con el número"""
repeticion=True
while(repeticion):
    apuesta=int(input("Haz tu apuesta pequeño ludópata:  "))
    ruleta=random.randint(1,36)
    print("La ruletita esta girando intensamente")
    time.sleep(3)
    if(apuesta==ruleta):
        print(f"el resultado ha sido: {ruleta}.Has ganado PERO MÁS HAS PERDIDO JAJAJAJ")
        repeticion=False
    else:
        print(f"Perdiste, el resultado es: {ruleta}")
        
"""Ejercicio 05. BlackJack
Simular la versión básica del juego del BlackJack. Repartir cartas al azar hasta que el jugador
decida plantarse o supere 21"""


"""Ejercicio 06. La Quiniela.
Realizar la simulación de una Quiniela con 15 partidos. Para cada partido, el resultado puede
ser “1” (gana el local), “X” (empate” o “2” (gana el visitante)"""
opciones = ["1", "X", "2"]
quiniela = [random.choice(opciones) for i in range(15)]

print("Simulación de la Quiniela:")
for i, resultado in enumerate(quiniela, 1):
    print(f"Partido {i}: {resultado}")

"""Ejercicio 07. La Primitiva.
La Primitiva consiste en seleccionar 6 números aleatorios entre el 1 y el 49. Además, se elige
un número complementario y un reintegro (entre 0 y 9). Realizar programa para generar una
apuesta de la Primitiva."""

numeros=[random.randint(1,49) for i in range(6)]
complementario = random.choice([n for n in range(1, 50) if n not in numeros])
reintegro=random.randint(0,9)

print("Apuesta de La Primitiva:")
print("Números:",numeros)
print("Complementario:", complementario)
print("Reintegro:", reintegro)