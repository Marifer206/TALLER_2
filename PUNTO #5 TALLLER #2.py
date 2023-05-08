def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Función para calcular el Mínimo Común Múltiplo de dos números
def mcm(a, b):
    return a * b // mcd(a, b)

# Versión iterativa
def mcm_iterativo(a, b):
    return mcm(a, b)

# Versión recursiva
def mcm_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mcm_recursivo(b, a % b) * a // mcd(a, b)

# Imprimimos los resultados
if __name__ == "__main__":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print("El Mínimo Común Múltiplo de", a, "y", b, "es:", mcm_iterativo(a, b))
    print("El Mínimo Común Múltiplo de", a, "y", b, "es:", mcm_recursivo(a, b))