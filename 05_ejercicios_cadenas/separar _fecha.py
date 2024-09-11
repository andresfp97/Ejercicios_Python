def pedir_fecha_nacimiento():
    # Pedir la fecha de nacimiento
    fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
    
    # split("/")---> Separar la fecha en día, mes y año
    # lo guarda en un arreglo
    
    partes_fecha = fecha.split("/")
    print(partes_fecha)
    
    # zfill ---> rellenar una cadena con ceros (0) a la izquierda hasta que la 
    # longitud de la cadena alcance el número especificado.
    
    dia = partes_fecha[0].zfill(2)
    mes = partes_fecha[1].zfill(2)
    anio = partes_fecha[2]
    
    # Mostrar el resultado
    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {anio}")

# Llamar a la función
pedir_fecha_nacimiento()