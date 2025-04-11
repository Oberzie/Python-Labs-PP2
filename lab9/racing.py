import pygame, sys  
import random, time  

pygame.init()
FPS = pygame.time.Clock()


SCREEN_WIDTH = 400 
SCREEN_HEIGHT = 600  
SPEED = 3
SCORE = 0  
COINS_COLLECTED = 0  


font = pygame.font.SysFont("Verdana", 60)  
font_small = pygame.font.SysFont("Verdana", 20) 
game_over = font.render("Game Over", True, (0, 0, 0))  

background = pygame.image.load("lab9/AnimatedStreet.png")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255)) 
pygame.display.set_caption("Race")  


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab9/Enemy.png")  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) 
        if self.rect.top > SCREEN_HEIGHT: 
            SCORE += 1 
            self.rect.top = 0  
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab9/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  

    def move(self):
        pressed_keys = pygame.key.get_pressed()  
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]: 
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab9/Coin.png").convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(500, 550)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(500, 550)) 

class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab9/Coin.png").convert_alpha()  
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(500, 550)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(500, 550))  

# Создаем объекты классов
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()

# Создаем группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins2 = pygame.sprite.Group()
coins2.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)


last_coin_boost = 0

while True:
    for event in pygame.event.get():
        
        # Если число монет кратны 3 — увеличиваем скорость
        if COINS_COLLECTED % 3 == 0 and COINS_COLLECTED != 0 and COINS_COLLECTED != last_coin_boost:
            SPEED += 1
            last_coin_boost = COINS_COLLECTED  # запоминаем, чтобы не повторить
            
        if COINS_COLLECTED % 5 == 0 and COINS_COLLECTED != 0 and COINS_COLLECTED != last_coin_boost:
            SPEED += 1.5
            last_coin_boost = COINS_COLLECTED 
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    
    # Отображаем счетчики
    scores = font_small.render(f"Score: {SCORE}", True, (0, 0, 0))
    coins_display = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0, 0, 0))
    screen.blit(scores, (10, 10)) 
    screen.blit(coins_display, (SCREEN_WIDTH - 100, 10))  
   
    

    P1.move()  
    E1.move() 

    # Отрисовываем все объекты
    for i in all_sprites:
        screen.blit(i.image, i.rect)
    
    # Проверяем столкновение игрока с врагом и монетами
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('lab9/crash.wav').play()
        time.sleep(0.5)
        screen.fill((255, 0, 0))  
        screen.blit(game_over, (30, 250)) 
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Удаляем все объекты
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1  # Увеличиваем счетчик монет
        for coin in coins:
            coin.kill()  # Удаляем текущую монету
        C1 = Coin()  # Создаем новую монету
        coins.add(C1)
        all_sprites.add(C1)

    if pygame.sprite.spritecollideany(P1, coins2):
        COINS_COLLECTED += 2  
        for coin in coins2:
            coin.kill() 
        C2 = Coin2()  
        coins2.add(C2)
        all_sprites.add(C2)



    pygame.display.update()
    FPS.tick(60)  