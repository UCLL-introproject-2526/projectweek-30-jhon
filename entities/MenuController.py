import pygame
from entities.Entity import Entity

class MenuController(Entity):
    """Handles keyboard shortcuts for menu"""
    def __init__(self, play_callback, settings_callback, quit_callback):
        super().__init__(0, 0, 0, 0, main=None, solid=False, name="MenuController")
        self.play_callback = play_callback
        self.settings_callback = settings_callback
        self.quit_callback = quit_callback
    
    def game_loop(self, delta_time, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("P pressed - Play!")
                    self.play_callback()
                elif event.key == pygame.K_s:
                    print("S pressed - Settings!")
                    self.settings_callback()
                elif event.key == pygame.K_q:
                    print("Q pressed - Quit!")
                    self.quit_callback()
    
    def get_texture(self):
        return None
