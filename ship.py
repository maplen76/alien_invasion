import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position
        """
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)
        
        # movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position base on the movement flag.
        """
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        
        if self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
            
        # update rect object from rect.center
        self.rect.centerx = self.center
        
    def blitme(self):
        """draw the ship at its current location
        """
        self.screen.blit(self.image, self.rect)