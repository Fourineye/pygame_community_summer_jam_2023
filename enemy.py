import jazz
from consts import *
from jazz import GAME_GLOBALS, Vec2


class BaseEnemy(jazz.Body):
    def __init__(self, **kwargs):
        kwargs.setdefault("name", "Enemy")
        kwargs.setdefault("layers", "0010")
        kwargs.setdefault("static", True)
        super().__init__(**kwargs)
        self.add_collider("Rect", w=E_HITBOX_X, h=E_HITBOX_Y)
        self.hp = E_HP

    def update(self, delta):
        hits = self.move_and_collide(Vec2(-E_SPEED * delta, 0))
        if hits:
            if hasattr(hits[0][0], "take_damage"):
                hits[0][0].take_damage(1)
                return self.queue_kill()

        if self.x < -E_HITBOX_X:
            self.queue_kill()

    def take_damage(self, damage: int):
        if self.x < GAME_GLOBALS["Scene"].width - 10:
            self.hp -= damage
            if self.hp <= 0:
                self.queue_kill()
