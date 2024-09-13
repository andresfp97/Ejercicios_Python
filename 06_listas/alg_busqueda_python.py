lista=  ["andres", "felipe", "maria", "cleotilde", "oscar"]
nombre = "maria"
if  nombre in lista:
    pos = lista.index(nombre)
    print ("pasa al ciclo 3")
    print (f"posicion en la lista: {pos}")
else:
    print("Gracias por participar en python")