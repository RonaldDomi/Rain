import pygame
from rain import *
import process

class Time():
    Hour = 24
    red = 0
    green = 0
    blue = 0

    def __init__(self, FPS, total_frames):

        if total_frames % (FPS * 1) == 0:
            Time.Hour += 1
        if Time.Hour == 25:
            Time.Hour = 1

    @staticmethod
    def draw_hour(screen):
        process.text_to_screen(screen, 'Hour : ' + str(Time.Hour), screen.get_width() - 150, screen.get_height() - 17)

    @staticmethod
    def draw_background(total_frames, FPS, screen):

        if Time.Hour < 6:           # whiter
            if total_frames % (FPS//11) == 0:
                Time.red += 1
                Time.green += 1
                Time.blue += 1
        elif Time.Hour < 9:         # reder
            if total_frames % (FPS//4) == 0:
                Time.red += 1
        elif Time.Hour < 12:        # yellower
            if total_frames % (FPS//3) == 0:
                Time.green += 1
        elif Time.Hour < 16:        #litle change
            if total_frames % (FPS//4) == 0:
                Time.green += 2
                Time.red += 2
        elif Time.Hour < 21:        # purple
            if total_frames % (FPS//4) == 0:
                Time.green -= 2
                Time.blue += 2
        elif Time.Hour <= 24:        #blacker
            if total_frames % (FPS//11) == 0:
                Time.blue -= 2
                Time.green -= 2
                Time.red -= 2

            if Time.red < 0:
                Time.red = 0
            if Time.green < 0:
                Time.green = 0
            if Time.blue < 0:
                Time.blue = 0


        screen.fill((Time.red, Time.green, Time.blue))
