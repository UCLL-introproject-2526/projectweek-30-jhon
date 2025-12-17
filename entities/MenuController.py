"""
MenuController Module
Manages the game's main menu interface with animated elements and keyboard navigation.
"""

import pygame
import math
from typing import Callable, Tuple, Optional
from dataclasses import dataclass
from entities.Entity import Entity


@dataclass
class ColorPalette:
    """Centralized color scheme for consistent theming"""
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    GRAY: Tuple[int, int, int] = (200, 200, 200)
    DARK_GRAY: Tuple[int, int, int] = (150, 150, 150)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    HIGHLIGHT: Tuple[int, int, int] = (255, 255, 100)
    ACCENT: Tuple[int, int, int] = (100, 200, 255)
    BG_HIGHLIGHT: Tuple[int, int, int] = (80, 80, 80)
    OVERLAY: Tuple[int, int, int] = (0, 0, 0)


@dataclass(frozen=True)
class MenuOption:
    """Represents a single menu option with its properties"""
    label: str
    key_upper: str
    key_lower: str
    callback: Callable
    icon: str
    
    def is_active(self, pressed_key: Optional[str]) -> bool:
        """Check if this option is currently active"""
        return pressed_key == self.key_lower


class AnimationController:
    """Handles all animation timing and effects"""
    
    def __init__(self):
        self.time = 0.0
        
    def update(self, delta_time: float) -> None:
        """Update animation timer"""
        self.time += delta_time
    
    def get_bounce_offset(self, speed: float = 2.0, amplitude: float = 5.0) -> float:
        """Calculate vertical bounce offset"""
        return math.sin(self.time * speed) * amplitude
    
    def get_pulse_size(self, speed: float = 8.0, base_size: float = 20.0, amplitude: float = 5.0) -> float:
        """Calculate pulsing size for highlights"""
        return abs(math.sin(self.time * speed)) * amplitude + base_size
    
    def get_fade_alpha(self, speed: float = 2.0, min_alpha: int = 130, max_alpha: int = 210) -> int:
        """Calculate fading alpha value"""
        normalized = (math.sin(self.time * speed) + 1) / 2  # 0 to 1
        return int(normalized * (max_alpha - min_alpha) + min_alpha)


