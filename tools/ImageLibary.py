import pygame

class ImageLibrary:
    def __init__(self):
        self.__images = []

    def get_image(self, source, alpha=True):
        if source is None:
            return None
        for image in self.__images:
            if image.path == source and image.alpha == alpha:
                return image.image
        new_image = Image(source, alpha)
        self.__images.append(new_image)
        return new_image.image

class Image:
    def __init__(self, path, alpha):
        self.path = path
        self.alpha = alpha
        if alpha:
            self.image = pygame.image.load(f"assets/textures/{path}").convert_alpha()
        else:
            self.image = pygame.image.load(f"assets/textures/{path}").convert()


image_library = ImageLibrary()