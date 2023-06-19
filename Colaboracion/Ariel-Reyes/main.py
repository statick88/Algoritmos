class Bicicleta:
    def __init__(self, marca, precio,tamaño):
        self.marca = marca
        self.precio = precio
        self.tamaño = tamaño

    def __str__(self):
        return f"{self.marca} (${self.precio}),{self.tamaño} metros"


def mostrar_bicicletas(bicicletas):
    if bicicletas:
        print("Bicicletas ingresadas: ")
        for bicicleta in bicicletas:
            print(bicicleta)
    else:
        print("No se han ingresado bicicletas.")


def eliminar_bicicleta(bicicletas):
    if bicicletas:
        nombre = input("Ingrese la marca de la bicicleta: ")
        bicicletas_filtradas = [bicicleta for bicicleta in bicicletas if bicicleta.marca != nombre]
        if len(bicicletas_filtradas) < len(bicicletas):
            bicicletas[:] = bicicletas_filtradas
            print("Bicicleta eliminada exitosamente.")
        else:
            print("No se encontró una bicicleta con esa marca")
    else:
        print("No se han ingresado bicicletas.")



def modificar_bicicleta(bicicletas):
    if bicicletas:
        nombre = input("Ingrese la marca de la bicicleta: ")
        for bicicleta in bicicletas:
            if bicicleta.marca == nombre:
                nuevo_marca = input("Ingrese la nueva marca: ")
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                nuevo_tamaño = float(input("Ingrese el nuevo tamaño: "))
                bicicleta.marca = nuevo_marca
                bicicleta.precio = nuevo_precio
                bicicleta.tamaño = nuevo_tamaño
                print("Bicicleta modificada exitosamente.")
                return
        print("No se encontró una icicleta con esa marca")
    else:
        print("No se han ingresado bicicletas.")

def ingresar_bicicletas(bicicletas):
    marca = input("Ingrese la marca de la bicicleta ")
    precio = int(input("Ingrese el precio de la bicicleta: "))
    tamaño = float(input("Ingrese el tamaño de la bicicleta: "))
    bicicleta = Bicicleta(marca,precio,tamaño)
    bicicletas.append(bicicleta)
    print("Bicicleta ingresada exitosamente.")
    return bicicletas

def menu():
    bicicletas = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar bicicleta")
        print("2. Mostrar bicicletas")
        print("3. Eliminar bicicleta")
        print("4. Modificar bicicleta")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            bicicletas = ingresar_bicicletas(bicicletas)
        elif opcion == "2":
            mostrar_bicicletas(bicicletas)
        elif opcion == "3":
            eliminar_bicicleta(bicicletas)
        elif opcion == "4":
            modificar_bicicleta(bicicletas)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()