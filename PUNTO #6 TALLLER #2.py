# Definimos una lista vacía para almacenar las cadenas de caracteres
lista=[]

# Pedimos al usuario que ingrese las cadenas de caracteres hasta que ingrese 'fin'
while True:
    cadena = input("Ingrese una cadena de caracteres (o escriba 'fin' para terminar): ")
    # Si el usuario ingresa 'fin', salimos del bucle
    if cadena == 'fin':
        break
    # Agregamos la cadena a la lista
    lista.append(cadena)

# Definimos una función para contar las vocales en una cadena
def contar_vocales(cadena):
    # Definimos una lista con las vocales (mayúsculas y minúsculas)
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # Inicializamos el contador de vocales en 0
    contador = 0
    # Recorremos la cadena de caracteres
    for letra in cadena:
        # Si la letra es una vocal, aumentamos el contador
        if letra in vocales:
            contador += 1
    # Devolvemos el contador de vocales
    return contador

# Definimos una variable para indicar si encontramos una cadena con dos o más vocales
encontrado = False

# Recorremos la lista de cadenas de caracteres
for cadena in lista:
    # Contamos las vocales en la cadena
    num_vocales = contar_vocales(cadena)
    # Si la cadena tiene dos o más vocales, la imprimimos y cambiamos el valor de la variable encontrado
    if num_vocales >= 2:
        print(f"La cadena '{cadena}' tiene {num_vocales} vocales.")
        encontrado = True

# Si no encontramos ninguna cadena con dos o más vocales, imprimimos 'No existe'
if not encontrado:
    print('No existe')