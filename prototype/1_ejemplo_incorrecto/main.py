import time

class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"
    
class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

        print(f"Cargando contenido de la carpeta '{self.nombre}' desde el disco")
        time.sleep(1)
    
    def agregar(self, componente):
        self.hijos.append(componente)
    
    def mostrar_contenido(self, indent=""):
        print(f"{indent} {self.nombre}")
        for hijo in self.hijos:
            if isinstance(hijo, Carpeta):
                hijo.mostrar_contenido(indent + " ")
            else:
                print(f"{indent} {hijo}")

    
if __name__ == "__main__":
    print("Creando 2 estructuras de proyecto \n")
    start_time = time.time()

    proyecto_alpha = Carpeta("Proyecto Alpha")
    src = Carpeta("src")
    src.agregar(Archivo("main.js"))
    src.agregar(Archivo("styles.css"))
    proyecto_alpha.agregar(src)
    proyecto_alpha.agregar(Archivo("index.html"))

    proyecto_beta = Carpeta("Proyecto Beta")
    src_beta = Carpeta("src")
    src_beta.agregar(Archivo("main.js"))
    src_beta.agregar(Archivo("styles.css"))
    proyecto_beta.agregar(src_beta)
    proyecto_beta.agregar(Archivo("index.html"))

    end_time = time.time()

    print(f"\n Creacion finalizada en {end_time - start_time:.2f} segundos\n")
    print("Estructura del proyecto alpha: ")
    proyecto_alpha.mostrar_contenido()

    print("\n Estructura del proyecto beta: ")
    proyecto_beta.mostrar_contenido()