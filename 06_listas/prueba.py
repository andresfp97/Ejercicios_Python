def mostrar_menu():
    print("Menú:")
    print("1. Mostrar calificación más alta")
    print("2. Mostrar calificación más baja")
    print("3. Salir")
    num = int(input("Selecciona una opción: "))
    return num

def calAlta(cal):
    return max(cal)

def calBaja(cal):
    return min(cal)

def esperar_tecla_para_continuar():
    input("Presiona Enter para continuar...")

cal = [85, 90, 78, 92, 88]  # Lista de calificaciones de ejemplo

while True:
    num = mostrar_menu()

    match num:
        case 1:
            mayor = calAlta(cal)
            print(f"La calificación más alta es: {mayor}")
            esperar_tecla_para_continuar()
        case 2:
            menor = calBaja(cal)
            print(f"La calificación más baja es: {menor}")
            esperar_tecla_para_continuar()
        case 3:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida, intenta de nuevo.")