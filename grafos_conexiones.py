import collections
class GrafoVuelos:
    def __init__(self):
        """Usamos códigos IATA como claves (nodos) y 
        listas de destinos como valores (aristas)"""
        self.rutas = {}

    def agregar_aeropuerto(self, iata_code):
        """Añade un aeropuerto (nodo) si no existe."""

        if iata_code not in self.rutas:
            self.rutas[iata_code] = []
            print(f"Aeropuerto '{iata_code}' agregado a la red.")

    def agregar_vuelo_directo(self, origen, destino, peso):
        if origen not in self.rutas:
            self.agregar_aeropuerto(origen)
        if destino not in self.rutas:
            self.agregar_aeropuerto(destino)

        if destino not in [d for d, p in self.rutas[origen]]:
            self.rutas[origen].append((destino, peso))
            print(f"Ruta directa añadida: {origen} -> {destino} (Peso: {peso})")

    def imprimir_rutas(self):
         """Imprime la representación de todas las rutas."""

         print("\n--- Red de Rutas Aéreas (Grafo Dirigido Ponderado) ---")
         for aeropuerto, destinos_con_peso in self.rutas.items():
            if destinos_con_peso:
                detalle_rutas = [f"{d}({p}h)"for d, p in destinos_con_peso]
                print(f"Desde {aeropuerto} puedes volar a: {', '.join(detalle_rutas)}")
            else:
                print(f"Aeropuerto {aeropuerto}: No hay rutas salientes directas registradas.")

         
         """IMPLEMENTACIÓN BFS"""
    def buscar_ruta_bfs(self, inicio, fin):
        """
        Encuentra la ruta más corta (menos escalas) usando BFS.
        BFS usa una cola (queue).
        """
        if inicio not in self.rutas or fin not in self.rutas:
            return f"Error: Aeropuerto de inicio o fin no existe."

        """Cola para la búsqueda: almacena el camino actual [nodo1, nodo2, ...]"""
        queue = collections.deque([[inicio]])
        """Conjunto para evitar visitar el mismo aeropuerto repetidamente"""
        visitados = set()

        while queue:
            """Sacamos el primer camino de la cola"""
            camino = queue.popleft()
            actual = camino[-1]
            if actual == fin:
                return camino

            if actual not in visitados:
                visitados.add(actual)
                for d, p in self.rutas[actual]:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(d)
                    queue.append(nuevo_camino)
        
        return f"No se encontró una ruta entre los aeropuertos especificados."
    
    """ IMPLEMENTACIÓN DFS """
    def buscar_ruta_dfs(self, inicio, fin, visitados=None, camino_actual=None):
        """
        Encuentra CUALQUIER ruta usando DFS (recursivo).
        DFS prioriza ir lo más profundo posible antes de retroceder.
        """
        if visitados is None:
            visitados = set()
        if camino_actual is None:
            camino_actual = []

        visitados.add(inicio)
        camino_actual = camino_actual + [inicio]

        """Si llegamos al destino, devolvemos el camino encontrado"""
        if inicio == fin:
            return camino_actual

        """Exploramos los vecinos (vuelos directos)"""
        for d, p in self.rutas[inicio]:
            if d not in visitados:
                """Llamada recursiva para seguir la ruta en profundidad"""
                ruta_encontrada = self.buscar_ruta_dfs(d, fin, visitados, camino_actual)
                if ruta_encontrada:
                    return ruta_encontrada
        
        """Si terminamos de explorar todos los vecinos y no llegamos al final, 
        retrocedemos (backtracking)"""
        return None

    def ordenamiento_topologico_embarque(self):
        """
        Calcula una secuencia de embarque/conexiones válida usando el algoritmo de Kahn.
        Se aplica si las rutas modelan dependencias estrictas (ej. A debe ocurrir antes que B).
        """
        grados_entrada = {nodo: 0 for nodo in self.rutas}
        for origen in self.rutas:
            for destino, peso in self.rutas[origen]:
                grados_entrada[destino] += 1
        cola_procesamiento = collections.deque([nodo for nodo in grados_entrada if grados_entrada[nodo] == 0])
        secuencia_embarque = []
        while cola_procesamiento:
            nodo_actual = cola_procesamiento.popleft()
            secuencia_embarque.append(nodo_actual)
            for vecino, peso in self.rutas.get(nodo_actual, []):
                grados_entrada[vecino] -= 1
                if grados_entrada[vecino] == 0:
                    cola_procesamiento.append(vecino)
        if len(secuencia_embarque) == len(self.rutas):
            return secuencia_embarque
        else:
            return "No se pudo realizar el ordenamiento topológico. ¡El grafo contiene un ciclo!"
    
    def dijkstra_ruta_optima(self, inicio, fin):
       """Encuentra la ruta más barata/rápida usando el algoritmo de Dijkstra.
    Requiere que las aristas tengan peso 
    (ej. self.rutas[origen] = [(destino, peso), ...]).
    """
       distancias = {nodo: float('inf') for nodo in self.rutas}
       distancias[inicio] = 0
       camino_previo = {nodo: None for nodo in self.rutas}
       cola_prioridad = [(0, inicio)]
       while cola_prioridad:
        peso_actual, nodo_actual = heapq.heappop(cola_prioridad)    
        if nodo_actual == fin:
            ruta = []
            while nodo_actual is not None:
                ruta.insert(0, nodo_actual)
                nodo_actual = camino_previo[nodo_actual]
            return ruta, distancias[fin]
        if peso_actual > distancias[nodo_actual]:
            continue
        for d, p in self.rutas.get(nodo_actual, []):
            nuevo_peso = peso_actual + p
            if nuevo_peso < distancias[d]:
                distancias[d] = nuevo_peso
                camino_previo[d] = nodo_actual
                heapq.heappush(cola_prioridad, (nuevo_peso, d))
    
        return "No se encontró una ruta óptima.", float('inf')    

