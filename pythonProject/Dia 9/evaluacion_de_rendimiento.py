"""
forma para verificar cual código es más eficiente segun el tiempo de ejecucion
"""
import time  # tiene menos precision
import timeit


def prueba_for(numero):
    """
    hace una lista con for
    :param numero:
    :return:
    """

    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    """
    hace una lista con while
    :param numero:
    :return:
    """

    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


"""
Time
"""
inicio = time.time()
print((prueba_for(10000)))
final = time.time()
print(final-inicio)

inicio = time.time()
print(prueba_while(10000))
final = time.time()
print(final-inicio)


inicio = time.time()
print((prueba_for(10000)))
final = time.time()
print(final-inicio)

inicio = time.time()
print(prueba_while(10000))
final = time.time()
print(final-inicio)

"""
timeit
"""
declaracion = """
prueba_for(10)
"""

mi_setup = """
def prueba_for(numero):
    
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""

duracion = timeit.timeit(declaracion, mi_setup, number=1000000)
print('timeit' )
print(duracion )

declaracion2 = """
prueba_while(10)
"""

mi_setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion2 = timeit.timeit(declaracion2, mi_setup2, number=1000000)
print(duracion2)

