<<<<<<< HEAD:json/libreria.py
import json


def guardar(lib):
    with open("json/libreria.json", "w") as fd:
        json.dump(lib, fd)

        if not fd.close:
            fd.close()


=======
from persistencia.persistencia import guardar

>>>>>>> origin/main:libreria/modelo/modelo.py
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


def insertar(lib, arch):
    print("\n\n *** 1. INSERTAR ***")
    cod = leerCodigo()
    if cod not in lib:
        titulo = leerTitulo()
        autor = leerAutor()
        precio = leerPrecio()

        datlib = {"titulo": titulo, 
                  "autor": autor,
                  "precio": precio}

        lib[cod] = datlib

        lib = dict(sorted(lib.items()))
        guardar(lib, arch)
    else:
        print("El codigo ya existe en la libreria.")

    input("Presione cualquier tecla para volver al menu")
    return lib


def consultar (lib):
    print("\n\n *** 2 CONSULTAR ***")

    cod = input("\n Codigo a consultar")
    if cod in lib:
        print("-> Codigo", cod)
        print(f"-> Titulo: .{lib[cod]['titulo']}")
        print(f"-> Autor: .{lib[cod]['autor']}")
        print(f"-> Precio: .{lib[cod]['precio']}")
    else:
        print(">>> error el codigo del libro no existe en la libreria")

    input("Presione cualquier tecla para volver al menu")
    