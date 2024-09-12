def posElemMayList(lst):
    mayor = lst[0]
    pos = 0
    for i in range(len(lst)):
        if lst[i] > mayor:
            mayor = lst[i]
            pos = i
    return [pos, mayor]


def posMayList(lst):
    mayor = lst[0]
    pos = 0
    for i in range(len(lst)):
        if lst[i] > mayor:
            mayor = lst[i]
            pos = i
    return pos


def mayorLista(lst):
    mayor= lst[0]
    for e in lst:
        if e > mayor:
            mayor = e
    return mayor


def menorLista(lst):
    menor= lst[0]
    for e in lst:
        if e < menor:
            menor = e
    return menor


def sumaLista(lst):
    suma = 0
    for e in lst:
        suma+= e
    return suma


def imprimirlista(lst):
    for e in lst:
        print(e, end= "| ")

list_numero = [10,15,20,25,30]

print(type(list_numero))

# recorre la lista por las posiciones

for i  in range(len(list_numero)):
    print(list_numero[i],end=", ")
print("")

for i in range(-1, -len(list_numero)-1, -1):
    print(list_numero[i], end= "* ")
print("")

for i in range(len(list_numero) -1, -1, -1):
    print(list_numero[i], end= "- ")
print("")
#2. por sus elementos

for e in list_numero:
    print(e, end="| ") 
print("")

imprimirlista(list_numero)
print("")
#funcion que devuelve la suma de los elementos de lista

print("La suma de los elementos de la lista es: ",sumaLista(list_numero))
print("")

#Imprimir el mayor elemento de la lista
print("El mayor elemento es: ", mayorLista(list_numero))
print("")

#imprimir el menor elemento de la lista
print("El menor elemento es: ", menorLista(list_numero))
print("")


#imprimir la posicion del elemento mayor de la lista
print("el elemento mayor se encuentra en la posicion: ",posMayList(list_numero)+1)
print("")

lstResult = posElemMayList(list_numero)
print(f"el elemento mayor y su posicion es: {lstResult[1], lstResult[0]+1}")


# list_numero = [10,15,20,25,30]
#modificar una lista

list_numero[-1] = 35

#operadores de las listas

list_numero2 = [1,2]
# operador de concatenacion

lstrlst = list_numero + list_numero2
print(lstrlst)

#operador (*) de repeticion
lstrlst = list_numero2 * 3
print(lstrlst)