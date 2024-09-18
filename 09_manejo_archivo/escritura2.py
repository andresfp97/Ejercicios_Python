fd = open("09_manejo_archivo/data2.txt", "w")

icad = ["Los pollitos dicen\n", "Yo sere la mascota"]

fd.writelines(icad)

fd.close()