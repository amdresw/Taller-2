#Ejercicio 10
#Andrés Araque
'''
Construya un algoritmo en Python, que permita ingresar la información de un empleado e imprima el nombre, los apellidos y la antigüedad. Los datos que se deben solicitarson los siguientes:
*Nombre* Teléfono
*Año de ingreso a la empresa*Apellidos
*Edad.
'''
from datetime import datetime

def CalcularAntiguedad(AnoIngreso):
    # Obtiene el año actual
    AnoActual = datetime.now().year
    # Calcula la antigüedad
    return AnoActual - AnoIngreso

def ObtenerInformacionEmpleado():
    # Solicita la información del empleado
    Nombre = input("Ingrese el nombre del empleado: ")
    Apellidos = input("Ingrese los apellidos del empleado: ")
    AnoIngreso = input("Ingrese el año de ingreso a la empresa: ")
    Telefono = input("Ingrese el teléfono del empleado: ")
    Edad = input("Ingrese la edad del empleado: ")

    # Verifica que el año de ingreso sea un número entero
    if not AnoIngreso.isdigit():
        print("Año de ingreso inválido. Debe ser un número entero.")
        return None

    # Convierte el año de ingreso a entero
    AnoIngreso = int(AnoIngreso)

    # Crea un diccionario con la información del empleado
    Empleado = {
        "Nombre": Nombre,
        "Apellidos": Apellidos,
        "AnoIngreso": AnoIngreso
    }

    return Empleado

def Main():
    # Obtiene la información del empleado
    Empleado = ObtenerInformacionEmpleado()
    
    if Empleado:
        # Calcula la antigüedad
        Antiguedad = CalcularAntiguedad(Empleado["AnoIngreso"])

        # Imprime la información del empleado
        print("\nInformación del Empleado:")
        print(f"Nombre: {Empleado['Nombre']}")
        print(f"Apellidos: {Empleado['Apellidos']}")
        print(f"Antigüedad en la empresa: {Antiguedad} años")

if __name__ == "__main__":
    Main()
