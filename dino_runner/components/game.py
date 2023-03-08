
import pygame
import random
import pygame.mixer
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, PLAYLIST, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.HUD.menu import Menu
from dino_runner.components.HUD.try_again_menu import TryAgainMenu
from dino_runner.components.HUD.score import Score




class Game:

    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.music = False
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('Press any key to start' , self.screen)
        self.try_again_menu = TryAgainMenu('Try Again' , self.screen)
        self.running = False
        self.score = Score()
        self.death_count = 0
    
    def execute(self):
        
        self.running = True
        while self.running:
            if not self.playing:
                self.music = False
                self.show_menu()
                
                
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.soundtrack()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update_score(self.game_speed)
    
    def soundtrack(self):
        if not self.music:
            self.current_soundtrack = random.choice(PLAYLIST)
            pygame.mixer.music.load(self.current_soundtrack)
            pygame.mixer.music.set_volume(0.12)
            pygame.mixer.music.play(-1)
            self.music = True

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw_score(self.screen)
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH //2
        half_screen_height = SCREEN_HEIGHT //2

        if self.death_count == 0:
            self.menu.draw(self.screen)
        
        else:
            self.try_again_menu.draw(self.screen)
            self.score.draw_score(self.screen)


        self.screen.blit(ICON, (half_screen_width - 50 , half_screen_height - 140))
        self.menu.update(self)
    

