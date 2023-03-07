import pygame
import random

from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Bird:
    def __init__(self, image):
        self.bird_height = [305, 200, 250]
        self.image = BIRD[0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 100 
        self.rect.y = random.choice(self.bird_height)

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))