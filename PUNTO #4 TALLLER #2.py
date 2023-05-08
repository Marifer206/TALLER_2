import math  # Se importa el módulo "math" que contiene funciones matemáticas

def aproximacion_coseno(x, n):  # Se define una función llamada "aproximacion_coseno" que toma dos argumentos: "x" y "n"
    aproximacion = 0  # Se inicializa la variable "aproximacion" en cero
    for i in range(n):  # Se utiliza un bucle "for" para iterar "n" veces
        termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)  # Se calcula el "i"-ésimo término de la serie de Taylor para el coseno y se almacena en la variable "termino"
        aproximacion += termino  # Se suma el "i"-ésimo término a la variable "aproximacion"
    return aproximacion  # Se devuelve la aproximación del coseno de "x" utilizando "n" términos de la serie de Taylor

x = float(input("Ingrese el valor de x: "))  # Se pide al usuario que ingrese el valor de "x" y se almacena en la variable "x" como un número de punto flotante

errores_deseados = [0.001, 0.1, 1, 10]  # Se define una lista de errores deseados

for error in errores_deseados:  # Se utiliza un bucle "for" para iterar sobre los errores deseados
    e = 0  # Se inicializa la variable "e" en cero
    while True:  # Se utiliza un bucle "while" infinito
        e += 1  # Se incrementa la variable "e" en uno en cada iteración
        aproximacion = aproximacion_coseno(x, e)  # Se llama a la función "aproximacion_coseno" con "x" y "e" como argumentos y se almacena el resultado en la variable "aproximacion"
        error_porcentual = abs((aproximacion - math.cos(x)) / math.cos(x)) * 100  # Se calcula el error porcentual entre la aproximación y el valor real del coseno de "x" y se almacena en la variable "error_porcentual"
        if error_porcentual <= error:  # Se utiliza una condición "if" para verificar si el error porcentual es menor o igual al error deseado
            break  # Si el error porcentual es menor o igual al error deseado, se sale del bucle "while"
    print("Aproximación: " + str(aproximacion))  # Se imprime en la pantalla la aproximación del coseno de "x" utilizando "e" términos de la serie de Taylor
    print("Valor real: " + str(math.cos(x)))  # Se imprime en la pantalla el valor real del coseno de "x"
    print("Con un error del " + str(error) + "% se necesitan " + str(e) + " términos de la serie")  # Se imprime en la pantalla el error deseado, el número de términos de la serie necesarios para alcanzar el error deseado y un mensaje indicando que se ha alcanzado el error deseado
    print("")  # Se imprime una línea en blanco para separar las salidas de cada iteración del bucle "for"