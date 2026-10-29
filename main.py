
# Developer: Eric Railef
# Curso: Programación Backend

# GIT: https://github.com/ericRailef/App-Taller-PB-V.git

# archivo main
from cliente import Cliente
from mecanico import Mecanico
from bicicleta import Bicicleta
from taller import Taller

def main():

    #Instanciar un objeto Taller
    taller = Taller("BikeMantencion", "Avenida San Carlos 123") 

    # Crear cliente 
    
    cliente_uno = Cliente("Juan Perez", "10925129-4", "+569936987", "Av Concha y Toro 456")

    #Crear Bicicleta

    bicicleta_uno = Bicicleta("Trek", "Mountain", "BIC1234")

    #Asociar bicicleta al cliente y registrar el cliente

    cliente_uno.agregar_bicicleta(bicicleta_uno)
    taller.registrar_cliente(cliente_uno)

    #Crear y registrar un mecanico
    mecanico_uno = Mecanico("Pedro Gonzalez","9856154-9", "+569987264", "Bicicleta de velocidad", 1000000)

    taller.contratar_mecanico(mecanico_uno)

    #Mostrar Informacion

    print("\n ---BICICLETA---")
    bicicleta_uno.mostrar_informacion()

    print("\n ---Mecanicos del taller---")
    taller.mostrar_mecanicos()

    print(f"Total de clientes del taller: {taller.contar_clientes()}")

    #Ejecutar metodo que retorna un String

    print(mecanico_uno.reparar_bicicleta(bicicleta_uno))  
    
    
    
    
    
    
if __name__ == "__main__":
    main()
