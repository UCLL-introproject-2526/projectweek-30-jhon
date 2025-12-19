from maps.MainMenu import MainMenu
from maps.Map1 import Map1
from maps.Map2 import Map2
from maps.Map3 import Map3
from maps.Map4 import Map4
from maps.map5 import Map5
from maps.Settings import Settings


def build_maps(main):
    maps = []

    main_menu = MainMenu(main)
    map1 = Map1(main)
    map2 = Map2(main)
    map3 = Map3(main)
    map4 = Map4(main)
    map5 = Map5(main)

    settings= Settings(main)
    maps.append(main_menu)
    maps.append(map1)
    maps.append(map3)
    maps.append(map4)
    maps.append(map5)
    maps.append(map2)


    maps.append(settings)
    return maps