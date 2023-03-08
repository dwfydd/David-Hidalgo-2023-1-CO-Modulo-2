import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.sprite import Sprite


class Score(Sprite):
    def __init__(self):
        self.score_counter = 0

    def update_score(self, game_speed):
        self.score_counter +=1

        if self.score_counter % 100 == 0 and game_speed < 500:
            game_speed +=1
        

    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE , 30)
        text = font.render(f'Score: {self.score_counter}' , True , (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)