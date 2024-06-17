"""
Uso de Pygame
"""

import pygame
import random
import math
import time
from pygame import mixer
import io

# Inicializa pygame
pygame.init()

# Crea la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Agregar Musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(.3)
mixer.music.play(-1)


# Titulo e icono
pygame.display.set_caption('Invasión Espacial')
# icono de Flaticon
icono = pygame.image.load("space-ship.png")
pygame.display.set_icon(icono)

# Jugador
jugador_img = pygame.image.load('jugador.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0


# Enemigo
enemigo_img = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
enemigo_cantidad = 8
enemigo_muerto_sonido = mixer.Sound('Golpe.mp3')

for enemigo in range(enemigo_cantidad):
    enemigo_img.append( pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(+50)
    time.sleep(.01)

# Fondo
fondo = pygame.image.load('fondo.png')

# Bala
bala_img = pygame.image.load('bala.png')
bala_x = 0
bala_y = 0
bala_x_cambio = 0
bala_y_cambio = -1
bala_visible = False
bala_sonido = mixer.Sound('disparo.mp3')


def fuente_bytes(fuentes):

    # Abre el archivo TTF en modo lectura binaria
    with open(fuentes, 'rb') as f:
        # Lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
    # Crea un objeto de BytesIO a partir de los bytes del archivo TTF
    return io.BytesIO(ttf_bytes)

# Puntaje
puntaje = 0
fuente_como_byte = fuente_bytes('freesansbold.ttf')

fuente = pygame.font.Font(fuente_como_byte, 32)
texto_x = 10
texto_y = 10

# Texto Final del juego
fuente_final = pygame.font.Font(fuente_como_byte, 40)
terminado = False

def texto_final():
    """
    muestra game over
    :return:
    """
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO', True, (255,255,255))
    pantalla.blit(mi_fuente_final,(220, 300))


def mostrar_puntaje(x, y):
    """
    muestra el puntaje
    :return:
    """
    texto = fuente.render(f"Natalias :(: {puntaje}", True,(255, 255, 255))
    pantalla.blit(texto, (x, y))


def jugador(x, y):
    """
    ubica el judagor en la pantalla
    :return:
    """
    pantalla.blit(jugador_img,(x,y))


def enemigo(enemigo_imagen, x, y):
    """
    ubica el enemigo en la pantalla
    :return:
    """
    pantalla.blit(enemigo_imagen,(x,y))


def disparar_bala(x, y):
    """
    movimiento de la bara
    :param x:
    :param y:
    :return:
    """
    global bala_visible
    bala_visible = True
    pantalla.blit(bala_img, (x + 16, y - 26))


def hay_colision(x1, x2, y1, y2):
    """
    calcula la distancia entre el enemigo y la bala
    :param x1:
    :param x2:
    :param y1:
    :param y2:
    :return:
    """
    distacia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distacia < 40:
        print('cho')
        return True
    else:
        return False






# Mantiene la pantalla y captura los eventos
se_ejecuta = True
while se_ejecuta:
    # pantalla.fill((205,144,228))
    # pantalla.fill((190, 130, 255))
    pantalla.blit(fondo,(0, 0))

# Movimiento del jugador
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if not terminado:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_x_cambio = -1
                if evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 1
                if evento.key == pygame.K_DOWN:
                    jugador_y_cambio = 1
                if evento.key == pygame.K_UP:
                    jugador_y_cambio = -1
                if evento.key == pygame.K_SPACE:
                    if not bala_visible:
                        bala_sonido.play()
                        bala_x = jugador_x
                        bala_y = jugador_y
                        disparar_bala(bala_x, bala_y)

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 0

                if evento.key == pygame.K_DOWN or evento.key == pygame.K_UP:
                    jugador_y_cambio = 0

    # Modificar ubicacion del Jugador
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio

    # Mantener entre los bordes al jugador
    if jugador_x < 0:
        jugador_x = 0
    elif jugador_x > 736:
        jugador_x = 736
    if jugador_y < 0:
        jugador_y = 0
    elif jugador_y > 536:
        jugador_y = 536

    jugador(jugador_x, jugador_y)

    # Modificar ubicacion del enemigo
    for e in range(enemigo_cantidad):
        # Calculo de Colision entre enemigo y jugador
        colision = hay_colision(jugador_x, enemigo_x[e], jugador_y, enemigo_y[e])
        if colision or jugador_y > 500:
            for k in range(enemigo_cantidad):
                enemigo(enemigo_img[k], -100, 1000)
            texto_final()
            jugador_y_cambio = 0
            jugador_x_cambio = 0
            terminado = True

            break
        if enemigo_x[e] < 0 or enemigo_x[e] > 736:
            enemigo_x_cambio[e] *= -1
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_y[e] > 536:
            enemigo_y[e] = random.randint(50, 200)

        # Mantener entre los bordes al enemigo
        enemigo_x[e] += enemigo_x_cambio[e]
        enemigo(enemigo_img[e], enemigo_x[e], enemigo_y[e])

        if bala_visible:
            # Calculo de Colision entre enemigo y bala
            colision = hay_colision(bala_x, enemigo_x[e], bala_y, enemigo_y[e])

            if colision:
                bala_visible = False
                puntaje += 1
                print(puntaje)
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)
                enemigo_muerto_sonido.play()







    # Movimiento de la bala
    if bala_visible:
        bala_y += bala_y_cambio
        disparar_bala(bala_x, bala_y)
        if bala_y <= -64:
            bala_visible = False
    mostrar_puntaje(texto_x,texto_y)
    pygame.display.update()

