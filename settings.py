class Settings:
    """Settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 640
        self.bg_color = (230, 230, 130)

        # Ship settings
        self.ship_image = 'images/ship.png'
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_image = 'images/alien.png'
