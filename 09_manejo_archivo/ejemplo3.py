import io

fd = open("09_manejo_archivo/data.txt", "r")

cad = fd.readlines()
print(cad)

fd.close()