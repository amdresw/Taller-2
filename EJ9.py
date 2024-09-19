#Ejercicio 9
#Andrés Araque
'''
Crea un programa que solicite al usuario ingresar una serie de números positivos y luego calcule e imprima el promedio de los números ingresados utilizando un bucle while.
El programa debe terminar cuando el usuario ingrese un número negativo.
'''
def CalcularPromedio(Suma, Cantidad):
    # Calcula el promedio de los números ingresados
    if Cantidad == 0:
        return 0  # Para evitar división por cero si no se ingresan números válidos
    return Suma / Cantidad

def Main():
    Suma = 0
    Cantidad = 0

    while True:
        Numero = input("Ingrese un número positivo (o un número negativo para terminar): ")
        
        if Numero.isdigit():  # Verifica que la entrada sea un número positivo
            Numero = int(Numero)
            
            if Numero < 0:
                break  # Termina el bucle si el número es negativo
            
            Suma += Numero
            Cantidad += 1
        else:
            print("Entrada inválida: Por favor ingrese un número positivo.")
    
    Promedio = CalcularPromedio(Suma, Cantidad)
    
    if Cantidad > 0:
        print(f"El promedio de los números ingresados es: {Promedio}")
    else:
        print("No se ingresaron números positivos.")

if __name__ == "__main__":
    Main()
