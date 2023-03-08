import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.components.HUD.hud import Hud


class Menu(Hud):
    half_screen_height = SCREEN_HEIGHT //2
    half_screen_width = SCREEN_WIDTH //2
   
   
    def __init__(self, message,  screen):
        super().__init__(message, screen)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)
    
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game.running = False
                game.playing = False
            
            elif event.type == pygame.KEYDOWN:
                game.run()
