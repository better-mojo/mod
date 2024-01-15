import environs

from mod_cli.commands import app


def run_app():
    env = environs.Env()
    debug = env.bool("DEBUG", False)

    if debug:
        print(f"DEBUG Mode: {debug}")
        app()
    else:
        try:
            app()  # TODO X: ignore exception
        except Exception as e:
            print(e)


if __name__ == "__main__":
    run_app()
