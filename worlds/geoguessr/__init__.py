import logging

from typing import List, Dict
from BaseClasses import Location, Item, ItemClassification
from worlds.AutoWorld import MultiWorld, WebWorld, Tutorial, World
from .options import GeoguessrOptions
from .items import item_table
from .locations import location_table
from .logic import obtain_random_maps
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

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    # item_name_groups = {
    # }
    # location_name_groups = {
    # }

    selected_countries: List[GeoguessrMap]
    required_client_version = (0, 4, 6)

    options_dataclass = GeoguessrOptions
    options: GeoguessrOptions

    web = GeoguessrWebWorld()
    total_progression_items: int

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.selected_countries = []

#The world has to provide the following things for generation:
    #the properties mentioned above
    #additions to the item pool
    #additions to the regions list: at least one called "Menu"
    #locations placed inside those regions
    #create_item(self, item: str) -> MyGameItem to create any item on demand
    #self.multiworld.push_precollected for world-defined start inventory

#In addition, the following methods can be implemented and are called in this order during generation:

#generate_early(self) called per player before any items or locations are created. You can set properties on your world here. Already has access to player options and RNG. This is the earliest step where the world should start setting up for the current multiworld, as the multiworld itself is still setting up before this point.
#create_regions(self) called to place player's regions and their locations into the MultiWorld's regions list. If it's hard to separate, this can be done during generate_early or create_items as well.
#create_items(self) called to place player's items into the MultiWorld's itempool. After this step all regions and items have to be in the MultiWorld's regions and itempool, and these lists should not be modified afterward.
#set_rules(self) called to set access and item rules on locations and entrances.
#generate_basic(self) player-specific randomization that does not affect logic can be done here.
#pre_fill(self), fill_hook(self) and post_fill(self) called to modify item placement before, during, and after the regular fill process; all finishing before generate_output. Any items that need to be placed during pre_fill should not exist in the itempool, and if there are any items that need to be filled this way, but need to be in state while you fill other items, they can be returned from get_prefill_items.
#generate_output(self, output_directory: str) creates the output files if there is output to be generated. When this is called, self.multiworld.get_locations(self.player) has all locations for the player, with attribute item pointing to the item. location.item.player can be used to see if it's a local item.
#fill_slot_data(self) and modify_multidata(self, multidata: Dict[str, Any]) can be used to modify the data that will be used by the server to host the MultiWorld.
#All instance methods can, optionally, have a class

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

    def create_item(self, name: str) -> GeoguessrItem:
        item = item_table[name]
        return GeoguessrItem(name, item.classification, item.code, self.player)

    def pre_fill(self) -> None:
        pass

    def create_items(self) -> None:
        pass

    def generate_basic(self) -> None:
        pass

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
