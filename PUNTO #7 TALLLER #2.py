# Definimos una lista vacía para almacenar los elementos
lista = []

# Pedimos al usuario que ingrese los elementos de lista
while True:
    elemento = input("Ingrese un elemento (o presione Enter para terminar): ")
    if elemento == '':
        break
    lista.append(int(elemento))

# Buscamos elementos repetidos en la lista
repetidos = False
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            repetidos = True
            break
    if repetidos:
        break
# Imprimimos la lista
print(lista)
# Imprimimos el resultado
if repetidos:
    print('Existen elementos repetidos en la lista')
else:
    print('No existen elementos repetidos en la lista')