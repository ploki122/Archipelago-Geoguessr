import enum
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, List

from BaseClasses import Item, ItemClassification
from .data.maps import COUNTRY_MAPS, WORLD_MAPS

BASE_ITEM_OFFSET = 0x6E0DA7A
logger = logging.getLogger(__name__)
world_folder = Path(__file__).parent


class ItemGroup(enum.Enum):
    CountryMap = enum.auto()
    WorldMap = enum.auto()
    AllMap = enum.auto()
    Movement = enum.auto()
    Helper = enum.auto()
    Everything = enum.auto()


@dataclass(frozen=True)
class ItemData(Item):
    code: Optional[int]
    name: str
    classification: ItemClassification


events = [
    ItemData(None, "Victory", ItemClassification.progression),
]

item_table: Dict[str, ItemData] = {}
item_group_table: Dict[str, List[str]] = {}

extra_items = [
    ItemData(BASE_ITEM_OFFSET + 1, "Time extension", ItemClassification.progression),
    ItemData(BASE_ITEM_OFFSET + 2, "Progressive 2-item Movement", ItemClassification.progression),
    ItemData(BASE_ITEM_OFFSET + 3, "Progressive 3-item Movement", ItemClassification.progression),
    ItemData(BASE_ITEM_OFFSET + 4, "Move", ItemClassification.progression),
    ItemData(BASE_ITEM_OFFSET + 5, "Pan", ItemClassification.useful),
    ItemData(BASE_ITEM_OFFSET + 6, "Zoom", ItemClassification.useful),
    ItemData(BASE_ITEM_OFFSET + 7, "Pan+Zoom", ItemClassification.useful),
    ItemData(BASE_ITEM_OFFSET + 8, "Temporary time extension", ItemClassification.filler),
]


def get_too_many_items_error_message(location_count: int, item_count: int) -> str:
    return f"There should be at least as many locations [{location_count}] as there are mandatory items [{item_count}]"


def initialize_item_tables():
    # Item groups need to be redone, this is shit code
    item_table.update({item.name: ItemData(BASE_ITEM_OFFSET + len(extra_items) + item.id, item.name + " Map",
                                           ItemClassification.progression) for item in WORLD_MAPS})
    item_group_table.update({"world_map": [item.name + " Map" for item in WORLD_MAPS]})

    item_table.update({item.name: ItemData(BASE_ITEM_OFFSET + len(extra_items) + item.id, item.name + " Map",
                                           ItemClassification.progression) for item in COUNTRY_MAPS})
    item_group_table.update({"country_map": [item.name + " Map" for item in WORLD_MAPS]})

    item_group_table.update({"all_map": [item.name + " Map" for item in COUNTRY_MAPS]})
    item_group_table.update({"all_map": [item.name + " Map" for item in WORLD_MAPS]})

    item_table.update({item.name: item for item in extra_items})
    item_group_table.update({"helper": [item.name for item in extra_items]})
    item_group_table.update({"movement": ["Time extension, Progressive Movement, Movement, Panning, Zoom"]})
