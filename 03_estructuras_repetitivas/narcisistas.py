#mostrar si un numero es narcisita
# un numero es narcisita si la suma  de sus dijitos elevado a 
# la cantidad de dijitos es igual al numero
# 153 =  1^3 + 5^3 + 3³



import math


n = int(input("ingrese un numero : "))


if n > 0:
   lnum = int(math.log10(n))+1 
   suma =0
   temp = n
   for i in range(0,lnum):
        d = n % 10
        suma += d**lnum
        n = n//10
   if suma == temp:
       print("el numero es narciso")
   else:
       print("el numero no es narciso")
    
else:
    print("el numero debe ser  mayor que 0")
