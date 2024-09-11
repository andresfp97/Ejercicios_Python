num1 = int(input("Ingrese el primer numero: \n"))
num2 = int(input("Ingrese el primer numero: \n"))
num3 = int(input("Ingrese el primer numero: \n"))


if  num1 > num2 and  num1 > num3 and num2 > num3:

    mayor = num1
    medio = num2
    menor = num3

    print("mayor: ", mayor)
    print("medio: ", medio)
    print("menor:", menor)

elif num2 > num1 and num2 > num3  and num1 > num3 :

    mayor = num2
    medio = num1
    menor = num3

    print("mayor: ", mayor)
    print("medio: ", medio)
    print("menor:", menor)

elif num3 > num1 and num3 > num2 and num2 > num1:
     
     mayor = num3
     medio = num2
     menor = num1

     print("mayor: ", mayor)
     print("medio: ", medio)
     print("menor:", menor)






