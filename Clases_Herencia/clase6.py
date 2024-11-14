class Estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.notas = []  
        self.promedio = 0  
    def anadir_nota(self, nota):
        if 0 <= nota <= 10:  
            self.notas.append(nota)
            print(f"La nota {nota} ha sido añadida.")
        else:
            print("La nota debe estar entre 0 y 10.")

    def calcular_promedio(self):
        if self.notas:
            self.promedio = sum(self.notas) / len(self.notas)
            return self.promedio
        else:
            print("No hay notas para calcular el promedio.")
            return 0

    def aprobado(self):
        if self.promedio >= 5:
            return True
        else:
            return False


estudiante = Estudiante("Juan Pérez", "Matemáticas")
estudiante.anadir_nota(6)
estudiante.anadir_nota(8)
estudiante.anadir_nota(7)
promedio = estudiante.calcular_promedio()
print(f"Promedio de notas: {promedio}")
print("Aprobado" if estudiante.aprobado() else "Reprobado")
