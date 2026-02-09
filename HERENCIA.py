class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola, soy", self.nombre)

class Estudiante(Persona):
    def estudiar(self):
        print(self.nombre, "está estudiando")

e = Estudiante("Juan")
e.saludar()
e.estudiar()
