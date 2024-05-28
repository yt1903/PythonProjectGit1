from collections import Counter,defaultdict, namedtuple,deque


#Counter
numeros =[2,3,3,3,4,4,4,4,5,5,6,6,6]
print(Counter(numeros))

palabra = "Missisipi"
print(Counter(palabra))

frase = "Al pan pan y al vino vion"
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3])
print(serie.most_common(2))
print(list(serie))

#defaultdict
mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

#nametuple

mi_tupla= (500,18,65)
print(mi_tupla[1])

Persona = namedtuple('Personas', ['nombre', 'altura','peso'])
ariel = Persona('Ariel',1.76, 79)
print(ariel.altura)
print(ariel.peso)
print(ariel.nombre)
print(ariel[1])

#Deque

serie_deque= deque([1,2,3,'4'])
serie_deque.append('d')
serie_deque.appendleft('a')
print(serie_deque)