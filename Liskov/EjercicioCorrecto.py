from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def comer(self):
        pass
    def respirar(self):
        pass

class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        pass

class AveNadadora(Ave):
    @abstractmethod
    def nadar(self):
        pass

class Aguila(AveVoladora):
    def comer(self):
        print("Aguila esta comiendo...")
    def respirar(self):
        print("Aguila esta respirando...")
    def volar(self):
        print("Aguila esta volando...")

class Paloma(AveVoladora):
    def comer(self):
        print("Paloma esta comiendo...")
    def respirar(self):
        print("Paloma esta respirando...")
    def volar(self):
        print("Paloma esta volando...")

