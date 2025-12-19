from maps.Map import Map
from entities.Wall2 import Wall2  # Import aangepast naar Wall2
from entities.Spike import Spike
from entities.Pressure_plate import Pressure_plate
from entities.Moving_Element import Moving_Element

class Map5(Map):
    def __init__(self, main):
        super().__init__(main, 'map5', 400, 250, 20, 180, 380, 50)
        self.setup(main)

    def setup(self, main):
        # Alle statische Walls zijn nu Wall2
        self.add_entity(Wall2(0, 240, 400, 30, main))
        self.add_entity(Wall2(-20, 0, 30, 250, main))
        self.add_entity(Wall2(400, 0, 30, 250, main))
        self.add_entity(Wall2(0, 0, 10, 250, main))

        self.add_entity(Wall2(250, 75, 150, 10, main))
        self.add_entity(Wall2(0, 200, 200, 10, main))
        self.add_entity(Wall2(250, 35, 10, 50, main))
        self.add_entity(Wall2(200, 0, 10, 50, main))
        self.add_entity(Wall2(210, 110, 40, 10, main))

        # Moving elements blijven Moving_Element (anders kunnen ze niet schuiven)
        self.add_entity(Moving_Element(325, 100, 10, 80, main, "wall_removable", texture='wall/platform', speed=400))
        self.add_entity(Moving_Element(170, -200, 90, 10, main, "wall_spawnable", texture='wall/platform', speed=100))

        # --- Spikes ---
        # Permanente spikes
        self.add_entity(Spike(280, 60, main))
        self.add_entity(Spike(150, 184, main))
        self.add_entity(Spike(125, 184, main))
        self.add_entity(Spike(210, 94, main))
        self.add_entity(Spike(230, 94, main))

        # Removable Spikes
        s1 = Spike(70, 225, main)
        s1.id = "spike_removable"
        self.add_entity(s1)

        s2 = Spike(120, 225, main)
        s2.id = "spike_removable"
        self.add_entity(s2)

        # Plates
        self.add_entity(Pressure_plate(50, 230, main, "plate_remove_wall"))
        self.add_entity(Pressure_plate(170, 189, main, "plate_spawn_wall"))
        self.add_entity(Pressure_plate(260, 64, main, "plate_remove_spikes"))

    def update(self, past_time, events):
        # Update logica blijft hetzelfde
        if self.get_entity_by_id("plate_remove_wall").get_pressure():
            self.get_entity_by_id("wall_removable").destination_y = -50
        else:
            self.get_entity_by_id("wall_removable").destination_y = 0

        if self.get_entity_by_id("plate_spawn_wall").get_pressure():
            self.get_entity_by_id("wall_spawnable").destination_y = 75
        else:
            self.get_entity_by_id("wall_spawnable").destination_y = -25

        should_disable = self.get_entity_by_id("plate_remove_spikes").get_pressure()

        for entity in self.entities:
            # Veilige check met getattr
            if getattr(entity, 'id', None) == "spike_removable":
                if should_disable:
                    entity.disable()
                else:
                    entity.enable()