import pygame as pg


class Rectangulo():


    def __init__(self, ancho:int, alto:int, color:tuple, pos_x:int, pos_y:int, max_an:int, max_al:int, surface, velocidad:int):
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_al = max_al - self.ancho
        self.max_an = max_an - self.alto
        self.velocidad = velocidad
        self.vx = velocidad
        self.vy = velocidad
        self.surface = surface


    def mover(self):

        # # # # # # # DENTRO DE LOS LÍMITES DEL EJE X & EJE Y # # # # # #
        # EJE X: pos_x >= 0 and pos_x < MÁX_ANCHO
        # EJE Y: pos_y >= 0 and pos_y < MÁX_ALTO
        #
        # EL ORIGEN (0,0) DE LA -PANTALLA-, SON EL LÍMITE *INFERIOR* DE CADA EJE
        # LA ANCHO Y ALTO DE LA -PANTALLA-, SON EL LÍMITE -SUPERIOR- DE CADA EJE
        # 
        # EL LÍMITE INFERIOR PUEDE SER IGUAL 0
        # EL LÍMITE SUPERIOR DEBE TENDER HACIA EL ANCHO/ALTO DE LA VENTANA (MAS NO LLEGAR)
        
        if self.pos_x < 0: # Si pos_x es menor que cero:
            self.pos_x = 0 # -> pos_x estará dentro del límite inferior del eje x

        if self.pos_x >= self.max_an: # Si pos_x es mayor/igual que el límite del ancho:
            self.pos_x = self.max_an - 1 # --> pos_x estará dentro del límite superior del eje x

        elif self.pos_y < 0: # Si pos_y es menor que cero:
            self.pos_y = 0 # --> pos_y estará dentro del límite inferior del eje y

        if self.pos_y >= self.max_al: # Si pos_y es mayor/igual que el límite del alto:
            self.pos_y = self.max_al - 1 # --> pos_y estará dentro del límite superior del eje y

        self.pos_x += self.vx # --> moverá horizontalmente a la figura
        self.pos_y += self.vy # --> moverá verticalmente a la figura
        
        # Si pos_x es menor al ancho de la pantalla o menor/igual que cero:
        if self.pos_x >= self.max_an or self.pos_x <= 0:
            self.vx *= -1 # --> pos_x cambiará de dirección (opuesta)
        
        # Si pos_y es menor al alto de la pantalla o menor/igual que cero:
        if self.pos_y >= self.max_al or self.pos_y <= 0:
            self.vy *= -1 # --> pos_y cambiará de dirección (opuesta)
    

    def dibujar(self):
        pg.draw.rect(self.surface, (self.color), (self.pos_x, self.pos_y, self.ancho, self.alto))


class Bola():


    def __init__(self, radio, color:tuple, pos_x:int, pos_y:int, max_an:int, max_al:int, surface, velocidad:int):
        self.radio = radio
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_al = max_al - self.radio
        self.max_an = max_an - self.radio
        self.velocidad = velocidad
        self.vx = velocidad
        self.vy = velocidad
        self.surface = surface


    def mover(self):

        # # # # # # # DENTRO DE LOS LÍMITES DEL EJE X & EJE Y # # # # # #
        # EJE X: pos_x >= radio and pos_x < MÁX_ANCHO
        # EJE Y: pos_y >= radio and pos_y < MÁX_ALTO
        #
        # EL RADIO, ES EL LÍMITE INFERIOR DE CADA EJE
        # LA ALTURA Y ANCHO DE LA PANTALLA, SON EL LÍMITE SUPERIOR DE CADA EJE
        # 
        # EL LÍMITE INFERIOR PUEDE SER IGUAL AL RADIO
        # EL LÍMITE SUPERIOR DEBE TENDER HACIA EL ALTO/ANCHO DE LA VENTANA (MAS NO LLEGAR)

        if self.pos_x < self.radio: # Si pos_x es menor al radio:
            self.pos_x = self.radio # -> pos_x estará dentro del límite inferior del eje x

        elif self.pos_x >= self.max_an: # Si pos_x es mayor/igual que el límite del ancho:
            self.pos_x = self.max_an - 1 # --> pos_x estará dentro del límite superior del eje x

        elif self.pos_y < self.radio: # Si pos_y es menor al radio:
            self.pos_y = self.radio # --> pos_y estará dentro del límite inferior del eje y

        elif self.pos_y >= self.max_al: # Si pos_y es mayor/igual que el límite del alto:
            self.pos_y = self.max_al - 1 # --> pos_y estará dentro del límite superior del eje y

        self.pos_x += self.vx # --> moverá horizontalmente a la figura
        self.pos_y += self.vy # --> moverá verticalmente a la figura

        # Si pos_x es menor/igual al radio o mayor al ancho de la pantalla:
        if self.pos_x <= self.radio or self.pos_x >= self.max_an:
            self.vx *= -1 # --> pos_x cambiará de dirección (opuesta)
            
        # Si pos_y es menor/igual al radio o mayor al ancho de la pantalla:
        elif self.pos_y <= self.radio or self.pos_y >= self.max_al:
            self.vy *= -1 # --> pos_y cambiará de dirección (opuesta)
    

    def dibujar(self):
        pg.draw.circle(self.surface, (self.color), (self.pos_x, self.pos_y), self.radio)