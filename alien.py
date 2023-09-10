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
