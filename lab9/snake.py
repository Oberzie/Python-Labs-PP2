import pygame
import random

pygame.init()

REMOVE_FOOD_EVENT = pygame.USEREVENT + 1
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("zmeyka")
font = pygame.font.SysFont("Arial", 20)


def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:
            return x, y
        
def generate_food1(snake):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:
            return x, y


snake = [(100, 100)]  
snake_dir = (CELL_SIZE, 0)  
food = generate_food(snake)
food1 = generate_food1(snake)
food_timer_started = False  # Флаг для проверки, запущен ли таймер для еды
food_timer = 0  # Время, через которое еда исчезнет (в миллисекундах)
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
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)
        
        # Если время на еду истекло, удаляем её
        if event.type == REMOVE_FOOD_EVENT:
            food = None  # Удаляем еду после n секунд, если её не съели
            food_timer_started = False  # Сбрасываем флаг таймера
            food = generate_food(snake)

        if event.type == REMOVE_FOOD_EVENT:
            food1 = None  # Удаляем еду после n секунд, если её не съели
            food_timer_started = False  # Сбрасываем флаг таймера
            food1 = generate_food1(snake)


    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = generate_food(snake) 
        food_timer_started = False  # Сбрасываем флаг, потому что еду съели
    
    elif new_head == food1:
        score += 2
        food1 = generate_food1(snake)
        food_timer_started = False  

    else:
        snake.pop()  

    # Запускаем таймер для удаления еды, если еда еще не была съедена
    if not food_timer_started and food is not None:
        pygame.time.set_timer(REMOVE_FOOD_EVENT, 4000)  # Устанавливаем таймер на 4 секунд
        food_timer_started = True  # Устанавливаем флаг, чтобы таймер запускался только один раз

    if not food_timer_started and food1 is not None:
        pygame.time.set_timer(REMOVE_FOOD_EVENT, 3000)  
        food_timer_started = True 

    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

    # Отрисовка еды, если она существует
    if food is not None:
        pygame.draw.rect(screen, (255, 0, 0), (*food, CELL_SIZE, CELL_SIZE))

    if food1 is not None:
        pygame.draw.rect(screen, (0, 0, 255), (*food1, CELL_SIZE, CELL_SIZE))

 
    score_text = font.render(f"Счёт: {score}  Уровень: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(7) 
