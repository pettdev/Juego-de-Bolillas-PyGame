class Bolilla():

    def __init__(self, ancho:int, alto:int, color:tuple, pos_x:int, pos_y:int, pant_al:int, pant_an:int, velocidad:int):
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pant_al = pant_al
        self.pant_an = pant_an
        self.velocidad = velocidad
        self.vx = velocidad
        self.vy = velocidad
        self.lim_x = pant_an - ancho
        self.lim_y = pant_al - alto

    def mover(self):
        self.pos_x += self.vx
        self.pos_y += self.vy
        
        if self.pos_x >= self.lim_x or self.pos_x <= 0:
            self.vx *= -1
        if self.pos_y >= self.lim_y or self.pos_y <= 0:
            self.vy *= -1
        
        return self.pos_x, self.pos_y