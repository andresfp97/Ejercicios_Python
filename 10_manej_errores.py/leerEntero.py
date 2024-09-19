from datetime import datetime

def leerFecha(msg):
    try:
        fecha = datetime.strptime(input(msg), "%d/%m/%Y")
        ano, mes, dia =str(fecha).split()[0].split("-")
        return f"{dia}/{mes}/{ano}"
    except ValueError:
        print("Error. formato de fecha invalidoo. \n")


def leerNumeroFloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print("Error, ingrese un numero decimal valido.\n")


def leerEnteropositivo(msg):
    while True:
        try:
            num = int(input(msg))
            if num < 0:
                print("Error. ingrese un numero positivo.\n")
            else:
                return num
        except ValueError:
            print("Error, ingrese un numero entero valido.\n")


def leerEntero(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except ValueError:
            print("Error, ingrese un numero entero valido.\n")
    return num


# temp = leerNumeroFloat("ingrese la temperatura ")
# print(temp, type(temp))

fecha = leerFecha("Ingrese la fecha de nacimiento")
print(fecha)
