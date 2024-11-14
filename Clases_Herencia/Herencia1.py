
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
       
        return f"{self.marca} {self.modelo} ({self.año})"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_motor):
        super().__init__(marca, modelo, año)
        self.tipo_motor = tipo_motor

    def acelerar(self):
       
        print(f"{self.marca} {self.modelo} está acelerando.")

    def frenar(self):
      
        print(f"{self.marca} {self.modelo} está frenando.")

    def tocar_claxon(self):
        
        print(f"{self.marca} {self.modelo} está tocando el claxon.")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_motor):
        super().__init__(marca, modelo, año)
        self.tipo_motor = tipo_motor

    def acelerar(self):
       
        print(f"{self.marca} {self.modelo} está acelerando.")

    def frenar(self):
   
        print(f"{self.marca} {self.modelo} está frenando.")

    def tocar_claxon(self):
     
        print(f"{self.marca} {self.modelo} está tocando el claxon.")


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_bicicleta):
        super().__init__(marca, modelo, año)
        self.tipo_bicicleta = tipo_bicicleta

    def pedalear(self):
   
        print(f"{self.marca} {self.modelo} está pedaleando.")

    def frenar(self):
      
        print(f"{self.marca} {self.modelo} está frenando.")


coche = Coche("Toyota", "Corolla", 2020, "Gasolina")
motocicleta = Motocicleta("Yamaha", "MT-07", 2021, "Gasolina")
bicicleta = Bicicleta("Trek", "Marlin 7", 2023, "Montaña")


print(coche.mostrar_info())
print(motocicleta.mostrar_info())
print(bicicleta.mostrar_info())


coche.acelerar()
coche.frenar()
coche.tocar_claxon()

motocicleta.acelerar()
motocicleta.frenar()
motocicleta.tocar_claxon()

bicicleta.pedalear()
bicicleta.frenar()
