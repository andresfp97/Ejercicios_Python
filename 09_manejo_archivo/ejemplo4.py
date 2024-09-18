import io

fd = open("09_manejo_archivo/data.txt", "r")

# recorrido de archivos
for linea in fd:
    print(linea.strip().title())


fd.seek(0)
for car in fd.read():
    print(car.strip(), end=",")

fd.close()