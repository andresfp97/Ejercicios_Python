import json
import os


def leerCodigo():
    while True:
        try:
            cod = input("Id del producto? ")
            if len(cod.strip()) == 0:
                print(">>> ERROR. Id invalido")
                continue
            return cod

        except Exception as e:
            print("Error al ingresar el codigo.\n", e)


def guardarDicJson(proAcme):
    ruta = "07_diccionarios/productosAcme.json"
    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
        with open(ruta, "r") as fd:
            try:
                data = json.load(fd)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}
    data.update(proAcme)
    with open(ruta, "w") as fd:
        json.dump(data, fd, indent=4)


def inserProd(proAcme):
    
    ruta = "07_diccionarios/productosAcme.json"

    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
        with open(ruta, "r") as fd:
            try:
                productosExistentes = json.load(fd)  
            except json.JSONDecodeError:
                productosExistentes = {} 
    else:
        productosExistentes = {}  

    
    proAcme.update(productosExistentes)
    
    nuevoProd = True
    while nuevoProd:
        print(">>> Nuevo Producto <<<")
        idProduct = leerCodigo()
        if idProduct not in proAcme:
            dDatos = {}
            dDatos["Nombre"] = input("Nombre? ")
            dDatos["Precio"] = float(input("ingrese el precio: "))
            dDatos["Cantidad"] = int(input("ingrese la Cantida: "))
            lisDes = []
            otroDes = True
            while otroDes:
                descuento = float(input("ingrese el descuento: "))
                lisDes.append(descuento)
                preguntaD = input("Quieres ingresar otro descuento? (y) =si  (n) = no ")
                if preguntaD == "y":
                    otroDes = True
                elif preguntaD == "n":
                    otroDes = False
            dDatos["Descuento"] = lisDes
            proAcme[idProduct] = dDatos
            preguntaP = input("Quieres ingresar otro producto? (y) =si  (n) = no ")
            if preguntaP == "y":
                nuevoProd = True
            elif preguntaP == "n":
                nuevoProd = False
        else:
            print("El codigo ya existe en la libreria.")

    return proAcme


def busProducto(proAcme):
    codigo = input("codigo a buscar? ")
    if codigo in proAcme:
        return proAcme[codigo]
    else:
        return "Producto no encontrado."


productosAcme = {}
print(inserProd(productosAcme))
guardarDicJson(productosAcme)
