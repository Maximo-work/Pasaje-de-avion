from equipaje import Equipaje
from pasajero import Pasajero
from vuelo import Vuelo
from reserva_pasajes import Reserva_Pasajes
from vuelo_binario import ArbolBinarioVuelos
from vuelo_general import VueloGeneral
from vuelo_general import HistorialVuelos
import Pasajero_heap


#implementación:
pasajero1 = Pasajero("Juan", "123456789", "Argentina")
pasajero2 = Pasajero("Maria", "987654321", "Brasil")
pasajero3 = Pasajero("Pedro", "456789123", "Chile")

equipaje1 = Equipaje(10, "Bolso chico")
equipaje2 = Equipaje(30, "mochila")
equipaje3 = Equipaje(50, "Bolso")
equipaje4 = Equipaje(20, "Bolso grande")

pasajero1.agregar_equipaje(equipaje1)
pasajero1.agregar_equipaje(equipaje2)
pasajero2.agregar_equipaje(equipaje3)
pasajero3.agregar_equipaje(equipaje4)
#pasajero1.quitar_equipaje(equipaje2)


pasajero1.mostrar_pasajero()
print()
pasajero2.mostrar_pasajero()
print()
pasajero3.mostrar_pasajero()


  # 1. Creamos una instancia de una reserva
print("--- Creación de Reserva ---")
mi_reserva = Reserva_Pasajes("R12345", "Juan Perez", "12A", "AA202", 250.75)

print(f"Reserva inicial creada: {mi_reserva}")
print(f"Precio inicial: ${mi_reserva.precio_pasaje:.2f}")

    # 2. Actualizamos el precio del pasaje
print("\n--- Actualización de Precio ---")
    # Caso exitoso
mensaje_precio_ok = mi_reserva.actualizar_precio_pasaje(300.00)
print(mensaje_precio_ok)
print(f"Nuevo precio almacenado: ${mi_reserva.precio_pasaje:.2f}")

    # Caso fallido (precio negativo)
mensaje_precio_error = mi_reserva.actualizar_precio_pasaje(-50.00)
print(mensaje_precio_error)


    # 3. Cancelamos la reserva
print("\n--- Cancelación de Reserva ---")
mensaje_cancelacion = mi_reserva.cancelar_reserva()
print(mensaje_cancelacion)
print(f"Estado de la reserva tras cancelación: {mi_reserva.activa}")
print(f"Descripción completa: {mi_reserva}")

    # Intentar cancelar una reserva ya cancelada
mensaje_cancelacion_doble = mi_reserva.cancelar_reserva()
print(mensaje_cancelacion_doble)


arbol_vuelos = ArbolBinarioVuelos()

# Insertar varios vuelos de prueba

print("Insertando vuelos...")
arbol_vuelos.insertar(100, "2025-01-15", "Nueva York")
arbol_vuelos.insertar(50, "2025-01-16", "Miami")
arbol_vuelos.insertar(150, "2025-01-17", "Londres")
arbol_vuelos.insertar(25, "2025-01-18", "Chicago")
arbol_vuelos.insertar(75, "2025-01-19", "Los Ángeles")
arbol_vuelos.insertar(125, "2025-01-20", "París")
arbol_vuelos.insertar(175, "2025-01-21", "Tokio")

print("\n--- Recorridos del Árbol ---")
    # Inorden: debe devolver los números de vuelo ordenados de menor a mayor
print(f"Recorrido Inorden:   {arbol_vuelos.inorden()}")

    # Preorden
print(f"Recorrido Preorden:  {arbol_vuelos.preorden()}")

    # Postorden
print(f"Recorrido Postorden: {arbol_vuelos.postorden()}")

print("\n--- Búsqueda de un Vuelo ---")
    # Buscar un vuelo existente
num_vuelo_buscar = 75
vuelo_encontrado = arbol_vuelos.buscar(num_vuelo_buscar)
if vuelo_encontrado:
        print(f"Vuelo {num_vuelo_buscar} encontrado:")
        print(f"  Destino: {vuelo_encontrado.destino}")
        print(f"  Fecha:   {vuelo_encontrado.fecha}")
else:
        print(f"Vuelo {num_vuelo_buscar} no encontrado.")

    # Buscar un vuelo inexistente
num_vuelo_buscar_inexistente = 999
vuelo_inexistente = arbol_vuelos.buscar(num_vuelo_buscar_inexistente)
if not vuelo_inexistente:
        print(f"Vuelo {num_vuelo_buscar_inexistente} no encontrado.")
    
