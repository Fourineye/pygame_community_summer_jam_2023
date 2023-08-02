import jazz
from consts import *
from jazz import GAME_GLOBALS, Vec2
from jazz.particles import Particle, ParticleEmitter


def _bubble_update(particle: Particle, delta: float):
    particle.vel = particle.vel.lerp(Vec2(0, -50), 0.1)
    if particle.life < 0.1:
        particle.img = particle.img


class Bullet(jazz.Body):
    def __init__(self, **kwargs):
        kwargs.setdefault("name", "Bullet")
        kwargs.setdefault("layers", "0000")
        kwargs.setdefault("collision_layers", "0010")
        super().__init__(**kwargs)
        self.add_collider("Circle", radius=4)

        self.add_child(
            ParticleEmitter(
                True,
                1,
                emission_speed=[[10, 100]],
                emission_angles=[(160, 360)],
                particle_life=0.5,
                particle_update=_bubble_update,
            )
        )
        self._damage = B_DAMAGE

    def update(self, delta: float):
        hits = self.move_and_collide(Vec2(B_SPEED, 0) * delta)
        if hits:
            if hasattr(hits[0][0], "take_damage"):
                hits[0][0].take_damage(self._damage)
            return self.queue_kill()

        if self.x > GAME_GLOBALS["Scene"].width + 100:
            self.queue_kill()
