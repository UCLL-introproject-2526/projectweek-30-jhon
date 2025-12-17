import pygame
from entities.Entity import Entity

class Button(Entity):
    def __init__(self, x, y, width, height, texture=None, main=None, callback=None):
        super().__init__(x, y, width, height, main, name="button", solid=False, texture=None)
        self.label = texture
        self._main = main
        self.callback = callback
    
    def get_texture(self):
        x, y, width, height = self.get_render_data()
        surface = pygame.Surface((width, height))
        surface.fill((0, 255, 0))  # GROEN voor debugging
        if self.label:
            font = pygame.font.Font(None, 24)
            text = font.render(self.label, True, (255, 255, 255))
            surface.blit(text, (5, 8))
        return surface
    
    def game_loop(self, delta_time, events):
        if not self._main:
            return
            
        map_obj = self._main.get_current_map()
        offset_x, offset_y, screen_width, screen_height = self._get_screen_area(map_obj)
        pixelsize = min(screen_width / map_obj.get_range()[0], screen_height / map_obj.get_range()[1])
        
        x, y, width, height = self.get_render_data()
        
        # Screen coordinates van button
        screen_x = offset_x + int(x * pixelsize)
        screen_y = offset_y + int(y * pixelsize)
        screen_w = int(width * pixelsize)
        screen_h = int(height * pixelsize)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if screen_x <= mouse_pos[0] <= screen_x + screen_w and screen_y <= mouse_pos[1] <= screen_y + screen_h:
                        print(f"Button clicked: {self.label}")
                        if self.callback:
                            self.callback()
    
    def _get_screen_area(self, map_obj):
        """Get render offset and dimensions (copy van Render)"""
        from logic.Loop_controller import Loop_controller
        window_width = 600
        window_height = 260
        current_map_width, current_map_height = map_obj.get_range()

        window_aspect_ratio = window_width / window_height
        map_aspect_ratio = current_map_width / current_map_height

        offset_x = 0
        offset_y = 0
        if window_aspect_ratio > map_aspect_ratio:
            screen_height = window_height
            screen_width = int(map_aspect_ratio * screen_height)
            offset_x = (window_width - screen_width) // 2
        else:
            screen_width = window_width
            screen_height = int(screen_width / map_aspect_ratio)
            offset_y = (window_height - screen_height) // 2
        return (offset_x, offset_y, screen_width, screen_height)




    

