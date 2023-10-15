class Settings:
    """Settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 640
        self.bg_color = (10, 10, 30)

        # Ship settings
        self.ship_image = 'images/ship.png'
        self.ship_speed = 1.5
        self.ship_limit = 2  # Three ships

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (160, 160, 160)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_image = 'images/alien.png'
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 => right, -1 => left
        