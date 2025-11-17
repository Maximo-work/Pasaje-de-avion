class Equipaje:
    """
    Este TAD permite registrar la información del equipaje de una persona en un avión.

    Peso: Expresado en kilogramos

    Descripción: Breve detalle del equipaje.

    """

    def __init__(self, peso, descripcion):
        self.peso = peso
        self.descripcion = descripcion


    def __str__(self):
        # TODO: Agregar f-string

        return f"{self.descripcion} {self.peso} kg."
