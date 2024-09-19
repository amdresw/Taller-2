#Ejercicio 8
#Andrés Araque, grupo J1
'''
Escribe un programa que solicite al usuario
ingresar un número y luego muestre la tabla
de multiplicar de ese número del 1 al 10
'''
def MostrarTablaDeMultiplicar(Numeros):
    # Muestra la tabla de multiplicar para el número dado
    for i in range(1, 11):
        Resultado = Numeros * i
        print(f"{Numeros} x {i} = {Resultado}")

def ObtenerNumero():
    # Solicita al usuario ingresar un número y verifica que sea un valor numérico válido
    Numero = input("Ingrese un número: ")
    
    if Numero.isdigit():
        return int(Numero)
    else:
        print("Entrada inválida: Por favor ingrese un valor numérico.")
        return None

def Main():
    Numero = ObtenerNumero()
    
    if Numero is not None:
        MostrarTablaDeMultiplicar(Numero)

if __name__ == "__main__":
    Main()
