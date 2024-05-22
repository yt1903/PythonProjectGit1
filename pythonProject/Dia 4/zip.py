nombres = ['ana', 'pedro', 'pepe']
edades = [23,56,21]

combinados = list(zip(nombres, edades))
print(combinados)

for nombre,edad in combinados:
    print( f"{nombre} tiene {edad}")