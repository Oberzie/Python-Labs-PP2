import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
cell_size = 20 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
font = pygame.font.SysFont("Arial", 20)


def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH // cell_size) - 1) * cell_size # Kоординаты еды кратные 20 — то есть строго по сетке
        y = random.randint(0, (HEIGHT // cell_size) - 1) * cell_size 
        if (x, y) not in snake: # Если позиция не занята телом змеи — возвращаем эту позицию
            return x, y

# Начальные параметры
snake = [(100, 100)] # Начальное положение змеи
snake_dir = (cell_size, 0)  # Движение змеи (вправо)
food = generate_food(snake)  
score = 0
level = 1
 
running = True
clock = pygame.time.Clock()


while running:
    screen.fill((255, 255, 255))
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, cell_size):
                snake_dir = (0, -cell_size)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -cell_size):
                snake_dir = (0, cell_size)
            elif event.key == pygame.K_LEFT and snake_dir != (cell_size, 0):
                snake_dir = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-cell_size, 0):
                snake_dir = (cell_size, 0)
    
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1]) # вычисляем позицию, куда должна переместиться голова змейки в следующем кадре, добавляя направление к текущей позиции.
    
    # смерть змеи
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT: 
        running = False
    if new_head in snake:
        running = False
   
    snake.insert(0, new_head) # добавляет новую голову в начало списка.
    
   
    if new_head == food: # Если съели еду увеличиваем счёт и создаём новую.
        score += 1
        food = generate_food(snake)
        
       
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop() # Удаление последнего сегмента: Если не съели убираем хвост чтобы змейка не росла
    
    # Отрисовка змеи
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, cell_size, cell_size))
    
   # Отрисовка еды
    pygame.draw.rect(screen, (255, 0, 0), (*food, cell_size, cell_size))
    
    # Отображение счёта и уровня
    score_text = font.render(f"Счёт: {score}  Уровень: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    
    pygame.display.update()
    clock.tick(7)  
