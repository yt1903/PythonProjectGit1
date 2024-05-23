mi_lista = ['a','b','c']
print(type(mi_lista))
print(mi_lista[0])
print(mi_lista[0:2])
print(len(mi_lista)) #da la longitud de la lista
print(min(mi_lista))
print(max(mi_lista))

mi_lista_2 = ['d','e','e']
print(mi_lista + mi_lista_2)

mi_lista_3 = mi_lista+mi_lista_2
print(mi_lista_3)

mi_lista_4 = mi_lista_3
mi_set= set(mi_lista_4)
print('mi_set')
print(mi_set)
mi_lista_4 = list(mi_set)
print(mi_lista_4.remove(max(mi_lista_4)))
print(mi_lista_4)

mi_lista_3[0]='alfa'
print(mi_lista_3)

mi_lista_3.append('beta')
print(mi_lista_3)

mi_lista_3.pop() #elimina el ultimo
print(mi_lista_3)

mi_lista_3.pop(0) #elimina el indice
print(mi_lista_3)

eliminado= mi_lista_3.pop(0)
print(eliminado)




lista_ordenar=['f','b','w','a']
lista_ordenar.sort()
print(lista_ordenar)

lista_ordenar.reverse()
print(lista_ordenar)

palabra='Python'
lista = [letra for letra in palabra]
print(lista)

lista = [n for n in range(0,21,2 ) if n*2>10]
print(lista)

lista = [n if n*2>10 else 'no' for n in range(0,21,2 ) ]
print(lista)

pies = [10,20,30]
pies.insert(2,89)
print(pies)
print(pies.index(20))
metros = [n*3.281 for n in pies]
print(metros)
metros.clear()
