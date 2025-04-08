import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")


font = pygame.font.SysFont("Arial", 20)


def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:
            return x, y


snake = [(100, 100)] 
snake_dir = (CELL_SIZE, 0)  
food = generate_food(snake)  
score = 0
level = 1
speed = 7  
running = True
clock = pygame.time.Clock()


while running:
    screen.fill(WHITE)
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)
    
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    
 
    if new_head in snake:
        running = False
   
    snake.insert(0, new_head)
    
   
    if new_head == food:
        score += 1
        food = generate_food(snake)
        
       
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop() 
    
  
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
   
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    
 
    score_text = font.render(f"Счёт: {score}  Уровень: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    
    pygame.display.update()
    clock.tick(speed)  

pygame.quit()