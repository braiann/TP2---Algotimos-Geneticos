import random
import statistics
import webbrowser
import matplotlib.pyplot as plt
import pdb

def toint(n):
    """Convierte el número binario recibido en el argumento a entero. El número binario tiene que estar en forma de lista de dígitos."""
    return int(''.join(n), 2)

def ruleta(f):
    """Toma una lista "f" fitness, y devuelve un índice de un elemento de esa lista usando el método de la ruleta."""
    resultado = []
    for i in range(len(f)): # Itera sobre cada elemento del argumento.
        for j in range (int(f[i]*100)): # Se repite la cantidad de veces correspondiente al fitness,
            resultado.append(i) # agregando el índice a la lista resultado esa cantidad de veces.
    return resultado[random.randint(0, len(resultado) - 1)] # Devuelve un elemento aleatorio.

def completar_ceros(b):
    """Completa los ceros por delante de una lista argumento para que tenga 30 dígitos"""
    for i in range(30 - len(b)):
        b.insert(0, '0')
    return b

def crossover(p, a, b, x, prob):
    # """Hay una probabilidad "prob" de que se haga el crossover entre "a" y "b" en el punto "x" en la población "p""""
    h1 = []
    h2 = []
    if random.randint(0, 100) < prob*100:
        for i in range(30):
            if (i < x):
                h1.append(a[i])
                h2.append(b[i])
            else:
                h1.append(b[i])
                h2.append(a[i])
        p.append(h1)
        p.append(h2)
    else:
        p.append(a)
        p.append(b)

def mutar(cromosoma, prob):
    """Hay una probabilidad "prob" de que exista una mutación en un bit aleatorio del cromosoma"""
    if random.randint(0, 100) < prob*100:
        bit_cambiado = random.randint(0,29)
        cromosoma[bit_cambiado] = str(abs(int(cromosoma[bit_cambiado]) - 1))

def elitismo(f):
    """Devuelve el índice del cromosoma de mayor fitness de la lista f"""
    return max(f)

def mostrar_info(cromosoma_final, maximos, minimos, promedios, prob_cross, prob_mut):
    """Crea un archivo HTML que muestra la información que se pide."""
    f = open('resultados.html', 'w')

    html_inicial = """<!DOCTYPE html>
    <html>
        <head>
            <title>Trabajo Práctico N°1</title>
            <link rel="stylesheet" type="text/css" href="styles.css">
        </head>
        <body>
            <div>
                <h1>Trabajo Práctico N°1</h1>
                <h2>Algoritmos Genéticos</h2>
                <p>Rafael Verde</p>
                <p>Braian Villasanti</p>"""

    # Muestra el cromosoma máximo final.
    cromosoma_maximo = """<p><b>Cromosoma máximo: </b><div class="monoespaciado">%s</div></p>""" % cromosoma_final

    #Muestra los valores de las probabilidades
    valores = """<p><b>Probabilidad de crossover: </b>%d&#37 <b>Probabilidad de mutacion: </b>%d&#37 </p>
    <h1>Tablas de valores</h1>""" %(prob_cross*100, prob_mut*100)

    # Muestra el valor máximo, mínimo, y promedio de cada población.
    header_tabla = """
    <table>
        <tr>
            <th>Generación</th>
            <th>Máximos</th>
            <th>Mínimos</th>
            <th>Promedios</th>
        </tr>
        """

    f.write(html_inicial)
    f.write(cromosoma_maximo)
    f.write(valores)
    f.write(header_tabla)

    for i in range(200):
        tabla = """<tr>
            <td>%d</td>
            <td>%f</td>
            <td>%f</td>
            <td>%f</td>
        </tr>""" %(i + 1, maximos[i], minimos[i], promedios[i])
        f.write(tabla)

    # Muestra tablas de máximos, mínimos, y promedios para 20, 100, y 200 corridas.
    tabla2 = """</table>
    <h1>Valores para las 20, 100, y 200 corridas</h1>
    <table>
        <tr>
            <th>Generación</th>
            <th>Máximos</th>
            <th>Mínimos</th>
            <th>Promedios</th>
        </tr>
        <tr>
            <td>20</td>
            <td>%f</td>
            <td>%f</td>
            <td>%f</td>
        </tr>
        <tr>
            <td>100</td>
            <td>%f</td>
            <td>%f</td>
            <td>%f</td>
        </tr>
        <tr>
            <td>200</td>
            <td>%f</td>
            <td>%f</td>
            <td>%f</td>
        </tr>
    </table>""" % (maximos[19], minimos[19], promedios[19], maximos[99], minimos[99], promedios[99], maximos[199], minimos[199], promedios[199])

    plt.plot(range(200), maximos)
    plt.xlim(0, 200)
    plt.ylim(0, 1)
    plt.autoscale(False)
    plt.savefig('graficos/maximos.svg', bbox_inches='tight')
    plt.clf()


    plt.plot(range(200), minimos)
    plt.xlim(0, 200)
    plt.ylim(0, 1)
    plt.autoscale(False)
    plt.savefig('graficos/minimos.svg', bbox_inches='tight')
    plt.clf()

    plt.plot(range(200), promedios)
    plt.xlim(0, 200)
    plt.ylim(0, 1)
    plt.autoscale(False)
    plt.savefig('graficos/promedios.svg', bbox_inches='tight')

    html_final = """
                <h1>Máximos<h1>
                <img src="graficos/maximos.svg">
                <h1>Mínimos<h1>
                <img src="graficos/minimos.svg">
                <h1>Promedios<h1>
                <img src="graficos/promedios.svg">
            </div>
        </body>
    </html>"""

    f.write(tabla2)
    f.write(html_final)
    f.close()

    webbrowser.open_new_tab('resultados.html')
