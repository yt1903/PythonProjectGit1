def saludar_persona(nombre):
    '''esta funcion
    saluda'''
    print('hola ' + nombre)

saludar_persona('lola')

def multiplicar(num1, num2):
    return num1*num2

def numero_3_cifras(numero):
    return numero in range(100,1000)

def numero_3_cifras(lista):
    for numero in lista:
        if numero in range(100,1000):
            return True
        else:
            pass
    return False

def calculo(*num):
    total=0
    for n in num:
        total=total+n

    sum(num)


def dicd(**dicionario):
    total = 0
    for d,e in dicionario.items():
        print(d,e)

dicd(nombre='yas', apellido='tru')
