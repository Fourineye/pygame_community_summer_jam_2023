import jazz
from game_scene import Game

if __name__ == "__main__":
    flags = jazz.locals.SCALED
    app = jazz.Application(640, 480, "Pygame Summer Jam", flags=flags, vsync=True)
    app.add_scene(Game)
    app.run()
