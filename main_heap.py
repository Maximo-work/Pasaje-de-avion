from vuelo_heap import Pasajero_heap, Vuelo_heap


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


