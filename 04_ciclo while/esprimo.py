# Indicar si el numero es primo
num = int(input("numero: "))

if num > 1:
    esprimo= True
    for i in range(2, num):
        if num % i == 0:
            esprimo = False
            break
    if esprimo:
        print("Es primo. ")
    else:
        print("No es primo. ")
else:
    print("No es primo. ")