import sys
import os
import pygame
from pygame.constants import KEYDOWN, QUIT
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]

class GameObject:
    """ Base class for a game object """
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0    

def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    player = pygame.image.load('images/character.png').convert() 
    background = pygame.image.load('images/background.bmp').convert()

    # scale the background image so that it fills the window and
    #   successfully overwrites the old sprite position.
    background = pygame.transform.scale2x(background)
    background = pygame.transform.scale2x(background)
    screen.blit(background, (0, 0))

    objects = []
    for x in range(3):
        o = GameObject(player, x*40, x)
        objects.append(o)

    while 1:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                return

        for o in objects:
            screen.blit(background, o.pos, o.pos)
        for o in objects:
            o.move()
            screen.blit(o.image, o.pos)
        
        pygame.display.update()

if __name__ == '__main__': main()

