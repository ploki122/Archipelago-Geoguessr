from BaseClasses import MultiWorld
from worlds.AutoWorld import LogicMixin


class ArchipIDLELogic(LogicMixin):
    def _archipidle_location_is_accessible(self, player_id, items_required):
        return sum(self.prog_items[player_id].values()) >= items_required


def set_rules(world: MultiWorld, player: int):
    for i in range(16, 31):
        world.get_location(f"IDLE item number {i}", player).access_rule = lambda \
            state: state._archipidle_location_is_accessible(player, 4)

    for i in range(31, 51):
        world.get_location(f"IDLE item number {i}", player).access_rule = lambda \
            state: state._archipidle_location_is_accessible(player, 10)

    for i in range(51, 101):
        world.get_location(f"IDLE item number {i}", player).access_rule = lambda \
            state: state._archipidle_location_is_accessible(player, 20)

    for i in range(101, 201):
        world.get_location(f"IDLE item number {i}", player).access_rule = lambda \
            state: state._archipidle_location_is_accessible(player, 40)

    world.completion_condition[player] =\
        lambda state: state.can_reach(world.get_location("IDLE item number 200", player), "Location", player)
