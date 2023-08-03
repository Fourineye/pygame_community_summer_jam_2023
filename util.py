from jazz import Vec2
from jazz.particles import Particle


def bubble_update(particle: Particle, delta: float):
    particle.vel = particle.vel.lerp(Vec2(0, -50), 0.1)
    if particle.life < 0.1:
        particle.img = particle.img