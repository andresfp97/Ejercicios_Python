import json
from re import M

# lista= ["Daniel", "Maria", "Ada", "Julian",["Gabriel", "Ricardo"]]


campers = {
    1:{

        "nombre": "Daniel",
        "edad": 21,
        "sexo": "m",
        "telefonos": [123,456]
    },
    2:{

        "nombre": "Maria",
        "edad": 20,
        "sexo": "f",
        "telefonos": [789]
    }

}

with open("json/datos.json", "w") as fd:
    json.dump(campers,fd)

if not fd.closed:
    fd.close()


  