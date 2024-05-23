mi_lista = [1, 1, 1, 1, 1, 1, 1, 1]
print(len(mi_lista))


class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor= autor
        self.titulo= titulo
        self.canciones=canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.autor} "
    def  __len__(self):
        return len(self.canciones)
    def __del__(self):
        print('Se elimino el cs')


mi_cd=CD('Marco','el tuyo', 'bella')

print(len(mi_cd))
print(mi_cd)

del mi_cd ###elimina la instancia