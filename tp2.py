# TODO:
## [HECHO] Generar una población inicial.
## Computar la función de evaluación de cada individuo.
## Repetir 200 veces (producir nueva generación en cada iteración):
#### Para cada miembro de la población (ciclo reproductivo):
###### Selección: Seleccionar dos individuos de la anterior generación para el cruce.
###### Crossover: Cruzar con cierta probabilidad los dos individuos obteniendo dos descendientes.
###### Mutación: Mutar los dos descendientes con cierta probabilidad.
###### Calcular la función evaluación de los dos descendientes mutados.
###### Insertar los dos descendientes mutados en la nueva generación.

from clases.cromosoma import Cromosoma

poblacion = []
n = 10

# Genera la población inicial
for i in range(n):
    poblacion.append(Cromosoma())
