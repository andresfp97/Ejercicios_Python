
porc_notas = {1:0.30, 2:0.40}
Estudiantes = {}
detener = 0
codigo = 999

while codigo != 999:

    print("\nEstudiante")
    cod = input("Codigo")
    codigo = cod
    dDatos ={}
    dDatos["nombre"] = input("Nombre? ")
    dDatos["nota1"] = float(input("ingrese la nota1"))
    dDatos["nota2"] = float(input("ingrese la nota1"))
    dDatos["nota3"] = float(input("ingrese la nota1"))
    dDatos["definitiva"] = dDatos["nota1"] * porc_notas [1] + dDatos["nota2"] * porc_notas [1] + dDatos["nota3"] * porc_notas [2] 
    

    docentes [cedula] = dDatos
    suma += dDatos["honorarios"] 

print(docentes)