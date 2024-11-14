class Reloj:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora  
        self.minuto = minuto  
        self.segundo = segundo  
    def ajustar_hora(self, hora, minuto, segundo):
        """Ajusta la hora, minuto y segundo del reloj."""
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        print(f"Hora ajustada a: {self.mostrar_hora()}")

    def avanzar_segundo(self):
        """Avanza un segundo en el reloj."""
        self.segundo += 1
        if self.segundo == 60:  
            self.segundo = 0
            self.avanzar_minuto()

    def avanzar_minuto(self):
        """Avanza un minuto en el reloj."""
        self.minuto += 1
        if self.minuto == 60:  
            self.minuto = 0
            self.avanzar_hora()

    def avanzar_hora(self):
        """Avanza una hora en el reloj."""
        self.hora += 1
        if self.hora == 24:  
            self.hora = 0

    def mostrar_hora(self):
        """Devuelve la hora actual en formato hh:mm:ss."""
        return f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"


reloj = Reloj(10, 30, 45)
print("Hora actual:", reloj.mostrar_hora()) 
reloj.avanzar_segundo()  
print("Hora después de avanzar un segundo:", reloj.mostrar_hora())
reloj.avanzar_minuto() 
print("Hora después de avanzar un minuto:", reloj.mostrar_hora())
reloj.ajustar_hora(14, 45, 30)  
print("Hora ajustada:", reloj.mostrar_hora())
