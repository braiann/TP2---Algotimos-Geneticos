import random

class Cromosoma:
    def __init__(self):
        self.binario = []
        for i in range(30): # Llena la variable binario con una lista de 30 dígitos binarios aleatorios.
            self.binario.append(str((random.randint(0,1))))
        self.entero = int("".join(self.binario), 2) # Guarda la variable binaria también en entero.