# Definimos la matriz bidimensional
matriz = [
    [5, 2, 8],
    [4, 1, 6],
    [7, 3, 9]
]

# Definimos la función de ordenación
def ordenar_fila(matriz, fila):
    # Utilizamos el algoritmo Bubble Sort para ordenar la fila
    for i in range(len(matriz[fila])):
        for j in range(len(matriz[fila]) - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiamos los elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

# Definimos la fila a ordenar
fila_a_ordenar = 1

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Llamamos a la función de ordenación
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)