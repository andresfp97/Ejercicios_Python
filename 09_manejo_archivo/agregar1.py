fd = open("09_manejo_archivo/data2.txt", "a")

icad = ["Nos vamos de azado \n", "invita anderson"]
fd.writelines(icad)

fd.close()