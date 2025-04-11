import pygame
import math


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

#дефолт настройки
radius = 5
mode = 'blue'
screen.fill((255, 255, 255))
drawing_mode = 'free_draw'
start_pos = None
points = []

def get_color(mode):
    colors = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0)
    }
    return colors.get(mode, (255, 255, 255))

    
def draw_line_between(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * (end[0] - start[0]))
        y = int(start[1] + float(i) / distance * (end[1] - start[1]))
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
            elif event.key == pygame.K_q:
                drawing_mode = 'square'
            elif event.key == pygame.K_t:
                drawing_mode = 'right_triangle'
            elif event.key == pygame.K_y:
                drawing_mode = 'equilateral_triangle'
            elif event.key == pygame.K_u:
                drawing_mode = 'rhombus'

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                if drawing_mode == 'free_draw':
                    points.append(start_pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos:
                end_pos = event.pos #сохраняем позицию курсора мыши в момент нажатия
                if drawing_mode == 'rectangle':
                    rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                    pygame.draw.rect(screen, get_color(mode), rect, 2)

                elif drawing_mode == 'square':
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    side = min(abs(dx), abs(dy)) #берём меньшее значение из dx и dy, чтобы квадрат точно влезал в рамки движения мыши
                    sign_x = 1 if dx >= 0 else -1 #cмотрим, в какую сторону двигали мышь по X чтобы правильно нарисовать квадрат даже если тянули в обратную сторону
                    sign_y = 1 if dy >= 0 else -1
                    square = pygame.Rect(start_pos[0], start_pos[1], sign_x * side, sign_y * side)
                    pygame.draw.rect(screen, get_color(mode), square, 2)

                elif drawing_mode == 'circle':
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    radius_draw = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(screen, get_color(mode), start_pos, radius_draw, 2)

                elif drawing_mode == 'right_triangle':
                    pygame.draw.polygon(screen, get_color(mode), [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)

                elif drawing_mode == 'equilateral_triangle':
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    side = math.hypot(dx, dy)
                    angle = math.atan2(dy, dx)
                    p1 = start_pos
                    p2 = (int(p1[0] + side * math.cos(angle)), int(p1[1] + side * math.sin(angle)))
                    angle2 = angle - math.radians(60)
                    p3 = (int(p1[0] + side * math.cos(angle2)), int(p1[1] + side * math.sin(angle2)))
                    pygame.draw.polygon(screen, get_color(mode), [p1, p2, p3], 2)

                elif drawing_mode == 'rhombus':
                    mid_x = (start_pos[0] + end_pos[0]) // 2
                    mid_y = (start_pos[1] + end_pos[1]) // 2
                    dx = abs(end_pos[0] - start_pos[0]) // 2
                    dy = abs(end_pos[1] - start_pos[1]) // 2
                    rhombus = [
                        (mid_x, start_pos[1]),
                        (end_pos[0], mid_y),
                        (mid_x, end_pos[1]),
                        (start_pos[0], mid_y)
                    ]
                    pygame.draw.polygon(screen, get_color(mode), rhombus, 2)

                start_pos = None

        elif event.type == pygame.MOUSEMOTION:
            pos = event.pos
            if drawing_mode == 'free_draw' and pygame.mouse.get_pressed()[0]:
                points.append(pos)
                if len(points) > 1:
                    draw_line_between(screen, points[-2], points[-1], radius, get_color(mode))
            elif drawing_mode == 'eraser' and pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(screen, (255, 255, 255), pos, radius)

    pygame.display.flip()
    clock.tick(60)


