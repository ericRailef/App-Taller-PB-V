
class Bicicleta:

    def __init__(self, marca, tipo, numero_serie):
        self.marca = marca
        self.tipo = tipo
        self.numero_serie = numero_serie

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Numero de serie: {self.numero_serie}")

    def obtener_marca(self):
        return self.marca
    