def sumas():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1+n2)
    print("Gracias por suma")

"""try:
    #codigo que se quiere ejecutar
    sumas()
except TypeError:
    # codigo que se quiere ejecutar cuando hay error
    print("error de concatenacion")
except ValueError:
    print("error de tipo de datos")
else:
    # codigo que se quiere ejecutar cuando NO hay error
    print("Todo bien")
finally:
    # codigo que se quiere ejecutar aunque haya error
    print("Eso fue todo")"""


def pedir_numero():
    while True:
        try:
            numero=int(input("Dame un numero: "))
        except:
            print("ese no es un numero")
        else:
            print(f"Ingresaste  el numero {numero}")
            break
    print('Gracias')
    return numero

print(pedir_numero())