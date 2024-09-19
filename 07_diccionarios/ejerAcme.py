import json
def guarArt(artAcme):
    with open("07_diccionarios/productos.json","w") as fd:
        json.dump(artAcme, fd)

def leerNombre():
    while True:
        try:
            nombre = input("Nombre del Prodcuto? ")
            if len(nombre.strip()) == 0:
                print(">>> ERROR. codigo invalido")
                continue
            return nombre

        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)


def leerPrecio():
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio < 4000:
                print(">>> Error.Precio incorrecto")
                continue
            return precio

        except ValueError:
            print("Error. precio invalido.\n")


def leerCantidad():
    while True:
        try:
            cant = int(input("Cantidad en el inventario: "))
            if cant < 0:
                print(">>> Error. en cantidd")
                continue
            return cant

        except ValueError:
            print("Error. cantidad invalido.\n")


def leerDescuento():
    lisDes = []

    while True:
        try:
            descuento = float(input("ingrese el descuento: (-1 para terminar) "))
            if descuento == -1:
                break
            else:
                lisDes.append(descuento)

        except ValueError:
            print("Error. precio invalido.\n")

    return lisDes


def ingProducto():
    
    while True:
        print("Nuevo Producto")
        print("="*50)
        print ("(-1)  para no ingresar productos")
        idProduct = int(input("Codigo de producto? : " ))
        if  idProduct != -1:
            dDatos = {}
            dDatos["Nombre"] = leerNombre()
            dDatos["Precio"] = leerPrecio()
            dDatos["Cantidad"] = leerCantidad()
            dDatos["Descuento"] = leerDescuento()
            productos[idProduct] = dDatos   
        else:
            break
    return productos


def busProducto(codigo):
    if codigo in productos:
        return productos[codigo]
    else:
        return "Producto no encontrado."


productos = {}

productos = ingProducto()
guarArt(productos)
print(productos)

