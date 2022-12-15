import pygame as pg
from figuras_mias import *

#Inicializar todos los modulos pygame
#pantallas, sonidos, teclados, etc
pg.init()

# Crear pantalla o Surface
ancho_pant = 800
alto_pant = 600

pantalla_principal = pg.display.set_mode( (ancho_pant, alto_pant) ) # Ventana y tamaño, con Ancho y Largo
pg.display.set_caption("Bolillas Rebotando") # Titulo para la ventana

game_over = False
velocidad = 1 

cuadrado1 = Rectangulo(20, 20, (244, 157, 26), 0, 246, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado2 = Rectangulo(20, 20, (233, 53, 53), 350, 0, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado3 = Rectangulo(20, 20, (175, 30, 104), 779, 10, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado4 = Rectangulo(20, 20, (224, 53, 53), 376, 147, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado5 = Rectangulo(20, 20, (106, 30, 104), 276, 55, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado6 = Rectangulo(20, 20, (200, 53, 53), 575, 242, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado7 = Rectangulo(20, 20, (255, 255, 255), 800, 200, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado8 = Rectangulo(20, 20, (211, 53, 53), 30, 200, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado9 = Rectangulo(20, 20, (158, 30, 104), 185, 0, ancho_pant, alto_pant, pantalla_principal, velocidad)
cuadrado10 = Rectangulo(20, 20, (255, 225, 93), 400, 300, ancho_pant, alto_pant, pantalla_principal, velocidad)

ball1 = Bola(20, (154, 220, 255), 456, 200, ancho_pant, alto_pant, pantalla_principal, velocidad)
ball2 = Bola(20, (255, 248, 154), 250, 579, ancho_pant, alto_pant, pantalla_principal, velocidad)
ball3 = Bola(20, (255, 178, 166), 113, 430, ancho_pant, alto_pant, pantalla_principal, velocidad)
ball4 = Bola(20, (255, 138, 174), 200, 320, ancho_pant, alto_pant, pantalla_principal, velocidad)

while not game_over:

    for eventos in pg.event.get(): # Captura todos los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (192, 238, 228) ) #Asignar color a la pantalla

    cuadrado1.dibujar()
    cuadrado2.dibujar()
    cuadrado3.dibujar()
    cuadrado4.dibujar()
    cuadrado5.dibujar()
    cuadrado6.dibujar()
    cuadrado7.dibujar()
    cuadrado8.dibujar()
    cuadrado9.dibujar()
    cuadrado10.dibujar()

    ball1.dibujar()
    ball2.dibujar()
    ball3.dibujar()
    ball4.dibujar()

    cuadrado1.mover()
    cuadrado2.mover()
    cuadrado3.mover()
    cuadrado4.mover()
    cuadrado5.mover()
    cuadrado6.mover()
    cuadrado7.mover()
    cuadrado8.mover()
    cuadrado9.mover()
    cuadrado10.mover()

    ball1.mover()
    ball2.mover()
    ball3.mover()
    ball4.mover()

    pg.display.flip() #Para aplicar todo el añadido de arriba.