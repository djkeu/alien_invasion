import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """Class to report scoring information."""

    def __init__(self,ai_game) -> None:
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.high_score_file = "txt/highscores.txt"

        # Font setting for scoring information
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial score images
        self.prep_images()


    def prep_images(self):
        """Prepare all initial score images."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the right top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def load_high_score(self):
        self.high_score = 0
        filename = self.high_score_file

        try:
            with open(filename, 'r') as f:
                score_to_load = int(f.readline())
        except FileNotFoundError:
            score_to_load = 0
        except ValueError:
            score_to_load = 0
        
        if score_to_load > self.stats.high_score:
            self.high_score = score_to_load
        else:
            self.high_score = round(self.stats.high_score, -1)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        self.load_high_score()

        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the highscore at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def check_high_score(self):
        """Check to see if there's a new highscore."""
        self.saved_high_score = 0
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def save_high_score(self):
        """Save the high score at the end of the game."""
        score_to_save = str(self.high_score)
        filename = self.high_score_file

        with open(filename, 'w') as f:
            f.write(score_to_save)


    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_scores(self):
        """Draw scores, levels and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
