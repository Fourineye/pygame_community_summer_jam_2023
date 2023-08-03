import jazz
from consts import *
from jazz import GAME_GLOBALS, Vec2
from jazz.particles import Particle, ParticleEmitter
from util import bubble_update


class Bullet(jazz.Body):
    def __init__(self, **kwargs):
        kwargs.setdefault("name", "Bullet")
        kwargs.setdefault("layers", "0000")
        kwargs.setdefault("collision_layers", "0010")
        super().__init__(**kwargs)
        self.add_collider("Circle", radius=4)
        self.vel = kwargs.get("vel", Vec2(B_SPEED, 0))

        self.add_child(
            ParticleEmitter(
                True,
                30,
                emission_speed=[[10, 100]],
                emission_angles=[(160, 360)],
                particle_life=0.5,
                particle_update=bubble_update,
            )
        )
        self._damage = B_DAMAGE

    def update(self, delta: float):
        hits = self.move_and_collide(self.vel * delta)
        if hits:
            if hasattr(hits[0][0], "take_damage"):
                hits[0][0].take_damage(self._damage)
            return self.queue_kill()

        if not self.collider.rect.colliderect(GAME_GLOBALS["Scene"].camera.screen_rect):
            self.queue_kill()
