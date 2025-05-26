
# Actividad 1 Factorial (Iterativo)
def factorial_no_recursivo(numero):
    fact = 1
    for i in range(numero, 1, -1):
        fact *= i
    return fact

# Actividad 2 Factorial (Recursivo)
def factorial_recursivo(numero):
    if numero < 2:
        return 1
    return numero * factorial_recursivo(numero - 1)

# Actividad 3 Huellas de tortuga (Iterativo)
def recorrido_no_recursivo():
    import turtle
    pantalla = turtle.Screen()
    tess = turtle.Turtle()
    size = 3
    for _ in range(30):
        tess.stamp()
        size += 3
        tess.forward(size)
        tess.right(24)
    pantalla.mainloop()

# Actividad 4 Huellas de tortuga (Recursivo)
def recorrido_recursivo(tortuga, espacio, huellas):
    if huellas > 0:
        tortuga.stamp()
        espacio += 3
        tortuga.forward(espacio)
        tortuga.right(24)
        recorrido_recursivo(tortuga, espacio, huellas - 1)

def ejecutar_recorrido_recursivo(huellas):
    import turtle
    pantalla = turtle.Screen()
    tess = turtle.Turtle()
    recorrido_recursivo(tess, 3, huellas)
    pantalla.mainloop()

# Actividadc 5 Fibonacci (Iterativo)
def fibonacci_iterativo_v2(numero):
    f1, f2 = 0, 1
    if numero == 1:
        return f1
    for _ in range(1, numero - 1):
        f1, f2 = f2, f1 + f2
    return f2

# Actividad 5.1 Fibonacci (Recursivo con memorización)
def fibonacci_memo(n, memoria=None):
    if memoria is None:
        memoria = {1: 0, 2: 1}
    if n not in memoria:
        memoria[n] = fibonacci_memo(n - 1, memoria) + fibonacci_memo(n - 2, memoria)
    return memoria[n]

# Actividad 6 Torres de Hanoi (Recursivo)
def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        torres_de_hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        torres_de_hanoi(n - 1, auxiliar, destino, origen)


