# funcion que me reciba un numero y me devuelva true
# si es primo y False si no lo es 

def esprimo(num):
    if num > 1:
        esprimo= True
        for i in range(2, num):
            if num % i == 0:
                esprimo = False
                break
        if esprimo:
            return True
        else:
            return False
    else:
        return False

def esprimo2(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


# programa que reciba una serie de numero hasta que se
# ingrese un primo

n = int(input("Ingrese un numero: "))
while not esprimo2(n):  # es equivalente a esprimo(n)== False
    n = int(input("Ingrese un numero: "))