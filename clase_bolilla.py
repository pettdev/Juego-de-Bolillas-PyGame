import pygame as pg

class Bolilla():

    def __init__(self, ancho:int, alto:int, color:tuple, pantalla:int, x:int, y:int):
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.pantalla = pantalla
        self.x = x
        self.y = y
        self.crear_bolilla()

    def crear_bolilla(self):
        return pg.draw.rect(self.pantalla, self.color, (self.x, self.y, self.ancho, self.alto))


class Limites():

    def __init__(self, x:int, y:int, width:int, height:int, lim_al:int, lim_an:int, speed:int):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.lim_al = lim_al
        self.lim_an = lim_an
    

    def coordLimites(self):
            espacioX = 0
            espacioY = 0

            espacioX = self.lim_an - self.width
            espacioY = self.lim_al - self.height

            self.x += self.speed
            self.y += self.speed
            
            if self.x <= espacioX or self.x == 0:
                self.speed *= -1
            elif self.y <= espacioY or self.y == 0:
                self.speed *= -1

            xResult = self.x
            yResult = self.y
            
            return xResult, yResult