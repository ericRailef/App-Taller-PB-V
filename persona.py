

#CLASE Persona

class Persona:
    
    def __init__(self, nombre , rut, telefono):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"RUT: {self.rut}")
        print(f"Teléfono: {self.telefono}")


    def obtener_nombre(self):
        return self.nombre
        