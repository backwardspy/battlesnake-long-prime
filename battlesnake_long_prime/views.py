import falcon

from battlesnake_long_prime import game, models
from battlesnake_long_prime.settings import settings


class Root:
    """
    An empty GET request made to the top-level URL of your Battlesnake,
    used for customization, checking latency, and verifying successful
    communication between the Battlesnake and the Battlesnake Engine.
    """

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        resp.media = {
            "apiversion": "1",
            "author": "backwardspy",
            "color": settings.snake_colour.as_hex(),
            "head": settings.snake_head,
            "tail": settings.snake_tail,
            "version": "0.1.0",
        }


class Start:
    """
    Your Battlesnake will receive this request when it has been entered into a new game.
    Every game has a unique ID that can be used to allocate resources or data you may need.
    Your response to this request will be ignored.
    """

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        pass


class Move:
    """
    This request will be sent for every turn of the game.
    Use the information provided to determine how your Battlesnake will move on that turn,
    either up, down, left, or right.
    """

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        gr = models.GameRequest(**req.media)
        moves = ["up", "right", "down", "left"]

        # sort directions by distance to closest food
        directions = [
            (
                direction,
                game.distance_to_food(game.step(gr.you.head, direction), gr.board.food),
            )
            for direction in moves
        ]
        directions = sorted(directions, key=lambda x: x[1])

        for direction, _ in directions:
            coord = game.step(gr.you.head, direction)
            checks = [
                game.is_on_board(coord, gr.board),
                not game.is_in_snake(coord, gr.you.body),
                not any(
                    game.is_in_snake(coord, snake.body) for snake in gr.board.snakes
                ),
            ]
            if all(checks):
                break
        resp.media = {
            "move": direction,
            "shout": f"i am moving {direction}",
        }


class End:
    """
    Your Battlesnake will receive this request whenever a game it was playing has ended.
    Use it to learn how your Battlesnake won or lost and deallocated any server-side resources.
    Your response to this request will be ignored.
    """

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        pass
