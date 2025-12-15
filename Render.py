import pygame


def create_main_surface():
    surface = pygame.display.set_mode((1000, 600))
    return surface


def render_spaceship(surface):
    bird_image = pygame.image.load("bird.png").convert_alpha()
    surface.blit(bird_image, (100, 100))


def main():
    pygame.init()

    main_surface = create_main_surface()
    render_spaceship(main_surface)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


main()
