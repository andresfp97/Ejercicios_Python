from cgi import print_form


def busquedaLineal(lst, elem):
    for i in range(len(lst)):
        if lst[i]== elem:
            return [True, i]
    return [False, None]

lista=  ["andres", "felipe", "maria", "cleotilde", "oscar"]
existe, pos = busquedaLineal(lista, "maria")

if existe:
    print("Pasa al ciclo 3")
    print("posicion: " ,pos)
else:
    print("Muchas gracias por estar en campus")