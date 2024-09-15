def diaMayorIng(mat, lst):
    lsting = []
    for f in range(len(mat[0])):  
        suma = 0
        for c in range(len(mat)):
            suma += mat[c][f] * lst[c]  
        lsting.append(suma)  
    return lsting

def proMayIngSem(mat, lst):
    lsting = []
    for f in range(len(mat)):
        suma = 0
        for c in range(len(mat[f])):
            suma += mat[f][c] * lst[f]
        lsting.append(suma)
        #lsting2.append(sum(mat[f] * lst [f]))    
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

#prod, ingprod = proMayIngSem(matVtas, lstPrecios)
#print("el producto que genera mas ingresos en la semana es:",prod, f"- vendio: ${ingprod: ,} ",)

lista = diaMayorIng(matVtas, lstPrecios)
mayor = max(lista)
dia = lista.index(mayor)+1

print(f"el dia de la semana que genera mas ingresos es{dia}",)



