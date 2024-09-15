def diaMayorIng(mat, lst):
    lsting = []
    for f in range(len(mat[0])):
        suma=0
        for c in range(len(mat)):
            suma += mat[c][f] * lst[c]
        lsting.append(suma)
    mayor = max(lsting)
    pos = lsting.index(mayor)+1
    return [pos, mayor]

def DiaSemana(num):
    dias_semana= ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
    if  num > 0 and num <= 7:
        return (dias_semana[num-1])
   

def proMayIngSem(mat, lst):
    lsting = []
    for f in range(len(mat)):
        suma = 0
        for c in range(len(mat[f])):
            suma += mat[f][c] * lst[f]
        lsting.append(suma)
        # lsting.append(sum(mat[f] * lst [f]))

    mayor = max(lsting)
    prod = lsting.index(mayor) + 1

    return [prod, mayor]


lstPrecios = [1500, 5000, 6500, 2500, 22500]

matVtas = [
    [100, 88, 92, 94, 85, 110, 100],
    [ 30, 42, 31, 32, 38,  40,  37],
    [ 23, 35, 39, 45, 55,  60,  61],
    [ 45, 50, 56, 65, 47,  57,  68],
    [ 18, 25, 33, 21, 22,  28,  32],
]

prod, ingprod = proMayIngSem(matVtas, lstPrecios)
dia, ingmayo = diaMayorIng(matVtas, lstPrecios)

print("el producto que genera mas ingresos en la semana es:",prod, f"- vendio: ${ingprod: ,} ",)
print(f"El dia de la semana que genera mas ingresos es el: {DiaSemana(dia)} con un valor de {ingmayo}")
