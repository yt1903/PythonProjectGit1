mi_lista = ['a','b','c']
print(type(mi_lista))
print(mi_lista[0])
print(mi_lista[0:2])
print(len(mi_lista)) #da la longitud de la lista

mi_lista_2 = ['d','e','e']
print(mi_lista + mi_lista_2)

mi_lista_3 = mi_lista+mi_lista_2
print(mi_lista_3)

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