

from persona import Persona
from bicicleta import Bicicleta

class Cliente(Persona):

    def __init__(self, nombre, rut, telefono, direccion):
        super().__init__(nombre, rut, telefono)

        self.direccion = direccion
        self.bicicletas = []

    def agregar_bicicleta(self, bicicleta: Bicicleta)-> None:
        self.bicicletas.append(bicicleta)
        print(f"Bicicleta registrada correctamente")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Direccion: {self.direccion}")

    def contar_bicicletas(self):
        return len(self.bicicletas)