def ingresarDatosMat(mat):
    for f in range(len(mat)):
        print(f"Ingrese Datos de la fila {f+1}")
        for c in  range(len(mat[f])):
            mat [f][c] = int(input(f"mat[{f+1}] [{c+1}]? "))
      


def imprimirMatriz(m):
    for f in range(len(m)):
        for c in  range(len(m[f])):
             print(m[f][c], end= "\t")
        print("")


def crearMatriz(fil, col):
    m = []
    for i in range(fil):
        m.append([None]* col)
    return m

m = [[1, 2, 3],
     [4, 5, 6]]

print(m[1][1])

mat = []
mat = crearMatriz(3,5)

# mat [2][2] =  15
# imprimirMatriz(mat)

ingresarDatosMat(mat)
imprimirMatriz(mat)