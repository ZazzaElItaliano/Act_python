class Mascota:
    def __init__(self, nombre, tipo_animal, edad):
        self.nombre = nombre  
        self.tipo_animal = tipo_animal  
        self.edad = edad  
        self.energia = 50  

    def alimentar(self):
        """Alimenta a la mascota, incrementando su energía."""
        self.energia += 20
        if self.energia > 100:  
            self.energia = 100
        print(f"{self.nombre} ha sido alimentado. Energía actual: {self.energia}%")

    def jugar(self):
        """Juega con la mascota, disminuyendo su energía."""
        self.energia -= 30
        if self.energia < 0:  
            self.energia = 0
        print(f"{self.nombre} ha jugado. Energía actual: {self.energia}%")

    def mostrar_energia(self):
        """Muestra la energía de la mascota y su estado."""
        if self.energia > 70:
            estado = "llena de energía"
        elif self.energia > 30:
            estado = "con energía"
        else:
            estado = "cansada"
        print(f"{self.nombre} está {estado}. Energía: {self.energia}%")


# Ejemplo de uso
mascota = Mascota("Rex", "Perro", 3)
mascota.mostrar_energia()  
mascota.alimentar()  
mascota.jugar()  
mascota.mostrar_energia()  
