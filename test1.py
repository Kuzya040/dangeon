from pygame import *
from time import time as sec
from time import sleep
image1 = image.load('background.png')
image2 = image.load('player.png')
image3 = image.load('monster.png')
image4 = image.load('platform.png')
image5 = image.load('door1.png')
image6= image.load('door.png')
image7 = image.load('lava.png')
image8 = image.load('heart.png')
image9 = image.load('bullet.png')
image10 = image.load('laser.png')
win = display.set_mode((1450,800))
bk = transform.scale(image1,(1450,800))
display.set_caption('dungeon') 
font.init()
mixer.init()
mixer.music.load('game.ogg')
mixer.music.play()
fire= mixer.Sound('fire.ogg')
text = font.SysFont('Arial',36)
bullet_fire = text.render('выстрел на правый ctrl',True, (190,170,74))
bulets = sprite.Group()
lasers = sprite.Group()
game = True
finish = False
finish1 = False
finish2 = False
time_rel = False
hearts1 = 3
hearts2 = 3
firer = 0
firer1 = 0
losers = text.render('You lose',True,(255,255,255))
winers = text.render('You won',True,(255,255,255)) 
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
        if keys[K_SPACE]:
            for p in platforms:
                if self.rect.bottom >=p.rect.y or p.rect.y - self.rect.y <= 20:
                    self.gravity -=20
                if p.rect.y - self.rect.y >=20:
                    self.gravity +=20

    def apl_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom >= 700:
            self.rect.bottom = 700
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                self.rect.bottom = plat.rect.y
    def fire(self):
        bulet = Bulet(image9,self.rect.centerx, self.rect.top, 45,45,15)
        bulets.add(bulet)
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 1200:
            self.direction = 'right'
        if self.rect.x >= 1450:
            self.direction = 'left'

        if self.direction == 'right':
            monster.rect.x +=15 
        else:
            monster.rect.x -=15 
    def fire(self):
        laser = Bulet(image10,self.rect.centerx, self.rect.top, 45,45,-5)
        lasers.add(laser)
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
class Bulet(GameSprite):    
    def update(self):
        self.rect.x += self.speed
        win.blit(self.image, (self.rect.x,self.rect.y))
        if self.rect.x >=1450:
            self.kill()
lavas = sprite.Group()
player = Player(image2,0,460,55,75,15)      
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
hearts3 =sprite.Group()
hearts3.add(
    Wall(image8,1300,0,100,100,0),
    Wall(image8,1200,0,100,100,0),
    Wall(image8,1100,0,100,100,0))

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if not finish:

        finish1 = True
        finish2 = True
        win.blit(bk,(0,0))
        win.blit(bullet_fire,(1000,750))
        player.update()
        player.player_i()
        player.apl_gravity()
        player.reset()
        bulets.update()
        for p in platforms:
          p.reset()
        for h in hearts:
            h.reset()
        door.reset()
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
            finish = True
            finish1 = True
            finish2 = True
            win.blit(losers,(700,400))
        keys = key.get_pressed()
        if keys[K_RCTRL]:
            if firer < 5 and time_rel == False:
                firer+=1
                fire.play()
                player.fire()
            if firer >= 5 and time_rel == False:
                last_time = sec()
                time_rel = True
        if time_rel == True:
            time_now = sec()
            if time_now - last_time < 1.5:
                peresaradka = text.render('recharge',True,(190,170,74))
                win.blit(peresaradka,(75,100))
            else:
                firer = 0
                time_rel = False
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
            win.blit(bullet_fire,(1000,750))
            player.update()
            player.player_i()
            player.apl_gravity()
            player.reset()
            door.reset()
            door1.reset()
            bulets.update()
        for p in platforms:
            p.reset()
        for h in hearts:
            h.reset()
        lavas.add(
            Wall(image7,980,487,120,15,0),
            Wall(image7,790,397,120,15,0),
            Wall(image7,590,397,120,15,0))
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
            win.blit(losers,(700,400))
        if sprite.collide_rect(player, door):
            finish = True
            finish1 = True
            finish2 = False
            player = Player(image2,0,560,55,75,15) 
            monster = Enemy(image3,1300,70,80,120,15)
        keys = key.get_pressed()
        if keys[K_RCTRL]:
            if firer < 5 and time_rel == False:
                firer+=1
                fire.play()
                player.fire()
            if firer >= 5 and time_rel == False:
                last_time = sec()
                time_rel = True
        if time_rel == True:
            time_now = sec()
            if time_now - last_time < 1.5:
                peresaradka = text.render('recharge',True,(190,170,74))
                win.blit(peresaradka,(75,100))
            else:
                firer = 0
                time_rel = False

    if not finish2:
        if finish2 == False:
            platforms = sprite.Group()
            platforms.add(
                Wall(image4,1230,560,155,55,0),
                Wall(image4,1000,490,155,55,0),
                Wall(image4,750,490,155,55,0),
                Wall(image4,550,400,155,55,0),
                Wall(image4,350,490,155,55,0),
                Wall(image4,150,400,155,55,0),
                Wall(image4,0,310,155,55,0),
                Wall(image4,150,180,155,55,0),
                Wall(image4,300,180,155,55,0),
                Wall(image4,450,180,155,55,0),
                Wall(image4,650,230,155,55,0),
                Wall(image4,900,180,155,55,0),
                Wall(image4,1050,180,155,55,0),
                Wall(image4,1200,180,155,55,0),
                Wall(image4,1350,180,155,55,0))

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
                win.blit(losers,(700,400))
            win.blit(bk,(0,0))
            win.blit(bullet_fire,(1000,750))
            player.update()
            player.player_i()
            player.apl_gravity()
            player.reset()
            if hearts2 >0:
                monster.reset()
                monster.fire()
            bulets.update()
            lasers.update()
            for p in platforms:
                p.reset()
            for h in hearts:
                h.reset()
            for h in hearts3:
                h.reset()
            lavas = sprite.Group()
            lavas.add(
                Wall(image7,200,179,100,15,0),
                Wall(image7,450,179,100,15,0),
                Wall(image7,970,179,100,15,0),
                Wall(image7,1170,179,100,15,0))
            for l in lavas:
                l.reset()
            keys = key.get_pressed()
            if keys[K_RCTRL]:
                if firer < 5 and time_rel == False:
                    firer+=1
                    fire.play()
                    player.fire()
                if firer >= 5 and time_rel == False:
                    last_time = sec()
                    time_rel = True
            if time_rel == True:
                time_now = sec()
                if time_now - last_time < 1.5:
                    peresaradka = text.render('recharge',True,(190,170,74))
                    win.blit(peresaradka,(75,100))
                else:
                    firer = 0
                    time_rel = False
            if sprite.spritecollide(player,lasers,False):
                hearts1 -= 1
            if sprite.spritecollide(monster,bulets,True):
                hearts2 -= 1
            if hearts2 == 2:
                hearts3 =sprite.Group()
                hearts3.add(
                    Wall(image8,1300,0,100,100,0),
                    Wall(image8,1200,0,100,100,0))
            if hearts2 == 1:
                hearts3 =sprite.Group()
                hearts3.add(
                    Wall(image8,1300,0,100,100,0))
            if hearts2 <=0:
                hearts3 = sprite.Group()
                door =Wall(image6,1350,80,125,100,0) 
                door.reset()
            if sprite.collide_rect(player, door):
                finish = True
                finish1 = True
                finish2 = True
                win.blit(winers,(700,400))
    display.update()
    time.delay(10)
