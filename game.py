import pygame, sys

head_list = ["Images/head1.png","Images/head2.png", "Images/head3.png"]
body_list = ["Images/body1.png","Images/body2.png", "Images/body3.png"]
shoe_list = ["Images/shoe1.png","Images/shoe2.png", "Images/shoe3.png"]

print("Player 1 skin select")

while True:
    Head = input("Select a head (Buisnessman, Gamer, King): ")
    if Head == "buisnessman":
        print ("You have selected the Buisnessman head")
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
    Body = input("Select a body (Buisnessman, Gamer, King): ")
    if Body == "buisnessman":
        print ("You have selected the Buisnessman body")
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
    shoes = input("Select shoes (Buisnessman, Gamer, King): ")
    if shoes == "buisnessman":
        print ("You have selected the Buisnessman shoes")
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
    Head2 = input("Select a head (Buisnessman, Gamer, King): ")
    if Head2 == "buisnessman":
        print ("You have selected the Buisnessman head")
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
    Body2 = input("Select a body (Buisnessman, Gamer, King): ")
    if Body2 == "buisnessman":
        print("You have selected the Buisnessman body")
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
    shoes2 = input("Select shoes (Buisnessman, Gamer, King): ")
    if shoes2 == "buisnessman":
        print ("You have selected the Buisnessman shoes")
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


pygame.init()
clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 600
FPS = 60


screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
bg=pygame.transform.scale(pygame.image.load("Images/background.png"), (WIDTH, HEIGHT))
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

class Body(Head):
    def __init__(self, x, y, width, height, y_shift):
        super().__init__(x, y, width, height)
        self.y_shift = y_shift
    def move(self, _speed):
        self.x-= _speed * d_t
    def draw(self):
        head = pygame.image.load(body_item)
        scale = pygame.transform.scale(head, (self.width, self.height))
        screen.blit(scale, (self.x, self.y+self.y_shift))

class Shoe(Head):
    def __init__(self, x, y, width, height, y_shift):
        super().__init__(x, y, width, height)
        self.y_shift = y_shift
    def move(self, _speed):
        self.x-= _speed * d_t
    def draw(self):
        head = pygame.image.load(body_item)
        scale = pygame.transform.scale(head, (self.width, self.height))
        screen.blit(scale, (self.x, self.y+self.y_shift))

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

class Body2(Body):
    def __init__(self, x, y, width, height, y_shift, x_shift):
        super().__init__(x, y, width, height,y_shift)
        self.x_shift = x_shift
    def move(self, _speed):
        self.x-= _speed * d_t
    def draw(self):
        head = pygame.image.load(body_item)
        scale = pygame.transform.scale(head, (self.width, self.height))
        screen.blit(scale, (self.x+self.x_shift, self.y))

class Shoe2(Shoe):
    def __init__(self, x, y, width, height, y_shift, x_shift):
        super().__init__(x, y, width, height,y_shift)
        self.x_shift = x_shift
    def move(self, _speed):
        self.x-= _speed * d_t
    def draw(self):
        head = pygame.image.load(body_item)
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
