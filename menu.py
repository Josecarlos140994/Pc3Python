from pregunta3 import Circulo
from pregunta4 import Rectangulo

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

def main():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print("El área del círculo es:", circulo.calcular_area())
        elif opcion == '2':
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print("El área del rectángulo es:", rectangulo.calcular_area())
        elif opcion == '3':
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print("El área del cuadrado es:", cuadrado.calcular_area())
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
