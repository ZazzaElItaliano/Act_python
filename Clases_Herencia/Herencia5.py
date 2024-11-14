
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def informacion(self):
       
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, curso):
        super().__init__(nombre, edad, genero)
        self.curso = curso

    def estudiar(self):
        return f"{self.nombre} está estudiando para su curso de {self.curso}."

    def informacion(self):
       
        return f"{super().informacion()}, Curso: {self.curso}"


class Profesor(Persona):
    def __init__(self, nombre, edad, genero, asignatura):
        super().__init__(nombre, edad, genero)
        self.asignatura = asignatura

    def enseñar(self):
        return f"{self.nombre} está enseñando la asignatura de {self.asignatura}."

    def informacion(self):
       
        return f"{super().informacion()}, Asignatura: {self.asignatura}"


class Director(Persona):
    def __init__(self, nombre, edad, genero, escuela):
        super().__init__(nombre, edad, genero)
        self.escuela = escuela

    def supervisar(self):
        return f"{self.nombre} está supervisando las actividades de la escuela {self.escuela}."

    def informacion(self):
        
        return f"{super().informacion()}, Escuela: {self.escuela}"


estudiante = Estudiante("Juan Pérez", 20, "Masculino", "Matemáticas")
profesor = Profesor("María Gómez", 35, "Femenino", "Física")
director = Director("Carlos López", 50, "Masculino", "Escuela Secundaria 1")


print(estudiante.informacion())
print(estudiante.estudiar())
print()
print(profesor.informacion())
print(profesor.enseñar())
print()
print(director.informacion())
print(director.supervisar())
