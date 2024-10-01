#Creamos el diccionario en donde vamos a colocar clave - valor
información= {"Nombre":"Juan", "Edad":24,"Ciudad": "Guayaquil","Email":"juan@gmail.com","Profesión": "Talento Humano"}


print("Diccionario actual\n",información)  #Imprimimos el diccionario
#Creamos un menú de opciones

print("\n MENÚ")
print("\n1.Acceder al valor asociado con la clave ciudad y modifícar con una ciudad diferente",
          "\n2. Agregar una nueva clave-valor al diccionario que represente la profesion de la persona.",
          "\n3. Verifica si la clave telefono existe en el diccionario",
          "\n4. Elimina la clave edad del diccionario",
          "\n5. Mostrar diccionario" )


opcion=int(input("\nIngrese la opcion: "))
while opcion :  #Creamos un bucle while para preguntar la opcion


    if opcion == 1 :
        print(información["Ciudad"])  #Imprimimos la ciudad actual
        información.update({"Ciudad": "Cuenca"})  #Modificamos la ciudad
        print(f"Información modificada: {información["Ciudad"]}")  #Imprimimos la ciudad modificada






    elif opcion == 2:
       información.update({"Profesión": "Ingeniero en Sistemas"})  #Actualizamos la profesion
       print(f"Profesión modificada: {información["Profesión"]}") #Imprimimos la porfesion modificada


    elif opcion ==3 :
    #Verificamos si existe la clave de telefono
        if "Telefono" in información:
            print("Si existe el telefono")
            print(f"Telefono: {información["Telefono"]}")

        else:
            print("Telefono añadido")
            información.update({"Telefono": 985687})
        print(f"Telefono : {información["Telefono"]}")


    elif opcion == 4:
        del información["Edad"]  #Borramos la edad
        print(f"{"Edad"} eliminada")

    elif opcion == 5 :
        print(f"El diccionario actualizado es: {información}")  #Imprimimos el diccionario actualizado


    elif opcion > 5:
        break #Si elije una opcion mayor a 5 se corta el programa

    opcion = int(input("\nIngrese la opcion: "))
