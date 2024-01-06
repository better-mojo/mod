from mod_cli.commands import app

if __name__ == "__main__":
    try:
        app()
    except Exception as e:
        print(e)
