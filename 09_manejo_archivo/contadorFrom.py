fd = open("09_manejo_archivo/mbox.txt", "r")

# contar lineas de un archivo que empiecen con From:

cont = 0
for linea in fd:
    if linea.startswith("From:"):
        cont +=1

print(cont)
