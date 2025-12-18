import pygame
import math
from entities.Entity import Entity

class MenuController(Entity):
    def __init__(self, play_callback, settings_callback, quit_callback):
        super().__init__(0, 0, 0, 0, main=None, solid=False, name="MenuController")
        
        # Callbacks
        self.__play_callback = play_callback
        self.__settings_callback = settings_callback
        self.__quit_callback = quit_callback
        
        # Colors
        self.__color_white = (255, 255, 255)
        self.__color_gray = (200, 200, 200)
        self.__color_black = (0, 0, 0)
        self.__color_highlight = (255, 255, 100)
        self.__color_accent = (100, 200, 255)
        self.__color_bg_highlight = (80, 80, 80)
        
        # Fonts
        self.__title_font = pygame.font.Font(None, 72)
        self.__subtitle_font = pygame.font.Font(None, 28)
        self.__menu_font = pygame.font.Font(None, 42)
        self.__instruction_font = pygame.font.Font(None, 24)
        self.__version_font = pygame.font.Font(None, 20)
        
        # Menu text
        self.__title = "MERGE CONFLICT"
        self.__subtitle = "A Two-Player Cooperative Platformer"
        self.__version = "v1.0"
        self.__instructions = "Press the key shown in brackets to make your selection"
        
        # Menu options: (label, key_upper, key_lower, callback, icon)
        self.__options = [
            ("Play Game", "P", "p", self.__play_callback, "▶"),
            ("Settings", "S", "s", self.__settings_callback, "⚙"),
            ("Quit", "Q", "q", self.__quit_callback, "✖")
        ]
        
        # Animation
        self.__animation_time = 0.0
        
        # State
        self.__active_key = None
        self.__hovered_option = None
        self.__option_rects = {}
    
    def game_loop(self, delta_time, events):
        self.__animation_time += delta_time
        self.__update_active_key()
        self.__update_mouse_hover()
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.__handle_key_press(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.__handle_mouse_click(event.pos)
    
    def __update_active_key(self):
        keys = pygame.key.get_pressed()
        self.__active_key = None
        
        for label, key_upper, key_lower, callback, icon in self.__options:
            key_constant = getattr(pygame, f"K_{key_lower}")
            if keys[key_constant]:
                self.__active_key = key_lower
                break
    
    def __update_mouse_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        self.__hovered_option = None
        
        for option, rect in self.__option_rects.items():
            if rect.collidepoint(mouse_pos):
                self.__hovered_option = option
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                return
        
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    def __handle_mouse_click(self, pos):
        for option, rect in self.__option_rects.items():
            if rect.collidepoint(pos):
                label, key_upper, key_lower, callback, icon = option
                print(f"{icon} {label}...")
                callback()
                break
    
    def __handle_key_press(self, key):
        for label, key_upper, key_lower, callback, icon in self.__options:
            key_constant = getattr(pygame, f"K_{key_lower}")
            if key == key_constant:
                print(f"{icon} {label}...")
                callback()
                break
    
    def __get_bounce_offset(self):
        return math.sin(self.__animation_time * 2.0) * 5.0
    
    def __get_pulse_size(self):
        return abs(math.sin(self.__animation_time * 8.0)) * 5.0 + 20.0
    
    def __get_fade_alpha(self):
        normalized = (math.sin(self.__animation_time * 2.0) + 1) / 2
        return int(normalized * 80 + 130)
    
    def render_menu_ui(self, screen):
        screen_width, screen_height = screen.get_size()
        
        # Overlay
        overlay = pygame.Surface(screen.get_size())
        overlay.set_alpha(120)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Title
        bounce_offset = self.__get_bounce_offset()
        title_y = screen_height // 4 + bounce_offset
        
        # Title shadow
        shadow = self.__title_font.render(self.__title, True, self.__color_black)
        shadow_rect = shadow.get_rect(center=(screen_width // 2 + 4, title_y + 4))
        screen.blit(shadow, shadow_rect)
        
        # Title main
        title_text = self.__title_font.render(self.__title, True, self.__color_white)
        title_rect = title_text.get_rect(center=(screen_width // 2, title_y))
        screen.blit(title_text, title_rect)
        
        # Title underline
        underline_y = title_rect.bottom + 8 + bounce_offset
        pygame.draw.line(
            screen,
            self.__color_accent,
            (screen_width // 2 - title_rect.width // 2, underline_y),
            (screen_width // 2 + title_rect.width // 2, underline_y),
            3
        )
        
        # Subtitle
        subtitle_text = self.__subtitle_font.render(self.__subtitle, True, self.__color_gray)
        subtitle_rect = subtitle_text.get_rect(center=(screen_width // 2, screen_height // 4 + 55))
        screen.blit(subtitle_text, subtitle_rect)
        
        # Menu options
        center_y = screen_height // 2 + 20
        pulse_size = self.__get_pulse_size()
        self.__option_rects.clear()
        
        for i, option in enumerate(self.__options):
            label, key_upper, key_lower, callback, icon = option
            y_pos = center_y + i * 55
            
            text_with_icon = f"{icon} [{key_upper}] {label}"
            is_active = self.__active_key == key_lower or self.__hovered_option == option
            
            color = self.__color_highlight if is_active else self.__color_white
            
            if is_active:
                text_surf = self.__menu_font.render(text_with_icon, True, color)
                text_rect = text_surf.get_rect(center=(screen_width // 2, y_pos))
                
                # Background highlight
                bg_rect = text_rect.inflate(pulse_size, 12)
                pygame.draw.rect(screen, self.__color_bg_highlight, bg_rect, border_radius=8)
                pygame.draw.rect(screen, self.__color_accent, bg_rect, 2, border_radius=8)
            
            # Shadow
            shadow = self.__menu_font.render(text_with_icon, True, self.__color_black)
            shadow_rect = shadow.get_rect(center=(screen_width // 2 + 2, y_pos + 2))
            screen.blit(shadow, shadow_rect)
            
            # Main text
            option_text = self.__menu_font.render(text_with_icon, True, color)
            option_rect = option_text.get_rect(center=(screen_width // 2, y_pos))
            screen.blit(option_text, option_rect)
            
            # Store rect for click detection
            self.__option_rects[option] = option_rect.inflate(20, 10)
        
        # Instructions
        fade_alpha = self.__get_fade_alpha()
        color = (fade_alpha, fade_alpha, fade_alpha)
        instruction_text = self.__instruction_font.render(self.__instructions, True, color)
        instruction_rect = instruction_text.get_rect(center=(screen_width // 2, screen_height - 30))
        screen.blit(instruction_text, instruction_rect)
        
        # Version
        version_text = self.__version_font.render(self.__version, True, (100, 100, 100))
        screen.blit(version_text, (screen_width - 50, screen_height - 20))
    
    def get_texture(self):
        return None