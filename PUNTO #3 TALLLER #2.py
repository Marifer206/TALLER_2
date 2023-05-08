def invertir_numero(numero):  # Se define una función llamada "invertir_numero" que toma un número entero "numero" como argumento
    numero_invertido = 0  # Se inicializa la variable "numero_invertido" en cero
    while numero > 0:  # Se utiliza un bucle "while" para iterar mientras "numero" sea mayor que cero
        digito = numero % 10  # Se utiliza el operador módulo "%" para obtener el último dígito de "numero" y se almacena en la variable "digito"
        numero_invertido = (numero_invertido * 10) + digito  # Se multiplica "numero_invertido" por 10 y se le suma "digito" para invertir el orden de los dígitos de "numero" y se almacena en la variable "numero_invertido"
        numero //= 10  # Se utiliza el operador de división entera "//" para eliminar el último dígito de "numero"
    return numero_invertido  # Se devuelve el número invertido

n = int(input("Ingrese el primer número: "))  # Se pide al usuario que ingrese el primer número y se almacena en la variable "n" como un número entero
m = int(input("Ingrese el segundo número: "))  # Se pide al usuario que ingrese el segundo número y se almacena en la variable "m" como un número entero

n_invertido = invertir_numero(n)  # Se llama a la función "invertir_numero" con el número "n" como argumento y se almacena el resultado en la variable "n_invertido"

if n_invertido == m:  # Se utiliza una condición "if" para verificar si el número invertido "n_invertido" es igual al número "m"
    print("Los números", n, "y", m, "son espejos.")  # Si los números son espejos, se imprime en la pantalla un mensaje indicando que los números son espejos
else:
    print("Los números", n, "y", m, "no son espejos.")  # Si los números no son espejos, se imprime en la pantalla un mensaje indicando que los números no son espejos
