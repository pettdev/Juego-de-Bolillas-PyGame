import pygame as pg

#Inicializar todos los modulos pygame
#pantallas, sonidos, teclados, etc
pg.init()

# Crear pantalla o Surface
pantalla_principal = pg.display.set_mode( (800, 600) ) # Ventana y tamaño, con Ancho y Largo
pg.display.set_caption("Bolillas Rebotando") # Titulo para la ventana

game_over = False

x = 400
y = 300
vx = 1
vy = 1

z = 000
a = 000
vz = 0.5
va = 0.5

while not game_over:

    for eventos in pg.event.get(): # Captura todos los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (52, 152, 219) ) #Asignar color a la pantalla

    x += vx
    y += vy
    z += vz
    a += va

    if x >= 780 or x == 0:
        vx *= -1
    if y >= 580 or y == 0:
        vy *= -1
    if z >= 780 or z == 0:
        vz *= -1
    if a >= 580 or a == 0:
        va *= -1
    

    # Crear un rectángulo que tenga largo y ancho
    #dibujar(pantalla, (color RGB), (Coord. Posicion An x La, tamaño An, Tamaño La))
    pg.draw.rect(pantalla_principal, (192, 57, 43), (x, y, 20, 20))
    pg.draw.rect(pantalla_principal, (50, 168, 82), (z, a, 40, 40))

    pg.display.flip() #Para aplicar todo el añadido de arriba.
