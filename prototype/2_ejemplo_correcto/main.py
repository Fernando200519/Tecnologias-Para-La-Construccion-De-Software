# 2_ejemplo_correcto/main.py
import time
import copy
from abc import ABC, abstractmethod

class ComponenteSistemaArchivos(ABC):
    @abstractmethod
    def clonar(self, modo='deep'):
        pass
    
    @abstractmethod
    def mostrar(self, indent=""):
        pass

class Archivo(ComponenteSistemaArchivos):
    def __init__(self, nombre):
        self.nombre = nombre

    def clonar(self, modo='deep'):
        return copy.deepcopy(self)

    def mostrar(self, indent=""):
        print(f"{indent} {self.nombre}")

class Carpeta(ComponenteSistemaArchivos):
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []
        print(f"Cargando prototipo de carpeta '{self.nombre}' desde el disco")
        time.sleep(1)

    def agregar(self, componente):
        self.hijos.append(componente)

    def clonar(self, modo='deep'):
        if modo == 'shallow':
            print(f" Clonando superficialmente '{self.nombre}'")
            return copy.copy(self)
        else:
            print(f" Clonando profundamente '{self.nombre}'")
            return copy.deepcopy(self)

    def mostrar(self, indent=""):
        print(f"{indent} {self.nombre}")
        for hijo in self.hijos:
            hijo.mostrar(indent + "  ")

if __name__ == "__main__":
    print("Creando el prototipo de 'Proyecto Web Base' \n")
    prototipo_proyecto = Carpeta("Proyecto Web Base")
    src = Carpeta("src")
    src.agregar(Archivo("app.js"))
    prototipo_proyecto.agregar(src)
    prototipo_proyecto.agregar(Archivo("index.html"))
    
    print("\nPrototipo creado. Clonación iniciada \n")

    print("Clonación Superficial")
    proyecto_malo = prototipo_proyecto.clonar(modo='shallow')
    proyecto_malo.nombre = "Proyecto Malo (Clon Superficial)"
    
    print("\nModificando 'app.js' a 'main.js' en el clon superficial")

    proyecto_malo.hijos[0].hijos[0].nombre = "main.js"

    print("\nContenido del PROTOTIPO ORIGINAL después de modificar el clon:")
    prototipo_proyecto.mostrar()
    print("\nEl prototipo original también cambió")

    print("\n\nClonación Profunda")
    proyecto_bueno = prototipo_proyecto.clonar(modo='deep')
    proyecto_bueno.nombre = "Proyecto Bueno (Clon Profundo)"

    print("\nModificando 'main.js' de vuelta a 'app.js' en el clon profundo")
    proyecto_bueno.hijos[0].hijos[0].nombre = "app.js"
    
    print("\nContenido del PROTOTIPO ORIGINAL después de modificar el clon profundo:")
    prototipo_proyecto.mostrar()
    print("\nContenido del CLON PROFUNDO:")
    proyecto_bueno.mostrar()
    print("\nEl prototipo original está intacto. El clon es independiente")