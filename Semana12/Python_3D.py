# Declaramos nuestra lista 3D
#3x7x3
temperatura_semana = [
    [  # Ciudad 1
        [24, 12, 13, 14, 19, 21, 22],#Semana
        [14, 18, 18, 20, 21, 23, 24],#Semana
        [19, 16, 17, 21, 24, 26, 28],#Semana
        [14, 26, 17, 21, 23, 27, 17]#Semana
    ],
    [  # Ciudad 2
        [25, 26, 21, 27, 29, 24, 26],#Semana
        [22, 21, 27, 22, 18, 21, 15],#Semana
        [22, 21, 28, 27, 26, 23, 25],#Semana
        [21, 24, 27, 22, 23, 27, 18]#Semana
    ],
    [  # Ciudad 3
        [24, 22, 23, 28, 12, 27, 24],#Semana
        [27, 22, 28, 31, 13, 11, 31],#Semana
        [22, 31, 11, 21, 24, 27, 21],#Semana
        [22, 27, 26, 27, 22, 18, 19]#Semana
    ]
]

 #Declaramos variables de la ciudad y la semana que queremos saber el promedio
ciudad = 1
semana= 1


# Inicializamos variables en cero
suma_total = 0
cantidad_total = 0

#
# Utilizamos bucles for anidados para recorrer la estructura
for ciudades in  range(len(temperatura_semana)):  #El bucle ciudades va a recorrer toda la lista
    if ciudad == ciudad: #Comparamos si al recorrer la lista nuestro numero es igual al de ciudad que declaramos
        for semanas in range (len(temperatura_semana[ciudad])):  # Bucle semanas va a recorrer dentro de nuestro bucle ciudades
            if semanas == semana : #Comparamos si al recorrer la lista nuestro numero es igual al de semanas que declaramos
                for temp in range (len(temperatura_semana[ciudad][semanas])):  # Este bulce temp va a recorrer las temperaturas
                        suma_total += temperatura_semana[ciudad][semanas][temp] # Sumamos las temperaturas de nuestra lista
                        cantidad_total += 1 #Sumamos en 1 nuestro contador

# Calculamos el promedio
promedio = suma_total / cantidad_total  # Declaramos el promedio y dividimos para nuestro contador

# Imprimimos el resultado con un print

print(f"El promedio de la temperatura de la ciudad {ciudad} de la semana {semana} es: {promedio}°C")

 #Declaramos variables de la ciudad y la semana que queremos saber el promedio
ciudad = 2
semana= 2


# Inicializamos variables en cero
suma_total = 0
cantidad_total = 0

#
# Utilizamos bucles for anidados para recorrer la estructura
for ciudades in  range(len(temperatura_semana)):  #El bucle ciudades va a recorrer toda la lista
    if ciudad == ciudad: #Comparamos si al recorrer la lista nuestro numero es igual al de ciudad que declaramos
        for semanas in range (len(temperatura_semana[ciudad])):  # Bucle semanas va a recorrer dentro de nuestro bucle ciudades
            if semanas == semana : #Comparamos si al recorrer la lista nuestro numero es igual al de semanas que declaramos
                for temp in range (len(temperatura_semana[ciudad][semanas])):  # Este bulce temp va a recorrer las temperaturas
                        suma_total += temperatura_semana[ciudad][semanas][temp] # Sumamos las temperaturas de nuestra lista
                        cantidad_total += 1 #Sumamos en 1 nuestro contador


# Calculamos el promedio
promedio = suma_total / cantidad_total  # Declaramos el promedio y dividimos para nuestro contador

# Imprimimos el resultado con un print

print(f"El promedio de la temperatura de la ciudad {ciudad} de la semana {semana} es: {promedio}°C")

