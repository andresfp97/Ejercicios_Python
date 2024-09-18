import io

fd = open("09_manejo_archivo/data.txt", "r")

cad = fd.readline().strip
print(cad)

cad = fd.readline()
print(cad)


fd.close()