import jazz
from bullet import Bullet
from consts import *
from jazz import GAME_GLOBALS, Vec2


class Player(jazz.Body):
    def __init__(self, **kwargs):
        kwargs.setdefault("name", "Player")
        kwargs.setdefault("layers", "0001")
        kwargs.setdefault("collision_layers", "0011")
        kwargs.setdefault("static", True)
        super().__init__(**kwargs)
        self.add_collider("Rect", w=P_HITBOX_X, h=P_HITBOX_Y)
        self._weapon_cooldown = 0

    def update(self, delta):
        self.handle_movement(delta)
        self.screen_confine()
        self.handle_weapon(delta)

    def handle_movement(self, delta):
        direction = Vec2()
        direction.x = GAME_GLOBALS["Key"].held(P_RIGHT) - GAME_GLOBALS["Key"].held(
            P_LEFT
        )
        direction.y = GAME_GLOBALS["Key"].held(P_DOWN) - GAME_GLOBALS["Key"].held(P_UP)

        if direction.magnitude_squared() != 0:
            direction.normalize_ip()

        self.move(direction * P_SPEED * delta)

    def screen_confine(self):
        x, y = self.x, self.y
        if self.x - P_HITBOX_X / 2 < 0:
            x = P_HITBOX_X / 2
        elif self.x + P_HITBOX_X / 2 > GAME_GLOBALS["Scene"].width:
            x = GAME_GLOBALS["Scene"].width - P_HITBOX_X / 2

        if self.y - P_HITBOX_Y / 2 < 0:
            y = P_HITBOX_Y / 2
        elif self.y + P_HITBOX_Y / 2 > GAME_GLOBALS["Scene"].height:
            y = GAME_GLOBALS["Scene"].height - P_HITBOX_Y / 2

        self.pos = (x, y)

    def handle_weapon(self, delta):
        if GAME_GLOBALS["Key"].held(P_SHOOT) and self._weapon_cooldown <= 0:
            GAME_GLOBALS["Scene"].add_object(Bullet(pos=(self.x + 16, self.y)))
            self._weapon_cooldown = P_W_COOLDOWN
        elif self._weapon_cooldown > 0:
            self._weapon_cooldown = max(0, self._weapon_cooldown - delta)

    def take_damage(self, damage: int):
        print("player dead")
