numero=int(input("Introduzca un número"))

if numero<=2:
    print("No es primo")

elif numero>2:
    for i in range(2,numero):
        if numero%i==0:
            print("No es primo")
            break
        else:
            print("Es primo")
            break
    breakpoint









"""def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True"""