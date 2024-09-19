#Ejercicio 4
#Andrés Araque, J1
'''
Crea un programa que solicite al usuario ingresar una contraseña y verifique si cumple con los siguientes requisitos: debe tener al menos 8 caracteres y contener al menos un número.
Si la contraseña cumple con los requisitos, muestra el mensaje"Contraseña válida". De lo contrario, muestra el mensaje "Contraseña inválida".
'''
def SolicitarContrasena():
    return input("Ingrese una contraseña: ")

def VerificarContrasena(Contrasena):
    TieneNumero = any(char.isdigit() for char in Contrasena)
    LongitudValida = len(Contrasena) >= 8
    
    if TieneNumero and LongitudValida:
        return True
    return False

def Main():
    Contrasena = SolicitarContrasena()
    if VerificarContrasena(Contrasena):
        print("Contraseña válida")
    else:
        print("Contraseña inválida")

if __name__ == "__main__":
    Main()
