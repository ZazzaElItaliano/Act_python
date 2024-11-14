
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_costo_total(self):
        return self.precio * self.cantidad


class Electrodomestico(Producto):
    def __init__(self, nombre, precio, cantidad, consumo_energetico):
        super().__init__(nombre, precio, cantidad)
        self.consumo_energetico = consumo_energetico

    def calcular_costo_total(self):
      
        costo = super().calcular_costo_total()
        if self.consumo_energetico > 1000: 
            descuento = costo * 0.10 
            costo -= descuento
        return costo


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def calcular_costo_total(self):
        costo = super().calcular_costo_total()
        if self.cantidad > 5: 
            descuento = costo * 0.15 
            costo -= descuento
        return costo


class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_de_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_de_vencimiento = fecha_de_vencimiento

    def calcular_costo_total(self):
        costo = super().calcular_costo_total()
        
        if self.fecha_de_vencimiento <= 7:  
            descuento = costo * 0.20  
            costo -= descuento
        return costo

producto_electrodomestico = Electrodomestico("Aspiradora", 150, 2, 1200)
producto_ropa = Ropa("Camiseta", 20, 6, "L")
producto_alimento = Alimento("Leche", 1.5, 10, 5)

print(f"Costo total del electrodoméstico: ${producto_electrodomestico.calcular_costo_total():.2f}")
print(f"Costo total de la ropa: ${producto_ropa.calcular_costo_total():.2f}")
print(f"Costo total del alimento: ${producto_alimento.calcular_costo_total():.2f}")
