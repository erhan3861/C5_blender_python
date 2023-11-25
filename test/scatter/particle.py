from ursina import *
import random

# Particle class for representing individual particles
class Particle(Entity):
    def __init__(self, position, velocity, color):
        super().__init__(
            model='cube',
            color=color,
            position=position,
            collider=None,
            scale=random.uniform(0.1, 0.3)
        )
        self.velocity = velocity
        self.lifetime = random.uniform(1, 2)

    def update(self):
        self.position += self.velocity * time.dt
        self.lifetime -= time.dt
        if self.lifetime <= 0:
            destroy(self)

def tiklama_oynat():
    cube.animate_scale(Vec3(0, 0, 0), duration=.3)

    for _ in range(20):
        position = cube.position
        velocity = Vec3(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2))
        clr = cube.color

        particle = Particle(position, velocity, clr)
        particle.texture = cube.texture
        
app = Ursina()
editor_camera = EditorCamera()

cube = Entity(model='cube', texture="brick", collider='box', scale=3, y=5)
cube.on_click = tiklama_oynat

ground = Entity(model="plane", scale=200, texture="grass", collider="box")
Sky()
app.run()
