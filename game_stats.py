class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize the statistics that can change during the game"""
        self.ship_left = self.ai_settings.ship_limit
