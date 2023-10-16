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
        self.ship_limit = 2  # Three ships

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

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game.""" 
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1  # 1 => right, -1 => left
