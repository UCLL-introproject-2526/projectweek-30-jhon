import pygame


def create_main_surface():
    surface = pygame.display.set_mode((800, 600))
    return surface

def clear_surface(surface):
    surface.fill((0, 0, 0))



def render_frame(surface, x):
    pygame.draw.circle(surface, (255, 0, 0), (x, 300), 50)
    pygame.display.flip()


def main():
    pygame.init()

    surface = create_main_surface()
    x = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render_frame(surface, x)
        x += 0.1

        clear_surface(surface)

    pygame.quit()


main()
