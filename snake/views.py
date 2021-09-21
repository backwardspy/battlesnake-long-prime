import falcon

from config import settings


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
        pass


class End:
    """
    Your Battlesnake will receive this request whenever a game it was playing has ended.
    Use it to learn how your Battlesnake won or lost and deallocated any server-side resources.
    Your response to this request will be ignored.
    """
    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        pass
