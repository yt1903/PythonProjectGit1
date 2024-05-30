"""import zipfile


mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
mi_zip.write('texto1.txt')
mi_zip.write('texto2.txt')

mi_zip.close()

mi_archivo = zipfile.ZipFile('archivo_comprimido.zip')
mi_archivo.extractall()

mi_archivo.close()"""

import shutil
carpeta_origen = "c:\\ruta"
archivo_destino = "c:\\carpeta_compromida"
shutil.make_archive(archivo_destino,'zip', carpeta_origen)

# descopromir
shutil.unpack_archive('carpeta_comprimida', 'extraccion terminada', 'zip')


