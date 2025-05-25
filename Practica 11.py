
# Actividad 1: Fuerza Bruta
from itertools import product
from string import ascii_letters, digits

def fuerza_bruta(con):
    caracteres = ascii_letters + digits
    if 3 <= len(con) <= 4:
        for i in range(3, 5):
            for comb in product(caracteres, repeat=i):
                prueba = "".join(comb)
                if prueba == con:
                    return f"Tu contrasena es: {prueba}"
        return "Contrasena no encontrada."
    else:
        return "Ingresa una contrasena que contenga de 3 a 4 caracteres"

print("Actividad 1:", fuerza_bruta("H0l4"))

# Actividad 2: Algoritmo Greedy para cambio de monedas
def cambio_greedy(cantidad, denominaciones):
    resultado = []
    for denom in denominaciones:
        if cantidad >= denom:
            num = cantidad // denom
            cantidad -= num * denom
            resultado.append((denom, num))
    return resultado

print("Actividad 2:", cambio_greedy(98, [50, 20, 5, 1]))

# Actividad 3: Fibonacci Bottom-Up (Programación Dinámica)
def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

print("Actividad 3:", fibonacci_bottom_up(10))

# Actividad 4: Fibonacci Top-Down (con memorización)
def fibonacci_top_down(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    return memo[n]

print("Actividad 4:", fibonacci_top_down(10))

# Actividad 5: Divide y vencerás (suma recursiva)
def suma_divide_venceras(arr):
    if len(arr) == 1:
        return arr[0]
    medio = len(arr) // 2
    izquierda = suma_divide_venceras(arr[:medio])
    derecha = suma_divide_venceras(arr[medio:])
    return izquierda + derecha

print("Actividad 5:", suma_divide_venceras([1, 2, 3, 4, 5, 6]))

# Actividad 6: Modelo RAM (suma con conteo de operaciones)
def suma_ram(arr):
    operaciones = 0
    suma = 0
    for num in arr:
        suma += num
        operaciones += 1
    return suma, operaciones

print("Actividad 6:", suma_ram([1, 2, 3, 4, 5, 6]))

# actividades de clase
# Actividad 1 Romper un candado (Número secreto)
import random

print("1. Romper el candado:")
numero_secreto = random.randint(1, 100)
intento = 0
while True:
    intento += 1
    adivinanza = random.randint(1, 100)
    if adivinanza == numero_secreto:
        print(f"¡Candado roto! El número era {numero_secreto}. Intentos: {intento}\n")
        break


# Actividad 2 Determinar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("2. Verificar si un número es primo:")
numero = 29
print(f"¿{numero} es primo? {'Sí' if es_primo(numero) else 'No'}\n")


# Actividad 3 Factorial Top-down (Recursivo con memoización)
def factorial_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = n * factorial_top_down(n-1, memo)
    return memo[n]

print("3. Factorial Top-Down:")
print("Factorial Top-Down de 5:", factorial_top_down(5), "\n")


# Actividad 4 Factorial Bottom-up (Iterativo)
def factorial_bottom_up(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

print("4. Factorial Bottom-Up:")
print("Factorial Bottom-Up de 5:", factorial_bottom_up(5), "\n")


# Actividad 5 Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mitad = len(arr) // 2
        izquierda = arr[:mitad]
        derecha = arr[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

print("5. Merge Sort:")
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista)
merge_sort(lista)
print("Lista ordenada:", lista)

