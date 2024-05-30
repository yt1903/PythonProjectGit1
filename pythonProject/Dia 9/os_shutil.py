"""
Manejo de archivos a mas profundidad
"""
import os
import shutil

archivo = open('pruebaos.txt', 'w')
archivo.write('Prueba uso libreria os')
archivo.close()

shutil.move('pruebaos.txt','C:\\Users\\yasmi\\Cursos')
os.remove('C:\\Users\\yasmi\\Cursos\\pruebaos.txt')

# es un generador y hay que pedir uno a uno
print(os.walk('C:\\Users\\yasmi\\Cursos'))


for carpeta, subcarpeta, archivo in os.walk('C:\\Users\\yasmi\\Cursos'):
    print(f'en la carpeta {carpeta}')
    print(f'en la subcarpeta son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f"\t{arch}")
    print('\n')

# os y shutil dan todas las funciones para manejo de archivo
"""
para poder enviar archivos a la papelera hay que instalar
pip  install send2trash
y luego 
import send2trash
"""

