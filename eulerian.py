'''
Titulo: Ciclos eulerianos
Descripcion: Este programa realiza el calculo de un ciclo o camino euleriano a partir de
	         un grafo dado, en este tipo de ciclos o caminos para construirlos solo se
             debe visitar cada arista exactamente una vez
Autor: Espinoza Bautista Daniel
Fecha: 7 de Junio del 2022
'''
# Importamos las librerias
import random
from time import time

def printCircuit(adj):
  
    # El arreglo adj representa la lista de adyacencia
    # del grafo y edge_count es el numero de aristas
    # energebtes de cada uno de los vertices
    edge_count = dict()
  
    for i in range(len(adj)):
  
        # Encontramos la cuenta de los vertices para
        # tenelos identicados y usar los que aun no
        # se pasa por ahi
        edge_count[i] = len(adj[i])
  
    if len(adj) == 0:
        return # Si no se encuentra regresamos un grafo vacio
  
    # Inicializamos la variable para el camino
    curr_path = []
  
    # Inicializamos el vector a guardar el circuito
    circuit = []
  
    # Empezamos por un vertice cualquiera y lo guardamos
    curr_path.append(0)
    curr_v = 0 
  
    while len(curr_path):
  
        # Si aun hay aristas
        if edge_count[curr_v]:
  
            # Obtenemos el vertice
            curr_path.append(curr_v)
  
            # Encontramos el siguiente nodo usando una arista
            next_v = adj[curr_v][-1]
  
            # Removemos la arista
            edge_count[curr_v] -= 1
            adj[curr_v].pop()
  
            # Nos movemos al siguiente vertice
            curr_v = next_v
  
        # Encontramos el circuito con busqueda en profundidad
        else:
            circuit.append(curr_v)
  
            # Busqueda DFS
            curr_v = curr_path[-1]
            curr_path.pop()
  
    # Lo mandamos a imprimir
    for i in range(len(circuit) - 1, -1, -1):
        print(circuit[i], end = "")
        if i:
            print(" -> ", end = "")
  
# Solicitamos al usuario que digite el numero de nodos
nodos = int(input("Dame el numero de nodos del grafo: "))

# Solicitamos al usuario que digite el numero de vertices
vertices = int(input("Dame el numero de vertices del grafo: "))

# Creamos el grafo a partir de los nodos
adj1 = [0] * nodos
for i in range(nodos):
    adj1[i] = []

# inicializamos el grafo
adj1[0].append(1)

# Realizamos el llenado de manera aleatoria
for i in range(vertices-1):
    aux1 = random.randint(0,nodos-1)
    aux2 = random.randint(0,nodos-1)
    if aux1 == aux2:
        aux2 += 1
        adj1[aux1].append(aux2)
    else:
        adj1[aux1].append(aux2)

# Inicializamos la variable para contar el tiempo de ejecucion
tiempo_in = time()

# Imprimimos el circuito de Euler
print("\nEl circuito de Euler es: ")
printCircuit(adj1)

# Calculamos el tiempo que tarda en ejecutarse y lo imprimimos
tiempo_fin = time() - tiempo_in
print("\n\nTiempo de ejecucion: %.10f segundos." %tiempo_fin)