
lista = [10,20,"Juan", 30, "Sergio"]
lista.append(40) # añade al final el 40
print(lista)

lista2 =["maria", 20]
# lista.append(lista2)
lista.extend(lista2)
print(lista)

# insert
lista.insert(2,50)
print(lista)

# pop
lista.pop()
print(lista)

lista.pop(2)
print(list)

# remove
lista.remove("Sergio")
print(lista)


lista = [40,30,5,90,20,1,20,50,60,20]
# min

print(min(lista))

#len
print(f"Tamaño de la lista: {len(lista)}")

# sorted  
# oedena creciente (menor a mayor)
print(sorted(lista))

#decreciente(mayor a menor)
print(sorted(lista, reverse = True))
# count 
print(lista.count(20))

lista = [40,30,5,90,20,1,20,50,60,20]

# del
del(lista[3])
print(lista)

# limpiar lista
lista.clear()
print(lista)
print(type(lista))


