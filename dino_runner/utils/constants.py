import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "MJ-wallpaper2.png"))

PLAYLIST = [
    os.path.join(MUSIC_DIR, "Soundtracks/Another-Part-Of-Me-8bit-shortened.mp3") ,
    os.path.join(MUSIC_DIR, "Soundtracks/Bad-8bit-shortened.mp3") ,
    os.path.join(MUSIC_DIR, "Soundtracks/Billie-Jean-8bit-shortened.mp3") ,
    os.path.join(MUSIC_DIR, "Soundtracks/Smooth-Criminal-8bit-shortened.mp3") ,
    os.path.join(MUSIC_DIR, "Soundtracks/Thriller-8bit-shortened.mp3")
]

DEATH_EFFECTS = [
    os.path.join(MUSIC_DIR, "Death_Effects/grunt-death-1.mp3") ,
    os.path.join(MUSIC_DIR, "Death_Effects/grunt-death-2.mp3") ,
    os.path.join(MUSIC_DIR, "Death_Effects/grunt-death-3.mp3") ,
    os.path.join(MUSIC_DIR, "Death_Effects/grunt-death-4.mp3") ,
    os.path.join(MUSIC_DIR, "Death_Effects/grunt-death-5.mp3") ,
    os.path.join(MUSIC_DIR, "Death_Effects/grunt-death-6.mp3") 
]

POWERUP_EFFECTS = [
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-1.mp3") ,
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-2.mp3") ,
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-3.mp3") ,
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-4.mp3") ,
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-5.mp3") ,
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-6.mp3") ,
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-7.mp3") ,
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-8.mp3") ,
    os.path.join(MUSIC_DIR, "PowerUp_Effects/grunt-9.mp3") 
]

TOMMY_GUN_EFFECT = os.path.join(MUSIC_DIR, "TOMMY-GUN-EFFECT.mp3")

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-moonwalk-1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-moonwalk-2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-shield-2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-shield-3.png"))
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-jump.png"))
JUMPING_SHIELD = [
    
    pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-shield-1.png")) ,
    pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-shield-2.png")) 
                  
                  ]
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-lean.png"))


DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-shield-1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/MJ-shield-2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

MJ_TOMMY_GUNN = [
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/MJ-TommyGunn1.png')) ,
    pygame.image.load(os.path.join(IMG_DIR, 'Dino/MJ-TommyGunn2.png'))
]

SMALL_CACTUS = [
    
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Small-speakers1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Small-speakers2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Small-speakers3.png")),
    
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Large-speakers1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Large-speakers2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/Large-speakers3.png"))
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
TOMMY_GUNN = pygame.image.load(os.path.join(IMG_DIR, 'Other/TommyGunn.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"

FONT_STYLE = "freesansbold.ttf"

SHIELD_TYPE = 'shield'

GUNN_TYPE = 'TommyGunn'