from . import main
from . import Client, __version__


def main() -> None:
    client = Client()
    print(f"python-vrage {__version__} - {client.ping()}")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
