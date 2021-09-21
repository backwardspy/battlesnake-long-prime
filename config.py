import pydantic
from pydantic.color import Color


class Settings(pydantic.BaseSettings):
    author: str

    snake_colour: Color = Color("#72e0d4")
    snake_head: str = "scarf"
    snake_tail: str = "coffee"


settings = Settings()
