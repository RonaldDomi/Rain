import pygame
import os
from process import Process
from rain import *
from Time import Time

print('')

pygame.init()
pygame.display.set_caption("Rain")
os.environ['SDL_VIDEO_CENTERED'] = '1'

width = 1028
height = 578
screen = pygame.display.set_mode((width, height))#, pygame.RESIZABLE)
#1200 600 forest
#1028, 578 foto
clock = pygame.time.Clock()
FPS = 60
total_frames = 0

forest = pygame.image.load('images/background.jpg')
foto_1 = pygame.image.load('images/foto_1.jpg')
foto_2 = pygame.image.load('images/foto_2.jpg')

while True:
    total_frames += 1
    screen.fill((0,0,0))
    #screen.blit(foto_2,(0,0))

    #day simulation
    # Time.draw_background(total_frames, FPS, screen)
    # Time.draw_hour(screen)


    Process(total_frames, FPS, screen)

    Rain.motion(screen)
    Rain.draw_drops(screen)
    Time(FPS, total_frames)

    pygame.display.flip()
    clock.tick(FPS)
