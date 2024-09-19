#Ejercicio 7
#Andrés Araque, J1
'''
Crea un programa que solicite al usuario ingresar tres
longitudes y determine si esas longitudes pueden formar
un triángulo válido.
'''
def VerificarTriangulo(LadoA, LadoB, LadoC):
    # Verifica si las longitudes cumplen con la desigualdad triangular
    return (LadoA + LadoB > LadoC) and (LadoA + LadoC > LadoB) and (LadoB + LadoC > LadoA)

def EsNumeroValido(Valor):
    # Verifica si el valor ingresado es un número entero positivo
    return Valor.isdigit()

def Main():
    while True:  # Bucle para repetir si hay error en las entradas
        LadoA = input("Ingrese la longitud del lado A: ")
        LadoB = input("Ingrese la longitud del lado B: ")
        LadoC = input("Ingrese la longitud del lado C: ")

        # Verificamos que todos los valores ingresados sean numéricos
        if EsNumeroValido(LadoA) and EsNumeroValido(LadoB) and EsNumeroValido(LadoC):
            LadoA = int(LadoA)
            LadoB = int(LadoB)
            LadoC = int(LadoC)

            # Verificamos si los tres lados forman un triángulo válido
            if VerificarTriangulo(LadoA, LadoB, LadoC):
                print("Los lados forman un triángulo válido.")
            else:
                print("Los lados no forman un triángulo válido.")
            break  # Salir del bucle si los datos son válidos y el programa termina
        else:
            print("Por favor, ingrese longitudes numéricas válidas.")

if __name__ == "__main__":
    Main()
