mi_tuple=(1,2,3,'q')
print(type(mi_tuple))

print(mi_tuple[0])
print(mi_tuple[-2])

mi_tuple=(1,2,(10,20),4)
print(mi_tuple[2][0])


mi_tuple=list(mi_tuple)
print(type(mi_tuple))

mi_tuple=tuple(mi_tuple)
print(type(mi_tuple))

mi_tuple=(1,2,3)
x,y,z=mi_tuple
print(x,y,z)

mi_tuple=('a','b','c','a')
print(len(mi_tuple))


print(mi_tuple.count('a'))
print(mi_tuple.index('a'))

