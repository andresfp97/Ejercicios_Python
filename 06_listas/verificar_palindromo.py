def contar_caracteres (cadena):
    conteo = {}
    for caracter in cadena:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1

    return conteo


cadena = input("Ingresar la palabra")
tamano = len(cadena)

if tamano > 0 and tamano <= 50:
    
    

 


