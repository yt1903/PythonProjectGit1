import os #Sistema operativo


ruta = os.getcwd()
print((ruta))

ruta = os.chdir("C:\\Users\\yasmi\\Cursos")
print((ruta))

mi_archivo= open('prueba.txt')
print(mi_archivo.read())

ruta = "C:\\Users\\yasmi\\Cursos\\prueba.txt"

print(os.path.basename(ruta))
print(os.path.dirname(ruta))
os.makedirs()

