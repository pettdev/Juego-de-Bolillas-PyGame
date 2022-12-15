import pygame as pg


class Rectangulo():


    def __init__(self, ancho:int, alto:int, color:tuple, pos_x:int, pos_y:int, max_an:int, max_al:int, surface, velocidad:int):
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_al = max_al
        self.max_an = max_an
        self.velocidad = velocidad
        self.vx = velocidad
        self.vy = velocidad
        self.lim_x = max_an - ancho
        self.lim_y = max_al - alto
        self.surface = surface


    def mover(self):
        self.pos_x += self.vx
        print('self.pos_x += self.vx =', self.pos_x)
        self.pos_y += self.vy
        
        if self.pos_x >= self.lim_x or self.pos_x <= 0:
            self.vx *= -1
            print('self.vx *= -1 =', self.vx)
        if self.pos_y >= self.lim_y or self.pos_y <= 0:
            self.vy *= -1
    

    def dibujar(self):
        print('pos_x dibujar:', self.pos_x)
        print('vx dibujar:', self.vx)
        
        pg.draw.rect(self.surface, (self.color), (self.pos_x, self.pos_y, self.ancho, self.alto))


class Bola():


    def __init__(self, radio, color:tuple, pos_x:int, pos_y:int, max_an:int, max_al:int, surface, velocidad:int):
        self.radio = radio
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_al = max_al
        self.max_an = max_an
        self.velocidad = velocidad
        self.vx = velocidad
        self.vy = velocidad
        self.surface = surface


    def mover(self):
        self.pos_x += self.vx
        self.pos_y += self.vy
        
        if self.pos_x <= (0 + self.radio) or self.pos_x >= (self.max_an - self.radio):
            self.vx *= -1
        if self.pos_y <= (0 + self.radio) or self.pos_y >= (self.max_al - self.radio):
            self.vy *= -1
    

    def dibujar(self):
        pg.draw.circle(self.surface, (self.color), (self.pos_x, self.pos_y), self.radio)