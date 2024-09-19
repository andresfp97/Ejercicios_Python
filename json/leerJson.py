import json
import pprint

with open("json/datos.json", "r") as fd:
    estructura = json.load(fd)
    
pprint.pprint(estructura)
