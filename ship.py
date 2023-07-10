import pygame 

class Ship:
    """Class managing ship"""
    def __init__(self, ai_game):
        """Initlaize ship and position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settinfs = ai_game.settings

        #Load ship and rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start ech new ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimal value of ships horizontal position
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ships position based on the movement flags"""
        #Ipdate ships x value
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settigs.ship_speed

        #Update the rect position based on x
        self.rect.x = self.x

    def blitme(self):
        """Draw tthe ship at its current location"""
        self.screen.blit(self.image, self.rect)

    