def aprobar(definitiva):
    if definitiva >= 3.0:
        return "Aprobo"
    else:
        return "Reprobo"


porc_notas = {1: 0.30, 2: 0.40}
estudiantes = {}
detener = 0


print("\nEstudiante")
cod = input("Codigo? ")

while cod != "999":
    
    dDatos = {}
    dDatos["nombre"] = input("Nombre? ")
    dDatos["nota1"] = float(input("ingrese la nota1: "))
    dDatos["nota2"] = float(input("ingrese la nota1: "))
    dDatos["nota3"] = float(input("ingrese la nota1: "))
    dDatos["definitiva"] = (
        (dDatos["nota1"] * porc_notas[1])
        + (dDatos["nota2"] * porc_notas[1])
        + (dDatos["nota3"] * porc_notas[2])
    )
    dDatos["status"] = aprobar(dDatos["definitiva"])
    estudiantes[cod] = dDatos
    detener = cod
    
    print("\nEstudiante")
    cod = input("Codigo? ")
    
print(estudiantes)
