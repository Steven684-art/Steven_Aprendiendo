#Creamos el diccionario en donde vamos a colocar clave - valor
informacion= {"Nombre":"Juan", "Edad":24,"Ciudad": "Guayaquil","Email":"juan@gmail.com","Profesión": "Talento Humano"}


print("Diccionario actual\n",informacion)  #Imprimimos el diccionario
#Creamos un menú de opciones

print("\n MENÚ")
print("\n1.Acceder al valor asociado con la clave ciudad y modifícar con una ciudad diferente",
          "\n2. Agregar una nueva clave-valor al diccionario que represente la profesion de la persona.",
          "\n3. Verifica si la clave teléfono existe en el diccionario",
          "\n4. Elimina la clave edad del diccionario",
          "\n5. Mostrar diccionario" )


opcion=int(input("\nIngrese la opcion: "))
while opción :  #Creamos un bucle while para preguntar la opción


    if opcion == 1 :
        print(información["Ciudad"])  #Imprimimos la ciudad actual
        informacion.update({"Ciudad": "Cuenca"})  #Modificamos la ciudad
        print(f"Información modificada: {información["Ciudad"]}")  #Imprimimos la ciudad modificada






    elif opcion == 2:
       informacion.update({"Profesión": "Ingeniero en Sistemas"})  #Actualizamos la profesion
       print(f"Profesión modificada: {informacion["Profesión"]}") #Imprimimos la porfesion modificada


    elif opcion ==3 :
    #Verificamos si existe la clave de telefono
        if "Telefono" in informacion:
            print("Si existe el telefono")
            print(f"Telefono: {informacion["Telefono"]}")

        else:
            print("Telefono añadido")
            informacion.update({"Telefono": 985687})
        print(f"Telefono : {informacion["Telefono"]}")


    elif opcion == 4:
        del informacion["Edad"]  #Borramos la edad
        print(f"{"Edad"} eliminada")

    elif opcion == 5 :
        print(f"El diccionario actualizado es: {informacion}")  #Imprimimos el diccionario actualizado


    elif opcion > 5:
        break #Si elije una opcion mayor a 5 se corta el programa

    opcion = int(input("\nIngrese la opción: "))
