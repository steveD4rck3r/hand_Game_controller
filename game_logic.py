import pygame
import random
from settings import *
from game_objects import *

class GameLogic:
    def __init__(self):
        self.objects = pygame.sprite.Group()
        self.basket = Basket(SCREEN_WIDTH - BASKET_SIZE - 20, SCREEN_HEIGHT - BASKET_SIZE - 20)
        self.hand = Hand()
        self.held_object = None
        self.score = 0
        self.time_remaining = GAME_DURATION
        self.last_spawn_time = 0
        self.font = pygame.font.SysFont(None, 36)
    
    def spawn_object(self, current_time):
        if current_time - self.last_spawn_time > OBJECT_SPAWN_RATE:
            x = random.randint(0, SCREEN_WIDTH - OBJECT_SIZE)
            y = random.randint(0, SCREEN_HEIGHT // 2)
            self.objects.add(Object(x, y))
            self.last_spawn_time = current_time
    
    def update(self, hand_pos, hand_closed, dt):
        # Mettre à jour la main
        self.hand.update_position(hand_pos, hand_closed)
        
        # Gestion de la prise d'objet
        if hand_closed and not self.held_object:
            for obj in self.objects:
                if pygame.sprite.collide_rect(self.hand, obj):
                    self.held_object = obj
                    obj.held = True
                    break
        
        # Gestion du relâchement d'objet
        elif not hand_closed and self.held_object:
            self.held_object.held = False
            
            # Vérifier si l'objet est dans le panier
            if pygame.sprite.collide_rect(self.held_object, self.basket):
                self.score += 1
                self.held_object.kill()
            
            self.held_object = None
        
        # Déplacer l'objet tenu
        if self.held_object:
            self.held_object.rect.center = hand_pos
        
        # Mettre à jour le temps
        self.time_remaining -= dt / 1000  # Convertir ms en secondes
    
    def draw(self, screen):
        # Dessiner le panier
        screen.blit(self.basket.image, self.basket.rect)
        
        # Dessiner les objets
        for obj in self.objects:
            screen.blit(obj.image, obj.rect)
        
        # Dessiner la main
        screen.blit(self.hand.image, self.hand.rect)
        
        # Dessiner le score et le temps
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        time_text = self.font.render(f"Temps: {max(0, int(self.time_remaining))}s", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))
    
    def is_game_over(self):
        return self.time_remaining <= 0
    
    def get_final_score(self):
        return self.score