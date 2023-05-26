from pygame import *
image1 = image.load('background.png')
image2 = image.load('player.png')
image3 = image.load('monster.png')
image4 = image.load('platform.png')
image5 = image.load('door1.png')
image6= image.load('door.png')
image7 = image.load('lava.png')
image8 = image.load('heart.png')
win = display.set_mode((1450,800))
bk = transform.scale(image1,(1450,800))
display.set_caption('dungeon') 
font.init()
mixer.init()
mixer.music.load('game.ogg')
mixer.music.play()
text = font.SysFont('Arial',36)
game = True
finish = False
finish1 = False
finish2 = False
hearts1 = 3
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(player_image,(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.gravity = 0
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):   
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 1450 - 100:
            self.rect.x += self.speed

            
    def player_i(self):
        keys = key.get_pressed()
        if keys[K_SPACE] and self.rect.bottom >=700:
            self.gravity -=20
            for p in platforms:
                if self.rect.bottom == p.rect.y:
                    self.gravity -=20




    def apl_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom >= 700:
            self.rect.bottom = 700
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                self.rect.bottom = plat.rect.y
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 550:
            self.direction = 'right'
        if self.rect.x >= 680:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x +=self.speed 
        else:
            self.rect.x -=self.speed 
class Wall(GameSprite):
    def __init__(self,wall_image,wall_x,wall_y,width,height, player_speed):
        super().__init__(player_image = wall_image, player_x=wall_x, player_y=wall_y, size_x=width, size_y=height, player_speed = player_speed)
        self.image = transform.scale(wall_image,(width, height))
        self.rect = self.image.get_rect()
        self.rect.width = width
        self.rect.height = height
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.speed = player_speed

    def draw(self):
        win.blit(self.image, (self.rect.x,self.rect.y))
lavas = sprite.Group()
player = Player(image2,0,460,55,75,15)      
monster = Enemy(image3,800,70,100,175,5)
platforms = sprite.Group()
platforms.add(
    Wall(image4,320,560,155,55,0),
    Wall(image4,150,490,155,55,0),
    Wall(image4,10,490,155,55,0),
    Wall(image4,130,310,155,55,0),
    Wall(image4,190,310,155,55,0),
    Wall(image4,410,370,155,55,0),
    Wall(image4,670,370,155,55,0),
    Wall(image4,900,470,155,55,0),
    Wall(image4,1100,370,155,55,0),    
    Wall(image4,1250,270,155,55,0),
    Wall(image4,1300,270,155,55,0),
    Wall(image4,1050,150,155,55,0),
    Wall(image4,940,150,155,55,0),
    Wall(image4,740,75,155,55,0),
    Wall(image4,630,75,155,55,0))
door = Wall(image6,695,-15,125,100,0)
hearts =sprite.Group()
hearts.add(
    Wall(image8,0,0,100,100,0),
    Wall(image8,100,0,100,100,0),
    Wall(image8,200,0,100,100,0))
while game:

    for i in event.get():
        if i.type == QUIT:
            game = False

    if not finish:
        finish1 = True
        finish2 = True
        win.blit(bk,(0,0))
        player.update()
        player.player_i()
        player.apl_gravity()
        player.reset()
        for p in platforms:
          p.reset()
        for h in hearts:
            h.reset()
        door.draw()
        if sprite.collide_rect(player, door):
            finish = True
            finish1 = False
            finish2 = True
            player = Player(image2,1230,560,55,75,20)
        if sprite.spritecollide(player,lavas,False):
            hearts1 -= 1
            player.rect.x +=100
        if hearts1 == 2:
            hearts =sprite.Group()
            hearts.add(
                Wall(image8,0,0,100,100,0),
                Wall(image8,100,0,100,100,0))
        if hearts1 == 1:
            hearts =sprite.Group()
            hearts.add(
                Wall(image8,0,0,100,100,0)) 
        if hearts1 <=0:
            game = False
    if not finish1:
        if finish1 == False:

            platforms = sprite.Group()
            platforms.add(
                Wall(image4,1230,560,155,55,0),
                Wall(image4,1000,490,155,55,0),
                Wall(image4,940,490,155,55,0),
                Wall(image4,800,400,155,55,0),
                Wall(image4,680,400,155,55,0),
                Wall(image4,560,400,155,55,0),
                Wall(image4,430,310,155,55,0),
                Wall(image4,250,430,155,55,0),
                Wall(image4,80,340,155,55,0),
                Wall(image4,230,170,155,55,0),
                Wall(image4,1300,270,155,55,0),
                Wall(image4,1090,267,155,55,0))
            door1 = Wall(image6,1300,175,125,100,0)
            door = Wall(image6,250,70,125,100,0)
            win.blit(bk,(0,0))
            player.update()
            player.player_i()
            player.apl_gravity()
            player.reset()
            door.reset()
            door1.reset()

        for p in platforms:
            p.reset()
        for h in hearts:
            h.reset()
        lavas.add(
            Wall(image7,980,487,120,35,0),
            Wall(image7,790,397,120,35,0),
            Wall(image7,590,397,120,35,0))
        for l in lavas:
            l.reset()
        if sprite.spritecollide(player,lavas,False):
            hearts1 -= 1
            player.rect.x +=50
        if hearts1 == 2:
            hearts =sprite.Group()
            hearts.add(
                Wall(image8,0,0,100,100,0),
                Wall(image8,100,0,100,100,0))
        if hearts1 == 1:
            hearts =sprite.Group()
            hearts.add(
                Wall(image8,0,0,100,100,0))
        if hearts1 <=0:
            hearts =sprite.Group()
            finish = True
            finish1 = True
            finish2 = True
        if sprite.collide_rect(player, door):
            finish = True
            finish1 = True
            finish2 = False
            player = Player(image2,1230,560,55,75,20) 


    if not finish2:
        if finish2 == False:
            platforms = sprite.Group()
            platforms.add(
                Wall(image4,1230,560,155,55,0),
                Wall(image4,1000,490,155,55,0),
                Wall(image4,940,490,155,55,0),
                Wall(image4,800,400,155,55,0),
                Wall(image4,680,400,155,55,0),
                Wall(image4,560,400,155,55,0),
                Wall(image4,430,310,155,55,0),
                Wall(image4,250,430,155,55,0),
                Wall(image4,80,340,155,55,0),
                Wall(image4,125,270,155,55,0),
                Wall(image4,1300,270,155,55,0))
        for h in hearts:
            h.reset()
        if sprite.spritecollide(player,lavas,False):
            hearts =sprite.Group()
            hearts.add(
                Wall(image8,0,0,100,100,0),
                Wall(image8,100,0,100,100,0))
            hearts1 -= 1
            player.rect.x +=20
        if hearts1 <=0:
            game = False 

    display.update()
    time.delay(10)
