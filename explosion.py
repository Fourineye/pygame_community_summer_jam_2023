import jazz
from consts import *
from jazz import GAME_GLOBALS, Vec2
from jazz.particles import Particle, ParticleEmitter
from util import bubble_update


class Explosion(jazz.GameObject):
    def __init__(self, name="Explosion", **kwargs):
        super().__init__(name, **kwargs)
        self.add_child(
            jazz.AnimatedSprite(
                spritesheet=BUBBLE_EXPLOSION,
                oneshot=True,
                animation_fps=15,
            ),
            "sprite",
        )
        self.add_child(
            ParticleEmitter(
                False,
                20,
                emission_speed=[[100, 200]],
                particle_graphics=BUBBLE_OPTIONS,
                particle_life=0.5,
                particle_update=bubble_update,
                particle_spawn=10,
            ),
            "emitter",
        )
        self.primed = True

    def update(self, delta):
        if self.sprite._frame >= 3 and self.primed:
            self.emitter.emit_particles(25)
            self.primed = False

        if not self.emitter._particles and not self.primed:
            self.queue_kill()
