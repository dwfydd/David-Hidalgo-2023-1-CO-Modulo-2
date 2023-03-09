import pygame
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.tommy_gunn import TommyGunn

from dino_runner.utils.constants import POWERUP_EFFECTS


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
        self.duration = random.randint(3, 5)
    
    def generate_power_up(self):
        self.when_appears += random.randint(200, 300)
        power_up = random.randint(0,1)
        if power_up == 0:
            power_up = Shield()
        else:
            power_up = TommyGunn()
        self.power_ups.append(power_up)
    
    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed , self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                self.sound_choice = random.choice(POWERUP_EFFECTS)
                self.sound_effect = pygame.mixer.Sound(self.sound_choice)
                self.effect_channel = pygame.mixer.Channel(1)
                self.effect_channel.play(self.sound_effect)
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200 , 300)
