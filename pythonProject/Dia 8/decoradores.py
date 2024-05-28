"""
uso de decoradores,
"""


def mayuscula(texto):
    """
    :param texto: texto a covertir
    :return: texto convertido
    """
    print(texto.upper())


def minuscula(texto):
    """
    :param texto: texto a covertir
    :return: texto convertido
    """
    print(texto.lower())


def una_funcion(funcion):
    """
    :param funcion: nombre de una funcion
    :return:
    """
    return funcion


una_funcion(mayuscula('funcion dentro de funcion'))

# ahora se puede usar mi_funcion como la funcion mayuscula
mi_funcion = mayuscula
mi_funcion('funcion en variable')



def cambiar_letra(tipo):
    """
    envuelve las funciones que estan adentro
    :param tipo: identifica que funcion se va a usar
    :return:
    """

    def mayuscula2(texto):
        """
        esta funcion para usar decorador
        :param texto:
        :return:
        """
        print(texto.upper())

    def minuscula2(texto):
        """
        esta funcion para usar decorador
        :param texto:
        :return:
        """
        print(texto.lower())

    if tipo == "may":
        return mayuscula2
    elif tipo == "min":
        return minuscula2

print('Prueba')
operacion = cambiar_letra('may')
operacion('palabra')

#como se usan los decoradores


def decorar_saludo(funcion):
    """
    decorador
    :param funcion:
    :return:
    """
    def otra_funcion(palabra):
        """
        arma saludo
        :param palabra:
        :return:
        """
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


# @decorar_saludo
def mayuscula3(texto):
    """
    :param texto: texto a covertir
    :return: texto convertido
    """
    print(texto.upper())


# @decorar_saludo
def minuscula3(texto):
    """
    :param texto: texto a covertir
    :return: texto convertido
    """
    print(texto.lower())


mayuscula3('Mayuscula decorado')

# Para usarla sin decorado
mayuscula_decorada = decorar_saludo(mayuscula3)
mayuscula_decorada('con saludo')
mayuscula3('sin saludo')


