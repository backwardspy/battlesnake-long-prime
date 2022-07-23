import math

from battlesnake_long_prime import models


def step(coord: models.Coordinate, direction: str) -> models.Coordinate:
    """
    Move the snake one step in the given direction.

    :param coord: The current position of the snake.
    :param direction: The direction in which to move the snake.
    :return: The new position of the snake.
    """
    if direction == "up":
        return models.Coordinate(x=coord.x, y=coord.y + 1)
    elif direction == "down":
        return models.Coordinate(x=coord.x, y=coord.y - 1)
    elif direction == "left":
        return models.Coordinate(x=coord.x - 1, y=coord.y)
    elif direction == "right":
        return models.Coordinate(x=coord.x + 1, y=coord.y)
    else:
        raise ValueError("Unknown direction: {}".format(direction))


def is_on_board(coord: models.Coordinate, board: models.Board) -> bool:
    """
    Check if the given coordinate is on the board.

    :param coord: The coordinate to check.
    :param board: The board to check in.
    :return: True if the coordinate is on the board, False otherwise.
    """
    return (
        coord.x >= 0
        and coord.x < board.width
        and coord.y >= 0
        and coord.y < board.height
    )


def is_in_snake(coord: models.Coordinate, body: list[models.Coordinate]) -> bool:
    """
    Check if the given coordinate is in the snake.

    :param coord: The coordinate to check.
    :param body: The snake body to check in.
    :return: True if the coordinate is in the snake, False otherwise.
    """
    return coord in body


def distance_to_food(head: models.Coordinate, food: list[models.Coordinate]) -> float:
    """
    Calculate the distance to the nearest food.

    :param head: The head of the snake.
    :param food: All food on the board.
    :return: The distance to the nearest food.
    """
    return min(
        [math.sqrt((head.x - food.x) ** 2 + (head.y - food.y) ** 2) for food in food]
    )
