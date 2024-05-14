from dataclasses import dataclass
from typing import Optional, Dict, List
from BaseClasses import Location
from .data.maps import COUNTRY_MAPS, GeoguessrMap

LOCATION_CODE_OFFSET = 0x6E0DA7A


@dataclass(frozen=True)
class LocationType:
    offset: int
    name: str
    score_mult: float
    map_number: int
    requires_map: bool
    requires_movement: bool
    requires_infinite_time: bool


@dataclass(frozen=True)
class LocationData(Location):
    code: Optional[int]
    region: str
    requires_map: bool
    requires_movement: bool
    requires_infinite_time: bool


location_table: Dict[str, LocationData] = {}

LOCATIONS_PER_MAP: List[LocationType] = [
    LocationType(0, "Easy 1-map score", 0.35, 1, True, False, False),
    LocationType(1, "Medium 1-map score", 0.6, 1, True, False, False),
    LocationType(2, "Hard 1-map score", 0.95, 1, True, True, False),
    LocationType(3, "Perfect 1-map score", 1.2, 1, True, True, True),

    LocationType(4, "Easy 3-map score", 1, 1, True, False, False),
    LocationType(5, "Medium 3-map score", 1.6, 1, True, False, False),
    LocationType(6, "Hard 3-map score", 2.75, 1, True, True, False),

    LocationType(7, "Easy 5-map score", 1.5, 1, True, False, False),
    LocationType(8, "Medium 5-map score", 3.25, 1, True, False, False),
    LocationType(9, "Hard 5-map score", 4.5, 1, True, True, False),
]

WORLD_LOCATIONS: List[LocationType] = [
    LocationType(0, "Easy 1-map score", 0.2, 1, False, False, False),
    LocationType(1, "Medium 1-map score", 0.45, 1, False, False, False),
    LocationType(2, "Hard 1-map score", 0.70, 1, False, False, False),
    LocationType(3, "Very hard 1-map score", 0.9, 1, False, True, False),
    LocationType(4, "Perfect 1-map score", 1.2, 1, False, True, True),

    LocationType(5, "Easy 2-map score", 0.4, 1, False, False, False),
    LocationType(6, "Medium 2-map score", 0.9, 1, False, False, False),
    LocationType(7, "Hard 2-map score", 1.4, 1, False, False, False),
    LocationType(8, "Very hard 2-map score", 1.8, 1, False, True, False),
    LocationType(9, "Perfect 2-map score", 2.4, 1, False, True, True),

    LocationType(10, "Easy 3-map score", 0.6, 1, False, False, False),
    LocationType(11, "Medium 3-map score", 1.35, 1, False, False, False),
    LocationType(12, "Hard 3-map score", 2.1, 1, False, False, False),
    LocationType(13, "Very hard 3-map score", 2.7, 1, False, True, False),

    LocationType(14, "Easy 4-map score", 0.8, 1, False, False, False),
    LocationType(15, "Medium 4-map score", 1.8, 1, False, False, False),
    LocationType(16, "Hard 4-map score", 2.8, 1, False, False, False),
    LocationType(17, "Very hard 4-map score", 3.6, 1, False, True, False),

    LocationType(18, "Easy 5-map score", 1, 1, False, False, False),
    LocationType(19, "Medium 5-map score", 2.25, 1, False, False, False),
    LocationType(20, "Hard 5-map score", 3.5, 1, False, False, False),
    LocationType(21, "Very hard 5-map score", 4.5, 1, False, True, False),
]


def initialize_location_table():
    for base_loc in WORLD_LOCATIONS:
        loc_name = f"World - {base_loc.name}"
        location_table[loc_name] = LocationData(LOCATION_CODE_OFFSET + base_loc.offset, "World", False,
                                                base_loc.requires_movement, base_loc.requires_infinite_time)

    for country_map in COUNTRY_MAPS:
        base_code: int = LOCATION_CODE_OFFSET + len(WORLD_LOCATIONS) + len(LOCATIONS_PER_MAP) * (country_map.id - 1)

        for location in LOCATIONS_PER_MAP:
            loc_name = f"{country_map.name} - {location.name}"
            location_code = base_code + location.offset
            location_table[loc_name] = LocationData(location_code, country_map.name, location.requires_map,
                                                    location.requires_movement, location.requires_infinite_time)
