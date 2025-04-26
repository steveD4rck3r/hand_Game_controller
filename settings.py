# Paramètres du jeu
import pygame
import cv2
import os

# Initialisation de pygame
pygame.init()

# Chemin des assets
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')

# Paramètres de la fenêtre
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Fruit Capture Game"
FPS = 60

# Paramètres de la caméra
CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paramètres du jeu
GAME_DURATION = 60
SPAWN_RATE = 2.0
OBJECT_SPEED = 3
OBJECT_SCALE = 0.5  # Échelle des fruits
HAND_SCALE = 0.2    # Échelle de la main