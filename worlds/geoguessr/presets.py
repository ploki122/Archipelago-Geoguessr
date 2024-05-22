from typing import Any, Dict

default_geoguessr = {
    "goal_score": 4500,
    "map_goal": 1,

    "movement_type": 0,
    "starting_time": 3,
    "maximum_time": 3,
    "allow_infinite_time": False,

    "death_link": False,
    "death_link_score": 0,
}

short_beginner_friendly = {
    "goal_score": 3500,
    "map_goal": 3,

    "movement_type": 0,
    "starting_time": 2,
    "maximum_time": 5,
    "allow_infinite_time": True,

    "death_link": False,
    "death_link_score": 0,
}

long_preset = {
    "goal_score": 4500,
    "map_goal": 8,

    "movement_type": 3,
    "starting_time": 3,
    "maximum_time": 3,
    "allow_infinite_time": False,

    "death_link": False,
    "death_link_score": 0,
}

geoguessr_options_presets: Dict[str, Dict[str, Any]] = {
    "Geoguessr default (3 min move)": default_geoguessr,
    "Short beginner-friendly": short_beginner_friendly,
    "Long": long_preset,
}
