"""12-4. Rocket: Make a game that begins with a rocket in the center of the screen. Allow the
player to move the rocket up, down, left, or right using the four arrow keys. Make sure the
rocket never moves beyond any edge of the screen.
12-5. Keys: Make a Pygame file that creates an empty screen. In the event loop, print the
event.key attribute whenever a pygame.KEYDOWN event is detected. Run the program and press
various keys to see how Pygame responds."""
import sys
import pygame

from settings import Settings
from ship import Ship
from keyboard import Keyboard

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initiate game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("ALIEN Inva5ion")

        self.ship = Ship(self)
        self.keyboard = Keyboard(self)
                
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.keyboard.update()
            self._update_screen()

    def _check_events(self):
        # Watch for Keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            self.keyboard.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            self.keyboard.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
            self.keyboard.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
            self.keyboard.moving_down = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            self.keyboard.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            self.keyboard.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
            self.keyboard.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            self.keyboard.moving_down = False

    def _update_screen(self):
        """Update images on screen"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.keyboard.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()