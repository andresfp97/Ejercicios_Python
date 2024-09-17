def menu():
    print(">>> MENU <<<") 
    print("1. Ver calificación más alta")
    print("2. Ver calificación más baja")
    print("3. Ordenar calificaciones de menor a mayor")
    print("4. Eliminar calificación incorrecta")
    print("5. Mostrar promedio de calificaciones")
    print("6. Mostrar número total de estudiantes")
    print("7. Salir")
    print(">>> SELECCIONE LA OPCION DE SU PREFERENCIA <<<") 
    
def calAlta(lst):
    return max(lst)

def calBaja(lst):
    return min(lst)

def ordMenorMayor(lst):
    return sorted(lst, reverse= True)

def elimCalIncorr(lst, pos):
    del (lst[pos])
    return lst
    
        
    
cal= [ 4,5,7,9,5]

print(elimCalIncorr(cal, 3))








