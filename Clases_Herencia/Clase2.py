class Persona:
    def __init__(self, nombre, edad, genero, altura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura

    def saludar(self, otra_persona):
        print(f"Hola, {otra_persona}! Me llamo {self.nombre}.")

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def edad_en_5_anos(self):
        return self.edad + 5


persona = Persona("Alejandro", 20, "Masculino", 1.96)
persona.saludar("Luis")
print("¿Es mayor de edad?", "Sí" if persona.es_mayor_de_edad() else "No")
print("Edad en 5 años:", persona.edad_en_5_anos())
