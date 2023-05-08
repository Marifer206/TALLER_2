numeros = []  # Se define una lista vacía llamada "numeros"
def separar_numero(x):  # Se define una función llamada "separar_numero" que toma un número entero "x" como argumento
    while x > 0:  # Se utiliza un bucle "while" para iterar mientras "x" sea mayor que cero
        numeros.append(x%10)  # Se utiliza el operador módulo "%" para obtener el último dígito de "x" y se agrega a la lista "numeros" utilizando el método "append()"
        x = x // 10  # Se utiliza el operador de división entera "//" para eliminar el último dígito de "x"
    numeros.reverse()  # Se invierte el orden de los elementos en la lista "numeros" utilizando el método "reverse()"
    print(numeros)  # Se imprime la lista "numeros" que contiene los dígitos individuales del número entero original

n = int(input("Ingrese el numero entero el cual quiera separar: "))  # Se pide al usuario que ingrese un número entero y se almacena en la variable "n"
separar_numero(n)  # Se llama a la función "separar_numero" con el número ingresado como argumento