def ingProducto(num):
    Productos = {}
    for i in range(num):
        print("Nuevo Producto")
        idProduct = input("Id? ")
        dDatos = {}
        dDatos["Nombre"] = input("Nombre? ")
        dDatos["Precio"] = float(input("ingrese el precio: "))
        dDatos["Cantidad"] = int(input("ingrese la Cantida: "))

        lisDes =[]
        canDes = int(input("Cantidad de descuentos :"))
        for d in range(1,canDes+1):
            descuento = float(input(f"ingrese el descuento numero {d}: "))
            lisDes.append(descuento)

        dDatos["Descuento"] = lisDes
        
        Productos[idProduct] = dDatos
            

    print(Productos)


num = int(input("ingrese la cantida de productos a registrar"))
ingProducto(num)