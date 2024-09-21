import json
from pathlib import Path

def guardar(lib, arch):
    with open(arch,"w") as fd:
        json.dump(lib, fd)

        if not fd.close:
            fd.close()
    
def cargar(arch):
    archivo = Path(arch)
    lib = {}
    if archivo.is_file():
        try:
            with open(arch, "r")as fd:
                lib = json.load(fd)
            if not fd.closed:
                fd.close()
        except Exception as e:
            print(">>> error al abrir el archivo. \n",e)
        
    else:
        print(">>> error.el archivo no existe")
        input(">>> Presione cualquier tecla para continuar...")
    
    return lib



