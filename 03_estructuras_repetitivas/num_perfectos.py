#mostrar si un numero es perfecto
# un numero es perfecto si la suma de sus divisores dan el mismo  numero

n = int(input("ingrese un numero entero positivo mayor que 1: "))
acu = 0

if n > 1:
    for i in range(1, n):
        if n % i == 0:
            acu += i

    if acu == n:
        print ("El numero es perfecto")
    else:
        print("el numero no es perfecto")

else:
    print("el numero debe ser mayor que 1")

