
s = " aver que borra esta vaina"
# elimina todos los caracteres en blanco al principio de la cadena.
print(f"{s.lstrip()}")
# elimina todos los caracteres en blanco al final de la cadena.
print(f"{s.rstrip()}")
# elimina todos los caracteres en blanco al inico y al final de la cadena.
print(f"{s.strip()}")
# elimina  todos los caracteres en blanco y ademas el caracter especifico
print('{}'.format(s.strip('a')))