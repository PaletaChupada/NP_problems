'''
Titulo: Ciclo hamiltoniano
Descripcion: Realizar la comprobacion de que un grapo dado es un ciclo hamiltoniano o un circuito,
             dicho camino es uno donde de un grafo no dirigido para construir el camino pasamos por
             un vertice solo una vez
Autor: Espinoza Bautista Daniel
Fecha: 7 de junio del 2022
'''

# Importamos la libreria para calcular el tiempo de ejecucion y los numeros aleatorios
from time import time
import random

# Creamos la clase del grafo
class Graph():
    # Lo inicializamos con el numero de vertices dado por el usuario
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)]
        self.V = vertices

    # Revisamos si el vertice es uno adjacente al vertice anterior previamente
    # ingresado y si este no esta incluido en el camino con anterioridad
    def isSafe(self, v, pos, path):
        # Revisamos si el vertice siguiente y el ultimo del grafo son adjacentes
        if self.graph[ path[pos-1] ][v] == 0:
            return False

        # Revisamos si el vertice actual no esta en el camino generado
        for vertex in path:
            if vertex == v:
                return False

        return True

    # Realizamos una funcion recursiva que revise si el camino calculado es un ciclo
    def hamCycleUtil(self, path, pos):

        # Definimos el caso base donde todos los vertices ya estan incluidos en el camino
        if pos == self.V:
            # Comprobamos si el ultimo vertice es adjacente al primero en el camino, ya que
            # ya que esta es la restriccion para que el camino sea un ciclo
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                return True
            else:
                return False

        # Probamos con diferentes vertices para encontrar un posible camino y que este sea un ciclo
        for v in range(1,self.V):
            if self.isSafe(v, pos, path) == True:
                path[pos] = v
                if self.hamCycleUtil(path, pos+1) == True:
                    return True

		# Removemos el vertice altual si no existe una solucion
                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V

        # Nos posicionamos en el vertice 0 siento este el primer vertice del camino, si existiera
        # un ciclo entonces se iniciarioa desde cualquier punto
        path[0] = 0

        if self.hamCycleUtil(path,1) == False:
            # Si no se encontrase una solucion, siendo esta un camino o un ciclo se le notifica al
	    # usuario
            print ("La solucion no existe para este grafo\n")
            return False
	# Si no mprimimos la solucion encontrada
        self.printSolution(path)
        return True

    def printSolution(self, path):
	# Si existe la solucion se lo hacemos saber al usuario
        print ("El ciclo Hamiltoniano es:")
        for vertex in path:
            print (vertex, end = " ")
        print (path[0], "\n")

# Solicitamos el numero de nodos que tendra el grafo
nodos = int(input("Dame el numero de nodos que tendra el grafo: "))
g1 = Graph(nodos)

# Guardamos aleatoriamente el grafo
i = 0
j = 0
for i in range(nodos):
    for j in range(nodos):
        aux = random.randint(0,1)
        g1.graph[i][j] = aux

# Imprimimos el grafo creado
print("Grafo generado: ")
print(g1.graph)

# Inicializamos la variable para contar el tiempo de ejecucion
tiempo_in = time()

# Calculamos si es un ciclo hamiltoniano o no
g1.hamCycle()

# Calculamos el tiempo que tarda en ejecutarse y lo imprimimos
tiempo_fin = time() - tiempo_in
print("Tiempo de ejecucion: %.10f segundos." %tiempo_fin)

