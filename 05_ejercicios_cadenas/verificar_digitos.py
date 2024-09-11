# se pide un numero de telefono con un formato especifico se separa el  numero
# a conveniencia y se imprima solo el numero 

num = input("Ingrese el numero de telefono en formato +34-123456789-56 ")
# separa la cadena  en un arreglo cuando encuentre "-"
sep_cadena = num.split("-")
# se muestra en consola  la parte [1] del arreglo donde quedo  la palabra separada.
print(sep_cadena[1])