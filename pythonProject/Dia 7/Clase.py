class Pajaro:
    alas = True
    #Metodo Constructor
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
    #Metodo de instacia
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self,metros):
        print(f"el pajaro ha volado {metros} mtrs")
        self.piar()

    def pintar_negro(self):
        print("Ahora el pájaro es negro")
    #Metodo de clase
    @classmethod   #no requiere de instacia y no tiene acceso a los atributos de los metodos de los metodos de instacia si con los de clase
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas=False
      #Metodo Estatico
    @staticmethod #no se relaciona con la instacia ni con las clases sirve para lo que no se puede modificar
    def mirar():
        print("El pajaro mira")



mi_pajaro = Pajaro('negro','Tucan')
print(mi_pajaro.color)

print(Pajaro.alas)

piolin= Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(9)

piolin.alas=False
print(piolin.alas)

Pajaro.poner_huevos(3)
