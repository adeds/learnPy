from typing import Any, Callable


def world():
    print("Hello, world!")


lam_world: Callable[[Any], str] = lambda name: "Hello, {}".format(name)
