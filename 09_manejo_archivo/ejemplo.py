import io

fd = open("09_manejo_archivo/data.txt", "r")

cad = fd.read()
print(cad)

fd.seek(0)
cad = fd.read(5)
print(cad)


fd.close()