from abc import ABC, abstractmethod
@abstractmethod

class Ave(ABC):
    def volar(self):
        pass
    def comer(self):
        pass
    def nadar(self):
        pass

class Aguila(Ave):
    def volar(self):
        print("Aguila volando...")
    def comer(self):
        print("Aguila comiendo...")
    def nadar(self):
        raise Exception("Las aguilas no nadan")
    
class Paloma(Ave):
    def volar(self):
        print("Paloma esta volando...")
    def comer(self):
        print("Paloma esta comiendo...")
    def nadar(self):
        print("Paloma está nadando...")

class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pinguinos no vuelan...")
    def comer(self):
        print("Pinguino está comiendo...")
    def nadar(self):
        print("Pinguino está nadando...")

a1 = Aguila()
pa1 = Paloma()
p1 = Pinguino()

a1.comer()
a1.volar()
pa1.nadar()
p1.volar()
