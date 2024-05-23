mi_archivo = open('../prueba.txt')

#print(mi_archivo)

"""#print(mi_archivo.read())
print(mi_archivo.readline())
print(mi_archivo.readline())"""


"""todas = mi_archivo.readlines()
print(type(todas))
mi_archivo.close()"""

#print(mi_archivo.readline())
mi_archivo.close()

mi_archivo = open('../prueba.txt', 'w')
mi_archivo.write("""Nuevo Texto
        Reemplaza en anterior """)

mi_archivo.close()

