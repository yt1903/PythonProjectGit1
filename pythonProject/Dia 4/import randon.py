from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio = round(uniform(1,5))
print(aleatorio)

aleatorio = random()
print(aleatorio)

aleatorio = choice(['azul','amarillo','verde'])
print(aleatorio)

aleatorio= list(range(5,50,5))
print(aleatorio)
shuffle(aleatorio) #desordena
print(aleatorio)
