import random
from typing import List

from worlds.geoguessr.data.maps import GeoguessrMap, COUNTRY_MAPS, WORLD_MAPS

WORLD_PERCENT = 0.10
MAP_ITEMS_COMPARED_TO_GOAL = 1.5


def obtain_random_maps(nb_map_for_goal: int, world_random: random.Random) -> List[GeoguessrMap]:
    countries: List[GeoguessrMap] = []
    expected_total: int = 1+int(nb_map_for_goal * MAP_ITEMS_COMPARED_TO_GOAL)
    expected_world: int = 1+int(expected_total * WORLD_PERCENT)

    if expected_world > len(WORLD_MAPS):
        expected_world = len(WORLD_MAPS)

    expected_countries: int = expected_total - expected_world
    if expected_countries > len(COUNTRY_MAPS):
        expected_countries = len(COUNTRY_MAPS)

    world_random.shuffle(WORLD_MAPS)
    world_random.shuffle(COUNTRY_MAPS)

    countries.extend(WORLD_MAPS[0:expected_world])
    countries.extend(COUNTRY_MAPS[0:expected_countries])

    return countries
