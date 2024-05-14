import enum
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

from BaseClasses import Item, ItemClassification
from .data.maps import COUNTRY_MAPS, WORLD_MAPS

BASE_ITEM_OFFSET = 0x6E0DA7A
logger = logging.getLogger(__name__)
world_folder = Path(__file__).parent


class ItemGroup(enum.Enum):
    MAP_UNLOCK = enum.auto()
    MOVEMENT = enum.auto()
    HELPER = enum.auto()


@dataclass(frozen=True)
class ItemData(Item):
    code: Optional[int]
    name: str
    classification: ItemClassification


events = [
    ItemData(None, "Victory", ItemClassification.progression),
]

item_table: Dict[str, ItemData] = {}

extra_items = [
    ItemData(BASE_ITEM_OFFSET + 1, "Time extension", ItemClassification.progression),
    ItemData(BASE_ITEM_OFFSET + 2, "Progressive Movement", ItemClassification.progression),
    ItemData(BASE_ITEM_OFFSET + 3, "Movement", ItemClassification.progression),
    ItemData(BASE_ITEM_OFFSET + 4, "Panning", ItemClassification.progression),
    ItemData(BASE_ITEM_OFFSET + 5, "Zoom", ItemClassification.useful),
]


def get_too_many_items_error_message(location_count: int, item_count: int) -> str:
    return f"There should be at least as many locations [{location_count}] as there are mandatory items [{item_count}]"


def initialize_item_table():
    item_table.update({item.name: ItemData(BASE_ITEM_OFFSET + len(extra_items) + item.id, item.name + " Map",
                                           ItemClassification.progression) for item in WORLD_MAPS})
    item_table.update({item.name: ItemData(BASE_ITEM_OFFSET + len(extra_items) + item.id, item.name + " Map",
                                           ItemClassification.progression) for item in COUNTRY_MAPS})
    item_table.update({item.name: item for item in extra_items})
