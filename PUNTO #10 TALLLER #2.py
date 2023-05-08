# Pedimos al usuario que ingrese los datos de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        elemento = int(input(f"Ingrese el elemento ({i+1},{j+1}): "))
        fila.append(elemento)
    matriz.append(fila)

# Calculamos la mágica
suma_magica = 0
for i in range(n):
    suma_magica matriz[0][i]

# Verificamos si la suma de cada fila, columna y diagonal es igual a la suma mágica
es_magica = True
for i in range(n):
    # Verificamos la suma de la fila i
    suma_fila = 0
    for j in range(n):
        suma_fila += matriz[i][j]
    if suma_fila != suma_magica:
        es_magica = False
        break
    # Verificamos la suma de la columna i
    suma_columna = 0
    for j in range(n):
        suma_columna += matriz[j][i]
    if suma_columna != suma_magica:
        es_magica = False
        break
    # Verificamos la suma de la diagonal principal
    suma_diagonal_principal = 0
    for j in range(n):
        if i == j:
            suma_diagonal_principal += matriz[i][j]
    if suma_diagonal_principal != suma_magica:
        es_magica = False
        break
    # Verificamos la suma de la diagonal secundaria
    suma_diagonal_secundaria = 0
    for j in range(n):
        if i + j == n - 1:
            suma_diagonal_secundaria += matriz[i][j]
    if suma_diagonal_secundaria != suma_magica:
        es_magica = False
        break

# Imprimimos el resultado
if es_magica:
    print("La matriz es mágica")
else:
    print("La matriz no es mágica")