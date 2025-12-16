import pygame
from entities.Entity import Entity
from entities.Button import Button
import settings.keyboard_layout as kb

class SettingsMap:
    def __init__(self, main, map_obj):
        self.main = main
        self.map = map_obj
        self._build()
    
    def _build(self):
        def toggle_layout():
            kb.keyboard_layout = "azerty" if kb.keyboard_layout == "qwerty" else "qwerty"
            print(f"Keyboard layout: {kb.keyboard_layout}")
            # update button label to reflect new layout
            self.layout_btn.label = f"LAYOUT: {kb.keyboard_layout}"
        
        def back():
            self.main.select_map(0)
        
        self.layout_btn = Button(50, 50, 140, 40, texture=f"LAYOUT: {kb.keyboard_layout}", main=self.main, callback=toggle_layout)
        self.map.add_entity(self.layout_btn)
        self.map.add_entity(Button(50, 110, 100, 40, texture="BACK", main=self.main, callback=back))
        self.map.add_entity(SettingsController(back))

class SettingsController(Entity):
    def __init__(self, back_callback):
        super().__init__(0, 0, 0, 0, main=None, solid=False)
        self.back_callback = back_callback
    
    def game_loop(self, delta_time, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.back_callback()
    
    def get_texture(self):
        return None
