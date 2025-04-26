import pygame
import sys
import time
from settings import *
from hand_controller import HandController
from game_object import GameObject
from game_ui import GameUI

class FruitCaptureGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialiser les composants
        self.hand_controller = HandController()
        self.ui = GameUI()
        self.objects = pygame.sprite.Group()
        
        # Variables pour le timing
        self.last_spawn_time = 0
        self.last_frame_time = time.time()
        
        # Son (optionnel)
        self.capture_sound = None
        try:
            pygame.mixer.init()
            self.capture_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "capture.wav"))
        except:
            pass
    
    def run(self):
        while self.running:
            current_time = time.time()
            dt = current_time - self.last_frame_time
            self.last_frame_time = current_time
            
            self.handle_events()
            self.update(dt)
            self.draw()
            
            self.clock.tick(FPS)
        
        self.cleanup()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE and not self.ui.game_active:
                    self.ui.start_game()
                    self.objects.empty()
    
    def update(self, dt):
        self.hand_controller.update()
        self.ui.update_timer(dt)
        
        if self.ui.game_active:
            if time.time() - self.last_spawn_time > SPAWN_RATE:
                self.objects.add(GameObject())
                self.last_spawn_time = time.time()
            
            self.objects.update()
            self.check_captures()
    
    def check_captures(self):
        hand_pos = self.hand_controller.get_screen_position()
        
        if hand_pos and self.hand_controller.is_pointing:
            hand_img = self.hand_controller.get_hand_image()
            hand_rect = hand_img.get_rect(center=hand_pos)
            
            for obj in self.objects:
                if not obj.captured and hand_rect.colliderect(obj.rect):
                    obj.captured = True
                    obj.kill()
                    self.ui.score += 1
                    
                    # Jouer le son de capture
                    if self.capture_sound:
                        self.capture_sound.play()
    
    def draw(self):
        # Dessiner l'interface utilisateur (qui inclut le fond)
        self.ui.draw(self.screen)
        
        # Dessiner les objets
        for obj in self.objects:
            self.screen.blit(obj.image, obj.rect)
        
        # Dessiner la main
        hand_pos = self.hand_controller.get_screen_position()
        if hand_pos:
            hand_img = self.hand_controller.get_hand_image()
            hand_rect = hand_img.get_rect(center=hand_pos)
            self.screen.blit(hand_img, hand_rect)
        
        pygame.display.flip()
    
    def cleanup(self):
        self.hand_controller.release()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = FruitCaptureGame()
    game.run()