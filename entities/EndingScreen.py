import pygame
from entities.Entity import Entity

class EndingScreen(Entity):
    """Displays an ending screen with victory message and menu options"""
    def __init__(self, replay_callback, menu_callback, quit_callback):
        super().__init__(0, 0, 0, 0, main=None, solid=False, name="EndingScreen")
        self.replay_callback = replay_callback
        self.menu_callback = menu_callback
        self.quit_callback = quit_callback
        
        # Attempt to load or create a font for the ending message
        try:
            self.font_large = pygame.font.Font(None, 72)
            self.font_medium = pygame.font.Font(None, 48)
            self.font_small = pygame.font.Font(None, 32)
        except:
            self.font_large = pygame.font.Font(None, 72)
            self.font_medium = pygame.font.Font(None, 48)
            self.font_small = pygame.font.Font(None, 32)
    
    def game_loop(self, delta_time, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("R pressed - Replay!")
                    self.replay_callback()
                elif event.key == pygame.K_m:
                    print("M pressed - Main Menu!")
                    self.menu_callback()
                elif event.key == pygame.K_q:
                    print("Q pressed - Quit!")
                    self.quit_callback()
    
    def get_texture(self):
        return None
    
    def render_ending_text(self, surface):
        """Draw ending screen text to the surface"""
        # Victory message
        victory_text = self.font_large.render("🎉 YOU WIN! 🎉", True, (255, 215, 0))
        victory_rect = victory_text.get_rect(center=(200, 50))
        surface.blit(victory_text, victory_rect)
        
        # Completion message
        completion_text = self.font_medium.render("Merge Conflict Complete!", True, (100, 255, 100))
        completion_rect = completion_text.get_rect(center=(200, 120))
        surface.blit(completion_text, completion_rect)
        
        # Options
        replay_text = self.font_small.render("Press [R] - Replay", True, (200, 200, 255))
        replay_rect = replay_text.get_rect(center=(200, 160))
        surface.blit(replay_text, replay_rect)
        
        menu_text = self.font_small.render("Press [M] - Main Menu", True, (200, 200, 255))
        menu_rect = menu_text.get_rect(center=(200, 200))
        surface.blit(menu_text, menu_rect)
        
        quit_text = self.font_small.render("Press [Q] - Quit", True, (200, 200, 255))
        quit_rect = quit_text.get_rect(center=(200, 240))
        surface.blit(quit_text, quit_rect)
