from dataclasses import dataclass
from Options import Range, DefaultOnToggle, Choice, PerGameCommonOptions, DeathLink


class GoalScore(Range):
    """The score to obtain, over a 5-round run, for that map to be considered completed."""
    display_name = "Score for goal"
    range_start = 1
    range_end = 25000
    default = 22500


class MapGoal(Range):
    """How many maps must be completed to finish a slot."""
    display_name = "Maps for goal"
    range_start = 1
    range_end = 100
    default = 10


class StartingTime(Range):
    """How much time, in seconds, the player begins with.
    Will be rounded to the nearest 10."""
    display_name = "Starting time"
    range_start = 10
    range_end = 600
    default = 30


class MaximumTime(Range):
    """How much time, in seconds, the player will get at most."""
    display_name = "Maximum time"
    range_start = 10
    range_end = 600
    default = 300


class AllowUnlimitedTime(DefaultOnToggle):
    """When enabled, a player that reaches the maximum time will have unlimited time instead."""
    display_name = "Allow unlimited time?"


class MovementType(Choice):
    """
    Determines how movement options are randomized

    Full Movement : Start with Move, Pan and Zoom.
    Move Shuffled : Start with No Move, Move is shuffled.
    2-item Progressive : Start with NMPZ (No movement, pan or zoom), then unlock Pan+Zoom, and then Move.
    3-item Progressive : Start with NMPZ, then unlock Zoom, Pan, and then Move.
    2-item Shuffled : Start with NMPZ, Zoom+Pan and Move are shuffled as distinct items.
    """
    display_name = "Randomize Wild Pokemon"
    default = 2
    option_full_movement = 0
    option_move_shuffled = 1
    option_2_item_progressive = 2
    option_3_item_progressive = 3
    option_2_item_shuffled = 4


class DeathLinkScore(Range):
    """
    If DeathLink is activated :
    Scoring less than this amount of points on a map will send a death to every other players.
    """
    display_name = "DeathLink threshold"
    range_start = 1
    range_end = 4999
    default = 500


@dataclass
class GeoguessrOptions(PerGameCommonOptions):
    goal_score: GoalScore
    map_goal: MapGoal

    movement_type: MovementType
    starting_time: StartingTime
    maximum_time: MaximumTime
    allow_infinite_time: AllowUnlimitedTime

    death_link: DeathLink
    death_link_score: DeathLinkScore
