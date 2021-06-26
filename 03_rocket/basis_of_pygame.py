import sys
import pygame
from pygame.constants import KEYDOWN

background = pygame.image.load('images/background.bmp')
player = pygame.image.load('images/character.png')
screen = pygame.display.set_mode((1200, 800)) 
screen.blit(background, (0, 0))
position = player.get_rect()

screen_rect = screen.get_rect()
position.center = screen_rect.center 

def check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()

x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x -= 10
    
    screen.blit(background, position, position)
    position = position.move(1, x)
    screen.blit(player, position)
    pygame.display.update()
    pygame.time.delay(50)