print("\n--- Manejo de Duplicados ---")
arbol_vuelos.insertar(100, "2025-01-01", "Duplicado")




# --- Invocaciones de ejemplo ---
if __name__ == "__main__":
    # 1. Crear los objetos de vuelo individuales
    vuelo_principal = VueloGeneral("AA101", "2025-10-25", "Miami", "Dallas")
    escala_dal_chi = VueloGeneral("UA202", "2025-10-25", "Dallas", "Chicago")
    escala_dal_den = VueloGeneral("SW303", "2025-10-25", "Dallas", "Denver")
    escala_chi_ny = VueloGeneral("AA404", "2025-10-26", "Chicago", "Nueva York")
    escala_den_la = VueloGeneral("UA505", "2025-10-26", "Denver", "Los Ángeles")

    # 2. Establecer la estructura del árbol (las conexiones)
    # Desde Miami a Dallas, las posibles conexiones son a Chicago o Denver
    vuelo_principal.agregar_conexion(escala_dal_chi)
    vuelo_principal.agregar_conexion(escala_dal_den)

    # Desde la escala de Chicago, hay una conexión a Nueva York
    escala_dal_chi.agregar_conexion(escala_chi_ny)

    # Desde la escala de Denver, hay una conexión a Los Ángeles
    escala_dal_den.agregar_conexion(escala_den_la)

    # 3. Inicializar el historial con el vuelo raíz
    historial = HistorialVuelos(vuelo_principal)

    print("--- Recorrido completo del historial de viaje (DFS) ---")
    # Utilizamos el método recorrer para ver la estructura completa del viaje
    for paso in historial.recorrer_historial():
        print(f"- {paso}")

    print("\n--- Búsqueda de un vuelo específico (Vuelo SW303) ---")
    # Buscamos un vuelo por su número
    num_busqueda = "SW303"
    vuelo_encontrado = historial.buscar_vuelo_general(num_busqueda)

    if vuelo_encontrado:
        print(f"¡Vuelo {num_busqueda} encontrado!")
        print(f"Detalles: {vuelo_encontrado}")
        print(f"Tiene {len(vuelo_encontrado.conexiones)} conexiones subsiguientes.")
    else:
        print(f"El vuelo {num_busqueda} no se encontró en el historial.")

    print("\n--- Búsqueda de un vuelo inexistente (Vuelo IB999) ---")
    num_inexistente = "IB999"
    vuelo_inexistente = historial.buscar_vuelo_general(num_inexistente)

    if not vuelo_inexistente:
        print(f"El vuelo {num_inexistente} no existe en este historial.")




# 1. Definimos las prioridades (1 es la más alta)
P_MOV_REDUCIDA = 2
P_MENOR_SOLO = 1
P_EMBARAZADA = 4
P_NINOS = 3

# 2. Creamos un vuelo de ejemplo
vuelo_madrid = Vuelo_heap(codigo="IB312", origen="BCN", destino="MAD", prioridad_vuelo=5)

# 3. Agregamos los pasajeros en CUALQUIER orden de llegada
vuelo_madrid.agregar_pasajero_prioridad(Pasajero_heap("Maria (Niños)", P_NINOS))
vuelo_madrid.agregar_pasajero_prioridad(Pasajero_heap("Ana (Emb.)", P_EMBARAZADA))
vuelo_madrid.agregar_pasajero_prioridad(Pasajero_heap("Carlos (Mov. Red.)", P_MOV_REDUCIDA))
vuelo_madrid.agregar_pasajero_prioridad(Pasajero_heap("David (Menor Solo)", P_MENOR_SOLO))
vuelo_madrid.agregar_pasajero_prioridad(Pasajero_heap("Elena (Niños)", P_NINOS))

print("-" * 20)

# 4. Cuando llamas al siguiente pasajero, salen por orden de prioridad (1, 2, 3, 4, 4)
print(vuelo_madrid.llamar_siguiente_pasajero()) # Sale Carlos (Prio 1)
print(vuelo_madrid.llamar_siguiente_pasajero()) # Sale David (Prio 2)
print(vuelo_madrid.llamar_siguiente_pasajero()) # Sale Ana (Prio 3)
print(vuelo_madrid.llamar_siguiente_pasajero()) # Sale Maria (Prio 4)
print(vuelo_madrid.llamar_siguiente_pasajero()) # Sale Elena (Prio 4)
print(vuelo_madrid.llamar_siguiente_pasajero()) # No hay más pasajeros
