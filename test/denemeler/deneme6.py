from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina import curve

def update():
    cube.rotation_y += 1

def input(key):
    if key == "left mouse down":
        mouse_position = mouse.world_point
        cube.animate_position(mouse_position, duration=0.5, curve=curve.in_out_quad)
        cube.color = color.random_color()
        create_particle_effect(cube.position, color.random_color())

def on_mouse_enter():
    cube.color = color.lime
    create_particle_effect(cube.position, color.yellow)

def on_mouse_exit():
    cube.color = color.red

def create_particle_effect(position, particle_color):
    particle = Entity(
        model='quad',
        color=particle_color,
        scale=0.3,
        position=position,
        add_to_scene_entities=True
    )

    particle.animate_scale(
        (0.01, 0.01, 0.01),
        duration=3,
        curve=curve.in_expo
        # autoremove=True
    )

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

cube = Entity(model="cube", color=color.red, scale=1.5, collider="box")
ground = Entity(model="plane", scale=10, texture="grass", collider="box")

cube.on_mouse_enter = on_mouse_enter
cube.on_mouse_exit = on_mouse_exit

EditorCamera()

app.run()
