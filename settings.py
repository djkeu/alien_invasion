class Settings:
    """Settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 640
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
