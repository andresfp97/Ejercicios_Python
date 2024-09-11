#recorrer cadena

#1 por sus elementos (caracteres)
s=  "voy volando..."
for c in s:
    print(c)

# cuantas vocales hay en la cadena
vocales = 0
for c in s:
    if c == "a" or c =="e" or \
       c =="i" or c =="o" or \
       c =="u":
        vocales +=1
print("Cantidad de vocales: ", vocales)
print("="*40)

#2.por su INDICE

for i in range(len(s)):
    print(s[i])

vocales = 0
for i in range(len(s)):
    if s[i]== "a" or s[i]=="e" or \
       s[i]=="i" or s [i]=="o" or \
       s[i]=="u":
       vocales +=1

# vereificar en que posicion aparece el primer espacio" "
for i in range(len(s)):
    if s [i] == " ":
        break
print ("El primer espacio esta en la posicion",i)