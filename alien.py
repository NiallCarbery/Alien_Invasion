import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class for single alien in fleet"""

    def __init__(self, ai_game):
        """Initialize the alien an set starting position"""
        super.__init__()
        self.screen = ai_game.screen

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('iamges/alien.bmp')
        self.rectt = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)