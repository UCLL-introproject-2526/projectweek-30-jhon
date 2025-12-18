from maps.MainMenu import MainMenu
from maps.Map1 import Map1
from maps.Map2 import Map2
from maps.Map3 import Map3


def build_maps(main):
    maps = []

    main_menu = MainMenu(main)
    map1 = Map1(main)
    map2 = Map2(main)
    map3 = Map3(main)
    maps.append(main_menu)
    maps.append(map1)
    maps.append(map2)
    maps.append(map3)

    return maps