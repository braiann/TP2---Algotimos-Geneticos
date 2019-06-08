import random

class Cromosoma:
    def __init__(self):
        self.binario = []
        for i in range(30): # Llena la variable binario con una lista de 30 dígitos binarios aleatorios.
            self.binario.append(str((random.randint(0,1))))
    
    def entero(self):
        """Devuelve la variable binaria convertida en entero."""
        return int("".join(self.binario), 2)
    
    def f_obj(self):
        """Devuelve el resultado de evaluar el cromosoma en la función objetivo."""
        x = self.entero()
        return (x/(2**30 - 1))**2