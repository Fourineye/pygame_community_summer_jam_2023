from consts import *
from jazz import GAME_GLOBALS, Vec2
from jazz.particles import Particle


def bubble_update(particle: Particle, delta: float):
    particle.vel = particle.vel.lerp(Vec2(0, -50), 0.1)
    if particle.life < 0.05:
        particle.img = GAME_GLOBALS["Scene"].load_resource(BUBBLE_BURST[1])
    elif particle.life < 0.1:
        particle.img = GAME_GLOBALS["Scene"].load_resource(BUBBLE_BURST[0])