# Dado la base y la altura  de un triangulo, calcular y mostrar
# su area a traves de la formula  area = (base*altura)/2

#ENTRADA
# b : base, h : altura

b = float(input("Introduzca la base del triangulo: "))
h = float(input("Introduzca la altura del triangulo: "))

#PROCESO
# a = b * h / 2

a = b * h / 2

#SALIDA
# a:area
#formateando la salida con format()
print("El área del triangulo es: {:.1f}".format(a))

# formateando la salida con cadenas f-string
print(f"El area del triangulo es: {a:.1f}")