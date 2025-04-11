import pygame

pygame.init()
    
#дефолт настройка
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
radius = 15
mode = 'blue'
drawing_mode = 'free_draw'
start_pos = None
points = []

def get_color(mode):
    colors = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0)
    }
    return colors.get(mode, (255, 255, 255)) #Мы достаём из словаря colors значение по ключу mode

def draw_line_between(screen, start, end, width, color):
    dx = start[0] - end[0] # конечная и начальная точка где мышь была отпущена
    dy = start[1] - end[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance): #по немногу добавляем кружки
        x = int(start[0] + float(i) / distance * (end[0] - start[0]))
        y = int(start[1] + float(i) / distance * (end[1] - start[1])) #берём начальную точку и добавляем к ней чуть-чуть пути в сторону конца.
        pygame.draw.circle(screen, color, (x, y), width) 

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen.fill((255, 255, 255))
                points = []

                
            elif event.key == pygame.K_r:
                mode = 'red'
            elif event.key == pygame.K_g:
                mode = 'green'
            elif event.key == pygame.K_b:
                mode = 'blue'

                
            elif event.key == pygame.K_f:
                drawing_mode = 'free_draw'
            elif event.key == pygame.K_e:
                drawing_mode = 'eraser'
            elif event.key == pygame.K_c:
                drawing_mode = 'circle'
            elif event.key == pygame.K_v:
                drawing_mode = 'rectangle'

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                if drawing_mode == 'free_draw':
                    points.append(start_pos) #при каждом движении мыши мы будем добавлять следующие точки и рисовать отрезки между ними
                    

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos:
                end_pos = event.pos #сохраняем позицию курсора мыши в момент нажатия
                if drawing_mode == 'circle':
                    dx = end_pos[0] - start_pos[0] 
                    dy = end_pos[1] - start_pos[1]
                    
                    radius_draw = int((dx ** 2 + dy ** 2) ** 0.5)
                    pygame.draw.circle(screen, get_color(mode), start_pos, radius_draw, 2)
                elif drawing_mode == 'rectangle':
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, get_color(mode), rect, 2)
                start_pos = None

        elif event.type == pygame.MOUSEMOTION:
            pos = event.pos #позиция курсора
            if drawing_mode == 'free_draw' and pygame.mouse.get_pressed()[0]:
                points.append(pos) #соединить точки
                if len(points) > 1:
                    draw_line_between(screen, points[-2], points[-1], radius, get_color(mode)) #между точками рисуем плавную линию
                        
            elif drawing_mode == 'eraser' and pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(screen, (255, 255, 255), pos, radius)

    pygame.display.flip()
    clock.tick(60)


