#Ejercicio 4
#Andrés Araque, J1
'''
Crea un programa que pida al usuario ingresar el nombre de un país y luego determine en qué continente se encuentra.Utiliza estructuras condicionales 
para asociar cada país con su respectivo continente y muestra un mensaje con el continente correspondiente.
'''
def DeterminarContinente(pais):
    match pais:
        case "Argentina":
            return "América del Sur"
        case "Canadá":
            return "América del Norte"
        case "Alemania":
            return "Europa"
        case "Australia":
            return "Oceanía"
        case "Egipto":
            return "África"
        case "Japón":
            return "Asia"
        case "Antártida":
            return "Antártida"
        case _:
            return "País no reconocido"

if __name__ == "_main_":
    # Mostrar las opciones disponibles
    print("Opciones de países disponibles:")
    print("- Argentina")
    print("- Canadá")
    print("- Alemania")
    print("- Australia")
    print("- Egipto")
    print("- Japón")
    print("- Antártida")

    # Solicitar al usuario que ingrese el nombre de un país
    pais = input("Ingresa el nombre de un país: ")

    # Determinar el continente
    continente = DeterminarContinente(pais)

    # Mostrar el resultado
    print(f"{pais} se encuentra en {continente}.")