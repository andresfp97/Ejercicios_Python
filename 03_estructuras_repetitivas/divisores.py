#mostrar  los divisores de un numero ingresado por el usuario
n = int(input("ingrese un numero entero positivo mayor que 1: "))

if n > 1:
    for i in range(1, n):
        if n % i == 0:
            print(i, end = ", ")
    
else:
    print("el numero debe ser mayor que 1")