import sys
import pygame
from pygame import event
import numpy as np
from pygame import draw
import time

from pygame import mouse

# inicializacion de la pantalla
pygame.init()

# ancho y alto de la pantalla
width, height = 1000, 1000

# creacion de la pantallla
screen = pygame.display.set_mode((height, width))

# Colores
bg = 25, 25, 25
white = 255, 255, 255
screen.fill(bg)

# especificacion de cuadros en ejes
ncX, ncY = 200, 200

# ancho
cuW = width / ncX
# alto cuadros
cuH = height / ncY

# Esatado de la celda. Vivas = 1, Muertas = 0
gameState = np.zeros((ncX, ncY))

gameState[int(ncX/2), 0] = 1

pauseExect = False
#       128 64 32 16 8  4  2  1
rules = [0, 1, 1, 0, 1, 1, 1, 0]
# crear otro funcion que creee la reglas a partir de un numero entero a un binario

# funcion para reproducir los sonidos


for y in range(0, ncY):
    for x in range(0, ncX):
        # se crea el poligono de para cada celda
        poly = [(x * cuW, y * cuH),
                ((x+1) * cuW, y * cuH),
                ((x+1) * cuW, (y+1) * cuH),
                (x * cuW, (y+1) * cuH)]
        # se dibujan los cuadrados para x y para y
        pygame.draw.polygon(screen, white, poly, 1)

y = 0

while True:

    newGameState = np.copy(gameState)

    # registro del teclado o mouse
    ev = pygame.event.get()

    for e in ev:
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed(num_buttons=3)

        if mouseClick[0] == True:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/cuW)), int(np.floor(posY/cuH))
            newGameState[celX, celY] = 1

    for x in range(0, ncX):
        # se crea el poligono de para cada celda
        ruleIdx = 4 * gameState[(x-1) % ncX, y] + 2 * \
            gameState[(x) % ncX, y] + 1 * gameState[(x+1) % ncX, y]

        newGameState[x, (y+1) % ncY] = rules[int(ruleIdx)]

        poly = [(x * cuW, y * cuH),
                ((x+1) * cuW, y * cuH),
                ((x+1) * cuW, (y+1) * cuH),
                (x * cuW, (y+1) * cuH)]

        # se dibujan los cuadrados para x y para y
        if newGameState[x, y] == 1:
            pygame.draw.polygon(screen, (0, 128, 0), poly, 0)

    if not pauseExect:
        y = (y+1) % ncY

    time.sleep(0.1)
    # actualizamos el juego
    gameState = np.copy(newGameState)
    pygame.display.flip()
