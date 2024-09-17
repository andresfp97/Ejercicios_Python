def menu():
    print(">>> MENU <<< " )
    print("1. Ver calificación más alta")
    print("2. Ver calificación más baja")
    print("3. Ordenar calificaciones de menor a mayor")
    print("4. Eliminar calificación incorrecta")
    print("5. Mostrar promedio de calificaciones")
    print("6. Mostrar número total de estudiantes")
    print("7. Salir")
    print()
    num = int(input(">>> SELECCIONE LA RESPUESTA QUE DESEA: "))
    return num


def calAlta(lst):
    mayor = max(lst)
    return mayor


def calBaja(lst):
    menor = min(lst)
    return menor


def ordMenorMay(lst):
      return sorted(lst)


def elimiCal(lst, pos):
    del lst[pos-1]
    return lst


def promCal(lst):
    promedio = 0
    promedio += sum(lst) / (len(lst))
    return promedio


def totEst(lst):
    cant = len(lst)
    return cant

def esperar_tecla_para_continuar():
    input("Presiona Enter para continuar...")
    print("\n" * 30)


cal = [4.5, 3, 3.8, 4.2, 3.3]


while True:
    num = menu()
    match num:
        case 1:
            mayor = calAlta(cal)
            print(f"la calificacion mas alta es: {mayor}")
            print("="*40)
            esperar_tecla_para_continuar()
        case 2:
            menor = calBaja(cal)
            print(f"la calificacion mas baja es: {menor}")
            print("="*40)
            esperar_tecla_para_continuar()
        case 3:
            ordenada = ordMenorMay(cal)
            print (f"La lista ordenada es: {ordenada}")
            print("="*40)
            esperar_tecla_para_continuar()
        case 4:
            print(cal)
            pos = int(input("ingrese la pocision a eliminar: ")) 
            print(elimiCal(cal, pos))
            print("="*40)
            esperar_tecla_para_continuar()
        case 5:
            promedio = promCal(cal)
            print(f"El promedio de calificaciones es : {promedio}")
            print("="*40)
            esperar_tecla_para_continuar()
        case 6:
            total = totEst(cal)
            print(f"El total de estudiantes es 8: {total}")
            print("="*40)
            esperar_tecla_para_continuar()
        case 7:
            print(">>> Eso fue todo :) hasta luego <<<")
            print("="*40)
            break
        case _:
            print("Número no reconocido intenta de nuevo")


