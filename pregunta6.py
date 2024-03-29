##Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
##Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
##método para agregar productos y otra para mostrar toda la lista de productos.
##Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
##agregar más atributos a los productos para que se puedan hacer otras funcionalidades


class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        for producto in self.productos:
            if producto.año == año:
                print(producto)

    def filtrar_por_rango_precio(self, precio_minimo, precio_maximo):
        for producto in self.productos:
            if precio_minimo <= producto.precio <= precio_maximo:
                print(producto)

# Ejemplo de uso
catalogo = Catalogo()

class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        for producto in self.productos:
            if producto.año == año:
                print(producto)

    def filtrar_por_rango_precio(self, precio_minimo, precio_maximo):
        for producto in self.productos:
            if precio_minimo <= producto.precio <= precio_maximo:
                print(producto)


catalogo = Catalogo()

catalogo.agregar_producto(Producto("Filtro de aire", 50, 2020))
catalogo.agregar_producto(Producto("Bujía", 15, 2018))
catalogo.agregar_producto(Producto("Aceite motor 5L", 30, 2021))


print("Todos los productos:")
catalogo.mostrar_productos()


print("\nProductos del año 2020:")
catalogo.filtrar_por_año(2020)

print("\nProductos con precio entre 20 y 40:")
catalogo.filtrar_por_rango_precio(20, 40)

print("Todos los productos:")
catalogo.mostrar_productos()

print("\nProductos del año 2020:")
catalogo.filtrar_por_año(2020)

print("\nProductos con precio entre 20 y 40:")
catalogo.filtrar_por_rango_precio(20, 40)