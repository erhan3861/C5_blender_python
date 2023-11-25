from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina import curve
import random

particle_list = []

def update():
    cube.rotation_y += 1

def input(key):
    if key == "left mouse down":
        mouse_position = mouse.world_point
        cube.animate_position(mouse_position, duration=0.5, curve=curve.in_out_quad)
        cube.color = color.random_color()
        for _ in range(10):
            create_particle_effect(cube.position, color.random_color())

def on_mouse_enter():
    cube.color = color.lime
    for _ in range(10):
        create_particle_effect(cube.position, color.yellow)

def on_mouse_exit():
    cube.color = color.red

def create_particle_effect(position, particle_color):
    offset = Vec3(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
    particle_position = position + offset

    particle = Entity(
        model='quad',
        color=particle_color,
        scale=0.3,
        position=particle_position,
        add_to_scene_entities=True
    )

    particle.animate_scale(
        (0.01, 0.01, 0.01),
        duration=0.8,
        curve=curve.in_expo
    )

    particle_list.append(particle)

    invoke(remove_particle_effect, particle, delay=0.8)

def remove_particle_effect(particle):
    particle_list.remove(particle)
    destroy(particle)

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

cube = Entity(model="cube", color=color.red, scale=1, collider="box", y=.5)
ground = Entity(model="plane", scale=10, texture="grass", collider="box")

cube.on_mouse_enter = on_mouse_enter
cube.on_mouse_exit = on_mouse_exit

editor_camera = EditorCamera()
directional_light = DirectionalLight()
directional_light.look_at((-1, -1, 1))

app.run()
