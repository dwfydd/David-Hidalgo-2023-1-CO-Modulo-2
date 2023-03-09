import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SHIELD_TYPE, GUNN_TYPE, DEFAULT_TYPE, TOMMY_GUN_EFFECT
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class ObstacleManager:
  def __init__(self):
    self.obstacles = []

  
  def generate_obstacle(self, obstacle_type):
    if obstacle_type == 0:
      cactus_type = 'SMALL'
      obstacle = Cactus(cactus_type)
    elif obstacle_type == 1:
      cactus_type = 'LARGE'
      obstacle = Cactus(cactus_type)
    else:
      obstacle = Bird()
    return obstacle
    
  def update(self, game):
    self.user_input = pygame.key.get_pressed()
    if len(self.obstacles) == 0:
      obstacle_type = random.randint(0, 2)
      obstacle = self.generate_obstacle(obstacle_type)
      self.obstacles.append(obstacle)
      
    
      
    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      
      if game.player.type == GUNN_TYPE and self.user_input[pygame.K_RIGHT]:
        self.sound_effect = pygame.mixer.Sound(TOMMY_GUN_EFFECT)
        self.effect_channel = pygame.mixer.Channel(2)
        self.sound_effect.set_volume(0.12)
        self.effect_channel.play(self.sound_effect)
  
        self.obstacles.remove(obstacle)
        break
      
      if game.player.dino_rect.colliderect(obstacle.rect):
        
        if game.player.type != SHIELD_TYPE:
          pygame.time.delay(1000)
          game.death_count.update()
          game.playing = False
          game.player.type == DEFAULT_TYPE
          break
          


        else:
          self.obstacles.remove(obstacle)
  
  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)
      
  def reset_obstacles(self):
    self.obstacles = []