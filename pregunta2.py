##Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
##la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
##calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
##cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
##formato. (Los métodos de cadena le serán de utilidad)

def convertir_calificaciones(cadena_calificaciones):

    calificaciones_str = cadena_calificaciones.split(",")
    calificaciones_int = []

    for calificacion in calificaciones_str:
        try:
            calificaciones_int.append(int(calificacion))

        except ValueError:
            print(f"Error: '{calificacion}' no puede ser convertido a entero.")
    
    return calificaciones_int

calificaciones_usuario = input("Ingrese las calificaciones separadas por comas (ejemplo: 10,8,9,7): ")

calificaciones = convertir_calificaciones(calificaciones_usuario)

print("Calificaciones convertidas a enteros:", calificaciones)