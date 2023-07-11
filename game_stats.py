class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game inactive
        self.game_active = False

    def reset_stats(self):
        """Reset statistics"""
        self.ships_left = self.settings.ship_limit