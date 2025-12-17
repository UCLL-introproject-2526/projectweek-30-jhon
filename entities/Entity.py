from fcntl import FASYNC

import pygame

from tools.importer import image

class Entity:
    def __init__(self, x, y, width, height, main, solid=True, texture=None, gravitation = False, weight = 100, bounce = 0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__solid = solid
        self.__texture = texture
        self.__gravitation = gravitation
        self.__bounce = bounce
        self.speed_x = 0
        self.speed_y = 0
        self.on_floor = False
        self.__main = main
        self.__weight = weight
        self.friction = 0.1
        if texture:
            self.set_texture(texture)

    def is_solid(self):
        return self.__solid

    def set_solid(self, solid):
        self.__solid = solid

    def set_height(self, height):
        self.__height = height

    def get_texture(self):
        return self.__texture
    
    def set_texture(self, texture):
        self.__texture = image(f"assets/textures/entities/{texture}")

    def get_render_data(self):
        return self.__x, self.__y, self.__width, self.__height
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y
    
    def set_y(self, y):
        self.__y = y

    def collision(self, other):
        x1, y1, w1, h1 = self.get_render_data()
        x2, y2, w2, h2 = other.get_render_data()

        return (
            x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2
        )

    def move(self, dx, dy):

        entities = self.__main.get_current_map().get_entities()

        # Y-Sweep
        if dy != 0:
            start_y = self.__y
            sweep_y = min(self.__y, self.__y + dy)
            sweep_h = abs(dy) + self.__height

            allowed_dy = dy
            self.on_floor = False


            for e in entities:
                if e is self or not e.is_solid():
                    continue

                ex, ey, ew, eh = e.get_render_data()

                if intersects_pixel(
                        (self.__x, sweep_y, self.__width, sweep_h),
                        (ex, ey, ew, eh)
                ):
                    if dy > 0:
                        # boven
                        max_dy = ey - (start_y + self.__height)
                        if 0 <= max_dy < allowed_dy:
                            allowed_dy = max_dy
                            self.on_floor = True
                            self.speed_y = 0
                    else:
                        # beneden
                        max_dy = (ey + eh) - start_y
                        if 0 >= max_dy > allowed_dy:
                            allowed_dy = max_dy
                            self.speed_y = 0

            self.__y += allowed_dy

        # X-Sweep
        if dx != 0:
            start_x = self.__x
            sweep_x = min(self.__x, self.__x + dx)
            sweep_w = abs(dx) + self.__width

            allowed_dx = dx

            for e in entities:
                if e is self or not e.is_solid():
                    continue

                ex, ey, ew, eh = e.get_render_data()

                if intersects_pixel(
                        (sweep_x, self.__y, sweep_w, self.__height),
                        (ex, ey, ew, eh)
                ):
                    if dx > 0:
                        # rechts
                        max_dx = ex - (start_x + self.__width)
                        if 0 <= max_dx < allowed_dx:
                            allowed_dx = max_dx
                            self.speed_x = 0
                    else:
                        # links
                        max_dx = (ex + ew) - start_x
                        if 0 >= max_dx > allowed_dx:
                            allowed_dx = max_dx
                            self.speed_x = 0

            self.__x += allowed_dx

    def calc_movement(self, delta_time):
        self.speed_y += self.__gravitation * delta_time * 40
        print(delta_time)
        dx = int(round(self.speed_x))
        dy = int(round(self.speed_y))
        self.move(dx, dy)

    def gravity(self, delta_time):
        print("Speed: ", self.speed_y)
        self.speed_y += self.__gravitation * delta_time * 50
        dx = int(round(self.speed_x))
        dy = int(round(self.speed_y))
        self.move(dx, dy)


    def calc_friction(self, delta_time):
        if self.on_floor:
            self.speed_x *= 1 - (0.3 / delta_time)
        else:
            self.speed_x *= 1 - (0.4 / delta_time)

    def game_loop(self, past_time, events):
        pass
    

def intersects_pixel(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b

    return (
        ax <= bx + bw - 1 and
        ax + aw - 1 >= bx and
        ay <= by + bh - 1 and
        ay + ah - 1 >= by
    )


