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

n = 10
poblacion = []
f_obj = []
fitness = []

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
    print(poblacion[i].entero(), '\t', f_obj[i], '\t', fitness[i])
print('\t\t', sum(f_obj), '\t', sum(fitness))