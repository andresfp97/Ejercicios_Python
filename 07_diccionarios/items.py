# d_categoria= {1:25_000, 2:30_000, 3:40_000, 4:45_000,5 :60_000}
# print(d_categoria.items())

# for k, v in d_categoria.items():
#     print(k, v)


# d_categoria.pop(4)
# print(d_categoria)

# for v in d_categoria.values():
#     print(v)



productos = {
    '001': {
        'nombre': 'Laptop',
        'precio': 800,
        'stock': 10
    },
    '002': {
        'nombre': 'Teléfono',
        'precio': 500,
        'stock': 25
    },
    '003': {
        'nombre': 'Tablet',
        'precio': 300,
        'stock': 15
    }
}
    
for i in productos:
   lis = productos.keys()
   print(lis)