import pygame as pg
from figura_class import Pelota,Raqueta

ANCHO = 800
ALTO = 600

class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()

        self.pelota = Pelota(ANCHO//2,ALTO//2,vx=2,vy=2)
        self.raqueta1 = Raqueta(10,ALTO//2,vy=5)
        self.raqueta2 = Raqueta(ANCHO-10,ALTO//2,vy=5)

        self.font = pg.font.Font(None, 30)

        

    def bucle_fotograma(self):

      
        game_over = False
       
        
        while not game_over:

          
            self.tasa_refresco.tick(280)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.raqueta1.mover(pg.K_w,pg.K_s)
            self.raqueta2.mover(pg.K_i,pg.K_k)
            self.pelota.mover()

            self.pantalla_principal.fill((0,128,94))
            self.pelota.comprobar_choqueV2(self.raqueta2,self.raqueta1)
            self.pelota.marcador(self.pantalla_principal)
            
            cont_linea1=0
            cont_linea2=50
            while cont_linea1 <= 560 and cont_linea2 <= 630:
                pg.draw.line(self.pantalla_principal, (255,255,255), (400,cont_linea1), (400,cont_linea2), width=10)
                cont_linea1 += 70
                cont_linea2 += 70
        

            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            self.mostrar_jugador()
            
            pg.display.flip()

        pg.quit()       


    def mostrar_jugador(self):
        jugador1 = self.font.render("Jugador 1",0, (255,255,0))
        jugador2 = self.font.render( "Jugador 2",0, (255,255,0))
        self.pantalla_principal.blit(jugador1, (200, 30))
        self.pantalla_principal.blit(jugador2, (600, 30 ))
