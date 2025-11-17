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

    def agregar_vuelo_directo(self, origen, destino):
        """
        Añade un vuelo directo (arista dirigida) entre dos aeropuertos.
        Asume que los aeropuertos ya existen en la red.
        """
        """Asegurarse de que ambos aeropuertos están en la red"""

        if origen not in self.rutas:
            self.agregar_aeropuerto(origen)
        if destino not in self.rutas:
            self.agregar_aeropuerto(destino)

        if destino not in self.rutas[origen]:
            self.rutas[origen].append(destino)
            print(f"Ruta directa añadida: {origen} -> {destino}")

    def imprimir_rutas(self):
         """Imprime la representación de todas las rutas."""

         print("\n--- Red de Rutas Aéreas (Grafo Dirigido) ---")
         for aeropuerto, destinos in self.rutas.items():
            if destinos:
                print(f"Desde {aeropuerto} puedes volar a: {', '.join(destinos)}")
            else:
                print(f"Aeropuerto {aeropuerto}: No hay rutas salientes directas registradas.")

# --- Ejemplo de Uso con Vuelos Reales ---
red_vuelos = GrafoVuelos()

# 1. Agregar aeropuertos importantes (nodos)
aeropuertos = ['MAD', 'BCN', 'LHR', 'CDG', 'FRA', 'AMS', 'JFK', 'DXB']
for aeropuerto in aeropuertos:
    red_vuelos.agregar_aeropuerto(aeropuerto)

# 2. Agregar rutas (aristas) basadas en conexiones comunes
red_vuelos.agregar_vuelo_directo('MAD', 'BCN') # Madrid a Barcelona
red_vuelos.agregar_vuelo_directo('MAD', 'LHR') # Madrid a Londres
red_vuelos.agregar_vuelo_directo('MAD', 'JFK') # Madrid a Nueva York
red_vuelos.agregar_vuelo_directo('BCN', 'LHR') # Barcelona a Londres
red_vuelos.agregar_vuelo_directo('BCN', 'AMS') # Barcelona a Amsterdam
red_vuelos.agregar_vuelo_directo('LHR', 'JFK') # Londres a Nueva York
red_vuelos.agregar_vuelo_directo('LHR', 'DXB') # Londres a Dubai
red_vuelos.agregar_vuelo_directo('JFK', 'LHR') # Nueva York a Londres (Vuelo de vuelta)
red_vuelos.agregar_vuelo_directo('FRA', 'DXB') # Frankfurt a Dubai
red_vuelos.agregar_vuelo_directo('AMS', 'CDG') # Amsterdam a Paris