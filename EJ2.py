"""
Crea un programa que solicite al usuario un número entero positivo y luego imprima los números desde ese número hasta 1 utilizando un buclewhile.
"""

def main():
    Numero = int(input("Ingrese un número entero positivo: ")) 
    if Numero <= 0:
        print("Número inválido")
    else:
        while Numero >= 1:
            print(Numero)
            Numero -= 1

if __name__ == "__main__":
    main()
