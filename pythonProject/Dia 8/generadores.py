"""
a diferencia de las funciones los generadores entregan un resultado por parte

en vez de return se devuelve con la palabra yield

y para poder ver el resultado la palabra next.

su ultidad esta en el uso optimo de la memoria
"""


def mi_funcion():
    """
    funcion normal
    :return:
    """
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista


def mi_generador():
    """
    diferencia de un generador
    :yield:
    """
    for x in range(1,5):
        yield x * 10


print(mi_funcion())
print(mi_generador())
g = mi_generador()
# imprime el primero
print(next(g))
# imprime el segundo
print(next(g))


def mi_generador2():
    """
    pueden ponerse varios yields
    :return: 
    """
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador2()

print(next(g))
print(next(g))
print(next(g))
range()
