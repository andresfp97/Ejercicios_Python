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