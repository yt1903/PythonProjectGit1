mi_set= set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)


otro_set= {1,2,3}
print(type(otro_set))
print(otro_set)

otro_set= {1,2,3,1,1,3,'9'}
print(type(otro_set))
print(otro_set)

#acepta tuple pero no listas ni diccionario
otro_set= {1,2,3,1,1,3,('9','0')}
print(type(otro_set))
print(len(otro_set))
print(2 in otro_set)


tercer_set=mi_set.union(otro_set)
print(tercer_set)

mi_set.add(23)
print(mi_set)

mi_set.remove(23)
print(mi_set)

mi_set.discard(99)

sorteo= mi_set.pop()
print(sorteo)

mi_set.clear()
print(mi_set)