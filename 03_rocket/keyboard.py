from settings import Settings
from sys import float_repr_style
import pygame

class Keyboard:
    """A class to manage the keyboard."""

    def __init__(self, ai_game):
        """Initialize the keyboard and set the starting position for the keys"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.settingsKeyboard = Settings()
       
        # Load the ship image and get its rect.
        self.image_arrowup = pygame.image.load('images/keyboard-UP-arrow.png')
        self.image_arrowdown = pygame.image.load('images/keyboard-DOWN-arrow.png')
        self.image_arrowleft = pygame.image.load('images/keyboard-LEFT-arrow.png')
        self.image_arrowright = pygame.image.load('images/keyboard-RIGHT-arrow.png')
        self.rect = self.image_arrowup.get_rect()
        self.rect = self.image_arrowdown.get_rect()
        self.rect = self.image_arrowleft.get_rect()
        self.rect = self.image_arrowright.get_rect()
        
        #                       DELETE
        #  Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)

        # Show keys flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship position depending on the flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right:
            #Update rect object from self.x.
            self.rect.x = self.settingsKeyboard.arrowkey_upx
            self.rect.y =  self.settingsKeyboard.arrowkey_upy
        elif self.moving_up:
            self.rect.x = self.settingsKeyboard.arrowkey_upx
            self.rect.y =  self.settingsKeyboard.arrowkey_upy
        elif self.moving_left:
            self.rect.x = self.settingsKeyboard.arrowkey_upx
            self.rect.y = self.settingsKeyboard.arrowkey_upy
        elif self.moving_down:
            self.rect.x = self.settingsKeyboard.arrowkey_downx
            self.rect.y =  self.settingsKeyboard.arrowkey_downy

    def blitme(self):
        """Draw the ship at its current location."""
        
        if self.moving_down:
            self.screen.blit(self.image_arrowdown, self.rect)
        elif self.moving_up:
            self.screen.blit(self.image_arrowup, self.rect)
        elif self.moving_right:
            self.screen.blit(self.image_arrowright, self.rect)
        elif self.moving_left:
            self.screen.blit(self.image_arrowleft, self.rect)