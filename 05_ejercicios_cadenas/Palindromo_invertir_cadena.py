def es_palindromo(palabra):
    
    # Convertir a minúsculas para evitar problemas de mayúsculas/minúsculas
    palabra = palabra.lower()
    
    # slicing ---> palabra[inicio:fin:paso]  el paso va en -1 para que el
    # entienda que se va leer de atras hacia delante 
    palabra_inversa = palabra[::-1]
    return palabra == palabra_inversa


palabra = input("Introduce una palabra: ")

if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")
