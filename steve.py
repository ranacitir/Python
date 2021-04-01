import pygame, sys
import random

pygame.init()
win = pygame.display.set_mode((700, 483))
pygame.display.set_caption("Steve")

bg = pygame.image.load('desert4.png')
zemin = pygame.image.load('zemin6.png')
jump = pygame.image.load('kangaroojump1.png')
sun = pygame.image.load('sun1.png')
go = pygame.image.load('gameover1.png')

song = "pixel2.mp3"
pygame.mixer.music.load(song)
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.05)

clock = pygame.time.Clock()

class toz(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('toz4.png')
        self.rt = 0
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 380

    def draw(self):
        win.blit(pygame.transform.rotate(self.image, self.rt), (self.rect.x, self.rect.y))
        self.rt += 10
        if (self.rect.x <= -500):
            self.rect.x = 900

class cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cactus1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 332
        self.rt = 0

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
        if (self.rect.x <= -700):
            self.rect.x = 1200


class steve(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('kangaroo1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 333

class player(object):
    def __init__(self, width, height, bgx, zx):
        self.bgx = bgx
        self.zx = zx
        self.width = width
        self.height = height
        self.isJump = False
        self.left = False
        self.right = False
        self.up = False
        self.jj = 1
        self.jumpCount = 15

    def sprite(self):
        win.blit(bg, (self.bgx, 0))
        win.blit(zemin, (self.zx, 413))
        win.blit(sun, (275, 50))

        if(self.zx <= -10135 ):
            self.zx = 0
        if(self.bgx <= -4095):
            self.bgx = 0

    def draw(self, win):

        if self.up:
            win.blit(jump, (steve1.rect.x, steve1.rect.y))
            self.bgx -= 2
            self.zx -= 8
            toz2.rect.x -= 12
            cactus1.rect.x -= 8
        else:
            win.blit(steve1.image, (steve1.rect.x, steve1.rect.y))
            self.bgx -= 1
            self.zx -= 7
            toz2.rect.x -= 10
            cactus1.rect.x -= 7

def redrawGameWindow():
    steve.sprite()
    cactus1.draw()
    toz2.draw()
    steve.draw(win)
    pygame.display.update()

toz2 = toz()
cactus1 =cactus()
steve1 = steve()
steve = player(64, 64, 0, 0)

run = True
gameOver = False
isJump = False

while run:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if(gameOver==False):
        if(steve.isJump==False):
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                steve.isJump=True
                steve.up = True
                steve.jj = 4
            else:
                steve.jj = 2
                steve.up = False

        else:
            if steve.jumpCount >= -15:
                steve1.rect.y -= (steve.jumpCount * steve.jj) * 0.5
                steve.jumpCount -=1
            else:
                steve.jumpCount = 15
                steve.up=False
                steve.isJump = False

    if (pygame.sprite.collide_mask(toz2, steve1) or
            pygame.sprite.collide_mask(cactus1, steve1)):
        gameOver = True
    else:
        gameOver = False

    if (gameOver == False):
        redrawGameWindow()
    else:
        win.blit(go, (200, 100))
        pygame.mixer.music.pause()
        pygame.display.update()

pygame.quit()
