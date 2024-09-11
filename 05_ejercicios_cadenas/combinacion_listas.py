countries = ["USA", "Canada", "UK", "Australia"]
cities = ["Washington", "Ottawa", "London", "Canberra"]


# zip(countries, cities--> ) toma dos o más iterables como argumentos y 
# devuelve un iterador de tuplas. Cada tupla contiene elementos de los iterables,
# emparejados por posición.

for x, y in zip(countries, cities):
    print(f"La capital de {x} is {y}.")