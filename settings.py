class Settings:
    """Settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 640
        self.bg_color = (10, 10, 30)

        # Ship settings
        self.ship_image = 'images/ship.png'
        self.ship_limit = 3  # Four ships

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (160, 160, 160)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_image = 'images/alien.png'
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game.""" 
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5

        self.fleet_direction = 1  # 1 => right, -1 => left

        # Scoring
        self.alien_points  = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        