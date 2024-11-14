class Cafetera:
    def __init__(self, marca, capacidad_maxima):
        self.marca = marca
        self.capacidad_maxima = capacidad_maxima 
        self.nivel_actual = capacidad_maxima  
    def servir_cafe(self, cantidad):
        if cantidad > self.nivel_actual:
            print("No hay suficiente café para servir esa cantidad.")
        elif cantidad > 0:
            self.nivel_actual -= cantidad
            print(f"Has servido {cantidad} litros de café. Nivel actual: {self.nivel_actual} litros.")
        else:
            print("La cantidad a servir debe ser positiva.")

    def rellenar_cafetera(self):
        self.nivel_actual = self.capacidad_maxima
        print(f"La cafetera ha sido rellenada a su capacidad máxima de {self.capacidad_maxima} litros.")

    def estado_cafetera(self):
        if self.nivel_actual == 0:
            return "La cafetera está vacía."
        elif self.nivel_actual == self.capacidad_maxima:
            return "La cafetera está llena."
        else:
            return f"La cafetera tiene {self.nivel_actual} litros de café disponibles."

cafetera = Cafetera("Nespresso", 2.0)
print(cafetera.estado_cafetera())
cafetera.servir_cafe(0.5)
print(cafetera.estado_cafetera())
cafetera.rellenar_cafetera()
print(cafetera.estado_cafetera())
