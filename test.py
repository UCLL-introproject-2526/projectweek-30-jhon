import pygame


def create_main_surface():
    surface = pygame.display.set_mode((1000, 600))
    return surface


def main():
    pygame.init()

    main_surface = create_main_surface()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


main()
