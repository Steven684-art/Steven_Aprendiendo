listas = []  # Creamos la lista vacía

num = int(input("Ingrese la cantidad de productos que comprará: ")) #Creamos una variable para saber cuantos productos vamos a comprar
for i in range(0, num):  #Creamos un for para recorrer dentro del rango de 0 a num de los prodcutos que elijamos
    producto = float(input("Ingrese el valor del producto2: "))  # Mientras for recorra las veces que elijamos, nos preguntara el valor de los prodcutos
    listas.append(producto)  # Agregamos a la lista los valores que vayamos agregando

print("\nVALORES DE LOS PRODUCTOS")  #Imprimimos un mnesaje
print("")
print(listas)  # Imprimimos la lista con los valores que fueron agregados

suma = 0  #Inicializamos la variable suma en 0
for j in range(len(listas)):  # Creamos un bucle for que va a recorrer la longitud de la lista
    suma = suma + listas[j] #Sumamos la lista por medio de nuestro iterador j uqe recorrera dentro de la lista

descuento = int(input("Ingrese el porcentaje del descuento: "))  # Declaramos la variable descuento en donde el usuairo ingresara


def desc(valor, desc):   #Cremoas nuestra función con 2 parametros
    val = valor - (valor * desc / 100)  # Calculamos el descuento restando nuestro valor
    return val  #Retornamos el valor


p_final = desc(suma, descuento)  # Llamamos un avariable y nuestra fucnión y agregamos de parametros la variable suma y descuento
print(
    f"La suma de los productos es {suma} $, con un descuento del {descuento} % el precio total a cancelar es de {p_final: .2f} $")   #Imprimimos un mensaje con la suma total, el descuento y el precio final con el descuento