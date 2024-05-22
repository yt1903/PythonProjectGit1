from random import randint
nombre = input('¿Cuál es tu nombre?')
print(f"{nombre} he pensado un número entre 1 y 100 ¿Te animas a adivinarlo?")
intentos=1
numeroelegido = randint(1,100)
print(numeroelegido)
while intentos <=8:
    numeroIntentado= int(input(f'Intento nro {str(intentos)}:'))
    if numeroIntentado<1 or numeroIntentado>100:
        print('Numero fuera del rango')
    elif numeroIntentado<numeroelegido:
        print('el numero tipeado es inferior')
    elif numeroIntentado>numeroelegido:
        print('el numero tipeado es superior')
    else:
        print(f'el numero {numeroIntentado} es correcto lo has logrado en el intento nro {intentos}')
        break
    intentos +=1
else: print('No logrado')
