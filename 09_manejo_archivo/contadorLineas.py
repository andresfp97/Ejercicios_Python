fd = open("09_manejo_archivo/mbox.txt", "r")

# contar lineas de un archivo  con ciclo for 

cont = 0
for i in fd:
    cont +=1

print(cont)

fd.seek(0)

# contar lineas de un archivo  con ciclo while
cont =0
linea = fd.readline()

while linea:
    cont+=1
    linea = fd.readline()

print(cont)
fd.close()