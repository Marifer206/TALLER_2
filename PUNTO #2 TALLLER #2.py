import math  # Se importa el módulo "math" que contiene funciones matemáticas

n = float(input("Ingrese el número del cual quiera saber su parte entera y su parte decimal: "))  # Se pide al usuario que ingrese un número y se almacena en la variable "n" como un número de punto flotante

entero = math.trunc(n)  # Se utiliza la función "trunc()" del módulo "math" para obtener la parte entera del número "n" y se almacena en la variable "entero"
decimal = n - entero  # Se resta la parte entera del número "n" a "n" para obtener la parte decimal y se almacena en la variable "decimal"

print("La parte entera del número " + str(n) + " es " + str(entero) + " y su parte decimal es " + str(decimal))  # Se imprime en la pantalla la parte entera y la parte decimal del número "n"