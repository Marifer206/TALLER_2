# :star: TALLER_2 :star:
##  Grupo: Team rocket cazadores de pockebugd
[![Team-rocket.png](https://i.postimg.cc/zvNyPVQD/Team-rocket.png)](https://postimg.cc/Pp6fCrh0)
# Desarrollo de taller #2;   {Programación de computadores} :smile: :computer:

# PUNTO 1 
1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.
## Codigo del programa
```ruby
numeros = []  # Se define una lista vacía llamada "numeros"
def separar_numero(x):  # Se define una función llamada "separar_numero" que toma un número entero "x" como argumento
    while x > 0:  # Se utiliza un bucle "while" para iterar mientras "x" sea mayor que cero
        numeros.append(x%10)  # Se utiliza el operador módulo "%" para obtener el último dígito de "x" y se agrega a la lista "numeros" utilizando el método "append()"
        x = x // 10  # Se utiliza el operador de división entera "//" para eliminar el último dígito de "x"
    numeros.reverse()  # Se invierte el orden de los elementos en la lista "numeros" utilizando el método "reverse()"
    print(numeros)  # Se imprime la lista "numeros" que contiene los dígitos individuales del número entero original

n = int(input("Ingrese el numero entero el cual quiera separar: "))  # Se pide al usuario que ingrese un número entero y se almacena en la variable "n"
separar_numero(n)  # Se llama a la función "separar_numero" con el número ingresado como argumento
```
## DESCRIPCION 
Este programa separa todos los digitos de un numero entero dado por medio de la funcion separar_numero y con el uso del bucle while para interar 

# PUNTO 2
2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.
## Codigo del programa
```ruby
import math  # Se importa el módulo "math" que contiene funciones matemáticas

n = float(input("Ingrese el número del cual quiera saber su parte entera y su parte decimal: "))  # Se pide al usuario que ingrese un número y se almacena en la variable "n" como un número de punto flotante

entero = math.trunc(n)  # Se utiliza la función "trunc()" del módulo "math" para obtener la parte entera del número "n" y se almacena en la variable "entero"
decimal = n - entero  # Se resta la parte entera del número "n" a "n" para obtener la parte decimal y se almacena en la variable "decimal"

print("La parte entera del número " + str(n) + " es " + str(entero) + " y su parte decimal es " + str(decimal))  # Se imprime en la pantalla la parte entera y la parte decimal del número "n"
```
## DESCRIPCION 
Este programa separA la parte entera y la parte decimal de un numero flotante ingresado y devuelve o entrega estas dos partes

# PUNTO 3
3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.
## Codigo del programa
```ruby
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

```
## DESCRIPCION 
Este progama determinar si dos numeros ingresados son espejos por medio de la funcion invertir_numero, este codigo tiene dos variables las cuales son m y n, estas son igresadas y debe ser un numero entero

# PUNTO 4
4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$
## Codigo del programa
```ruby
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
```
## DESCRIPCION
El código es una implementación de la aproximación del coseno utilizando la serie de Taylor y se utiliza para determinar cuántos términos de la serie son necesarios para lograr una determinada precisión del resultado. El usuario ingresa el valor de "x" y una lista de errores deseados, y el código itera a través de cada uno de los errores deseados para determinar cuántos términos de la serie son necesarios para lograr esa precisión.

# PUNTO 5
5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.
## Codigo del programa
```ruby
# Función para calcular el Máximo Común Divisor de dos números
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
    
```
## DESCRIPCION
El código proporcionado define funciones para calcular el Máximo Común Divisor (MCD) y el Mínimo Común Múltiplo (MCM) de dos números enteros, utilizando el algoritmo de Euclides para el MCD. Además, proporciona dos versiones para calcular el MCM: una iterativa y otra recursiva que utiliza la función de MCD definida anteriormente. El programa también solicita al usuario que ingrese dos números enteros y muestra el resultado del cálculo del MCM utilizando ambas versiones de la función..

# PUNTO 6
6. Desarrollar un programa que determine si en una lista no existen elementos repetidos.
## Codigo del programa
```ruby
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
```
## DESCRIPCION

Este programa pide al usuario ingresar una lista de números enteros y busca elementos repetidos en ella.
Si encuentra elementos repetidos, imprime un mensaje indicando que existen elementos repetidos.
Si no encuentra elementos repetidos, imprime un mensaje indicando que no existen elementos repetidos.
Primero, define una lista vacía y luego utiliza un bucle while para que el usuario ingrese elementos de la lista.
Luego, utiliza dos bucles for para comparar cada elemento de la lista con los demás y determinar si hay elementos repetidos.
Finalmente, imprime la lista y el resultado.

# PUNTO 7
7. Desarrollar un programa que determine si en una lista se encuentra
una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
## Codigo del programa
```ruby
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
```
## DESCRIPCION
Este código pide al usuario que ingrese varias cadenas de caracteres hasta que escriba "fin". Luego, se define una función que cuenta el número de vocales en una cadena. A continuación, el programa recorre la lista de cadenas y para cada una de ellas, cuenta el número de vocales y si encuentra dos o más, imprime la cadena y el número de vocales. Si no encuentra ninguna cadena con dos o más vocales, imprime "No existe".
# PUNTO 8
8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. **Ejemplo:**
<center>
<table border="1">
<tr>
<td>
lista1: [1, 'Hola', -12.3 ,True]<br>
lista2: [11, -12.3, 'Hola', False]
</td>
</tr>
<tr>
<td>
salida: [1, True]
</td>
</tr>
</table>
</center>

## Codigo del programa
```ruby
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
print("Los elementos que están en la primera lista pero no en la segunda lista son:", diferencia)
```
## DESCRIPCION


# PUNTO 9
9. Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.
## Codigo del programa
```ruby
# Pedir 5 números reales al usuario
numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Calcular el promedio aritmético
promedio_aritmetico = sum(numeros) / len(numeros)

# Calcular la mediana
numeros_ordenados = sorted(numeros)
mediana = 0
if len(numeros_ordenados) % 2 == 0:
    # Si el número de elementos es par, se promedian los dos del centro
    indice_medio = len(numeros_ordenados) // 2
    mediana = (numeros_ordenados[indice_medio-1] + numeros_ordenados[indice_medio]) / 2
else:
    # Si el número de elementos es impar, se toma el del centro
    indice_medio = len(numeros_ordenados) // 2
    mediana = numeros_ordenados[indice_medio]

# Calcular el promedio multiplicativo
from functools import reduce
promedio_multiplicativo = reduce(lambda x, y: x * y, numeros) ** (1/len(numeros))

# Ordenar los números de forma ascendente y descendente
numeros_ascendente = sorted(numeros)
numeros_descendente = sorted(numeros, reverse=True)

# Calcular la potencia del mayor número elevado al menor número
mayor = max(numeros)
menor = min(numeros)
potencia = mayor ** menor

# Calcular la raíz cúbica del menor número
raiz_cubica = menor ** (1/3)

# Mostrar los resultados
print(f"El promedio aritmético es: {promedio_aritmetico}")
print(f"La mediana es: {mediana}")
print(f"El promedio multiplicativo es: {promedio_multiplicativo}")
print(f"Los números en orden ascendente son: {numeros_ascendente}")
print(f"Los números en orden descendente son: {numeros_descendente}")
print(f"El mayor número elevado al menor número es: {potencia}")
print(f"La raíz cúbica del menor número es: {raiz_cubica}")
```
## DESCRIPCION
nota: las explicaciones estan en los comentarios del codigo

# PUNTO 10
10. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
## Codigo del programa
```ruby
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
```
## DESCRIPCION
nota: las explicaciones estan en los comentarios del codigo

