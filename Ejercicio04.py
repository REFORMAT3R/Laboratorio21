import geometria

try:
    print("Área del círculo:", geometria.area_circulo(5))
    print("Perímetro del círculo:", geometria.perimetro_circulo(5))

    print("Área del rectángulo:", geometria.area_rectangulo(4, 3))
    print("Perímetro del rectángulo:", geometria.perimetro_rectangulo(4, 3))

except ValueError as e:
    print("Error:", e)