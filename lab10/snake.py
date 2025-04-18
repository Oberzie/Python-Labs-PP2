import psycopg2
import pygame
import random


def get_conn():
    return psycopg2.connect(
        dbname="gamebd",  
        user="postgres",      
        password="7355608", 
        host="localhost",
        port="5432"
    )


def get_or_create_user(username):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, level, score FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        user_id, level, score = user
        print(f"Добро пожаловать, {username}! Уровень: {level}, Счёт: {score}")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id, level, score", (username,))
        user_id, level, score = cur.fetchone()
        conn.commit()
        print(f"Создан новый пользователь {username}. Начнём с уровня {level} и счёта {score}!")

    cur.close()
    conn.close()
    return user_id, level, score


pygame.init()

# Функция сохранения прогресса
def save_score(user_id, score, level):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level)
    )
    cur.execute(
        "UPDATE users SET level = %s, score = %s WHERE id = %s",
        (level, score, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()


WIDTH, HEIGHT = 600, 400
cell_size = 20 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
font = pygame.font.SysFont("Arial", 20)


def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH // cell_size) - 1) * cell_size 
        y = random.randint(0, (HEIGHT // cell_size) - 1) * cell_size 
        if (x, y) not in snake:  
            return x, y


username = input("Введите ваше имя: ")
user_id, level, score = get_or_create_user(username)

# Настройка начальной скорости на основе уровня
speed = 7 + (level - 1) * 2

snake = [(100, 100)] 
snake_dir = (cell_size, 0)  
food = generate_food(snake)
running = True
clock = pygame.time.Clock()

# Игровой цикл
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
            elif event.key == pygame.K_p:  # Пауза с сохранением
                save_score(user_id, score, level)
                print("Игра на паузе. Прогресс сохранён.")
                running = False

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = generate_food(snake)
        if score % 5 == 0:  # Уровень увеличивается каждые 5 очков
            level += 1
            speed += 2
    else:
        snake.pop()

    
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, cell_size, cell_size))


    pygame.draw.rect(screen, (255, 0, 0), (*food, cell_size, cell_size))

    
    score_text = font.render(f"Счёт: {score}  Уровень: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))  

    pygame.display.update()
    clock.tick(speed)  

# Сохраняем результат по завершении игры
save_score(user_id, score, level)
print("Вы проиграли. Прогресс сохранён.")
pygame.quit()