# --- Ejemplo de Uso con Vuelos Reales ---
red_vuelos = GrafoVuelos()

# 1. Agregar aeropuertos importantes (nodos)
aeropuertos = ['MAD', 'BCN', 'LHR', 'CDG', 'FRA', 'AMS', 'JFK', 'DXB']
for aeropuerto in aeropuertos:
    red_vuelos.agregar_aeropuerto(aeropuerto)

# 2. Agregar rutas (aristas) basadas en conexiones comunes
red_vuelos.agregar_vuelo_directo('MAD', 'BCN', 1.5) # Madrid a Barcelona
red_vuelos.agregar_vuelo_directo('MAD', 'LHR', 2.0) # Madrid a Londres
red_vuelos.agregar_vuelo_directo('MAD', 'JFK', 8.0) # Madrid a Nueva York
red_vuelos.agregar_vuelo_directo('BCN', 'LHR', 2.1) # Barcelona a Londres
red_vuelos.agregar_vuelo_directo('BCN', 'AMS', 1.8) # Barcelona a Amsterdam
red_vuelos.agregar_vuelo_directo('LHR', 'JFK', 7.5) # Londres a Nueva York
red_vuelos.agregar_vuelo_directo('LHR', 'DXB', 7.0) # Londres a Dubai
red_vuelos.agregar_vuelo_directo('JFK', 'LHR', 7.0) # Nueva York a Londres (Vuelo de vuelta)
red_vuelos.agregar_vuelo_directo('FRA', 'DXB', 6.5) # Frankfurt a Dubai
red_vuelos.agregar_vuelo_directo('AMS', 'CDG', 1.2) # Amsterdam a Paris
red_vuelos.agregar_vuelo_directo('DXB', 'FRA', 6.0) # Dubaí a Frankfurt

red_vuelos.imprimir_rutas()

print("\n" + "="*40)
#Buscar la ruta óptima (menos escalas) de Madrid (MAD) a Dubai (DXB)
ruta_bfs = red_vuelos.buscar_ruta_bfs('MAD', 'DXB')
print(f"Ruta óptima (BFS/Menos escalas) MAD a DXB: {ruta_bfs}")

print("\n" + "="*40)
# Buscar cualquier ruta de Barcelona (BCN) a Paris (CDG)
ruta_dfs = red_vuelos.buscar_ruta_dfs('BCN', 'CDG')
print(f"Ruta DFS BCN a CDG: {ruta_dfs}")

print("\n" + "="*40)
# Intento de ruta inexistente
ruta_inexistente = red_vuelos.buscar_ruta_bfs('CDG', 'MAD')
print(f"Ruta CDG a MAD: {ruta_inexistente}")
