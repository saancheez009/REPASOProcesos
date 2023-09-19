import random
numero=1
numAleatorio = random.randint(1, 100)

while numero>0 and numero!=numAleatorio:
    numero=int(input("Introduzca un número"))

    if numero<numAleatorio:
        print("MAYOR")
    elif numero>numAleatorio:
        print("MENOR")
    else:
        print("¡HAS ACERTADO!")
        break
 