# Definimos la matriz bidimensional
matriz = [
    [5, 2, 8],
    [4, 1, 6],
    [7, 3, 9]
]

# Definimos la función de búsqueda
def orden (fila):
    n = len(fila)  # Declaramos la variable que cuente nuestra fila
    for i in range(n): # Recorremos el bucle hasta la longitud de la fila
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]: #Si la fila en la posicion j es mayor al siguiente iterador j
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Ordenamos la fila por que si j es mayor al siguiente numero, va a ir primero el numero menor y luego el numero mayor


def ordenar_fila(m, i):
    # Ordena la fila especificada de la matriz
    if 0 <= i < len(m):
        orden(m[i])
    else:
        print("Esta fuera del rango.")



# Imprimir matriz original
for fi in matriz :
  print(fi)

#Usuario elije que fila ordena
ord = int(input("¿Qué fila desea ordenar? "))
#Ordenar las filas
ordenar = ordenar_fila(matriz,ord)


# Imprimir matriz después de ordenar, y seleccionamos la fila
print(f"\nMatriz después de ordenar la fila : {ord} ")
for fi in matriz:
    print(fi)