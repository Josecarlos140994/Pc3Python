##Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
##ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
##atributos de la clase


class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

mi_rectangulo = Rectangulo(10, 5)

print(f"El área del rectángulo es: {mi_rectangulo.calcular_area()}")