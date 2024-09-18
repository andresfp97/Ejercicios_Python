with open("09_manejo_archivo/mbox.txt","r") as fd:
    lstEmail = []

    for linea in fd:
        if linea.startswith("From: "):
            correo = linea.split()[1]+ "enviado [ok] \n"
            if correo not in lstEmail:
                lstEmail.append(correo )

lstEmail.reverse()

with open("09_manejo_archivo/correos_enviados.txt","w") as fd:
    fd.writelines(lstEmail)
