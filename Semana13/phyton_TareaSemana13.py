# Declaramos nuestra lista 3D
#3x7x3
temperatura_semana = [
    [  # Ciudad 1
        [24, 12, 13, 14, 19, 21, 22],#Semana1
        [14, 18, 18, 20, 21, 23, 24],#Semana2
        [19, 16, 17, 21, 24, 26, 28],#Semana3
        [14, 26, 17, 21, 23, 27, 17]#Semana4
    ],
    [  # Ciudad 2
        [25, 26, 21, 27, 29, 24, 26],#Semana1
        [22, 21, 27, 22, 18, 21, 15],#Semana2
        [22, 21, 28, 27, 26, 23, 25],#Semana3
        [21, 24, 27, 22, 23, 27, 18]#Semana4
    ],
    [  #Ciudad 3
        [24, 22, 23, 28, 12, 27, 24],#Semana1
        [27, 22, 28, 31, 13, 11, 31],#Semana2
        [22, 31, 11, 21, 24, 27, 21],#Semana3
        [22, 27, 26, 27, 22, 18, 19]#Semana4
    ]
]

def promedio (c,s): #Creamos nuestra funcion, la cual le damos 2 argumentos que son de ciudades y semanas





    # Inicializamos variables en cero
    suma_total = 0
    cantidad_total = 0


    # Utilizamos bucles for anidados para recorrer la estructura
    for ciudades in  range(len(temperatura_semana)):  #El bucle ciudades va a recorrer toda la lista
     if ciudades == c: #Comparamos si al recorrer la lista nuestro numero es igual al de ciudad que declaramos
            for semanas in range (len(temperatura_semana[ciudades])):  # Bucle semanas va a recorrer dentro de nuestro bucle ciudades
                if semanas == s : #Comparamos si al recorrer la lista nuestro numero es igual al de semanas que declaramos
                    for temp in range (len(temperatura_semana[ciudades][semanas])):  # Este bucle temp va a recorrer las temperaturas
                        suma_total += temperatura_semana[ciudades][semanas][temp] # Sumamos las temperaturas de nuestra lista
                        cantidad_total += 1 #Sumamos en 1 nuestro contador

    # Calculamos el promedio
    promedio = suma_total / cantidad_total   # Calculamos el promedio y dividimos para nuestro contador
    return f"El promediooo de la temperatura de la ciudad {c} de la semana {s} es: {promedio: }°C"  #Retornamos  un mensaje en el cual nos dara el promedio


ciudad = int(input("Ingrese la ciudad (1 a 3): "))   #Creamos la variable ciudad para que el usuario ingrese que ciudad desea
semana = int(input("Ingrese la semana (1 a 4 ): "))   #Creamos la variable semana para que el usuario ingrese la semana que desea el promedio

#Llamamos a nuestra funcion y colocamos los argumentos en este caso las varaibles ciudad y semana
print(promedio(ciudad,semana))

