

#Ejemplo juego

import random

numeroPC = random.randint(1,20)
adivine = False

while adivine==False:
    numeroUsuario = int(input("preguntarle al usuario: "))
    if numeroPC == numeroUsuario:
        print("Felicitaciones!")
        adivine = True
    else:
        if numeroUsuario > numeroPC:
            print("Numero muy grande, probar uno mas pequeño")
        else:
            print("Numero muy pequeño, probar uno mas grande")

