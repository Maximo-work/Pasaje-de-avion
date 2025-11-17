class Pasajero:
  def __init__(self, nombre, documento, nacionalidad):
    self.nombre = nombre
    self.documento = documento
    self.nacionalidad = nacionalidad
    self.historial_de_vuelo = []
    self.equipajes = []
    self.equipajes_peso = 0

  def mostrar_pasajero(self):
    print(f"Nombre: {self.nombre}")
    print(f"Documento: {self.documento}")
    print(f"Nacionalidad: {self.nacionalidad}")
    print(f"Equipajes: Peso Total: {self.equipajes_peso} Kg")
    for e in self.equipajes:
      print(e)

  def agregar_vuelo(self, vuelo):
    """
     Permite agregar un vuelo al pasajero.
    """

    self.historial_de_vuelo.append(vuelo)
    

  def agregar_equipaje(self, equipaje):
      """
       Permite agregar un equipaje al pasajero.
      """
      
      self.equipajes.append(equipaje)
      self.equipajes_peso += equipaje.peso
      

  def quitar_equipaje(self, equipaje):
     self.equipajes.remove(equipaje)
     self.equipajes_peso -= equipaje.peso
     
