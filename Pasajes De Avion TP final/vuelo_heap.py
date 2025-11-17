import heapq

class Pasajero_heap:
    """ creamos una clase pasajero compatible con heapq"""
    def __init__(self, nombre, prioridad, peso_e):
        self.nombre = nombre
        self.prioridad = prioridad 
        self.peso_e = peso_e

    def __lt__(self, other):
        """heapq usa este método para ordenar: True significa "va antes"""""
        return self.prioridad < other.prioridad
    
    def __repr__(self):

        return f"(Nombre:{self.nombre}, Prioridad:{self.prioridad}, peso: {self.peso_e})"



class Vuelo_heap:
    """creamos la clase vuelo con prioridad de pasajeros y capacidad de peso"""
    def __init__(self, codigo, origen, destino, prioridad_vuelo, peso_total):
        self.codigo = codigo
        self.origen = origen
        self.destino = destino
        """CAMBIO CLAVE: Inicializamos esto como una estructura de heap (montículo)"""
        self.lista_de_pasajeros = [] 
        self.prioridad_vuelo = prioridad_vuelo 
        self.peso_total = peso_total
        self.sum_peso = 0

    """Este método __lt__ es para comparar objetos Vuelo con otros Vuelo"""
    def __lt__(self, otros):
        return self.prioridad_vuelo < otros.prioridad_vuelo

    def agregar_pasajero_prioridad(self, pasajero):
        """Usamos heapq.heappush para añadir el pasajero
        heapq mantiene la lista 'self.lista_de_pasajeros' automáticamente ordenada
        por la prioridad definida en la clase Pasajero (usando __lt__)"""

        if self.sum_peso + pasajero.peso_e > self.peso_total:
            return f"No se pudo agregar a: {pasajero.nombre}, se excedería el limíte de peso de equipaje, Peso Actual: {self.sum_peso}, Limite: {self.peso_total}"
        else:
            heapq.heappush(self.lista_de_pasajeros, pasajero)
            self.sum_peso += pasajero.peso_e
            return f"Agregado: {pasajero.nombre} con prioridad {pasajero.prioridad} y peso: {pasajero.peso_e}, Peso Total Actual:{self.sum_peso}"
        
    def llamar_siguiente_pasajero(self):
        """Usamos heapq.heappop para sacar al pasajero con MAYOR prioridad 
        (el primero de la lista)"""
        if self.lista_de_pasajeros:
            siguiente = heapq.heappop(self.lista_de_pasajeros)
            self.sum_peso -= siguiente.peso_e
            return f"Llamando a: {siguiente.nombre}"
        else:
            return "No hay pasajeros pendientes."

    def mostrar_orden_embarque(self):
        return f"Pasajeros en cola (heap representation): {self.lista_de_pasajeros}"


#  Definimos las prioridades (1 es la más alta)
P_MOV_REDUCIDA = 2
P_MENOR_SOLO = 1
P_EMBARAZADA = 4
P_NINOS = 3
Sin_prioridad = 5

#  Creamos un vuelo de ejemplo
vuelo_madrid = Vuelo_heap("IB312", "BCN", "MAD", 5, 50)

#creamos pasajeros
pasajero1 = Pasajero_heap("Maria", P_NINOS, 15)
pasajero2 = Pasajero_heap("Ana", P_EMBARAZADA, 20)
pasajero3 = Pasajero_heap("Carlos", P_MOV_REDUCIDA, 16)
pasajero4 = Pasajero_heap("David", P_MENOR_SOLO, 9)
pasajero5 = Pasajero_heap("Elena", P_NINOS, 11)
pasajero6 = Pasajero_heap("Juan", Sin_prioridad, 6)
pasajero7 = Pasajero_heap("Sofia", Sin_prioridad, 8)

#agregamos pasajeros
print(vuelo_madrid.agregar_pasajero_prioridad(pasajero1))
print(vuelo_madrid.agregar_pasajero_prioridad(pasajero2))
print(vuelo_madrid.agregar_pasajero_prioridad(pasajero3))
print(vuelo_madrid.agregar_pasajero_prioridad(pasajero4))
print(vuelo_madrid.agregar_pasajero_prioridad(pasajero5))
print(vuelo_madrid.agregar_pasajero_prioridad(pasajero6))
print(vuelo_madrid.agregar_pasajero_prioridad(pasajero7))



print("-" * 20)

# Cuando llamas al siguiente pasajero, salen por orden de prioridad (1, 2, 3, 4, 5)
print(vuelo_madrid.llamar_siguiente_pasajero()) 
print(vuelo_madrid.llamar_siguiente_pasajero()) 
print(vuelo_madrid.llamar_siguiente_pasajero()) 
print(vuelo_madrid.llamar_siguiente_pasajero()) 
print(vuelo_madrid.llamar_siguiente_pasajero()) 
print(vuelo_madrid.llamar_siguiente_pasajero()) 
print(vuelo_madrid.llamar_siguiente_pasajero())