class Reserva_Pasajes:
    def __init__(self, numero_reserva, pasajero, asiento, vuelo, precio_pasaje):
      self.numero_reserva = numero_reserva
      self.pasajero = pasajero
      self.asiento = asiento
      self.vuelo = vuelo
      self.precio_pasaje = precio_pasaje
      self.activa = True

    def agregar_reserva(self):
        if self.numero_reserva in self.numero_reserva:
          return "El numero de reserva ya existe"
        else:
          self.numero_reserva.append(self.numero_reserva)
          return self.numero_reserva

    def cancelar_reserva(self):
        if self.activa:
          self.activa = False
          return "La reserva ha sido cancelada"
        else:
          return "La reserva ya está cancelada"


    def actualizar_precio_pasaje(self, nuevo_precio):
        if self.precio_pasaje < 0:
          return "El precio del pasaje no puede ser negativo"
        else:
          self.precio_pasaje = nuevo_precio
          return nuevo_precio

    def __str__(self):
        """Representación legible del objeto."""
        estado = "Activa" if self.activa else "Cancelada"
        return f"Reserva {self.numero_reserva} | Pasajero: {self.pasajero} | Vuelo: {self.vuelo} | Estado: {estado}"



   