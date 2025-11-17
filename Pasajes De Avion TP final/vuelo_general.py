""" Arbol General para Historias de vuelo de pasajero:
Este árbol modela el historial de un pasajero, donde cada nodo es un vuelo y sus hijos son las posibles conexiones o escalas
 subsiguientes en ese viaje. No hay un límite fijo de hijos por nodo."""


class VueloGeneral:
    def __init__(self, numero_vuelo, fecha, origen, destino):
        self.numero_vuelo = numero_vuelo
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.conexiones = [] # Lista de nodos hijos (conexiones/escalas)

    def __str__(self):
        """Representación en cadena para facilitar la impresión."""
        return f"Vuelo {self.numero_vuelo} ({self.origen} -> {self.destino}) en {self.fecha}"

    def agregar_conexion(self, vuelo):
        self.conexiones.append(vuelo)

class HistorialVuelos:
    def __init__(self, vuelo_inicial):
        self.raiz = vuelo_inicial

    # Recorrido simple (similar a preorden en este contexto)
    def recorrer_historial(self):
        resultado = []
        self._recorrer_recursivo(self.raiz, resultado)
        return resultado

    def _recorrer_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(f"Vuelo {nodo.numero_vuelo} de {nodo.origen} a {nodo.destino}")
            for conexion in nodo.conexiones:
                self._recorrer_recursivo(conexion, resultado)

    # Búsqueda (DFS - Profundidad)
    def buscar_vuelo_general(self, numero_vuelo):
        return self._buscar_vuelo_recursivo_general(self.raiz, numero_vuelo)

    def _buscar_vuelo_recursivo_general(self, nodo, numero_vuelo):
        if nodo is None:
            return None
        if nodo.numero_vuelo == numero_vuelo:
            return nodo
        for conexion in nodo.conexiones:
            resultado = self._buscar_vuelo_recursivo_general(conexion, numero_vuelo)
            if resultado:
                return resultado
        return None
