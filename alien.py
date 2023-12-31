from typing import Any
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class to represent a singel alien."""

    def __init__(self, ai_game) -> None:
        """Initialize the alien and its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image, set its rect attribute
        self.image = pygame.image.load(self.settings.alien_image).convert_alpha()
        self.rect = self.image.get_rect()

        # Start new aliens near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True is alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
