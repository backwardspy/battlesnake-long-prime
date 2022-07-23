"""
https://docs.battlesnake.com/references/api#object-definitions
"""

import pydantic


def to_camel_case(snake_str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


class Model(pydantic.BaseModel):
    """
    Base model class, provides camelCase aliases for all fields.
    """

    class Config:
        """
        Pydantic model configuration.
        """

        alias_generator = to_camel_case


class RoyaleSettings(Model):
    """
    Game settings used in royale mode.
    """

    shrink_every_n_turns: int


class SquadSettings(Model):
    """
    Game settings used in squad mode.
    """

    allow_body_collisions: bool
    shared_elimination: bool
    shared_health: bool
    shared_length: bool


class RulesetSettings(Model):
    """
    Game settings used in all rulesets.
    """

    food_spawn_chance: int
    minimum_food: int
    hazard_damage_per_turn: int
    royale: RoyaleSettings
    squad: SquadSettings


class Ruleset(Model):
    """
    A named ruleset with associated settings used in a game.
    """

    name: str
    version: str
    settings: RulesetSettings


class Game(Model):
    """
    An instance of a game of battlesnake.
    """

    id: str
    ruleset: Ruleset
    timeout: int


class Coordinate(Model):
    """
    2D coordinates used in the battlesnake grid.
    """

    x: int
    y: int


class Battlesnake(Model):
    """
    An individual battlesnake.
    """

    id: str
    name: str
    health: int
    body: list[Coordinate]
    latency: str
    head: Coordinate
    length: int
    shout: str
    squad: str


class Board(Model):
    """
    A 2D game board.
    """

    height: int
    width: int
    food: list[Coordinate]
    hazards: list[Coordinate]
    snakes: list[Battlesnake]


class GameRequest(Model):
    """
    Schema for the information passed in each POST request from the game engine.
    """

    game: Game
    turn: int
    board: Board
    you: Battlesnake
