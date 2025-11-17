class Vuelo:
  def __init__(self, codigo, origen, destino):
    self.codigo = codigo
    self.origen = origen
    self.destino = destino
    self.lista_de_pasajeros = []
    


  def agregar_pasajero(self, pasajero,reserva):
     if self.pasajero in self.lista_de_pasajeros:
        return f"el pasajero ya se encuetra"
     elif self.codigo != reserva.vuelo_asociado:
       return f"el vuelo no coincide"
     else:
        self.lista_de_pasajeros.append(pasajero)
        

  def quitar_pasajero(self, pasajero):
     if self.pasajero in self.lista_de_pasajeros:
      self.lista_de_pasajeros.remove(pasajero)


  def mostrar_vuelo(self):
      return f"Codigo: {self.codigo}, Origen: {self.origen}, Destino: {self.destino}"


