import json


def guardar(lib):
    with open("json/libreria.json", "w") as fd:
        json.dump(lib, fd)

        if not fd.close:
            fd.close()


def leerPrecio():
    while True:
        try:
            precio = int(input("Precio del libro"))
            if precio < 500:
                print(">>> Error.Precio incorrecto")
                continue
            return precio

        except ValueError:
            print("Error. precio invalido.\n")


def leerAutor():
    while True:
        try:
            autor = input("Titulo del autor? ")
            if len(autor.strip()) == 0:
                print(">>> ERROR. codigo invalido")
                continue
            return autor

        except Exception as e:
            print("Error al ingresar el autor.\n" + e)


def leerTitulo():
    while True:
        try:
            tit = input("Titulo del libro? ")
            if len(tit.strip()) == 0:
                print(">>> ERROR. codigo invalido")
                continue
            return tit

        except Exception as e:
            print("Error al ingresar el titulo.\n" + e)


def leerCodigo():
    while True:
        try:
            cod = input("Codigo del libro? ")
            if len(cod.strip()) == 0:
                print(">>> ERROR. codigo invalido")
                continue
            return cod

        except Exception as e:
            print("Error al ingresar el codigo.\n" + e)


def insertar(lib):
    print("\n\n *** 1. INSERTAR ***")
    cod = leerCodigo()
    if cod not in lib:
        titulo = leerTitulo()
        autor = leerAutor()
        precio = leerPrecio()

        datlib = {"titulo": titulo, "autor": autor, "precio": precio}

        lib[cod] = datlib

        lib = dict(sorted(lib.items()))
    else:
        print("El codigo ya existe en la libreria.")

    input("Presione cualquier tecla para volver al menu")
    return lib


def consultar():
    print("\n\n *** 2.CONSULTAR ***")
    input("Presione cualquier tecla para volver al menu")


def menu():
    while True:
        print("*** Libreria ***")
        print("1. Insertar")
        print("2. Consultar")
        print("3. Salir")

        print(">>> Opcion ?", end="")

        try:
            opcion = int(input())
            if opcion < 1 or opcion > 3:
                print("Error. opcion no valida")
                input("presione cualquier tecla para volver al menu")
                continue
            return opcion
        except ValueError:
            print("Error opcion no valida.")
            input("Presione cualquier tecla para volver al menu")


# Programa Principal

libreria = {}

while True:
    op = menu()

    match op:
        case 1:
            libreria = insertar(libreria)
            guardar(libreria)
        case 2:
            consultar(libreria)
        case 3:
            print("\n\nGracias por usar el software")
            break
