class Serie:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"

    def buscar_por_anio(self, anio):
        if self.anio == anio:
            return True
        else:
            return False


def mostrar_series(series):
    if series:
        print("Series ingresadas:")
        for serie in series:
            print(serie)
    else:
        print("No se han ingresado series.")

# Resto del código...

def menu():
    series = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar serie")
        print("2. Mostrar serie")
        print("3. Eliminar serie")
        print("4. Modificar serie")
        print("5. Buscar serie por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la Serie: ")
            anio = int(input("Ingrese el año de la Serie: "))
            serie = Serie(nombre, anio)
            series.append(serie)
            print("Serie ingresada exitosamente.")
        elif opcion == "2":
            mostrar_series(series)
        elif opcion == "3":
            eliminar_serie(series)
        elif opcion == "4":
            modificar_serie(series)
        elif opcion == "5":
            anio = int(input("Ingrese el año a buscar: "))
            series_encontradas = [serie for serie in series if serie.buscar_por_anio(anio)]
            if series_encontradas:
                print("Series encontradas:")
                for serie in series_encontradas:
                    print(serie)
            else:
                print("No se encontraron series con ese año.")
        elif opcion == "0":
            print("¡Gracias por usar la aplicacion modificada :D !")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()