#dado una cantidad de segundos, indique cuantas horas, minutos
#y segundos corresponde

segundos = int(input("Introduzca la cantidad de segundos "))


minutos = segundos//60
horas = minutos//60
minutosf = minutos%60
segundosf = segundos%60


print("las horas: ", horas)
print("los minutos: ", minutosf)
print("los minutos: ", segundosf)

