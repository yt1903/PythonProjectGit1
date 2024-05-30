nombre = ['juan','ana','carlos','belen','fran']
for elemento in nombre:
    print(elemento)
    print(nombre.index(elemento))
    if elemento.startswith('b'):
        print('cumplio')

for elemento in  enumerate(nombre):
    print('enumarate' ,elemento[0])
    print(elemento)

palabra='reconciliacion'
for letra in palabra:
    print(letra)

monedas = 5
while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else: print("Se acabó")

#("dentro del while estan pass cuando no sabemos el codigo que se va a poner"
# "break continue")

numero = 10

while numero>=0:
    print(numero)
    numero -= 1
