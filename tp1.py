## TRABAJO PRÁCTICO 1
## Braian Villasanti, Rafael Verde

import random
from helpers import ruleta, completar_ceros, crossover, mutar, mostrar_info, toint, elitismo
import statistics
import argparse
import pdb

parser = argparse.ArgumentParser()
poblacion = [] # Población en números enteros
pob_bin = [] # Población en números binarios
f_obj = [] # Resultados de la función objetivo para cada cromosoma
fitness = [] # Resultados de la función fitness
prob_cross = 0.75
prob_mut = 0.05
x = []
x_minimos = []
x_promedios= []
x_maximos = []
n = 10 # Tamaño de la población

# Creación de argumentos para los comandos de cmd
parser.add_argument("-c", "--crossover", help="Cambia el valor de la probabilidad de crossover", type=int)
parser.add_argument("-m", "--mutacion", help="Cambia el valor de la probabilidad de mutación", type=int)
args = parser.parse_args()

# Verfica si se llamó a la flag y si esta cumple con los requisitos; si no cumple termina el programa
if args.crossover:
	if args.crossover <= 100 and args.crossover >= 0:
 		prob_cross = args.crossover/100
	else:
		print("! El nro de crossover tiene que ser entre 0 y 100")
		exit()

if args.mutacion:
	if args.mutacion <= 100 and args.mutacion >= 0:
		prob_mut = args.mutacion/100
	else:
		print("! El nro de mutacion tiene que ser entre 0 y 100")
		exit()

# Genera población inicial y la guarda
for i in range(n):
	cromosoma = []
	for j in range(30):
		cromosoma.append(str(random.randint(0, 1)))
	pob_bin.append(cromosoma)
	#pdb.set_trace()
	poblacion.append(toint(cromosoma))
	f_obj.append((toint(cromosoma)/((2**30) - 1))**2)
    #pdb.set_trace()
    # x = random.randint(0, (2**30) - 1)
    # poblacion.append(x) # como números decimales
    # pob_bin.append(completar_ceros((list(str(bin(x))))[2:])) # y como números binarios de 30 dígitos.
    # f_obj.append((x/(2**30 - 1))**2) # Llena la tabla de función objetivo.

#pdb.set_trace()
# Genera resultados de función fitness.
for i in range(n):
    fitness.append(f_obj[i] / sum(f_obj))

#pdb.set_trace()

# Bucle de 200 iteraciones para cada iteración del algoritmo.
for generacion in range(200):
    #pdb.set_trace()
    resultado_ruleta = [] # Lista que guarda los padres que resultarán de la selección.
    for i in range(n):
        resultado_ruleta.append(pob_bin[ruleta(fitness)])

    pdb.set_trace()

    cromosoma_elite = pob_bin[fitness.index(max(fitness))] # Buscar y guardar cromosoma elite en la función elite

    # Crossover
    for i in range(0, 9, 2):
        padre = resultado_ruleta[i]
        madre = resultado_ruleta[i + 1]
        punto_cross = random.randint(0,28)
        crossover(pob_bin, padre, madre, punto_cross, prob_cross)

    # Mutación
    for i in range(n):
        mutar(pob_bin[i], prob_mut)

    pob_bin.append(cromosoma_elite) # Agregar cromosoma elite a la población,
    pob_bin.remove(pob_bin[fitness.index(min(fitness))]) # y remover cromosoma de menor fitness.

    #pdb.set_trace()

    x_maximos.append(max(f_obj))
    x_minimos.append(min(f_obj))
    x_promedios.append(statistics.mean(f_obj))

    # Resetear todos los datos menos los de la población binaria
    poblacion = []
    f_obj = []
    fitness = []

    # Generar la nueva población en números enteros
    for i in range(n):
        poblacion.append(int(''.join(pob_bin[i]), 2))

    # Genera resultados de la función objetivo
    for i in range(n):
        f_obj.append((poblacion[i]/(2**30 - 1))**2)

    # Genera resultados de función fitness.
    for i in range(n):
        fitness.append(f_obj[i] / sum(f_obj))

# Mostrar todo en un archivo HTML
mostrar_info(''.join(max(pob_bin)), x_maximos, x_minimos, x_promedios, prob_cross, prob_mut)