class MenuRenderer:
    """Handles all rendering operations for the menu"""
    
    def __init__(self, color_palette: ColorPalette):
        self.colors = color_palette
        self._init_fonts()
    
    def _init_fonts(self) -> None:
        """Initialize font objects"""
        self.title_font = pygame.font.Font(None, 72)
        self.subtitle_font = pygame.font.Font(None, 28)
        self.menu_font = pygame.font.Font(None, 42)
        self.instruction_font = pygame.font.Font(None, 24)
        self.version_font = pygame.font.Font(None, 20)
    
    def render_overlay(self, screen: pygame.Surface, alpha: int = 120) -> None:
        """Render semi-transparent overlay for better readability"""
        overlay = pygame.Surface(screen.get_size())
        overlay.set_alpha(alpha)
        overlay.fill(self.colors.OVERLAY)
        screen.blit(overlay, (0, 0))
    
    def render_title(self, screen: pygame.Surface, title: str, bounce_offset: float) -> None:
        """Render animated title with shadow and accent line"""
        screen_width, screen_height = screen.get_size()
        title_y = screen_height // 4 + bounce_offset
        
        # Shadow
        shadow = self.title_font.render(title, True, self.colors.BLACK)
        shadow_rect = shadow.get_rect(center=(screen_width // 2 + 4, title_y + 4))
        screen.blit(shadow, shadow_rect)
        
        # Main title
        title_text = self.title_font.render(title, True, self.colors.WHITE)
        title_rect = title_text.get_rect(center=(screen_width // 2, title_y))
        screen.blit(title_text, title_rect)
        
        # Accent underline
        underline_y = title_rect.bottom + 8 + bounce_offset
        pygame.draw.line(
            screen,
            self.colors.ACCENT,
            (screen_width // 2 - title_rect.width // 2, underline_y),
            (screen_width // 2 + title_rect.width // 2, underline_y),
            3
        )
    
    def render_subtitle(self, screen: pygame.Surface, subtitle: str) -> None:
        """Render subtitle text"""
        screen_width, screen_height = screen.get_size()
        subtitle_text = self.subtitle_font.render(subtitle, True, self.colors.GRAY)
        subtitle_rect = subtitle_text.get_rect(center=(screen_width // 2, screen_height // 4 + 55))
        screen.blit(subtitle_text, subtitle_rect)
    
    def render_menu_option(
        self, 
        screen: pygame.Surface, 
        option: MenuOption, 
        y_pos: int,
        is_active: bool,
        pulse_size: float
    ) -> pygame.Rect:
        """Render a single menu option with active state effects and return its rect"""
        screen_width = screen.get_width()
        text_with_icon = f"{option.icon} [{option.key_upper}] {option.label}"
        
        # Determine color and draw highlight if active
        color = self.colors.HIGHLIGHT if is_active else self.colors.WHITE
        
        if is_active:
            text_surf = self.menu_font.render(text_with_icon, True, color)
            text_rect = text_surf.get_rect(center=(screen_width // 2, y_pos))
            
            # Animated background highlight
            bg_rect = text_rect.inflate(pulse_size, 12)
            pygame.draw.rect(screen, self.colors.BG_HIGHLIGHT, bg_rect, border_radius=8)
            pygame.draw.rect(screen, self.colors.ACCENT, bg_rect, 2, border_radius=8)
        
        # Shadow
        shadow = self.menu_font.render(text_with_icon, True, self.colors.BLACK)
        shadow_rect = shadow.get_rect(center=(screen_width // 2 + 2, y_pos + 2))
        screen.blit(shadow, shadow_rect)
        
        # Main text
        option_text = self.menu_font.render(text_with_icon, True, color)
        option_rect = option_text.get_rect(center=(screen_width // 2, y_pos))
        screen.blit(option_text, option_rect)
        
        # Return the rect for click detection
        return option_rect.inflate(20, 10)
    
    def render_instructions(self, screen: pygame.Surface, text: str, alpha: int) -> None:
        """Render bottom instructions with fade effect"""
        screen_width, screen_height = screen.get_size()
        color = (alpha, alpha, alpha)
        instruction_text = self.instruction_font.render(text, True, color)
        instruction_rect = instruction_text.get_rect(center=(screen_width // 2, screen_height - 30))
        screen.blit(instruction_text, instruction_rect)
    
    def render_version(self, screen: pygame.Surface, version: str) -> None:
        """Render version info in corner"""
        screen_width, screen_height = screen.get_size()
        version_text = self.version_font.render(version, True, (100, 100, 100))
        screen.blit(version_text, (screen_width - 50, screen_height - 20))


class MenuController(Entity):
    """Main menu controller with keyboard navigation and animations"""
    
    def __init__(self, play_callback: Callable, settings_callback: Callable, quit_callback: Callable):
        super().__init__(0, 0, 0, 0, main=None, solid=False, name="MenuController")
        
        # Initialize components
        self.colors = ColorPalette()
        self.animator = AnimationController()
        self.renderer = MenuRenderer(self.colors)
        
        # Menu configuration
        self.title = "MERGE CONFLICT"
        self.subtitle = "A Two-Player Cooperative Platformer"
        self.version = "v1.0"
        self.instructions = "Press the key shown in brackets to make your selection"
        
        # Menu options
        self.options = [
            MenuOption("Play Game", "P", "p", play_callback, "▶"),
            MenuOption("Settings", "S", "s", settings_callback, "⚙"),
            MenuOption("Quit", "Q", "q", quit_callback, "✖")
        ]
        
        # State tracking
        self.active_key: Optional[str] = None
        self.hovered_option: Optional[MenuOption] = None
        self.option_rects: dict[MenuOption, pygame.Rect] = {}
    
    def _update_active_key(self) -> None:
        """Track which key is currently pressed for visual feedback"""
        keys = pygame.key.get_pressed()
        self.active_key = None
        
        for option in self.options:
            key_constant = getattr(pygame, f"K_{option.key_lower}")
            if keys[key_constant]:
                self.active_key = option.key_lower
                break
    
    def _update_mouse_hover(self) -> None:
        """Track which option is being hovered over"""
        mouse_pos = pygame.mouse.get_pos()
        self.hovered_option = None
        
        for option, rect in self.option_rects.items():
            if rect.collidepoint(mouse_pos):
                self.hovered_option = option
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                return
        
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    def _handle_mouse_click(self, pos: Tuple[int, int]) -> None:
        """Handle mouse click on menu options"""
        for option, rect in self.option_rects.items():
            if rect.collidepoint(pos):
                print(f"{option.icon} {option.label}...")
                option.callback()
                break
    
    def _handle_key_press(self, key: int) -> None:
        """Handle keyboard input and trigger appropriate callback"""
        for option in self.options:
            key_constant = getattr(pygame, f"K_{option.key_lower}")
            if key == key_constant:
                print(f"{option.icon} {option.label}...")
                option.callback()
                break
    
    def game_loop(self, delta_time: float, events: list) -> None:
        """Main update loop: handle input and update animations"""
        self.animator.update(delta_time)
        self._update_active_key()
        self._update_mouse_hover()
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                self._handle_key_press(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._handle_mouse_click(event.pos)
    
    def render_menu_ui(self, screen: pygame.Surface) -> None:
        """Render all menu elements with animations"""
        screen_width, screen_height = screen.get_size()
        
        # Render overlay for better readability
        self.renderer.render_overlay(screen)
        
        # Render title with bounce animation
        bounce_offset = self.animator.get_bounce_offset()
        self.renderer.render_title(screen, self.title, bounce_offset)
        
        # Render subtitle
        self.renderer.render_subtitle(screen, self.subtitle)
        
        # Render menu options
        center_y = screen_height // 2 + 20
        pulse_size = self.animator.get_pulse_size()
        self.option_rects.clear()
        
        for i, option in enumerate(self.options):
            y_pos = center_y + i * 55
            is_active = option.is_active(self.active_key) or (self.hovered_option == option)
            rect = self.renderer.render_menu_option(screen, option, y_pos, is_active, pulse_size)
            self.option_rects[option] = rect
        
        # Render instructions with fade effect
        fade_alpha = self.animator.get_fade_alpha()
        self.renderer.render_instructions(screen, self.instructions, fade_alpha)
        
        # Render version info
        self.renderer.render_version(screen, self.version)
    
    def get_texture(self):
        return None