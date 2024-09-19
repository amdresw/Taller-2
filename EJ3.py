#Ejercicio 3
#Andrés Araque, J1
"""""
Escribe un programa que solicite al usuario ingresar su calificación en un examen y determine si ha aprobado o no. 
Si la calificación es igual o mayor a 60, muestra el mensaje "Has aprobado". 
De lo contrario, muestra el mensaje "Has reprobado".
"""""

def obtener_calificacion():
    while True:
    
        calificacion = int(input("Ingrese una calificación: "))
        if calificacion < 0 or calificacion > 100:
                print("Invalida")
        else:
            return calificacion

def evaluar_calificacion(calificacion):
    if 60 <= calificacion <= 100:
        return "Aprobado"
    else:
        return "Desaprobado"

def main():
    calificacion = obtener_calificacion()
    resultado = evaluar_calificacion(calificacion)
    print(resultado)

if __name__ == "_main_":
    main()