from cliente import Cliente
from mecanico import Mecanico

class Taller:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.mecanicos = []
        self.clientes = []

    def contratar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico) 
        print("Mecanico registrado en el taller.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente registrado en el taller")

    def mostrar_mecanicos(self):
        print(F"\n Mecanicos del taller {self.nombre}")
        for mecanico in self.mecanicos:
            mecanico.mostrar_informacion()
            print("-----------------------")

    def contar_clientes(self):
        return len(self.clientes)
        


