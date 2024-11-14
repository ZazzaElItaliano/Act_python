import math


class Figura:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo

    def calcular_area(self):
        """Método que debe ser sobrescrito en las clases derivadas."""
        raise NotImplementedError("Este método debe ser sobrescrito en las clases derivadas.")

    def calcular_perimetro(self):
        """Método que debe ser sobrescrito en las clases derivadas."""
        raise NotImplementedError("Este método debe ser sobrescrito en las clases derivadas.")


class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color, "Círculo")
        self.radio = radio

    def calcular_area(self):
        """Calcular el área de un círculo: π * r^2."""
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        """Calcular el perímetro de un círculo: 2 * π * r."""
        return 2 * math.pi * self.radio


class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color, "Cuadrado")
        self.lado = lado

    def calcular_area(self):
        """Calcular el área de un cuadrado: lado^2."""
        return self.lado ** 2

    def calcular_perimetro(self):
        """Calcular el perímetro de un cuadrado: 4 * lado."""
        return 4 * self.lado


class Triangulo(Figura):
    def __init__(self, color, base, altura, lado1, lado2, lado3):
        super().__init__(color, "Triángulo")
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        """Calcular el área de un triángulo: (base * altura) / 2."""
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        """Calcular el perímetro de un triángulo: suma de los tres lados."""
        return self.lado1 + self.lado2 + self.lado3


circulo = Circulo("Rojo", 5)
cuadrado = Cuadrado("Azul", 4)
triangulo = Triangulo("Verde", 6, 4, 3, 4, 5)


print(f"Círculo: área = {circulo.calcular_area():.2f}, perímetro = {circulo.calcular_perimetro():.2f}")
print(f"Cuadrado: área = {cuadrado.calcular_area():.2f}, perímetro = {cuadrado.calcular_perimetro():.2f}")
print(f"Triángulo: área = {triangulo.calcular_area():.2f}, perímetro = {triangulo.calcular_perimetro():.2f}")
