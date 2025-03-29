import pygame
from pygame.locals import *
import sys
import random

pygame.init()
height, width = 1000, 800
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Hears of iron 4")
black = pygame.Color(0, 0, 0)         
white = pygame.Color(255, 255, 255)  
grey = pygame.Color(128, 128, 128)   
red = pygame.Color(255, 0, 0)       
fps = pygame.time.Clock()
screen.fill(white)
background = pygame.image.load("lab8/background.jpg") 
background = pygame.transform.scale(background, (width, height))  


class Opps(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/enemy.png")
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > height):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
        
        
class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/player.png")
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.center = (160,250)
        
    def update(self):
        press_keys = pygame.key.get_pressed()
        if press_keys[K_w]:
            self.rect.move_ip(0, -5)
        if press_keys[K_s]:
            self.rect.move_ip(0,5)
            
        if self.rect.left > 0:
            if press_keys[K_a]:
                self.rect.move_ip(-5,0)
        if self.rect.right < width:        
            if press_keys[K_d]:
                self.rect.move_ip(5,0)
    def draw(self,surface):
        surface.blit(self.image, self.rect)
        
        
        
        
        
        
        
        
player = Player()
enemy = Opps()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    player.update()
    enemy.move()
    screen.fill(white)
    screen.blit(background, (0, 0))  
    player.draw(screen)
    enemy.draw(screen)
    
    
    pygame.display.update()
    fps.tick(160)