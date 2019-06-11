# TODO:
## [HECHO] Generar una población inicial.
## [HECHO] Computar la función de evaluación de cada individuo.
## Repetir 200 veces (producir nueva generación en cada iteración):
#### Para cada miembro de la población (ciclo reproductivo):
###### Selección: Seleccionar dos individuos de la anterior generación para el cruce.
###### Crossover: Cruzar con cierta probabilidad los dos individuos obteniendo dos descendientes.
###### Mutación: Mutar los dos descendientes con cierta probabilidad.
###### Calcular la función evaluación de los dos descendientes mutados.
###### Insertar los dos descendientes mutados en la nueva generación.

from clases.cromosoma import Cromosoma
from helpers import ruleta, crossover
import random
import pdb

n = 10
poblacion = []
nueva_poblacion = []
f_obj = []
fitness = []
prob_cross = 0.5
prob_mut = 0.01

# Genera la población inicial.
for i in range(n):
    poblacion.append(Cromosoma())

# Genera los resultados de la función objetivo.
for i in range(n):
    f_obj.append(poblacion[i].f_obj())

# Genera los resultados de la función fitness.
for i in range(n):
    fitness.append(f_obj[i]/sum(f_obj))

for i in range(n):
    print(poblacion[i].binario_lindo, poblacion[i].entero(), '\t', f_obj[i], '\t', fitness[i])
print('\t\t\t\t\t\t', sum(f_obj), '\t', sum(fitness))

#for i in range(200):
resultado_ruleta = []
for j in range(n):
    resultado_ruleta.append(ruleta(fitness))
print(resultado_ruleta)

for j in range(0, 9, 2):
    crossover(nueva_poblacion, poblacion[resultado_ruleta[j]].binario, poblacion[resultado_ruleta[j+1]].binario, random.randint(1, 28), prob_cross)

#for j in range(n)
