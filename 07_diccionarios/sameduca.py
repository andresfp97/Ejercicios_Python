d_categoria= {1:25_000, 2:30_000, 3:40_000, 4:45_000,5 :60_000}

n = int(input("Cantidad de docentes? "))

docentes= {}
suma = 0
for i in range(n):
    print(f"\nDocente{i+1}")
    cedula = input("Cedula?")
    dDatos ={}
    dDatos["nombre"] = input("Nombre? ")
    dDatos["categoria"] = int(input("Categoria (1 al 5)"))
    dDatos["horas_lab"] = int(input("Horas laboradas? "))
    
    dDatos["honorarios"] = d_categoria[dDatos["categoria"]]* dDatos["horas_lab"]

    docentes [cedula] = dDatos
    suma += dDatos["honorarios"] 

print(docentes)

# informe
print("*** INFORME ***".center(40))
print("")

for k in docentes.keys():
    print("Nombre: ", docentes[k]["nombre"])
    print(f"Honorarios: ${docentes[k]['honorarios']:,}")
    print ("-"*30, "\n")

print("")
print ("-"*30, "\n")
print(f"valor de los honorarios es: ${suma:,}")
