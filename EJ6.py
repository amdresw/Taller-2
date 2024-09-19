#Ejercicio 6
#Andrés Araque
'''

'''
def EsBisiesto(Anio):
    # Verifica si un año es bisiesto (Ejercicio 8 taller previo)
    return (Anio % 4 == 0 and Anio % 100 != 0) or (Anio % 400 == 0)

def ObtenerDiasDelMes(Mes, Anio):
    # Verifica el número de días para cada mes
    if Mes == 1 or Mes == 3 or Mes == 5 or Mes == 7 or Mes == 8 or Mes == 10 or Mes == 12:
        return 31
    elif Mes == 4 or Mes == 6 or Mes == 9 or Mes == 11:
        return 30
    elif Mes == 2:
        if EsBisiesto(Anio):
            return 29
        else:
            return 28
    else:
        return -1  # Mes inválido

def VerificarFechaValida(Dia, Mes, Anio):
    # Obtenemos los días del mes y verificamos si el día es válido
    DiasDelMes = ObtenerDiasDelMes(Mes, Anio)
    if DiasDelMes == -1:
        return False
    return 1 <= Dia <= DiasDelMes

def Main():
    while True:  # Bucle para volver a solicitar datos si hay un error
        Dia = input("Ingrese el día: ")
        Mes = input("Ingrese el mes: ")
        Anio = input("Ingrese el año: ")

        if Dia.isdigit() and Mes.isdigit() and Anio.isdigit():
            Dia = int(Dia)
            Mes = int(Mes)
            Anio = int(Anio)

            if VerificarFechaValida(Dia, Mes, Anio):
                print("Fecha válida")
                break
            else:
                print("Fecha inválida. Inténtelo de nuevo.")
        else:
            print("Entrada inválida: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    Main()
