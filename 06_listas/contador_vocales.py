def imprimirlista(lst):
    for e in lst:
        print(e, end="| ")


n = int(input("cuantas letras va ingresar"))

lstvocales = [0] * 5
print(lstvocales)
for i in range(n):
    letra = input(f"ingrese la letra {i+1}: ")
    letra = letra.strip()

    if len(letra) > 0:
        letra = letra[0].lower()
        #   if letra.lower()== "a":
        #        lstvocales[0]+= 1
        #   elif letra.lower()== "e":
        #        lstvocales[1]+= 1
        #   elif letra.lower()== "i":
        #        lstvocales[2]+= 1
        #   elif letra.lower()== "o":
        #        lstvocales[3]+= 1
        #   elif letra.lower()== "u":
        #        lstvocales[4]+= 1
        match letra:
            case "a":
                lstvocales[0] += 1
            case "e":
                lstvocales[1] += 1
            case "i":
                lstvocales[2] += 1
            case "o":
                lstvocales[3] += 1
            case "u":
                lstvocales[4] += 1
            case _:
                pass


imprimirlista(lstvocales)
