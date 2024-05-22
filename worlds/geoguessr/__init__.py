import logging
import random

from typing import List, Dict
from BaseClasses import Location, Item, ItemClassification, Region
from worlds.AutoWorld import MultiWorld, WebWorld, Tutorial, World
from .logic import obtain_random_maps, calculate_time_item_count
from .options import GeoguessrOptions, MovementType
from .items import item_table, item_group_table
from .locations import location_table
from .data.maps import GeoguessrMap, COUNTRY_MAPS, WORLD_MAPS

logger = logging.getLogger("Geoguessr")


class GeoguessrLocation(Location):
    game: str = "Geoguessr"


class GeoguessrItem(Item):
    game: str = "Geoguessr"


class GeoguessrWebWorld(WebWorld):
    theme = "jungle"
    bug_report_page = ("https://github.com/ploki122/Archipelago-Geoguessr/issues/new?labels=bug"
                       "&title=%5BBug%5D%3A+Brief+Description+of+bug+here")
    # options_presets = geoguessr_presets

    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Geoguessr with Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Ploki122"]
        )]


class GeoguessrWorld(World):
    """
    Geoguessr is a browser-based game where you have to guess where you are on the world map, based on a street view.
    """

    game = "Geoguessr"
    topology_present = False

    items.initialize_item_tables()
    item_name_to_id = {name: data.code for name, data in item_table.items()}

    locations.initialize_location_table()
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    options_dataclass = GeoguessrOptions
    options: GeoguessrOptions

    item_name_groups = item_group_table
    web = GeoguessrWebWorld()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.selected_countries = []

    def generate_early(self):
        self.force_change_options_if_incompatible()
        self.selected_countries = obtain_random_maps(self.options.map_goal.value, self.random)

    def force_change_options_if_incompatible(self):
        if self.options.maximum_time < self.options.starting_time:
            self.options.maximum_time = self.options.starting_time
            max_time = self.options.maximum_time
            start_time = self.options.starting_time
            player_name = self.multiworld.player_name[self.player]
            logging.warning(f"Maximum time '{max_time}' was lower than start time '{start_time}. "
                            f"Maximum time was forced to starting time for player {self.player} ({player_name})")

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)

        world_region = Region("World", self.player, self.multiworld)
        world_region.connect(menu_region)

        for country in self.selected_countries:
            map_region = Region(country, self.player, self.multiworld)
            map_region.connect(menu_region, None, lambda state: state.has(f"{country} Map"))

    def create_item(self, name: str) -> GeoguessrItem:
        item = item_table[name]
        return GeoguessrItem(name, item.classification, item.code, self.player)

    def pre_fill(self) -> None:
        pass

    def create_items(self) -> None:
        starting_items: List[str] = []
        shuffled_items: List[str] = []

        starting_items += f"{self.selected_countries[0]} Map"
        for index in range(1, len(self.selected_countries)):
            shuffled_items += f"{self.selected_countries[index]} Map"

        shuffled_items += ["Time extension"]*calculate_time_item_count(self.options)

        match self.options.movement_type:
            case MovementType.option_full_movement:
                starting_items += ["Move", "Pan", "Zoom"]
            case MovementType.option_move_shuffled:
                starting_items += ["Pan", "Zoom"]
                shuffled_items += "Move"
            case MovementType.option_2_item_shuffled:
                shuffled_items += ["Move", "Pan+Zoom"]
            case MovementType.option_2_item_progressive:
                shuffled_items += ["Progressive 2-item Movement"]*2
            case MovementType.option_3_item_progressive:
                shuffled_items += ["Progressive 3-item Movement"]*3

        for item in starting_items:
            self.multiworld.push_precollected(item_table[item])

        while len(shuffled_items) < len(self.multiworld.get_unfilled_locations()):
            shuffled_items += self.get_filler_item_name()

        self.multiworld.itempool += shuffled_items

    def get_filler_item_name(self) -> str:
        return "Temporary time extension"

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        pass
    # if self.stage_shuffle_enabled:
    #     regions = {LocationName.level_names[level]: level for level in LocationName.level_names}
    #     level_hint_data = {}
    #     for level in regions:
    #         for stage in range(7):
    #             stage_name = self.multiworld.get_location(self.location_id_to_name[self.player_levels[level][stage]],
    #                                                       self.player).name.replace(" - Complete", "")
    #             stage_regions = [room for room in self.rooms if stage_name in room.name]
    #             for region in stage_regions:
    #                 for location in [location for location in region.locations if location.address]:
    #                     level_hint_data[location.address] = f"{regions[level]} {stage + 1 if stage < 6 else 'Boss'}"
    #     hint_data[self.player] = level_hint_data
