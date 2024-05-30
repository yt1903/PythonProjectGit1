"""
modulo re para hacer busquedas en una cadena de texto y establecer mascaras para
datos como telefonos correos codigos
"""
import re

texto = 'si necesitas ayuda llama al 564-525-6588 para ayuda'
palabra = 'ayuda' in texto
print(palabra)

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())
print(re.findall(patron, texto))

for x in re.finditer(patron, texto):
    print(x.span())


# Uso de marcaras

patron = r'\d\d\d-\d\d\d-\d\d\d\d'

patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron,texto)
print(resultado)
print(resultado.group())

patron = r'(\d{3})-(\d{3})-(\d{4})'
resultado = re.search(patron,texto)
print(resultado)
print(resultado.group())
print(resultado.group(3))


"""clave = input('Clave: ')
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)
print(chequear)"""


texto = 'No atendemos los lunes ni martes'
buscar = re.search(r'lunes|martes', texto)
print('con o')
print(buscar)


buscar = re.search(r'demos', texto)
print(buscar)

buscar = re.search(r'.demos', texto)
print(buscar)

buscar = re.search(r'..demos', texto)
print(buscar)

buscar = re.search(r'^\D', texto) # principio de la cadena
print(buscar)

buscar = re.search(r'\D$', texto) # final de la cadena
print(buscar)

buscar = re.findall(r'[^\s+]+', texto) # final de la cadena
print(buscar)


correo = input('Correo: ')
patron = r'\w{1,}@\w{1,}.com'
patron = r'@\w+.com'
chequear = re.search(patron, correo)
print(chequear)