##Implemente un programa que solicite al usuario una fracción, con
##formato X/Y, donde cada uno de X e Y es un número entero, y luego
##muestra, como un porcentaje redondeado al número entero más
##cercano, donde se indicará la cantidad de combustible en el
##tanque. Se debe tener en cuenta los siguientes casos:
##- Colocar E en caso X/Y sea menor a 1% del total
##- Colocar F en caso X/Y sea mayor a 99%.
##- En otro caso, devolver el valor en porcentaje %
##También debe tomar en cuenta los siguientes casos:
##- X y Y deben ser números enteros
##- X debe ser menor o igual a Y, y Y != 0
##De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
##cualquier excepción como ValueError o ZeroDivisionError.


def calcular_porcentaje_combustible():
    while True:
        try:
            fraccion = input("Ingrese la fracción del combustible en el tanque (formato X/Y): ")
            x, y = map(int, fraccion.split('/'))

# Verificar que X <= Y y Y != 0
            
            if x > y or y == 0:
                raise ValueError("X debe ser menor o igual a Y, y Y debe ser diferente de 0.")

# Calcular el porcentaje
            porcentaje = (x / y) * 100

# Decidir el mensaje basado en el porcentaje
            
            if porcentaje < 1:
                mensaje = "E"
            elif porcentaje > 99:
                mensaje = "F"
            else:
                mensaje = f"{round(porcentaje)}%"
            
            return mensaje

        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese valores válidos.")
        except ZeroDivisionError:
            print("Error: División por cero. Asegúrese de que Y no sea 0.")

combustible = calcular_porcentaje_combustible()
print(f"Combustible en el tanque: {combustible}")