nombre= input("Escriba el nombre del conductor: ")
codigo= input("Escriba el codigo de factura: ")
print("escriba el estado v = (vigente) o s = (suspendido)")
estado= input("EScriba el estado: ")
estrato = int(input("escriba el estrato"))
consumo= int(input("Ingrese el consumo del mes en cm3: ")) 
tb1 = 10_000
tb2 = 20_000
tb3 = 30_000
tb4 = 45_000
tb5 = 60_000
tb6 = 70_000
tb=0

if estado == "v":

    if estrato ==  1:
        vp = tb1 + (consumo* 200)
    elif estrato == 2:
        vp = tb2 +(consumo * 200)
    elif estrato == 3:
        vp = tb3 + (consumo * 200)
    elif estrato == 4:
        vp = tb4 + (consumo *200)
    elif estrato == 5:
        vp = tb5 + (consumo * 200)
    elif estrato == 6:
         vp = tb6 + (consumo * 200)
    print(nombre)
    print(codigo)
    print()
    print(consumo)
    print("Evalor a pagar es :",vp)

else:
    print("El usuario esta suspendido")
  


  