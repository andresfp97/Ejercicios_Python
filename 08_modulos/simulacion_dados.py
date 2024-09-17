import random


def numeroVeces(num):

    lanzamientos =[0]*13

    for i in range(num):
        dado1 =  random.randrange(1,7)
        dado2 =  random.randrange(1,7)
        suma= dado1 + dado2
        lanzamientos[suma]+=1
    return lanzamientos.index(max(lanzamientos))


print("el numero que mas cae es: ", numeroVeces(10000000))




        
