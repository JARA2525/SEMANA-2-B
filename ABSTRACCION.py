from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("El perro ladra")

class Gato(Animal):
    def sonido(self):
        print("El gato maulla")

p = Perro()
g = Gato()
p.sonido()
g.sonido()
