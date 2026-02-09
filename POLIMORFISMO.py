class Ave:
    def volar(self):
        print("El ave vuela")

class Pinguino(Ave):
    def volar(self):
        print("El pingüino no vuela")

def hacer_volar(ave):
    ave.volar()

a = Ave()
p = Pinguino()

hacer_volar(a)
hacer_volar(p)
