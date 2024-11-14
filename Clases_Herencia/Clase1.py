class Libro:
    def __init__(self, titulo, autor, numero_paginas, editorial, ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.editorial = editorial
        self.ano_publicacion = ano_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.numero_paginas}")
        print(f"Editorial: {self.editorial}")
        print(f"Año de publicación: {self.ano_publicacion}")

    def es_largo(self):
        if self.numero_paginas > 300:
            return "Este libro es largo."
        else:
            return "Este libro es corto."

# Ejemplo de uso
libro = Libro("Cien años de soledad", "Gabriel García Márquez", 417, "Editorial Sudamericana", 1967)
libro.mostrar_informacion()
print(libro.es_largo())
