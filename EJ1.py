#Ejercicio 1
#Andrés Araque, J1
"""
Escribe un programa que solicite al usuario ingresar su edad y luego determine si es mayor de edad o no utilizando una declaración if.
Si la edad es mayor o igual a 18, muestra el mensaje "Eres mayor de edad", de lo contrario, muestra el mensaje "Eres menor de edad"
"""

def ObtenerEdad():
    while True:
        Edad = int(input("Ingrese su edad: "))
        if Edad <= 0 :
            print("Edad invalida")
        else:
            return Edad
        
def ClasificarEdad (Edad):
    if Edad >= 18:
        return "Usted es mayor de edad"
    else:
        return "Usted es menor de edad"
    
def main():
    Edad = ObtenerEdad()
    Resultado= ClasificarEdad (Edad)
    print(Resultado)

if __name__ == "_main_":
    main()