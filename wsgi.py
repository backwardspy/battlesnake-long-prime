from battlesnake_long_prime.api import create_app

application = create_app()


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    run_simple(
        hostname="0.0.0.0",
        port=6502,
        application=application,
        use_reloader=True,
        use_debugger=False,
    )
