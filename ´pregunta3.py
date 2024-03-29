##Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
##“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.141592653589793 * self.radio ** 2

#instancia de la clase Circulo con un radio de 5
mi_circulo = Circulo(5)


print(f"El área del círculo es: {mi_circulo.calcular_area()}")