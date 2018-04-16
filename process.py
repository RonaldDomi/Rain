import pygame
import sys
from random import randint
from rain import Rain

def Process(total_frames, FPS, screen):                                 # INPUT()   SPAWN_RAIN()   CHANGE_RAIN()
    Input(Rain.intensity, FPS)
    spawn_rain(total_frames, FPS, screen, Rain.intensity)
    change_rain(total_frames, FPS, screen)

def text_to_screen(screen, text, x, y, size = 15):                      # draw text to x,y

    text = str(text)
    font = pygame.font.SysFont('monospace', size)
    text = font.render(text, True, [255,255,255])
    screen.blit(text, (x,y))
def Input(intensity, FPS):                                              # intensity changed on mousewheel  rain-direction changed on keypress

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:    #up
                if Rain.intensity + 1 > 5:
                    pass
                else:
                    Rain.intensity += 1
            elif event.button == 5:  #down
                if Rain.intensity - 1 <= 0:
                    pass
                else:
                    Rain.intensity -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                Rain.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                Rain.direction = 'right'
            elif event.key == pygame.K_DOWN:
                Rain.direction = 'down'
            # if event.key == pygame.VIDEORESIZE:
            #     screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
            #     screen.fill((0,0,0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        for drop in Rain.List:
            Rain.List.remove(drop)
            del(drop)
def draw_rain(screen):                                                  # if direction than RAIN(direction)

    if Rain.direction == 'down':
        Rain(screen)
    elif Rain.direction == 'left':
        Rain(screen, 'go_left')
    else:
        Rain(screen, 'go_right')
def spawn_rain(total_frames, FPS, screen, intensity):                        # for each intensity, if enought time, than     DRAW_RAIN()

    if intensity == 1:  #          FPS = total
        if total_frames % FPS == 0:
            draw_rain(screen)
    if intensity == 2:  # 2 * draw_rain     FPS//6
        if total_frames % (FPS//6) == 0:
            for i in range(0, 2):
                draw_rain(screen)
    if intensity == 3:  # 3 * draw_rain     FPS//20
        if total_frames % (FPS//20) == 0:
            for i in range(0, 3):
                draw_rain(screen)
    if intensity == 4:  # 2 * draw_rain     FPS//40
        if total_frames % (FPS//40) == 0:
            for i in range(0, 2):
                draw_rain(screen)
    if intensity == 5:  # 6 * draw_rain     FPS//40
        if total_frames % (FPS//40) == 0:
            for i in range(0, 6):
                draw_rain(screen)
def change_rain(total_frames, FPS, screen):                             # if enough time than   BLITZ(), CHANGE_RAIN()

    if (total_frames + FPS*2) % (FPS*4) == 0:  #(FPS*randint(5)) == 0:      #direction      blitz
        #blitz(screen, [0,0,0])
        Rain.change_direction()

        # text_to_screen(screen, 'changed direction', 250, 300, 50)
        # pygame.display.flip()
        # pygame.time.delay(800)
    if total_frames % (FPS*4) == 0:   #(FPS*randint(8)) == 0:      #intensity     blitz
        #blitz(screen, [0,0,0])
        Rain.change_intensity()

        # text_to_screen(screen, 'changed intensity', 250, 300, 50)
        # pygame.display.flip()
        # pygame.time.delay(800)
def blitz(screen, color):                                               # fill color for 50ms

    screen.fill((color))
    pygame.display.flip()
    pygame.time.delay(60)
