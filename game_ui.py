import pygame
import os
from settings import *

class GameUI:
    def __init__(self):
        self.font_large = pygame.font.SysFont('Arial', 48)
        self.font_medium = pygame.font.SysFont('Arial', 36)
        self.font_small = pygame.font.SysFont('Arial', 24)
        
        # Charger l'image de fond
        self.background = self._load_background()
        
        self.score = 0
        self.time_left = GAME_DURATION
        self.game_active = False
    
    def _load_background(self):
        path = os.path.join(ASSETS_DIR, "bg.jpeg")
        try:
            bg = pygame.image.load(path).convert()
            return pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            # Fallback si l'image ne charge pas
            surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            surf.fill((50, 50, 100))  # Fond bleu foncé
            return surf
    
    def update_timer(self, dt):
        if self.game_active:
            self.time_left -= dt
            if self.time_left <= 0:
                self.game_active = False
                self.time_left = 0
    
    def draw(self, surface):
        # Dessiner le fond
        surface.blit(self.background, (0, 0))
        
        # Dessiner le score et le temps
        score_text = self.font_medium.render(f"Score: {self.score}", True, WHITE)
        surface.blit(score_text, (20, 20))
        
        time_text = self.font_medium.render(f"Time: {int(self.time_left)}s", True, WHITE)
        surface.blit(time_text, (SCREEN_WIDTH - 150, 20))
        
        # Message de début/fin
        if not self.game_active:
            if self.time_left <= 0:
                message = self.font_large.render("Game Over!", True, WHITE)
                restart = self.font_medium.render("Press SPACE to restart", True, WHITE)
                score_msg = self.font_medium.render(f"Final Score: {self.score}", True, WHITE)
                
                message_rect = message.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 80))
                restart_rect = restart.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40))
                score_rect = score_msg.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                
                surface.blit(message, message_rect)
                surface.blit(score_msg, score_rect)
                surface.blit(restart, restart_rect)
            else:
                title = self.font_large.render("Fruit Capture Game", True, WHITE)
                instructions = [
                    "Use your hand to control the cursor",
                    "Point at fruits to capture them",
                    "Press SPACE to start"
                ]
                
                title_rect = title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
                surface.blit(title, title_rect)
                
                for i, line in enumerate(instructions):
                    text = self.font_medium.render(line, True, WHITE)
                    text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + i * 40))
                    surface.blit(text, text_rect)
    
    def start_game(self):
        self.score = 0
        self.time_left = GAME_DURATION
        self.game_active = True