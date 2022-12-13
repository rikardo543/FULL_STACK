from random import randint

i = 1
numero_secreto = randint(1,100)
nombre = input("Ingresa tu nombre\n")


numero_usuario = int(input(f"Hola!! {nombre}\nHe pensado en un numero que deberas de adivinar\nSolo tendras 8 intentos para lograrlo\nIntroduce un numero del 1 al 100\n"))

while i < 8:
    i += 1
    if numero_usuario not in range(1,100):
        print("numero invalido, intenta otro numero del 1 al 100")
        numero_usuario = int(input())
    elif numero_usuario < numero_secreto:
        print("numero incorrecto, el numero correcto es mayor\nIntente de nuevo")
        numero_usuario = int(input())
    elif numero_usuario > numero_secreto:
        print("numero incorrecto, el numero correcto es menor\nIntente de nuevo")
        numero_usuario = int(input())
    elif numero_usuario == numero_secreto:
            print(f"Felididades encontraste el numero en {i} intentos")
            break

if numero_usuario != numero_secreto:
    print(f"no lograste encontrar el numero el numero secreto era {numero_secreto}")
print("Juego Terminado")

