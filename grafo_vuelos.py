class Grafo:
    def __init__(self):
        # El corazón del grafo: un diccionario de adyacencia
        self.estructura = {}

    def agregar_nodo(self, nodo):
        """Añade un nodo si no existe."""
        if nodo not in self.estructura:
            self.estructura[nodo] = []

    def agregar_arista(self, origen, destino):
        """
        Añade una conexión dirigida (arista) entre dos nodos.
        Se asume que ambos nodos ya existen.
        """
        if origen in self.estructura and destino not in self.estructura[origen]:
            self.estructura[origen].append(destino)

    def imprimir_grafo(self):
         """Imprime la representación del grafo."""
         for nodo, vecinos in self.estructura.items():
            print(f"Nodo {nodo}: -> {', '.join(vecinos)}")

# --- Ejemplo de Uso ---
mi_grafo = Grafo()

# 1. Agregar nodos
mi_grafo.agregar_nodo('Estación 1')
mi_grafo.agregar_nodo('Estación 2')
mi_grafo.agregar_nodo('Estación 3')
mi_grafo.agregar_nodo('Estación 4')

# 2. Agregar aristas (conexiones)
mi_grafo.agregar_arista('Estación 1', 'Estación 2')
mi_grafo.agregar_arista('Estación 2', 'Estación 3')
mi_grafo.agregar_arista('Estación 4', 'Estación 2')
mi_grafo.agregar_arista('Estación 3', 'Estación 4')

# 3. Mostrar el grafo
print("\nRepresentación del Grafo Dirigido:")
mi_grafo.imprimir_grafo()

# 1. Agregar nodos
mi_grafo.agregar_nodo('Estación 1')
mi_grafo.agregar_nodo('Estación 2')
mi_grafo.agregar_nodo('Estación 3')
mi_grafo.agregar_nodo('Estación 4')

# 2. Agregar aristas (conexiones)
mi_grafo.agregar_arista('Estación 1', 'Estación 2')
mi_grafo.agregar_arista('Estación 2', 'Estación 3')
mi_grafo.agregar_arista('Estación 4', 'Estación 2')
mi_grafo.agregar_arista('Estación 3', 'Estación 4')

# 3. Mostrar el grafo
print("\nRepresentación del Grafo Dirigido:")
mi_grafo.imprimir_grafo()

