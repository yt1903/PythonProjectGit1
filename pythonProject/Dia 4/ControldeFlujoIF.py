if 10 >19 :
    print('primero')
elif 115 < 10:
    print('segunda')
else:
    print('ninguno')


#Case
serie='Agua'
match serie:
    case 'tierra':
        print('tierra')
    case 'Mar':
        print('azul')
    case _:
        'ninguno'

cliente = {'nombre' : 'Federico',
           'edad':  45,
           'ocupacion': 'instructor'}
pelicula = {'titulo': 'Matrix',
            'ficha tecnica':{'Protagonista': 'KR',
                             'director': 'LLW'}}
elementos=[cliente, pelicula, 'libro']

print(elementos)

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un clienta")
            print(nombre,edad,ocupacion)

        case {'titulo': titulo,
            'ficha tecnica':{'Protagonista': protagonista,
                             'director': director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print('no se')






