class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.menu = []  

    def anadir_plato(self, plato):
        self.menu.append(plato)
        print(f"El plato '{plato}' ha sido añadido al menú.")

    def mostrar_menu(self):
        if self.menu:
            print(f"Menú del restaurante '{self.nombre}':")
            for plato in self.menu:
                print(f"- {plato}")
        else:
            print("El menú está vacío. Añade platos para mostrar el menú.")

    def tomar_pedido(self, plato):
        if plato in self.menu:
            print(f"Pedido recibido: {plato}. Preparando su plato...")
        else:
            print(f"Lo siento, el plato '{plato}' no está en el menú.")


restaurante = Restaurante("La Cocina Mexicana", "Mexicana")
restaurante.anadir_plato("Tacos al Pastor")
restaurante.anadir_plato("Guacamole")
restaurante.mostrar_menu()
restaurante.tomar_pedido("Tacos al Pastor")
restaurante.tomar_pedido("Burrito")
