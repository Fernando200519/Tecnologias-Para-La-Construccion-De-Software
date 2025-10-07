class Animal:
    def hablar (self):
        raise NotImplemented ("Funcion no implementada")

class Perro(Animal):
    def hablar(self): return "guau"

class Gato(Animal):
    def hablar(self): return "miau"

class Caja:
    def __init__(self):
        self._items = []
    def meter (self, x):
        self._items.append(x)
    def primero(self):
        return self._items[0]

class MedidorEnergia:
    def energia(self, a: Animal) -> float:
        return len(a.hablar() )* 1.0

    
def describir(a):
    if isinstance(a, Perro):
        return "Es un perro"
    elif isinstance (a, Gato):
        return "Es un gato"
    else:
        return "Animal"

def saludar(animal):
    print(animal.hablar())

saludar(Perro())
saludar(Gato())

c1 = Caja()
c2 = Caja()
c1.meter(Perro())
c2.meter(Gato())
print (c1.primero().hablar())
print (c2.primero().hablar())

print(describir(Perro()))
print(describir(Gato()))

m = MedidorEnergia()
e = m.energia(Perro())
x = 2
print(e + x)