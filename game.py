import pygame, sys
import random

head_list = ["Images/head1.png","Images/head2.png", "Images/head3.png"]
body_list = ["Images/body1.png","Images/body2.png", "Images/body3.png"]
shoe_list = ["Images/shoe1.png","Images/shoe2.png", "Images/shoe3.png"]

print("Player 1 skin select")

while True:
    Head = input("Select a head (businessman, Gamer, King): ")
    if Head == "businessman":
        print ("You have selected the businessman head")
        index_head = 0
        break
    elif Head == "gamer":
        print ("You have selected the Gamer head")
        index_head = 1
        break
    elif Head == "king":
        print ("You have selected the King head")
        index_head = 2
        break
    else:
        print("Please select one of the given heads")  

print("body")
while True:
    Body = input("Select a body (businessman, Gamer, King): ")
    if Body == "businessman":
        print ("You have selected the businessman body")
        index_body = 0
        break
    elif Body == "gamer":
        print ("You have selected the Gamer body")
        index_body = 1
        break
    elif Body == "king":
        print ("You have selected the King body")
        index_body = 2
        break
    else:
        print("Please select one of the given bodies")
while True:
    shoes = input("Select shoes (businessman, Gamer, King): ")
    if shoes == "businessman":
        print ("You have selected the businessman shoes")
        index_shoes = 0
        break
    elif shoes == "gamer":
        print ("You have selected the Gamer shoes")
        index_shoes = 1
        break
    elif shoes == "king":
        print ("You have selected the King shoes")
        index_shoes = 2
        break
    else:
        print("Please select one of the given shoes")

print("Player 2 skin select")
while True:
    Head2 = input("Select a head (businessman, Gamer, King): ")
    if Head2 == "businessman":
        print ("You have selected the businessman head")
        index_head2 = 0
        break
    elif Head2 == "gamer":
        print ("You have selected the Gamer head")
        index_head2 = 1
        break
    elif Head2 == "king":
        print ("You have selected the King head")
        index_head2 = 2
        break
    else:
        print("Please select one of the given heads")  

while True:
    Body2 = input("Select a body (businessman, Gamer, King): ")
    if Body2 == "businessman":
        print("You have selected the businessman body")
        index_body2 = 0
        break
    elif Body2 == "gamer":
        print ("You have selected the Gamer body")
        index_body2 = 1
        break
    elif Body2 == "king":
        print ("You have selected the King body")
        index_body2 = 2
        break
    else:
        print("Please select one of the given bodies")
while True:
    shoes2 = input("Select shoes (businessman, Gamer, King): ")
    if shoes2 == "businessman":
        print ("You have selected the businessman shoes")
        index_shoes2 = 0
        break
    elif shoes2 == "gamer":
        print ("You have selected the Gamer shoes")
        index_shoes2 = 1
        break
    elif shoes2 == "king":
        print ("You have selected the King shoes")
        index_shoes2 = 2
        break
    else:
        print("Please select one of the given shoes")

head_item = head_list[index_head]
body_item = body_list[index_body]
shoe_item = shoe_list[index_shoes]

head_item2 = head_list[index_head2]
body_item2 = body_list[index_body2]
shoe_item2 = shoe_list[index_shoes2]

rope = "Images/Rope.png"



pygame.init()
clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.SHOWN)
bg=pygame.transform.scale(pygame.image.load("Images/background.png"), (WIDTH, HEIGHT))
player_posA = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
player_posB = pygame.Vector2(3*screen.get_width() / 4, screen.get_height() / 2)
d_t = 1 / FPS
Char1_posx= 200
Char1_posy= HEIGHT - 202.5
speed=1000

class Head:
    def __init__(self, x,y,width, height,image):
        self.x= x
        self.y= y
        self.width = width
        self.height = height
        self.image = image
    def move(self, _speed):
        self.x-= _speed * d_t
        for cc in chara_under:
            cc.move(_speed)
    def draw(self):
        scale = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(scale, (self.x, self.y))
        for cc in chara_under:
            cc.draw()

class Head2(Head):
    def __init__(self, x, y, width, height, x_shift,y_shift,image):
        super().__init__(x, y, width, height,image)
        self.x_shift = x_shift
        self.y_shift = y_shift
    def move(self, _speed):
        self.x-= _speed * d_t
    def draw(self):
        scale = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(scale, (self.x+self.x_shift, self.y+self.y_shift))

chara = Head(Char1_posx, Char1_posy, 50,50,pygame.image.load(head_item))
chara_under = [Head2(Char1_posx, Char1_posy, 50,50, 800,0,pygame.transform.flip(pygame.image.load(head_item2), True, False)), 
               Head2(Char1_posx, Char1_posy,800, 100,11,10,pygame.image.load(rope)),
               Head2(Char1_posx, Char1_posy, 50,50, 800,50,pygame.transform.flip(pygame.image.load(body_item2), True, False)),
               Head2(Char1_posx, Char1_posy, 45,35, 795,98,pygame.transform.flip(pygame.image.load(shoe_item2), True, False)),
               Head2(Char1_posx, Char1_posy, 50,50,0,50, pygame.image.load(body_item)),
               Head2(Char1_posx, Char1_posy, 45,35,5,98, pygame.image.load(shoe_item))]
zone = 1100
status = True
won_player = ''
shift_var = WIDTH / 2 - 400 - 50
trans_dict = {'Player 1': -1, 'Player 2': 1}

def movement():
    global status, won_player
    if chara.x <= WIDTH//2 - zone//2:
        status = False
        won_player = 'Player 1'
    if chara_under[0].x + 832 >= WIDTH//2 + zone//2:
        status = False
        won_player = 'Player 2'



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                chara.move(speed)
            elif event.key == pygame.K_RCTRL:
                chara.move(-speed)
    movement()
    screen.blit(bg, (0,0))

    chara.draw()

    if status == False:
        speed = 0
        text = pygame.font.SysFont('Impact', 70).render(f'{won_player} WINS', False, BLACK)
        screen.blit(text, text.get_rect(center=(WIDTH/2 + trans_dict[won_player] * shift_var, HEIGHT/2)))

    clock.tick(FPS)    
    pygame.display.flip()
