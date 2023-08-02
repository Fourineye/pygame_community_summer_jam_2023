from random import randint

import jazz
from consts import *
from enemy import BaseEnemy
from jazz import GAME_GLOBALS, Vec2
from jazz.utils import clamp

# wave_list format
# [
#   [enemy_type, lane, delay]
# ]


class WaveManager(jazz.GameObject):
    def __init__(self, wave_list: list, **kwargs):
        kwargs.setdefault("name", "Wave Manager")
        super().__init__(**kwargs)
        self.active = kwargs.get("active", True)
        self.wave_list = wave_list
        self._wave_progress = 0
        self._delay = 0

    def update(self, delta):
        if self.active:
            while self._delay <= 0 and self.active:
                if self._wave_progress < len(self.wave_list):
                    e_type, lane, delay = self.wave_list[self._wave_progress]
                    print(e_type, lane, delay)
                    if e_type is not None:
                        if lane is not None:
                            self.spawn_enemy(e_type, lane)
                        else:
                            self.spawn_enemy(e_type, randint(0, len(LANES) - 1))
                    self._delay = delay
                    self._wave_progress += 1
                else:
                    self.active = False
            else:
                self._delay = max(0, self._delay - delta)

    def spawn_enemy(self, type, lane):
        print("spawn")
        lane = clamp(lane, 0, len(LANES) - 1)
        GAME_GLOBALS["Scene"].add_object(
            BaseEnemy(pos=(GAME_GLOBALS["Scene"].width + 10, LANES[lane]))
        )
