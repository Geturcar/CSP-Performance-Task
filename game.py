import pygame, sys

head_list = ["head1.png","head2.png", "head3.png"]
body_list = ["body1.png","body2.png", "body3.png"]
leg_list = ["leg1.png","leg2.png", "leg3.png"]

print("Player 1 skin select")
while True:
        Head = input("Select a head (Buisnessman, Gamer, King): ")
        if Head.lower == "buisnessman":
            print ("You have selected the Buisnessman head")
            index_head = 0
            break
        elif Head.lower == "gamer":
            print ("You have selected the Gamer head")
            index_head = 1
            break
        elif Head.lower == "king":
            print ("You have selected the King head")
            index_head = 2
            break
        else:
            print("Please select one of the given heads")  

while True:
        Body = input("Select a body (Buisnessman, Gamer, King): ")
        if Body.lower == "buisnessman":
            print ("You have selected the Buisnessman body")
            index_body = 0
            break
        elif Body.lower == "gamer":
            print ("You have selected the Gamer body")
            index_body = 1
            break
        elif Body.lower == "king":
            print ("You have selected the King body")
            index_body = 2
            break
        else:
            print("Please select one of the given bodies")
while True:
        Legs = input("Select a body (Buisnessman, Gamer, King): ")
        if Legs.lower == "buisnessman":
            print ("You have selected the Buisnessman legs")
            index_legs = 0
            break
        elif Legs.lower == "gamer":
            print ("You have selected the Gamer legs")
            index_legs = 1
            break
        elif Legs.lower == "king":
            print ("You have selected the King legs")
            index_legs = 2
            break
        else:
            print("Please select one of the given legs")

print("Player 2 skin select")
while True:
        Head2 = input("Select a head (Buisnessman, Gamer, King): ")
        if Head2.lower == "buisnessman":
            print ("You have selected the Buisnessman head")
            index_head2 = 0
            break
        elif Head2.lower == "gamer":
            print ("You have selected the Gamer head")
            index_head2 = 1
            break
        elif Head2.lower == "king":
            print ("You have selected the King head")
            index_head2 = 2
            break
        else:
            print("Please select one of the given heads")  

while True:
        Body2 = input("Select a body (Buisnessman, Gamer, King): ")
        if Body2.lower == "buisnessman":
            print ("You have selected the Buisnessman body")
            index_body2 = 0
            break
        elif Body2.lower == "gamer":
            print ("You have selected the Gamer body")
            index_body2 = 1
            break
        elif Body2.lower == "king":
            print ("You have selected the King body")
            index_body2 = 2
            break
        else:
            print("Please select one of the given bodies")
while True:
        Legs2 = input("Select a body (Buisnessman, Gamer, King): ")
        if Legs2.lower == "buisnessman":
            print ("You have selected the Buisnessman legs")
            index_legs2 = 0
            break
        elif Legs2.lower == "gamer":
            print ("You have selected the Gamer legs")
            index_legs2 = 1
            break
        elif Legs2.lower == "king":
            print ("You have selected the King legs")
            index_legs2 = 2
            break
        else:
            print("Please select one of the given legs")

head_item = head_list[index_head]
body_item = body_list[index_body]
leg_item = leg_list[index_legs]

head_item2 = head_list[index_head2]
body_item2 = body_list[index_body2]
leg_item2 = leg_list[index_legs2]


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

class Head:
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
        head = pygame.image.load(head_item)
        scale = pygame.transform.scale(head, (self.width, self.height))
        screen.blit(scale, (self.x, self.y))
        for cc in chara_under:
            cc.draw()

class Head2(Head):
    def __init__(self, x, y, width, height, x_shift):
        super().__init__(x, y, width, height)
        self.x_shift = x_shift
    def move(self, _speed):
        self.x-= _speed * d_t
    def draw(self):
        head = pygame.image.load(head_item2)
        scale = pygame.transform.scale(head, (self.width, self.height))
        screen.blit(scale, (self.x+self.x_shift, self.y))

chara = Head(Char1_posx, Char1_posy, 50,50)
chara_under = [Head2(Char1_posx, Char1_posy, 50,50, 800), Head2(Char1_posx, Char1_posy+20,800, 10,0)]
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
