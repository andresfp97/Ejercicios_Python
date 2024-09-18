# Escriba un programa que envie un mensaje: "Vota por mi mascota"
#a todos los correos que aparecen en el Front:
# su programa debe mostrar un mensaje como el siguiente por cada correo:
#cwen@iupi.edu ---> "Vota pormi mascota" ::: [CORREO ENVIADO]

fd = open("09_manejo_archivo/mbox.txt", "r")

for linea in fd:
    if linea.find("@") != -1:
        pos = linea
        print(pos)
       
fd.close()

#terminar en casa