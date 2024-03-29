import random

def generar_numeros():
    """Genera 20 números enteros aleatorios entre 0 y 100 y devuelve una lista."""
    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros

def mostrar_lista(lista):
    """Muestra una lista por pantalla."""
    print(lista)

def ordenar_y_mostrar(lista):
    """Ordena los valores de la lista y la muestra por pantalla."""
    lista_ordenada = sorted(lista)
    mostrar_lista(lista_ordenada)