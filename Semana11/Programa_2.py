# Definimos la matriz bidimensional
matriz = [
    [5, 2, 8],
    [4, 1, 6],
    [7, 3, 9]
]

# Definimos la función de búsqueda
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devolvemos la posición del valor
    return None  # Devolvemos None si no se encuentra el valor

# Definimos el valor a buscar
valor_a_buscar = 6

# Llamamos a la función de búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostramos el resultado
if posicion is not None:
    print(f"El valor {valor_a_buscar} se encontró en la posición ({posicion[0]}, {posicion[1]})")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz")