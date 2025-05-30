import pygame
import time
pygame.init()
pygame.display.set_caption('Mickey Mouse Clocks')

screen = pygame.display.set_mode((1000,800)) 

image = pygame.image.load('lab7/mickeyclock1.png').convert()
hand = pygame.image.load('lab7/hand1.png').convert()
handmin = pygame.image.load('lab7/hand2.png').convert()
x = (1000 - image.get_width()) // 2 
y = (800 - image.get_height()) // 2
# находим центр часов upd. его сдвинул немного, чтобы начало стрелки совпадало с центром часов
clock_center = (x + image.get_width() // 2, y + image.get_height() // 2)
hand_length = hand.get_height()
handmin_length = handmin.get_height()

running = True
while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        screen.fill((0,0,0)) # заполнение фона 
       
        screen.blit(image, (x, y)) # переводим пнгшку часов на фон
        # беру с библиотеки тайм текущее время в секундах 
        seconds = time.localtime().tm_sec
        mins = time.localtime().tm_min
        angle = -seconds * 6 # расчитываю градус для руки 
        angle1 = -mins * 6
        #кручу руку по углу ( энгл) который ранее прописал
        rotated_hand = pygame.transform.rotate(hand, angle)
        rotated_handmin = pygame.transform.rotate(handmin, angle1)
        # позицианируем руку в центре часов 
        hand_rect = rotated_hand.get_rect()
        handmin_rect = rotated_handmin.get_rect()
        hand_rect.center = (clock_center[0], clock_center[1])  # Центр стрелки в центре часов
        handmin_rect.center = (clock_center[0], clock_center[1])
        #hand_rect.y -= hand_length // 2  # Смещение вверх, чтобы начало было в центре
        screen.blit(rotated_hand, hand_rect.topleft)
        screen.blit(rotated_handmin, handmin_rect.topleft)
        pygame.display.flip()
        pygame.time.delay(1000)

pygame.quit()