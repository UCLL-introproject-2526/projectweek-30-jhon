import pygame
from entities.Button import Button
from entities.TextEntity import TextEntity
from entities.Wall import Wall


class PauseMenu:
    def __init__(self, main):
        self.main = main
        self.is_open = False
        self.entities = []
        self.setup()
    
    def setup(self):        
        # Title (centered, yellow/gold color)
        self.add_entity(TextEntity(150, 65, self.main, "PAUSED", (255, 215, 0), id="pause_title", has_bg=True))
        
        # Menu buttons (centered, stacked vertically)
        self.add_entity(Button(150, 100, self.main, "Resume", id="resume", is_big=True))
        self.add_entity(Button(150, 130, self.main, "Reset Level", id="restart", is_big=True))
        self.add_entity(Button(150, 160, self.main, "Main Menu", id="main_menu", is_big=True))
        self.add_entity(Button(150, 190, self.main, "Quit", id="quit", is_big=True))
    
    def add_entity(self, entity):
        self.entities.append(entity)
    
    def get_entity_by_id(self, id):
        for entity in self.entities:
            if entity.get_id() == id:
                return entity
        return None
    
    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def toggle(self):
        self.is_open = not self.is_open
    
    def update(self, past_time, events):
        if not self.is_open:
            return False
        
        # Check button clicks BEFORE updating entities (same pattern as MainMenu/Ending)
        if self.get_entity_by_id('resume').is_clicked():
            self.close()
            return True
        
        if self.get_entity_by_id('restart').is_clicked():
            self.main.restart_map()
            self.close()
            return True
        
        if self.get_entity_by_id('main_menu').is_clicked():
            self.main.map(0)
            self.close()
            return True
        
        if self.get_entity_by_id('quit').is_clicked():
            self.main.quit()
            return True
        
        # Update entities after checking clicks
        for entity in self.entities:
            entity.game_loop(past_time, events)
        
        return True
        
    
    def get_entities(self):
        return self.entities if self.is_open else []
