def menu():
    print(">>> MENU <<<")
    print("1. Ver calificación más alta")
    print("2. Ver calificación más baja")
    print("3. Ordenar calificaciones de menor a mayor")
    print("4. Eliminar calificación incorrecta")
    print("5. Mostrar promedio de calificaciones")
    print("6. Mostrar número total de estudiantes")
    print("7. Salir")
    print("SELECCIONE LA RESPUESTA QUE DESEA")


def calAlta(lst):
    mayor = max(lst)
    return mayor


def calBaja(lst):
    menor = min(lst)
    return menor


def ordMayMenor(lst):
    lst = sorted(lst)
    return lst


def elimiCal(lst, pos):
    del lst[pos]
    return lst


def promCal(lst):
    promedio = 0
    promedio += sum(lst) / (len(lst))
    return promedio


def totEst(lst):
    cant = len(lst)
    return cant


cal = [4.5, 3, 3.8, 4.2, 3.3]


def elegirProceso(num):
    match num:
        case 1:
            mayor = calAlta(cal)
            print(f"la calificacion mas alta es: {mayor}")
        case 2:
            menor = calBaja(cal)
            print(f"la calificacion mas alta es: {menor}")
        case 3:
            ordMayMenor(cal)
            print (f"La lista ordenada es: {cal}")
        case 4:
            pos = int(input("ingrese la pocision a eliminar")) 
            elimiCal(cal,pos)
            print (f"La lista con el valor eliminado es: {cal}")
        case 5:
            promedio = promCal(cal)
            print(f"la calificacion mas alta es: {promedio}")
        case _:
            return "Número no reconocido"
