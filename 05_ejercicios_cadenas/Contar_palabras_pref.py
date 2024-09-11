# se ingresa N palabras y se le pide al usuario que indique un prefijo
# y se verifica cuantas palabras contienen el prefijo 

num = int(input("Ingrese el numero de palabras: "))
pref = input("ingrese el prefijo: ")
cont = 0

for i in range(num):
    pal = input("ingrese la palabra: ")
    if pal.startswith(pref):
        cont+=1

print(cont)
