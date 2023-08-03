from random import choice

import jazz
from consts import *
from enemy import BaseEnemy
from jazz import GAME_GLOBALS, SETTINGS
from player import Player
from wave_manager import WaveManager


class Game(jazz.Scene):
    name = "Game"

    def on_load(self, data):
        self.add_object(Player(pos=(100, self.height / 2)), "player")
        self.add_object(WaveManager(WAVE_1), "wave_manager")
        # self.camera.debug = True
        self.camera.set_bg_color("#808faa")

    def update(self, delta):
        ...
        # if self.enemy_timer > 0:
        #     self.enemy_timer = max(self.enemy_timer - delta, 0)
        # else:
        #     self.add_object(BaseEnemy(pos=(self.width + 10, choice(LANES))))
        #     self.enemy_timer = 1
