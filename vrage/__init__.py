"""python-vrage package

Minimal public API for packaging.
"""
__all__ = ["__version__", "Client"]

__version__ = "0.0.1"


class Client:
    """Tiny placeholder client for VRage Remote API."""

    def __init__(self):
        pass

    def ping(self) -> str:
        """Return a simple greeting to verify import."""
        return "python-vrage: pong"


"""python-vrage package

Lightweight package exposing a small client placeholder and version.
"""

__version__ = "0.0.1"


def info():
    return {
        "name": "python-vrage",
        "version": __version__,
        "description": "a Python client for the VRage Remote API of Space Engineers 1",
    }


def main():
    print(f"python-vrage {__version__}: a VRage Remote API client placeholder")
