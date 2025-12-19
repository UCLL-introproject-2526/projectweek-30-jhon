import pygame

class Render:
    def __init__(self, caption, width=800, height=500):
        self.__width = width
        self.__height = height
        print("setupDisplay")
        self.__screen = pygame.display.set_mode((self.__width, self.__height), pygame.RESIZABLE)
        pygame.display.set_caption(caption)

        self.__fullscreen = False

    def update(self, main):
        if not pygame.display.get_init() or self.__screen is None:
            return
        map = main.get_current_map()
        offset_x, offset_y, screen_width, screen_height = self.__get_usable_screen_area(map)
        pixel_size = min(screen_width / map.get_range()[0], screen_height / map.get_range()[1])

        # Clear screen
        self.__screen.fill((30, 30, 30))

        # Draw map background first
        pygame.draw.rect(self.__screen, (50, 50, 50), (offset_x, offset_y, screen_width, screen_height))

        # background image
        scaled_image = pygame.transform.scale(map.get_bg(), (screen_width, screen_height))
        self.__screen.blit(scaled_image, (offset_x, offset_y))

        # Draw entities on top
        for entity in map.get_entities():
            x, y, width, height = entity.get_render_data()
            if entity.get_texture() is not None:
                scaled_entity_image = pygame.transform.scale(entity.get_texture(),
                                                             (int(width * pixel_size), int(height * pixel_size)))
                self.__screen.blit(scaled_entity_image, (offset_x + int(x * pixel_size), offset_y + int(y * pixel_size)))

        # front image
        scaled_image = pygame.transform.scale(map.get_fg(), (screen_width, screen_height))
        self.__screen.blit(scaled_image, (offset_x, offset_y))

        pygame.display.flip()

    def __get_usable_screen_area(self, map):
        if not pygame.display.get_init() or self.__screen is None:
            window_width, window_height = self.__width, self.__height
        else:
            try:
                window_width, window_height = self.__screen.get_size()
            except Exception:
                window_width, window_height = self.__width, self.__height

        current_map_width, current_map_height = map.get_range()

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
        return offset_x, offset_y, screen_width, screen_height

    def get_cursor_position(self, main):
        if not pygame.display.get_init() or self.__screen is None:
            return None

        map = main.get_current_map()
        offset_x, offset_y, screen_width, screen_height = self.__get_usable_screen_area(map)
        map_w, map_h = map.get_range()
        pixel_size = min(screen_width / map_w, screen_height / map_h)

        mx, my = pygame.mouse.get_pos()

        local_x = mx - offset_x
        local_y = my - offset_y

        if local_x < 0 or local_y < 0 or local_x >= screen_width or local_y >= screen_height:
            return None

        grid_x = int(local_x / pixel_size)
        grid_y = int(local_y / pixel_size)

        grid_x = max(0, min(grid_x, map_w - 1))
        grid_y = max(0, min(grid_y, map_h - 1))

        return grid_x, grid_y



    def enter_fullscreen(self):
        if self.__fullscreen:
            return
        if not self.__fullscreen:
            self.__screen = pygame.display.set_mode(
                (self.__width, self.__height),
                pygame.FULLSCREEN
            )
            self.__fullscreen = True

    def leave_fullscreen(self):
        if not self.__fullscreen:
            return
        if self.__fullscreen:
            self.__screen = pygame.display.set_mode(
                (self.__width, self.__height)
            )
            self.__fullscreen = False

    def toggle_fullscreen(self):
        if self.__fullscreen:
            self.leave_fullscreen()
        else:
            self.enter_fullscreen()

    def is_fullscreen(self):
        return self.__fullscreen

    def quit(self):
        pygame.quit()
        self.__screen = None
        exit('Game was closed.')
