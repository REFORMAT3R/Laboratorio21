import math

class Figura:
    def area(self):
        return 0
    def perimetro(self):
        return 0
    def mostrar_datos(self):
        print(f"{self.__class__.__name__}")
        print(f"Área: {self.area():.2f}")
        print(f"Perímetro: {self.perimetro():.2f}")
        print("-" * 30)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(Figura):
    def __init__(self, base, altura, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado2 + self.lado3

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

figuras = [
    Rectangulo(5, 3),
    Triangulo(3, 6, 5, 4),
    Circulo(4)
]

for figura in figuras:
    figura.mostrar_datos()