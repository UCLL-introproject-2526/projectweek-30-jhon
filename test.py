import pygame

x = 1000
y = 800
def create_main_surface():
    surface = pygame.display.set_mode((x,y))
    return surface


def render_frame(surface):
    pygame.draw.circle(surface, (255, 0, 0), (x/2, y/2), 40)
    pygame.display.flip()


def main():
    pygame.init()

    surface = create_main_surface()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render_frame(surface)

    pygame.quit()


main()
