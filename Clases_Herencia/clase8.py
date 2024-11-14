class Smartphone:
    def __init__(self, marca, modelo, memoria, bateria_maxima):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.bateria_maxima = bateria_maxima  
        self.bateria_actual = bateria_maxima  

    def llamar(self, contacto):
        """Simula una llamada a un contacto, reduciendo la batería."""
        if self.bateria_actual > 0:
            self.bateria_actual -= 5  
            if self.bateria_actual < 0:
                self.bateria_actual = 0  
            print(f"Llamando a {contacto}... Nivel de batería actual: {self.bateria_actual}%")
        else:
            print("No hay suficiente batería para realizar una llamada. Carga el teléfono.")

    def cargar(self, cantidad):
        """Simula la carga del teléfono, incrementando el nivel de batería."""
        self.bateria_actual += cantidad
        if self.bateria_actual > self.bateria_maxima:
            self.bateria_actual = self.bateria_maxima  
        print(f"El teléfono ha sido cargado. Nivel de batería actual: {self.bateria_actual}%")

    def mostrar_nivel_bateria(self):
        """Muestra el nivel de batería actual."""
        print(f"Nivel de batería actual: {self.bateria_actual}%")


smartphone = Smartphone("Apple", "iPhone 14", "128GB", 100)
smartphone.mostrar_nivel_bateria()  
smartphone.llamar("Juan") 
smartphone.cargar(20)  
smartphone.mostrar_nivel_bateria()  
