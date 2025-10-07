class A:
    def method(self):
        print("from A")

class B(A): # B hereda de A para que el MRO tenga sentido
    def method(self):
        print("from B")

class C(A): # C hereda de A para que el MRO tenga sentido
    def method(self):
        print("from C")

class D(B, C): # D hereda de B y C para demostrar el MRO
    def hello(self):
        print("from D")

d = D()

print(D.mro())
d.method()