# :star: TALLER_2 :star:
##  Grupo: Team rocket cazadores de pockebugd
[![Team-rocket.png](https://i.postimg.cc/zvNyPVQD/Team-rocket.png)](https://postimg.cc/Pp6fCrh0)
# Desarrollo de taller #2;   {Programación de computadores} :smile: :computer:

# PUNTO 1 
1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. g
## Codigo del programa
```ruby
numeros = []
def separar_numero(x):
    while x > 0:
        numeros.append(x%10)
        x = x // 10
    numeros.reverse()
    print(numeros)

n = int(input("Ingrese el numero entero el cual quiera separar: "))
separar_numero(n)
```
# PUNTO 2
2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.
## Codigo del programa
```ruby
import math
from decimal import Decimal

n = float(input("Ingrese el número del cual quiera saber su parte entera y su parte decimal: "))

entero = math.trunc(n)
decimal = n - entero

print("La parte entera del número " + str(n) + " es " + str(entero) + " y su parte decimal es " + str(decimal))
```
# PUNTO 3
3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.
## Codigo del programa
```ruby
def invertir_numero(numero):
    numero_invertido = 0
    while numero > 0:
        digito = numero % 10
        numero_invertido = (numero_invertido * 10) + digito
        numero //= 10
    return numero_invertido

n = int(input("Ingrese el primer número: "))
m = int(input("Ingrese el segundo número: "))

n_invertido = invertir_numero(n)

if n_invertido == m:
    print("Los números", n, "y", m, "son espejos.")
else:
    print("Los números", n, "y", m, "no son espejos.")

```
# PUNTO 4
4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$
## Codigo del programa
```ruby
import math

def aproximacion_coseno(x, n):
    aproximacion = 0
    for i in range(n):
        termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        aproximacion += termino
    return aproximacion

x = float(input("Ingrese el valor de x: "))

errores_deseados = [0.001, 0.1, 1, 10]

for error in errores_deseados:
    e = 0
    while True:
        e += 1
        aproximacion = aproximacion_coseno(x, e)
        error_porcentual = abs((aproximacion - math.cos(x)) / math.cos(x)) * 100
        if error_porcentual <= error:
            break
    print("Aproximación: " + str(aproximacion))
    print("Valor real: " + str(math.cos(x)))
    print("Con un error del " + str(error) + "% se necesitan " + str(e) + " términos de la serie")
    print("")

```
# PUNTO 5
5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.
## Codigo del programa
```ruby

```
# PUNTO 6
6. Desarrollar un programa que determine si en una lista no existen elementos repetidos.
## Codigo del programa
```ruby

```
# PUNTO 7
7. Desarrollar un programa que determine si en una lista se encuentra
una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
## Codigo del programa
```ruby

```
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

```

# PUNTO 9
9. Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.
## Codigo del programa
```ruby

```

# PUNTO 10
10. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
## Codigo del programa
```ruby

```
