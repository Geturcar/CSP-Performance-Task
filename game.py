import pygame, sys
import time

pygame.init()
clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 600
FPS = 60


screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
bg=pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
player_posA = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
player_posB = pygame.Vector2(3*screen.get_width() / 4, screen.get_height() / 2)


d_t = 1 / FPS
Char1_posx= 200
Char1_posy= 200
speed=1000

class Character:
    def __init__(self, x,y,width, height):
        self.x= x
        self.y= y
        self.width = width
        self.height = height
    def move(self, _speed):
        self.x-= _speed * d_t
        for cc in chara_under:
            cc.move(_speed)
    def draw(self):
        Char1= pygame.Rect(self.x,self.y, self.width, self.height)
        pygame.draw.rect(screen, 'red', Char1)
        for cc in chara_under:
            cc.draw()

class Character2(Character):
    def __init__(self, x, y, width, height, x_shift):
        super().__init__(x, y, width, height)
        self.x_shift = x_shift
    def move(self, _speed):
        self.x-= _speed * d_t
    def draw(self):
        Char1= pygame.Rect(self.x + self.x_shift,self.y, self.width, self.height)
        pygame.draw.rect(screen, 'red', Char1)

chara = Character(Char1_posx, Char1_posy, 50,50)
chara_under = [Character2(Char1_posx, Char1_posy, 50,50, 800), Character2(Char1_posx, Char1_posy+20,800, 10,0)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                chara.move(speed)
            elif event.key == pygame.K_RCTRL:
                chara.move(-speed)



    screen.blit(bg, (0,0))

    chara.draw()


    
    clock.tick(FPS)    
    pygame.display.flip()
      # limits FPS to 60
