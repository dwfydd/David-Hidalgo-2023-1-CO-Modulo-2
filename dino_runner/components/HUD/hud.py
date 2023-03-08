import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.sprite import Sprite



class Hud(Sprite):

    half_screen_height = SCREEN_HEIGHT //2
    half_screen_width = SCREEN_WIDTH //2
   
   
    def __init__(self, message,  screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width , self.half_screen_height )


    def draw(self, screen):
        screen.blit(self.text , self.text_rect)

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))
