nom = input("Nombre del trabajador? \n")
sal = int (input("Salario del trabajador? \n$"))

aux=0
if sal >= 1_200_000:
    aux = 120_000

print(f"El auxilio de transporte es de {aux:,}\n")