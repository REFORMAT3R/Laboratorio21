import math

def area_circulo(radio):
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return 2 * math.pi * radio

def area_rectangulo(base, altura):
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura deben ser positivas")
    return base * altura

def perimetro_rectangulo(base, altura):
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura deben ser positivas")
    return 2 * (base + altura)