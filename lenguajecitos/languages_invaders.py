#posiciones: Posx, Posy, Tamx, Tamy
import pygame, sys, random

pygame.init()
reloj = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((1280,720))

class JavaScripts(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.v_x = 10
        self.v_y = 10
        self.image = pygame.image.load("imagenes/javascript64.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 40
    def update(self):
        self.rect.y += self.v_y

class GloriosoPython(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.v_x = 20
        #self.v_y = 10
        self.image = pygame.image.load("imagenes/plogo64.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 640
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x-=self.v_x
        if keys[pygame.K_s]:
            self.rect.x+=self.v_x  

#Instanciamos lo que va a ir en el juego
sprites = pygame.sprite.Group()
enemigo_js = JavaScripts()
sprites.add(enemigo_js)
navecita = GloriosoPython()
sprites.add(navecita)

NEGRO = (0,0,0)
ROJO = (255,0,0)
pygame.display.set_caption('Lenguajecitos invader')
icono = pygame.image.load("imagenes/linvaders.png")
fondo = pygame.image.load("imagenes/fondo11280720.jpg").convert()
epx = random.randint(64, 1216)
epy = 20

pygame.display.set_icon(icono)

while True:
    reloj.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    sprites.update()
    PANTALLA.blit(fondo, (0,0))
    sprites.draw(PANTALLA)
    pygame.display.flip()