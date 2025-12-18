from tools.importer import image
from tools.SoundLibrary import SoundLibrary

class Entity:
    def __init__(self, x, y, width, height, main, solid=False, texture=None, gravitation=False, id=None):
        self.x = x
        self.y = y
        self.speed_y = 0
        self.speed_x = 0
        self.width = width
        self.height = height
        self.main = main
        self.__is_solid = solid
        self.texture = texture
        self.__gravitation = gravitation
        self.__id = id
        self.__restore = (x,y)
        self.__SoundLibrary = SoundLibrary()
        if texture:
            self.set_texture(texture)

    def play(self, sound):
        self.__SoundLibrary.play(sound)

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def is_solid(self):
        return self.__is_solid

    def set_texture(self, texture):
        self.texture = image(f"entities/{texture}.png")

    def restore_entity(self):
        self.restore()
        self.__restore_position()

    def restore(self):
        pass

    def __restore_position(self):
        self.x, self.y = self.__restore
        print(f"position has been restored to {self.x}, {self.y}")

    def get_texture(self):
        return self.texture

    def get_render_data(self):
        return self.x, self.y, self.width, self.height

    def set_height(self, height):
        self.height = height

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

        entities = self.main.get_current_map().get_entities()

        # Y-Sweep
        if dy != 0:
            start_y = self.y
            sweep_y = min(self.y, self.y + dy)
            sweep_h = abs(dy) + self.height

            allowed_dy = dy
            self.on_floor = False


            for e in entities:
                if e is self or not e.is_solid():
                    continue

                ex, ey, ew, eh = e.get_render_data()

                if intersects_pixel(
                        (self.x, sweep_y, self.width, sweep_h),
                        (ex, ey, ew, eh)
                ):
                    if dy > 0:
                        # boven
                        max_dy = ey - (start_y + self.height)
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

            self.y += allowed_dy

        # X-Sweep
        if dx != 0:
            start_x = self.x
            sweep_x = min(self.x, self.x + dx)
            sweep_w = abs(dx) + self.width

            allowed_dx = dx

            for e in entities:
                if e is self or not e.is_solid():
                    continue

                ex, ey, ew, eh = e.get_render_data()

                if intersects_pixel(
                        (sweep_x, self.y, sweep_w, self.height),
                        (ex, ey, ew, eh)
                ):
                    if dx > 0:
                        # rechts
                        max_dx = ex - (start_x + self.width)
                        if 0 <= max_dx < allowed_dx:
                            allowed_dx = max_dx
                            self.speed_x = 0
                    else:
                        # links
                        max_dx = (ex + ew) - start_x
                        if 0 >= max_dx > allowed_dx:
                            allowed_dx = max_dx
                            self.speed_x = 0

            self.x += allowed_dx

    def gravity(self, delta_time):
        print("Speed: ", self.speed_y)
        self.speed_y += self.__gravitation * delta_time * 50
        dx = int(round(self.speed_x))
        dy = int(round(self.speed_y))
        self.move(dx, dy)

    def game_loop(self, past_time, events):
        pass

    def calc_movement(self, delta_time):
        self.speed_y += self.__gravitation * delta_time * 40
        dx = int(round(self.speed_x))
        dy = int(round(self.speed_y))
        self.move(dx, dy)

    def get_colliding_objects(self):
        colliding_entities = []
        for entity in self.main.get_current_map().get_entities():
            if self.collision(entity):
                colliding_entities.append(entity)
        return colliding_entities



def intersects_pixel(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b

    return (
            ax <= bx + bw - 1 and
            ax + aw - 1 >= bx and
            ay <= by + bh - 1 and
            ay + ah - 1 >= by
    )
