from pathlib import Path, PureWindowsPath
carpeta =Path("/Users/yasmi/Cursos") #esto lo lee windows o Mac
archivo= carpeta / "prueba.txt"
print(archivo)
ruta_windows = PureWindowsPath(archivo)
print(ruta_windows)
print(archivo.read_text())
print(archivo.name)
print(archivo.suffix)
print(archivo.stem)

if not archivo.exists():
    print('no existe')

base= Path.home()
print(base)
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada Familia"))

print('guia')

guia = Path("C:/Users/yasmi/Europa/España")/'Barcelona'/'Sagrada Familia/prueba.txt'
print('Parents')
print(guia.parents[0])
print(guia.parents[1])
print(guia.parents[2])
print(guia.parents[3])
print(guia.stem)

guia2= guia.with_name('La Pedrera')
print(guia2)
print(guia.parent)
print(guia.parent.parent)


"""guia= Path(Path.home(),"nombreCarpeta")
for txt in Path(guia).glob("**/*".txt):
    print(txt)

guia = Path(base,"Europa","España",Path("Barcelona","Sagrada Familia"))
en_europa =guia.relative_to(Path("Europa"))
en_europa =guia.relative_to(Path("Europa","España"))
"""