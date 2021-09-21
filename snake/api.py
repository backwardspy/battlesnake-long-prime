import falcon

from snake import views


def create_app() -> falcon.App:
    """
    Initialises and returns the battlesnake API application.
    """
    app = falcon.App()
    app.add_route("/", views.Root())
    app.add_route("/start", views.Start())
    app.add_route("/move", views.Move())
    app.add_route("/end", views.End())
    return app
