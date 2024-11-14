
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        """Método común para hacer un sonido, debe ser sobrescrito por cada animal."""
        raise NotImplementedError("Este método debe ser sobrescrito en las clases derivadas")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        """El perro hace el sonido de 'ladrido'."""
        print(f"{self.nombre} dice: ¡Guau! ¡Guau!")

    def correr(self):
        """El perro corre."""
        print(f"{self.nombre} está corriendo.")


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        """El gato hace el sonido de 'maullido'."""
        print(f"{self.nombre} dice: ¡Miau! ¡Miau!")

    def dormir(self):
        """El gato duerme mucho."""
        print(f"{self.nombre} está durmiendo.")


class Pajaro(Animal):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad)
        self.especie = especie

    def hacer_sonido(self):
        """El pájaro hace el sonido de 'canto'."""
        print(f"{self.nombre} dice: ¡Pío! ¡Pío!")

    def volar(self):
        """El pájaro vuela."""
        print(f"{self.nombre} está volando.")


perro = Perro("Rex", 5, "Pastor Alemán")
gato = Gato("Miau", 3, "Negro")
pajaro = Pajaro("Loro", 2, "Loro de Australia")


perro.hacer_sonido() 
perro.correr()  

gato.hacer_sonido()  
gato.dormir() 

pajaro.hacer_sonido()  
pajaro.volar() 
