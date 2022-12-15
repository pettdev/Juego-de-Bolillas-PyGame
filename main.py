import pygame as pg
from figuras_mias import *
import random as rn

#Inicializar todos los modulos pygame
#pantallas, sonidos, teclados, etc
pg.init()

# Crear pantalla o Surface
ancho_pant = 800
alto_pant = 600

pantalla_principal = pg.display.set_mode( (ancho_pant, alto_pant) ) # Ventana y tamaño, con Ancho y Largo
pg.display.set_caption("Bolillas Rebotando") # Titulo para la ventana

game_over = False
velocidad = 0.2 

listaCuadritos = []
listaBolillas = []

for i in range (0, 6):
    listaCuadritos.append(Rectangulo(15, 15, (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255)), rn.randint(-999, 1000), rn.randint(-999, 1000), ancho_pant, alto_pant, pantalla_principal, velocidad))
for i in range (0, 6):
    listaBolillas.append(Bola(rn.randint(5, 15),(rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255)), rn.randint(0, 800), rn.randint(0, 600), ancho_pant, alto_pant, pantalla_principal, velocidad))

while not game_over:

    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((192, 238, 228))

    for cuadro in listaCuadritos:
        cuadro.dibujar()
        cuadro.mover()

    for bolita in listaBolillas:
        bolita.dibujar()
        bolita.mover()

    pg.display.flip()