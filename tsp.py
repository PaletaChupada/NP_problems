
# Importamos las librerias necesarias
from time import time
import math
import random

# Definimos el valor maximo como flotante
maxsize = float('inf')
  
# Function to copy temporary solution
# to the final solution
# Funcion para copiar temporalmente la solucion
# final
def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

# Funcion que encuentra el costo minimo de la arista
# que termina en el vertice i
def firstMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]
  
    return min
  
# Funcion para encontrar el segundo costo minimo
# de la arista que termina en el vertice i
def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
  
        elif(adj[i][j] <= second and 
             adj[i][j] != first):
            second = adj[i][j]
  
    return second

# Funcion que toma como argumentos:
# el limite bajo del nodo raiz
# el peso del camino actual
# el nivel actual mientras se busca en el arbol
# en donde se guardara la solucion 
# que finalmente sera copiada a la variable de camino actual
def TSPRec(adj, curr_bound, curr_weight, 
              level, curr_path, visited):
    global final_res
      
    # Caso base donde llegamos a todos los niveles de N
    # lo que significa que ya se cubrio todos los nodos una vez
    if level == N:
          
        # Revisamos si existe un vertice desde 
        # el ultimo vertice del camio hasta el primero
        if adj[curr_path[level - 1]][curr_path[0]] != 0:

            # Guardamos el peso total de la solucion 
            # o del camino solucion
            curr_res = curr_weight + adj[curr_path[level - 1]]\
                                        [curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    # Para todos los niveles de iteracion para todos los vertices
    # realizamos la construccion de un arbol de busqueda recursivo
    for i in range(N):
          
        # Cosideramos el siguiente vertice si no es el mismo
        # (entrada diagonal en la matriz de adyacencia y no visitado aun)
        if (adj[curr_path[level-1]][i] != 0 and
                            visited[i] == False):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            # Realizamos el calculo del nuevo limite inferior
            # para el nivel 2 de los otros niveles
            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) + 
                                firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
                                 firstMin(adj, i)) / 2)
  
            # Obtenemos el nuevo limite inferior partiendo del nodo
            # al que acabamos de llegar
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True

                # Llamamos a la llamada recursiva para el siguiente
                # nivel
                TSPRec(adj, curr_bound, curr_weight, 
                       level + 1, curr_path, visited)
  
            # Cortamos el nodo reseteando todos sus cambios en su
            # peso actual y en sus otros nodos ligados a el
            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
  
            # Reiniciamos el arreglo de visitados
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True
  
# Funcion para tomar el camino final
def TSP(adj):
      
    # Calculamos el limite inicial para el nodo raiz
    # para todos los vertices e inicializamos el arreglo
    # de camino actual y el arreglo de visitados
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N
  
    # Computamos el limite inicial
    for i in range(N):
        curr_bound += (firstMin(adj, i) + 
                       secondMin(adj, i))
  
    # Redondeamos el limite inferior a un entero
    curr_bound = math.ceil(curr_bound / 2)
  
    # Empezamos desde el vertice 1 para que el 
    # primer vertice del camino actual sea 0
    visited[0] = True
    curr_path[0] = 0
  
    # Llamamos a la funcion recursiva para los pesos actuales
    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)
  
# Solicitamos al usuario que digite la cantidad de nodos que tendra el grafo
N = int(input("Digite la cantidad de nodos: "))
  
# Creamos el grafo en forma de matriz con numeros random
adj = [[0 for x in range(N)] for y in range(N)]
for i in range(N):
    for j in range(N):
        if j==i:
            adj[i][j]=0
        else:
            aux = random.randint(0,50)
            adj[i][j] = aux

# Imprimos el grafo creado
print("\nGrafo generado: \n",adj)
  
# Guardamos la solucion final en una lista
final_path = [None] * (N + 1)
  
# Mantenemos la lista de los nodos ya visitados
visited = [False] * N
  
# Guardamos el peso final del camino mas corto
final_res = maxsize

# Inicializamos la variable para contar el tiempo de ejecucion
tiempo_in = time()

# Realizamos el calculo del camino mas corto
TSP(adj)

# Imprimimos el camino mas corto y la ruta  
print("\nCamino más corto:", final_res)
print("Ruta tomada: ", end = ' ')
for i in range(N + 1):
    print(final_path[i], end = ' ')

# Calculamos el tiempo que tarda en ejecutarse y lo imprimimos
tiempo_fin = time() - tiempo_in
print("\n\nTiempo de ejecucion: %.10f segundos." %tiempo_fin)