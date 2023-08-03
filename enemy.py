from random import uniform

import jazz
from bullet import Bullet
from consts import *
from jazz import GAME_GLOBALS, Vec2
from jazz.particles import ParticleEmitter
from util import bubble_update


class BaseEnemy(jazz.Body):
    def __init__(self, **kwargs):
        kwargs.setdefault("name", "Enemy")
        kwargs.setdefault("layers", "0010")
        kwargs.setdefault("static", True)
        super().__init__(**kwargs)
        self.add_collider("Rect", w=E_HITBOX_X, h=E_HITBOX_Y)
        self.hp = E_HP
        self.add_child(
            ParticleEmitter(
                False,
                20,
                emission_speed=[[10, 100]],
                emission_angles=[(160, 360)],
                particle_graphics=BUBBLE_OPTIONS,
                particle_life=0.5,
                particle_update=bubble_update,
                pos=(-P_HITBOX_X / 6, 0),
                particle_spawn=jazz.Rect(
                    -P_HITBOX_X / 3, -P_HITBOX_Y / 2, 2 * P_HITBOX_X / 3, P_HITBOX_Y
                ),
            ),
            "move_particles",
        )

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


class ShooterEnemy(BaseEnemy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shoot_cooldown = 0
        self.shots = E_SHOTS
        self.hp = E_SHOOTER_HP

    def update(self, delta):
        if self.x > GAME_GLOBALS["Scene"].width * 5 / 6 or self.shots == 0:
            hits = self.move_and_collide(Vec2(-E_SHOOTER_SPEED * delta, 0))
        else:
            hits = self.move_and_collide(Vec2())
            if self.shoot_cooldown <= 0:
                self.shoot()
                self.shoot_cooldown = E_COOLDOWN + uniform(-0.1, 0.5)
                self.shots -= 1
            else:
                self.shoot_cooldown = max(0, self.shoot_cooldown - delta)

        if hits:
            if hasattr(hits[0][0], "take_damage"):
                hits[0][0].take_damage(1)
                return self.queue_kill()

        if self.x < -E_HITBOX_X:
            self.queue_kill()

    def shoot(self):
        if hasattr(GAME_GLOBALS["Scene"], "player"):
            direction = GAME_GLOBALS["Scene"].player.pos - self.pos
            direction.normalize_ip()
            for i in range(3):
                vel = direction.rotate(-15 + 15 * i) * B_SPEED
                GAME_GLOBALS["Scene"].add_object(
                    Bullet(
                        collision_layers="0001",
                        vel=vel,
                        pos=(self.x - E_HITBOX_X / 2, self.y),
                    )
                )
