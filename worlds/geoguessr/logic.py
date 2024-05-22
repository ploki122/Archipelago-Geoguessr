import math
import random
from typing import List

from BaseClasses import CollectionState
from . import GeoguessrMap, WORLD_MAPS, COUNTRY_MAPS, GeoguessrOptions
from .locations import LOCATIONS_PER_MAP, WORLD_LOCATIONS
from .options import MovementType

WORLD_PERCENT = 0.10
MAP_ITEMS_COMPARED_TO_GOAL = 1.5


def obtain_random_maps(nb_map_for_goal: int, world_random: random.Random) -> List[GeoguessrMap]:
    countries: List[GeoguessrMap] = []
    expected_total: int = 1 + int(nb_map_for_goal * MAP_ITEMS_COMPARED_TO_GOAL)
    expected_world: int = 1 + int(expected_total * WORLD_PERCENT)

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


def calculate_time_item_count(options: GeoguessrOptions) -> int:
    if options.maximum_time == options.starting_time:
        if options.allow_infinite_time:
            return 1
        else:
            return 0
    else:
        if options.maximum_time - options.starting_time < 60:
            return math.ceil((options.maximum_time - options.starting_time) / 10)
        else:
            return math.ceil((options.maximum_time - options.starting_time) / 30)


def calculate_movement_item_count(movement: MovementType) -> int:
    match movement:
        case MovementType.option_full_movement:
            return 0
        case MovementType.option_move_shuffled:
            return 1
        case MovementType.option_2_item_shuffled, MovementType.option_2_item_progressive:
            return 2
        case MovementType.option_3_item_progressive:
            return 3
