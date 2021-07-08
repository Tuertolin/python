"""12-6. Sideways Shooter: Write a game that places a ship on the left side of the screen and
allows the player to move the ship up and down. Make the ship fire a bullet that travels right
across the screen when the player presses the spacebar. Make sure bullets are deleted once they
disappear off the screen.."""
import sys
import pygame

from settings import Settings
from ship import Ship
from keyboard import Keyboard
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()
                
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.keyboard.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared 
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)

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
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
            self.keyboard.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
            self.keyboard.moving_down = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
            self.keyboard.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            self.keyboard.moving_down = False

    def _fire_bullet(self):
        """Create a new buller and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on screen"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.keyboard.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()