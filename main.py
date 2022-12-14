import pygame as pg
from bolilla_mia import *

#Inicializar todos los modulos pygame
#pantallas, sonidos, teclados, etc
pg.init()

# Crear pantalla o Surface
ancho_pant = 600
alto_pant = 800

pantalla_principal = pg.display.set_mode( (alto_pant, ancho_pant) ) # Ventana y tamaño, con Ancho y Largo
pg.display.set_caption("Bolillas Rebotando") # Titulo para la ventana

game_over = False
velocidad = 0.1

bola = Bolilla(20, 20, (255, 225, 93), 400, 300, ancho_pant, alto_pant, velocidad)
bola1 = Bolilla(20, 20, (244, 157, 26), 0, 246, ancho_pant, alto_pant, velocidad)
bola2 = Bolilla(20, 20, (233, 53, 53), 350, 0, ancho_pant, alto_pant, velocidad)
bola3 = Bolilla(20, 20, (175, 30, 104), 784, 75, ancho_pant, alto_pant, velocidad)
bola4 = Bolilla(20, 20, (224, 53, 53), 376, 147, ancho_pant, alto_pant, velocidad)
bola5 = Bolilla(20, 20, (106, 30, 104), 276, 55, ancho_pant, alto_pant, velocidad)
bola6 = Bolilla(20, 20, (200, 53, 53), 575, 242, ancho_pant, alto_pant, velocidad)
bola7 = Bolilla(20, 20, (0, 0, 0), 800, 200, ancho_pant, alto_pant, velocidad)
bola8 = Bolilla(20, 20, (211, 53, 53), 30, 200, ancho_pant, alto_pant, velocidad)
bola9 = Bolilla(20, 20, (158, 30, 104), 185, 0, ancho_pant, alto_pant, velocidad)

while not game_over:

    for eventos in pg.event.get(): # Captura todos los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (192, 238, 228) ) #Asignar color a la pantalla

    # Crear un rectángulo que tenga largo y ancho

    #dibujar(pantalla, (color RGB), (Coord. Posicion An x La, tamaño An, Tamaño La))
    """ pg.draw.rect(pantalla_principal, (192, 57, 43), (x, y, 20, 20)) """

    pg.draw.rect(pantalla_principal, bola.color, (bola.mover()[0], bola.mover()[1], bola.ancho, bola.alto))
    pg.draw.rect(pantalla_principal, bola1.color, (bola1.mover()[0], bola1.mover()[1], bola1.ancho, bola1.alto))
    pg.draw.rect(pantalla_principal, bola2.color, (bola2.mover()[0], bola2.mover()[1], bola2.ancho, bola2.alto))
    pg.draw.rect(pantalla_principal, bola3.color, (bola3.mover()[0], bola3.mover()[1], bola3.ancho, bola3.alto))
    pg.draw.rect(pantalla_principal, bola4.color, (bola4.mover()[0], bola4.mover()[1], bola4.ancho, bola4.alto))
    pg.draw.rect(pantalla_principal, bola5.color, (bola5.mover()[0], bola5.mover()[1], bola5.ancho, bola5.alto))
    pg.draw.rect(pantalla_principal, bola6.color, (bola6.mover()[0], bola6.mover()[1], bola6.ancho, bola6.alto))
    pg.draw.rect(pantalla_principal, bola7.color, (bola7.mover()[0], bola7.mover()[1], bola7.ancho, bola7.alto))
    pg.draw.rect(pantalla_principal, bola8.color, (bola8.mover()[0], bola8.mover()[1], bola8.ancho, bola8.alto))
    pg.draw.rect(pantalla_principal, bola9.color, (bola9.mover()[0], bola9.mover()[1], bola9.ancho, bola9.alto))
    pg.display.flip() #Para aplicar todo el añadido de arriba.