from entities.Entity import Entity


class Button(Entity):
    def __init__(self, x, y, width, height, texture, main, text):
        super().__init__(x, y, width, height, main, texture=texture)
        self.text = text
        self.__main = mai

