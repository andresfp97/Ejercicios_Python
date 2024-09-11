nom = input("Nombre del estudiante  \n")
can = float(input("ingrese la calificacion cuantitativa \n"))

cali = ""

if can >= 0 and can <= 59:
    cali = "D"
elif can >= 60 and can <= 79:
    cali = "C"
elif can >= 80 and can <= 89:
    cali = "B"
elif can >= 90 and can <= 100:
    cali = "A"
else:
    cali = ""

if cali != "":
    print("\n--------------------")
    print("nombre: ", nom)
    print(f"calificacion cuantitativa: {can:.1f}")
    print("calificacion cualitativa: ", cali)
else:
    print(">>ERROR. Calificacion invalidad. ")
