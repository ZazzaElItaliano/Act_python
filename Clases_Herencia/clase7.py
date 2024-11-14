class Pelota:
    def __init__(self, tipo_deporte, tamano, presion_aire):
        self.tipo_deporte = tipo_deporte 
        self.tamano = tamano  
        self.presion_aire = presion_aire 
    def inflar(self):
        """Aumenta la presión de aire de la pelota."""
        if self.presion_aire < 10:
            self.presion_aire += 1
            print(f"La pelota ha sido inflada. Presión actual: {self.presion_aire}")
        else:
            print("La pelota ya está completamente inflada.")

    def desinflar(self):
        """Disminuye la presión de aire de la pelota."""
        if self.presion_aire > 0:
            self.presion_aire -= 1
            print(f"La pelota ha sido desinflada. Presión actual: {self.presion_aire}")
        else:
            print("La pelota ya está completamente desinflada.")

    def estado_presion(self):
        """Muestra el estado de la presión actual de la pelota."""
        if self.presion_aire < 4:
            estado = "baja"
        elif self.presion_aire <= 7:
            estado = "normal"
        else:
            estado = "alta"
        print(f"Estado de la presión de la pelota: {estado}.")


pelota = Pelota("Fútbol", "Mediana", 5)
pelota.estado_presion()  
pelota.inflar()  
pelota.estado_presion()  
pelota.desinflar()  
pelota.estado_presion()  