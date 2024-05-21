diccionario={'c1':'valor1', 'c2':'valor2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre:' : 'Juan', 'apellido:' : 'Perez', 'peso:' : 88, 'talla:' : 1.76}
consulta = (cliente['apellido:'])
print(consulta)

dic={'c1' : 55, 'c2':[10,20,30], 'c3': {'s1': 200, 's2':100}}
print(dic['c2'][0])
print(dic['c3']['s1'])

dic={'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic['c2'][1].upper())

dic['c3']='c'
print(dic)

dic['c1'][1]='B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())


