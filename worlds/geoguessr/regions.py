from typing import Dict
from .data.maps import WORLD_MAPS, COUNTRY_MAPS


class RegionData:
    name: str

    def __init__(self, name):
        self.name = name


region_list: Dict[str, RegionData]


def initialize_region_list():
    region_list.update({country.name: RegionData(country.name) for country in COUNTRY_MAPS})
    region_list.update({world.name: RegionData(world.name) for world in WORLD_MAPS})
