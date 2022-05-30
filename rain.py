import pygame
from random import randint
import process
from Time import Time

class Rain():

    direction = 'left'
    intensity = 3
    List = []
    color = [255, 255, 255]

    def __init__(self, screen, f = 'go_down'):                      # x, y, height, velX, velY, go according to direction
        Rain.List.append(self)

        self.x = randint(0, screen.get_width())
        self.y = randint(-20, -3)
        if f != 'go_down':
            rand = randint(1, 4)
            if rand == 1:
                self.y = randint(1, screen.get_height())            # moving   left
                if f == 'go_left': #f == -1
                    self.x = screen.get_width()
                if f == 'go_right':  #f == 1                        # moving   right
                    self.x = 0

        self.height = randint(5, 13)                                #height should be changable

        self.velY = randint(3,8)
        self.velX = 0

    @staticmethod
    def motion(screen):                                             # if left, go left   drop+=vel    if drop than delete
        for drop in Rain.List:
            if Rain.direction == 'left':
                drop.velX = randint(1, 3)
                drop.velX = -drop.velX
            elif Rain.direction == 'right':
                drop.velX = randint(1, 3)

            drop.y += drop.velY
            drop.x += drop.velX

            if drop.y + drop.height > screen.get_height():
                Rain.List.remove(drop)
                del(drop)
            elif drop.x < 0 or drop.x > screen.get_width():
                Rain.List.remove(drop)
                del(drop)

    @staticmethod
    def change_direction():                                         # change direction to random

        dir = randint(1, 2)
        if Rain.direction == 'down':
            if dir == 1:
                Rain.direction = 'left'
            if dir == 2:
                Rain.direction = 'right'
        elif Rain.direction == 'left':
            if dir == 1:
                Rain.direction = 'down'
            if dir == 2:
                Rain.direction = 'right'
        elif Rain.direction == 'right':
            if dir == 1:
                Rain.direction = 'down'
            if dir == 2:
                Rain.direction = 'left'

    @staticmethod
    def change_intensity():                                         # change intensity 1-5
        Rand_List = [x for x in range(1, 6)]
        Rand_List.remove(Rain.intensity)

        random_Index = randint(0, 3)
        Rain.intensity = Rand_List[random_Index]


    @staticmethod
    def draw_drops(screen):                                         # draw line and text
        process.text_to_screen(screen, Rain.direction, 0, screen.get_height() - 20, 20)
        process.text_to_screen(screen, 'Intensity : ' + str(Rain.intensity), 0, screen.get_height() - 42, 20)
        for drop in Rain.List:
            pygame.draw.line(screen, Rain.color, (drop.x, drop.y),(drop.x, drop.y + drop.height))
