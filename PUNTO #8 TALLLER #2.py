# Pedimos al usuario que ingrese los elementos de la primera lista
lista1 = []
while True:
    elemento = input("Ingrese un elemento para la primera lista (o presione Enter para terminar): ")
    if elemento == '':
        break
    lista1.append(int(elemento))

# Pedimos al usuario que ingrese los elementos de la segunda lista
lista2 = []
while True:
    elemento = input("Ingrese un elemento para la segunda lista (o presione Enter para terminar): ")
    if elemento == '':
        break
    lista2.append(int(elemento))

# Creamos una lista vacía para almacenar los elementos que están en la primera lista pero no en la segunda lista
diferencia = []

# Recorremos la primera lista y verificamos si cada elemento está en la segunda lista
for elemento in lista1:
    esta_en_lista2 = False
    for elemento2 in lista2:
        if elemento == elemento2:
            esta_en_lista2 = True
            break
    if not esta_en_lista2:
        diferencia.append(elemento)

# Imprimimos los elementos que están en la primera lista pero no en la segunda lista
print("Los elementos que están en la primera lista pero no en la segunda lista son:", diferencia)