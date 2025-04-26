import pygame
import random
import os
from settings import *

class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Charger une image de fruit aléatoire
        fruit_image = random.randint(1, 6)
        self.image_path = os.path.join(ASSETS_DIR, f"{fruit_image}.png")
        
        try:
            # Charger et redimensionner l'image originale
            self.original_image = pygame.image.load(self.image_path).convert_alpha()
            width = int(self.original_image.get_width() * OBJECT_SCALE)
            height = int(self.original_image.get_height() * OBJECT_SCALE)
            self.original_image = pygame.transform.scale(self.original_image, (width, height))
            
            # Créer une copie pour l'image courante
            self.image = self.original_image.copy()
        except:
            # Fallback si l'image ne charge pas
            self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.circle(self.original_image, 
                             (random.randint(100, 255), 
                              random.randint(100, 255), 
                              random.randint(100, 255)), 
                             (25, 25), 25)
            self.image = self.original_image.copy()
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        
        self.speed = random.randint(1, OBJECT_SPEED)
        self.captured = False
        self.rotation = 0
        self.rotation_speed = random.uniform(-2, 2)
    
    def update(self):
        # Déplacer l'objet vers le bas avec une légère rotation
        self.rect.y += self.speed
        self.rotation += self.rotation_speed
        
        # Appliquer la rotation
        center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, self.rotation)
        self.rect = self.image.get_rect(center=center)
        
        # Vérifier si l'objet est sorti de l'écran
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()