class Producto:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"


def mostrar_productos(productos):
    if productos:
        print("Productos ingresados:")
        for producto in productos:
            print(producto)
    else:
        print("No se han ingresado productos.")


def eliminar_producto(productos):
    if productos:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        productos_filtrados = [producto for producto in productos if producto.nombre != nombre]
        if len(productos_filtrados) < len(productos):
            productos[:] = productos_filtrados
            print("Producto eliminado exitosamente.")
        else:
            print("No se encontró un producto con ese nombre.")
    else:
        print("No se han ingresado ningun producto.")



def modificar_producto(productos):
    if productos:
        nombre = input("Ingrese el nombre del producto a modificar: ")
        for producto in productos:
            if producto.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del producto ")
                producto.nombre = nuevo_nombre
                print("Producto modificado exitosamente.")
                return
        print("No se encontró un producto con ese nombre.")
    else:
        print("No se han ingresado ningun producto.")

def menu():
    productos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar producto")
        print("2. Mostrar producto")
        print("3. Eliminar producto")
        print("4. Modificar producto")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            producto = Producto(nombre)
            productos.append(producto)
            print("Película ingresada exitosamente.")
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            eliminar_producto(productos)
        elif opcion == "4":
            modificar_producto(productos)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()