from pygame.constants import SRCCOLORKEY
from bullet import Bullet
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode( (ai_settings.screen_width, ai_settings.screen_height) )
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship, a goupr of bullets, and group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # start the main loop for the game.
    while True:
        # watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()