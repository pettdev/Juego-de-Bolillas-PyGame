import pygame as pg
from clase_bolilla import *

#Inicializar todos los modulos pygame
#pantallas, sonidos, teclados, etc
pg.init()

# Crear pantalla o Surface
ancho_pant = 600
alto_pant = 800
pantalla_principal = pg.display.set_mode( (alto_pant, ancho_pant) ) # Ventana y tamaño, con Ancho y Largo
pg.display.set_caption("Bolillas Rebotando") # Titulo para la ventana

game_over = False

velocidad = 1

coord = Limites(400, 300, 20, 20, ancho_pant, alto_pant, velocidad)
coord1 = Limites(200, 100, 20, 20, ancho_pant, alto_pant, velocidad)
coord2 = Limites(100, 200, 20, 20, ancho_pant, alto_pant, velocidad)
coord3 = Limites(300, 150, 20, 20, ancho_pant, alto_pant, velocidad)

bola, bola1, bola2, bola3 = Bolilla, Bolilla, Bolilla, Bolilla


while not game_over:

    for eventos in pg.event.get(): # Captura todos los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (52, 152, 219) ) #Asignar color a la pantalla

    # Crear un rectángulo que tenga largo y ancho

    #dibujar(pantalla, (color RGB), (Coord. Posicion An x La, tamaño An, Tamaño La))
    """ pg.draw.rect(pantalla_principal, (192, 57, 43), (x, y, 20, 20)) """

    bola(20, 20, (192, 57, 36), pantalla_principal, coord.coordLimites()[0], coord.coordLimites()[1])
    bola1(20, 20, (132, 13, 74), pantalla_principal, coord1.coordLimites()[0], coord1.coordLimites()[1])
    bola2(20, 20, (111, 86, 18), pantalla_principal, coord2.coordLimites()[0], coord2.coordLimites()[1])
    bola3(20, 20, (98, 32, 96), pantalla_principal, coord3.coordLimites()[0], coord3.coordLimites()[1])

    pg.display.flip() #Para aplicar todo el añadido de arriba.