from random import randint

import jazz
from consts import *
from enemy import BaseEnemy, ShooterEnemy
from jazz import GAME_GLOBALS, Vec2
from jazz.utils import clamp

# wave_list format
# [
#   [enemy_type, lane, delay]
# ]
E_TYPES = [BaseEnemy, ShooterEnemy]


class WaveManager(jazz.GameObject):
    def __init__(self, wave_list: list, **kwargs):
        kwargs.setdefault("name", "Wave Manager")
        super().__init__(**kwargs)
        self.active = kwargs.get("active", True)
        self.wave_list = wave_list
        self._wave_progress = 0
        self._blockers = []
        self._delay = 0

    def update(self, delta):
        if self.active:
            while self._delay <= 0 and self.active:
                if self._wave_progress < len(self.wave_list):
                    e_type, lane, delay, blocking = self.wave_list[self._wave_progress]
                    print(e_type, lane, delay, blocking)
                    if e_type is not None:
                        if lane is not None:
                            enemy = self.spawn_enemy(e_type, lane)
                        else:
                            enemy = self.spawn_enemy(e_type, randint(0, len(LANES) - 1))
                    if blocking:
                        self._blockers.append(enemy)
                    self._delay = delay
                    self._wave_progress += 1
                else:
                    self.active = False
            else:
                if not self._blockers:
                    self._delay = max(0, self._delay - delta)
                else:
                    for blocker in self._blockers[::-1]:
                        if blocker.do_kill:
                            self._blockers.remove(blocker)

    def spawn_enemy(self, type, lane):
        print("spawn")
        lane = clamp(lane, 0, len(LANES) - 1)
        type = clamp(type, 0, len(E_TYPES) - 1)
        enemy = E_TYPES[type](pos=(GAME_GLOBALS["Scene"].width + 10, LANES[lane]))
        GAME_GLOBALS["Scene"].add_object(enemy, f"e{self._wave_progress}")
        return enemy
